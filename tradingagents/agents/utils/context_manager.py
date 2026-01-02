"""
Agent Context Manager
Manages knowledge base and API information for each agent
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
import hashlib


class AgentContextManager:
    """Manages context and knowledge base for each agent."""
    
    def __init__(self, base_dir: str = "agent-context", config: Optional[Dict[str, Any]] = None):
        """
        Initialize the context manager.
        
        Args:
            base_dir: Base directory for storing agent contexts
            config: Configuration dictionary
        """
        self.base_dir = Path(base_dir)
        self.config = config or {}
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories for different types of context
        self.context_types = [
            "knowledge",
            "apis",
            "tools",
            "preferences",
            "history"
        ]
        
        for context_type in self.context_types:
            (self.base_dir / context_type).mkdir(parents=True, exist_ok=True)
    
    def store_knowledge(
        self,
        agent_name: str,
        knowledge: Dict[str, Any],
        category: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Store knowledge/information for an agent.
        
        Args:
            agent_name: Name of the agent
            knowledge: Knowledge data to store (dict, list, or string)
            category: Optional category for organizing knowledge
            metadata: Optional metadata (source, timestamp, etc.)
        
        Returns:
            str: ID of the stored knowledge entry
        """
        agent_dir = self.base_dir / "knowledge" / agent_name
        agent_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate unique ID for this knowledge entry
        knowledge_str = json.dumps(knowledge, sort_keys=True)
        knowledge_id = hashlib.md5(knowledge_str.encode()).hexdigest()[:12]
        
        # Create entry with metadata
        entry = {
            "id": knowledge_id,
            "agent": agent_name,
            "category": category or "general",
            "knowledge": knowledge,
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "source": metadata.get("source", "manual") if metadata else "manual",
                **(metadata or {})
            }
        }
        
        # Save to file
        filename = f"{knowledge_id}.json"
        if category:
            category_dir = agent_dir / category
            category_dir.mkdir(parents=True, exist_ok=True)
            filepath = category_dir / filename
        else:
            filepath = agent_dir / filename
        
        with open(filepath, 'w') as f:
            json.dump(entry, f, indent=2)
        
        return knowledge_id
    
    def retrieve_knowledge(
        self,
        agent_name: str,
        category: Optional[str] = None,
        query: Optional[str] = None,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Retrieve knowledge for an agent.
        
        Args:
            agent_name: Name of the agent
            category: Optional category to filter by
            query: Optional search query (searches in knowledge content)
            limit: Maximum number of results to return
        
        Returns:
            List of knowledge entries
        """
        agent_dir = self.base_dir / "knowledge" / agent_name
        
        if not agent_dir.exists():
            return []
        
        results = []
        
        # Search in category directory or all categories
        if category:
            search_dirs = [agent_dir / category] if (agent_dir / category).exists() else []
        else:
            search_dirs = [d for d in agent_dir.iterdir() if d.is_dir()] + [agent_dir]
        
        for search_dir in search_dirs:
            if not search_dir.exists():
                continue
                
            for filepath in search_dir.glob("*.json"):
                try:
                    with open(filepath, 'r') as f:
                        entry = json.load(f)
                    
                    # Simple text search if query provided
                    if query:
                        entry_str = json.dumps(entry).lower()
                        if query.lower() not in entry_str:
                            continue
                    
                    results.append(entry)
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                    continue
        
        # Sort by timestamp (newest first) and limit
        results.sort(key=lambda x: x.get("metadata", {}).get("timestamp", ""), reverse=True)
        return results[:limit]
    
    def store_api_info(
        self,
        agent_name: str,
        api_name: str,
        api_config: Dict[str, Any],
        credentials: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Store API information for an agent.
        
        Args:
            agent_name: Name of the agent
            api_name: Name/identifier of the API
            api_config: API configuration (base_url, endpoints, etc.)
            credentials: Optional credentials (will be stored securely)
        
        Returns:
            str: ID of the stored API entry
        """
        agent_dir = self.base_dir / "apis" / agent_name
        agent_dir.mkdir(parents=True, exist_ok=True)
        
        api_entry = {
            "api_name": api_name,
            "agent": agent_name,
            "config": api_config,
            "credentials": credentials or {},
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "last_used": None
            }
        }
        
        filepath = agent_dir / f"{api_name}.json"
        with open(filepath, 'w') as f:
            json.dump(api_entry, f, indent=2)
        
        return api_name
    
    def get_api_info(
        self,
        agent_name: str,
        api_name: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get API information for an agent.
        
        Args:
            agent_name: Name of the agent
            api_name: Optional specific API name
        
        Returns:
            List of API entries
        """
        agent_dir = self.base_dir / "apis" / agent_name
        
        if not agent_dir.exists():
            return []
        
        results = []
        
        if api_name:
            filepath = agent_dir / f"{api_name}.json"
            if filepath.exists():
                try:
                    with open(filepath, 'r') as f:
                        results.append(json.load(f))
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
        else:
            for filepath in agent_dir.glob("*.json"):
                try:
                    with open(filepath, 'r') as f:
                        results.append(json.load(f))
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
        
        return results
    
    def update_api_usage(self, agent_name: str, api_name: str):
        """Update last used timestamp for an API."""
        agent_dir = self.base_dir / "apis" / agent_name
        filepath = agent_dir / f"{api_name}.json"
        
        if filepath.exists():
            try:
                with open(filepath, 'r') as f:
                    api_entry = json.load(f)
                
                api_entry["metadata"]["last_used"] = datetime.now().isoformat()
                
                with open(filepath, 'w') as f:
                    json.dump(api_entry, f, indent=2)
            except Exception as e:
                print(f"Error updating API usage: {e}")
    
    def store_tool_config(
        self,
        agent_name: str,
        tool_name: str,
        tool_config: Dict[str, Any]
    ):
        """
        Store tool configuration for an agent.
        
        Args:
            agent_name: Name of the agent
            tool_name: Name of the tool
            tool_config: Tool configuration
        """
        agent_dir = self.base_dir / "tools" / agent_name
        agent_dir.mkdir(parents=True, exist_ok=True)
        
        tool_entry = {
            "tool_name": tool_name,
            "agent": agent_name,
            "config": tool_config,
            "metadata": {
                "timestamp": datetime.now().isoformat()
            }
        }
        
        filepath = agent_dir / f"{tool_name}.json"
        with open(filepath, 'w') as f:
            json.dump(tool_entry, f, indent=2)
    
    def get_tool_configs(self, agent_name: str) -> List[Dict[str, Any]]:
        """Get all tool configurations for an agent."""
        agent_dir = self.base_dir / "tools" / agent_name
        
        if not agent_dir.exists():
            return []
        
        results = []
        for filepath in agent_dir.glob("*.json"):
            try:
                with open(filepath, 'r') as f:
                    results.append(json.load(f))
            except Exception as e:
                print(f"Error reading {filepath}: {e}")
        
        return results
    
    def store_preference(
        self,
        agent_name: str,
        preference_key: str,
        preference_value: Any
    ):
        """Store a preference for an agent."""
        agent_dir = self.base_dir / "preferences" / agent_name
        agent_dir.mkdir(parents=True, exist_ok=True)
        
        prefs_file = agent_dir / "preferences.json"
        
        if prefs_file.exists():
            with open(prefs_file, 'r') as f:
                preferences = json.load(f)
        else:
            preferences = {}
        
        preferences[preference_key] = {
            "value": preference_value,
            "updated": datetime.now().isoformat()
        }
        
        with open(prefs_file, 'w') as f:
            json.dump(preferences, f, indent=2)
    
    def get_preference(self, agent_name: str, preference_key: str, default: Any = None) -> Any:
        """Get a preference for an agent."""
        agent_dir = self.base_dir / "preferences" / agent_name
        prefs_file = agent_dir / "preferences.json"
        
        if not prefs_file.exists():
            return default
        
        try:
            with open(prefs_file, 'r') as f:
                preferences = json.load(f)
            return preferences.get(preference_key, {}).get("value", default)
        except Exception as e:
            print(f"Error reading preferences: {e}")
            return default
    
    def get_all_context(self, agent_name: str) -> Dict[str, Any]:
        """Get all context for an agent (knowledge, APIs, tools, preferences)."""
        return {
            "knowledge": self.retrieve_knowledge(agent_name, limit=100),
            "apis": self.get_api_info(agent_name),
            "tools": self.get_tool_configs(agent_name),
            "preferences": self._get_all_preferences(agent_name)
        }
    
    def _get_all_preferences(self, agent_name: str) -> Dict[str, Any]:
        """Get all preferences for an agent."""
        agent_dir = self.base_dir / "preferences" / agent_name
        prefs_file = agent_dir / "preferences.json"
        
        if not prefs_file.exists():
            return {}
        
        try:
            with open(prefs_file, 'r') as f:
                prefs = json.load(f)
            return {k: v.get("value") for k, v in prefs.items()}
        except Exception as e:
            print(f"Error reading preferences: {e}")
            return {}

