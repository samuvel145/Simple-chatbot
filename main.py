"""
Main entry point for the Gemini Chatbot application.
"""

import sys
from src.chatbot import GeminiChatbot


def main():
    """Main function to run the chatbot."""
    try:
        chatbot = GeminiChatbot()
        chatbot.start_chat()
    except Exception as e:
        print(f"❌ Failed to initialize chatbot: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()