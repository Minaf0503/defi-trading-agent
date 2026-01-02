"""
Tool Registry
Manages tools for each agent, allowing dynamic registration and API querying
"""

import json
import requests
from typing import Dict, Any, List, Optional, Callable, Annotated
from langchain_core.tools import tool, BaseTool
from langchain_core.tools import StructuredTool
from functools import wraps
import inspect


class ToolRegistry:
    """Registry for managing tools for each agent."""
    
    def __init__(self, context_manager=None):
        """
        Initialize the tool registry.
        
        Args:
            context_manager: Optional AgentContextManager instance
        """
        self.context_manager = context_manager
        self._agent_tools: Dict[str, List[BaseTool]] = {}
        self._registered_tools: Dict[str, BaseTool] = {}
    
    def register_tool(self, tool: BaseTool, agent_names: Optional[List[str]] = None):
        """
        Register a tool for specific agents or globally.
        
        Args:
            tool: LangChain tool instance
            agent_names: List of agent names to register for, or None for all agents
        """
        self._registered_tools[tool.name] = tool
        
        if agent_names is None:
            # Register for all agents
            for agent_name in self._agent_tools.keys():
                if tool not in self._agent_tools[agent_name]:
                    self._agent_tools[agent_name].append(tool)
        else:
            for agent_name in agent_names:
                if agent_name not in self._agent_tools:
                    self._agent_tools[agent_name] = []
                if tool not in self._agent_tools[agent_name]:
                    self._agent_tools[agent_name].append(tool)
    
    def get_agent_tools(self, agent_name: str) -> List[BaseTool]:
        """Get all tools registered for an agent."""
        return self._agent_tools.get(agent_name, [])
    
    def create_api_query_tool(
        self,
        api_name: str,
        endpoint: str,
        method: str = "GET",
        description: str = "",
        agent_name: Optional[str] = None
    ) -> BaseTool:
        """
        Create a tool for querying an API endpoint.
        
        Args:
            api_name: Name of the API
            endpoint: API endpoint URL
            method: HTTP method (GET, POST, etc.)
            description: Tool description
            agent_name: Optional agent name for context
        
        Returns:
            LangChain tool instance
        """
        @tool
        def api_query_tool(
            params: Annotated[str, "Query parameters as JSON string"],
            headers: Annotated[Optional[str], "Optional headers as JSON string"] = None
        ) -> str:
            """Query an API endpoint."""
            try:
                # Parse parameters
                query_params = json.loads(params) if isinstance(params, str) else params
                query_headers = json.loads(headers) if headers and isinstance(headers, str) else (headers or {})
                
                # Get API credentials if context manager available
                if self.context_manager and agent_name:
                    api_info = self.context_manager.get_api_info(agent_name, api_name)
                    if api_info:
                        api_config = api_info[0].get("config", {})
                        credentials = api_info[0].get("credentials", {})
                        
                        # Add API key to headers if available
                        if "api_key" in credentials:
                            query_headers["Authorization"] = f"Bearer {credentials['api_key']}"
                        elif "api_key_header" in api_config and "api_key" in credentials:
                            query_headers[api_config["api_key_header"]] = credentials["api_key"]
                        
                        # Use base URL from config if endpoint is relative
                        if "base_url" in api_config and not endpoint.startswith("http"):
                            endpoint = f"{api_config['base_url']}/{endpoint.lstrip('/')}"
                
                # Make request
                if method.upper() == "GET":
                    response = requests.get(endpoint, params=query_params, headers=query_headers, timeout=30)
                elif method.upper() == "POST":
                    response = requests.post(endpoint, json=query_params, headers=query_headers, timeout=30)
                elif method.upper() == "PUT":
                    response = requests.put(endpoint, json=query_params, headers=query_headers, timeout=30)
                elif method.upper() == "DELETE":
                    response = requests.delete(endpoint, params=query_params, headers=query_headers, timeout=30)
                else:
                    return f"Unsupported HTTP method: {method}"
                
                response.raise_for_status()
                
                # Update API usage if context manager available
                if self.context_manager and agent_name:
                    self.context_manager.update_api_usage(agent_name, api_name)
                
                return json.dumps(response.json(), indent=2)
                
            except requests.exceptions.RequestException as e:
                return f"API request error: {str(e)}"
            except json.JSONDecodeError as e:
                return f"JSON parsing error: {str(e)}"
            except Exception as e:
                return f"Error: {str(e)}"
        
        # Set tool name and description
        api_query_tool.name = f"{api_name}_query"
        api_query_tool.description = description or f"Query {api_name} API endpoint: {endpoint}"
        
        return api_query_tool
    
    def create_context_query_tool(
        self,
        agent_name: str,
        context_manager
    ) -> BaseTool:
        """
        Create a tool for querying agent context/knowledge base.
        
        Args:
            agent_name: Name of the agent
            context_manager: AgentContextManager instance
        
        Returns:
            LangChain tool instance
        """
        @tool
        def query_agent_context(
            query: Annotated[str, "Search query to find relevant knowledge"],
            category: Annotated[Optional[str], "Optional category to filter by"] = None,
            limit: Annotated[int, "Maximum number of results"] = 5
        ) -> str:
            """Query the agent's knowledge base and context."""
            try:
                results = context_manager.retrieve_knowledge(
                    agent_name=agent_name,
                    category=category,
                    query=query,
                    limit=limit
                )
                
                if not results:
                    return f"No knowledge found for query: {query}"
                
                formatted_results = []
                for result in results:
                    formatted_results.append({
                        "id": result.get("id"),
                        "category": result.get("category"),
                        "knowledge": result.get("knowledge"),
                        "timestamp": result.get("metadata", {}).get("timestamp")
                    })
                
                return json.dumps(formatted_results, indent=2)
            except Exception as e:
                return f"Error querying context: {str(e)}"
        
        query_agent_context.name = f"{agent_name}_context_query"
        query_agent_context.description = f"Query {agent_name}'s knowledge base and stored context"
        
        return query_agent_context
    
    def create_context_store_tool(
        self,
        agent_name: str,
        context_manager
    ) -> BaseTool:
        """
        Create a tool for storing information in agent context.
        
        Args:
            agent_name: Name of the agent
            context_manager: AgentContextManager instance
        
        Returns:
            LangChain tool instance
        """
        @tool
        def store_agent_context(
            knowledge: Annotated[str, "Knowledge/information to store as JSON string"],
            category: Annotated[Optional[str], "Optional category for organizing"] = None,
            source: Annotated[Optional[str], "Source of the information"] = None
        ) -> str:
            """Store information in the agent's knowledge base."""
            try:
                knowledge_dict = json.loads(knowledge) if isinstance(knowledge, str) else knowledge
                
                metadata = {}
                if source:
                    metadata["source"] = source
                
                knowledge_id = context_manager.store_knowledge(
                    agent_name=agent_name,
                    knowledge=knowledge_dict,
                    category=category,
                    metadata=metadata
                )
                
                return f"Successfully stored knowledge with ID: {knowledge_id}"
            except json.JSONDecodeError as e:
                return f"Invalid JSON format: {str(e)}"
            except Exception as e:
                return f"Error storing context: {str(e)}"
        
        store_agent_context.name = f"{agent_name}_context_store"
        store_agent_context.description = f"Store information in {agent_name}'s knowledge base"
        
        return store_agent_context
    
    def register_api_tools_for_agent(
        self,
        agent_name: str,
        context_manager
    ):
        """
        Register API query tools for an agent based on stored API configurations.
        
        Args:
            agent_name: Name of the agent
            context_manager: AgentContextManager instance
        """
        api_infos = context_manager.get_api_info(agent_name)
        
        for api_info in api_infos:
            api_name = api_info.get("api_name")
            api_config = api_info.get("config", {})
            
            # Create tools for each endpoint
            endpoints = api_config.get("endpoints", [])
            for endpoint_config in endpoints:
                endpoint = endpoint_config.get("path", "")
                method = endpoint_config.get("method", "GET")
                description = endpoint_config.get("description", f"Query {api_name} {endpoint}")
                
                tool = self.create_api_query_tool(
                    api_name=api_name,
                    endpoint=endpoint,
                    method=method,
                    description=description,
                    agent_name=agent_name
                )
                
                self.register_tool(tool, [agent_name])
    
    def setup_agent_tools(
        self,
        agent_name: str,
        context_manager,
        base_tools: Optional[List[BaseTool]] = None
    ) -> List[BaseTool]:
        """
        Set up all tools for an agent (base tools + context tools + API tools).
        
        Args:
            agent_name: Name of the agent
            context_manager: AgentContextManager instance
            base_tools: Optional list of base tools to include
        
        Returns:
            List of all tools for the agent
        """
        tools = []
        
        # Add base tools
        if base_tools:
            tools.extend(base_tools)
        
        # Add context query tool
        context_query_tool = self.create_context_query_tool(agent_name, context_manager)
        tools.append(context_query_tool)
        
        # Add context store tool
        context_store_tool = self.create_context_store_tool(agent_name, context_manager)
        tools.append(context_store_tool)
        
        # Register and add API tools
        self.register_api_tools_for_agent(agent_name, context_manager)
        api_tools = self.get_agent_tools(agent_name)
        tools.extend(api_tools)
        
        return tools

