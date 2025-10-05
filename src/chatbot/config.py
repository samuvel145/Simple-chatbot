"""
Configuration module for the Gemini Chatbot.
"""

import os
from typing import Optional


class Config:
    """Configuration class for the Gemini Chatbot."""
    
    # API Configuration
    GEMINI_API_KEY: str = "AIzaSyCCzyBjjaQsnMC40DN29bVS9a_BWPStPVI"
    
    # Model Configuration
    DEFAULT_MODEL: str = "models/gemini-2.5-flash-preview-05-20"
    
    # Chat Configuration
    TYPING_DELAY: float = 0.3
    TYPING_DOTS: int = 3
    
    # UI Configuration
    WELCOME_BORDER_CHAR: str = "🤖"
    BORDER_LENGTH: int = 50
    
    # Commands
    EXIT_COMMANDS: list = ['quit', 'exit', 'bye', 'q']
    HELP_COMMAND: str = 'help'
    STATS_COMMAND: str = 'stats'
    CLEAR_COMMAND: str = 'clear'
    
    @classmethod
    def get_api_key(cls) -> str:
        """Get the Gemini API key."""
        # Try to get from environment variable first
        env_key = os.getenv("GEMINI_API_KEY")
        if env_key:
            return env_key
        return cls.GEMINI_API_KEY
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate the configuration."""
        api_key = cls.get_api_key()
        if not api_key or len(api_key) < 10:
            raise ValueError("❌ Invalid API key. Please check your configuration.")
        return True
