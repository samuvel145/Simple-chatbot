"""
User Interface module for the Gemini Chatbot.
"""

import time
from datetime import datetime
from typing import Optional
from .config import Config


class ChatUI:
    """User Interface handler for the chatbot."""
    
    def __init__(self):
        self.start_time = datetime.now()
        self.message_count = 0
    
    def show_welcome(self) -> None:
        """Display welcome message and instructions."""
        border = Config.WELCOME_BORDER_CHAR * Config.BORDER_LENGTH
        print(f"{Config.WELCOME_BORDER_CHAR}{border}{Config.WELCOME_BORDER_CHAR}")
        print(f"{Config.WELCOME_BORDER_CHAR}           GEMINI CHATBOT v1.0           {Config.WELCOME_BORDER_CHAR}")
        print(f"{Config.WELCOME_BORDER_CHAR}{border}{Config.WELCOME_BORDER_CHAR}")
        print(f"{Config.WELCOME_BORDER_CHAR} Powered by Google's Gemini AI")
        print(f"{Config.WELCOME_BORDER_CHAR} Type '{Config.HELP_COMMAND}' for available commands")
        print(f"{Config.WELCOME_BORDER_CHAR} Type '{Config.EXIT_COMMANDS[0]}', '{Config.EXIT_COMMANDS[1]}', or '{Config.EXIT_COMMANDS[2]}' to end the conversation")
        print(f"{Config.WELCOME_BORDER_CHAR}{border}{Config.WELCOME_BORDER_CHAR}")
        print()
    
    def show_help(self) -> None:
        """Display help information."""
        print("\n📚 Available Commands:")
        print(f"  • {Config.HELP_COMMAND:<8} - Show this help message")
        print(f"  • {Config.STATS_COMMAND:<8} - Show conversation statistics")
        print(f"  • {Config.CLEAR_COMMAND:<8} - Clear conversation history")
        print(f"  • {Config.EXIT_COMMANDS[0]}/{Config.EXIT_COMMANDS[1]}/{Config.EXIT_COMMANDS[2]} - End the conversation")
        print("  • Just type normally to chat with Gemini!")
        print()
    
    def show_stats(self) -> None:
        """Display conversation statistics."""
        duration = datetime.now() - self.start_time
        print(f"\n📊 Conversation Statistics:")
        print(f"  • Messages exchanged: {self.message_count}")
        print(f"  • Session duration: {duration}")
        print(f"  • Started at: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
    
    def show_typing_indicator(self) -> None:
        """Show typing indicator."""
        print("🤖 Gemini: ", end="", flush=True)
        for i in range(Config.TYPING_DOTS):
            print(".", end="", flush=True)
            time.sleep(Config.TYPING_DELAY)
        print(" ", end="", flush=True)
    
    def show_message(self, message: str) -> None:
        """Display a message from Gemini."""
        print(message)
        self.message_count += 1
    
    def show_error(self, error: str) -> None:
        """Display an error message."""
        print(f"\n❌ Error: {error}")
        print("Please try again or type 'quit' to exit.")
    
    def show_goodbye(self) -> None:
        """Display goodbye message."""
        print("\n🤖 Gemini: Goodbye! Have a great day!")
    
    def show_clear_message(self) -> None:
        """Display conversation cleared message."""
        print("\n🧹 Conversation history cleared!")
        print()
        self.message_count = 0
    
    def get_user_input(self) -> str:
        """Get user input."""
        return input("👤 You: ").strip()
    
    def is_exit_command(self, user_input: str) -> bool:
        """Check if user input is an exit command."""
        return user_input.lower() in Config.EXIT_COMMANDS
    
    def is_help_command(self, user_input: str) -> bool:
        """Check if user input is a help command."""
        return user_input.lower() == Config.HELP_COMMAND
    
    def is_stats_command(self, user_input: str) -> bool:
        """Check if user input is a stats command."""
        return user_input.lower() == Config.STATS_COMMAND
    
    def is_clear_command(self, user_input: str) -> bool:
        """Check if user input is a clear command."""
        return user_input.lower() == Config.CLEAR_COMMAND
