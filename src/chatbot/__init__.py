"""
Gemini Chatbot Package

A modular chatbot implementation using Google's Gemini AI.
"""

from .chatbot import GeminiChatbot
from .config import Config
from .ui import ChatUI

__version__ = "1.0.0"
__all__ = ["GeminiChatbot", "Config", "ChatUI"]
