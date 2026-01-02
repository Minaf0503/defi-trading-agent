"""
RSS Feed Utilities for News Analysis
Fetches and parses RSS feeds from news sources
"""

import feedparser
import requests
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import re
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
)
def fetch_rss_feed(feed_url: str, timeout: int = 30) -> feedparser.FeedParserDict:
    """
    Fetch and parse an RSS feed.
    
    Args:
        feed_url: URL of the RSS feed
        timeout: Request timeout in seconds
    
    Returns:
        Parsed feed object
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/101.0.4951.54 Safari/537.36"
        )
    }
    
    response = requests.get(feed_url, headers=headers, timeout=timeout)
    response.raise_for_status()
    
    feed = feedparser.parse(response.content)
    return feed


def parse_rss_entries(feed: feedparser.FeedParserDict) -> List[Dict]:
    """
    Parse RSS feed entries into a structured format.
    
    Args:
        feed: Parsed feed object
    
    Returns:
        List of article dictionaries
    """
    articles = []
    
    for entry in feed.entries:
        # Parse published date
        published_date = None
        if hasattr(entry, 'published_parsed') and entry.published_parsed:
            published_date = datetime(*entry.published_parsed[:6])
        elif hasattr(entry, 'published'):
            try:
                published_date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z')
            except:
                try:
                    published_date = datetime.strptime(entry.published, '%Y-%m-%dT%H:%M:%S%z')
                except:
                    pass
        
        # Extract summary/description
        summary = ""
        if hasattr(entry, 'summary'):
            summary = entry.summary
        elif hasattr(entry, 'description'):
            summary = entry.description
        
        # Clean HTML from summary
        if summary:
            soup = BeautifulSoup(summary, 'html.parser')
            summary = soup.get_text()
        
        article = {
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "summary": summary,
            "published": published_date.isoformat() if published_date else None,
            "published_timestamp": published_date.timestamp() if published_date else None,
            "author": entry.get("author", ""),
            "tags": [tag.get("term", "") for tag in entry.get("tags", [])],
        }
        
        articles.append(article)
    
    return articles


def filter_articles_by_asset(
    articles: List[Dict],
    asset_symbol: str,
    asset_name: Optional[str] = None,
    case_sensitive: bool = False
) -> List[Dict]:
    """
    Filter articles that mention a specific asset.
    
    Args:
        articles: List of article dictionaries
        asset_symbol: Asset symbol (e.g., "BTC", "ETH", "UNI")
        asset_name: Optional asset name (e.g., "Bitcoin", "Ethereum")
        case_sensitive: Whether to perform case-sensitive matching
    
    Returns:
        Filtered list of articles
    """
    if not case_sensitive:
        asset_symbol = asset_symbol.upper()
        if asset_name:
            asset_name = asset_name.lower()
    
    filtered = []
    
    for article in articles:
        title = article.get("title", "")
        summary = article.get("summary", "")
        tags = " ".join(article.get("tags", []))
        
        # Combine all text for searching
        search_text = f"{title} {summary} {tags}"
        
        if not case_sensitive:
            search_text = search_text.upper()
            title = title.upper()
            summary = summary.upper()
        
        # Check for asset symbol
        # Use word boundaries to avoid partial matches (e.g., "BTC" not matching "ABTC")
        symbol_pattern = r'\b' + re.escape(asset_symbol) + r'\b'
        if re.search(symbol_pattern, search_text):
            filtered.append(article)
            continue
        
        # Check for asset name if provided
        if asset_name:
            name_pattern = r'\b' + re.escape(asset_name) + r'\b'
            if re.search(name_pattern, search_text, re.IGNORECASE):
                filtered.append(article)
                continue
    
    return filtered


def filter_articles_by_date(
    articles: List[Dict],
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    days_back: Optional[int] = None
) -> List[Dict]:
    """
    Filter articles by date range.
    
    Args:
        articles: List of article dictionaries
        start_date: Start date for filtering
        end_date: End date for filtering
        days_back: Number of days to look back from end_date
    
    Returns:
        Filtered list of articles
    """
    if days_back and end_date:
        start_date = end_date - timedelta(days=days_back)
    
    filtered = []
    
    for article in articles:
        published_timestamp = article.get("published_timestamp")
        if not published_timestamp:
            # If no date, include it (or exclude based on preference)
            continue
        
        published_date = datetime.fromtimestamp(published_timestamp)
        
        if start_date and published_date < start_date:
            continue
        
        if end_date and published_date > end_date:
            continue
        
        filtered.append(article)
    
    return filtered


def fetch_dlnews_rss(
    asset_symbol: Optional[str] = None,
    asset_name: Optional[str] = None,
    days_back: Optional[int] = 7
) -> List[Dict]:
    """
    Fetch and filter articles from DL News RSS feed.
    
    Args:
        asset_symbol: Asset symbol to filter for (e.g., "BTC", "ETH")
        asset_name: Asset name to filter for (e.g., "Bitcoin", "Ethereum")
        days_back: Number of days to look back
    
    Returns:
        List of filtered articles
    """
    feed_url = "https://www.dlnews.com/rss/"
    
    try:
        feed = fetch_rss_feed(feed_url)
        articles = parse_rss_entries(feed)
        
        # Filter by date if specified
        if days_back:
            end_date = datetime.now()
            articles = filter_articles_by_date(articles, days_back=days_back, end_date=end_date)
        
        # Filter by asset if specified
        if asset_symbol or asset_name:
            articles = filter_articles_by_asset(articles, asset_symbol or "", asset_name)
        
        return articles
    
    except Exception as e:
        print(f"Error fetching DL News RSS feed: {e}")
        return []


def fetch_article_content(article_url: str, timeout: int = 30) -> Optional[str]:
    """
    Fetch full article content from URL.
    
    Args:
        article_url: URL of the article
        timeout: Request timeout in seconds
    
    Returns:
        Article content text or None if failed
    """
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/101.0.4951.54 Safari/537.36"
            )
        }
        
        response = requests.get(article_url, headers=headers, timeout=timeout)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try to find main content
        # Common article content selectors
        content_selectors = [
            'article',
            '.article-content',
            '.post-content',
            '.entry-content',
            'main',
            '[role="article"]',
        ]
        
        content = None
        for selector in content_selectors:
            content_elem = soup.select_one(selector)
            if content_elem:
                content = content_elem.get_text(separator='\n', strip=True)
                break
        
        # Fallback to body if no specific content found
        if not content:
            body = soup.find('body')
            if body:
                # Remove script and style elements
                for script in body(["script", "style", "nav", "header", "footer"]):
                    script.decompose()
                content = body.get_text(separator='\n', strip=True)
        
        return content
    
    except Exception as e:
        print(f"Error fetching article content from {article_url}: {e}")
        return None

