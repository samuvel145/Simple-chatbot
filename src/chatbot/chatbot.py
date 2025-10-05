"""
Main chatbot module using Google's Gemini AI.
"""

import google.generativeai as genai
from .config import Config
from .ui import ChatUI


class GeminiChatbot:
    """Main chatbot class using Google's Gemini AI."""
    
    def __init__(self):
        """Initialize the chatbot."""
        # Validate configuration
        Config.validate_config()
        
        # Configure API key
        genai.configure(api_key=Config.get_api_key())
        
        # Initialize the model
        self.model = genai.GenerativeModel(model_name=Config.DEFAULT_MODEL)
        
        # Start a chat session
        self.chat = self.model.start_chat(history=[])
        
        # Initialize UI
        self.ui = ChatUI()
        
        # Show welcome message
        self.ui.show_welcome()
    
    def start_chat(self) -> None:
        """Start the interactive chat session."""
        while True:
            try:
                # Get user input
                user_input = self.ui.get_user_input()
                
                # Check for exit commands
                if self.ui.is_exit_command(user_input):
                    self.ui.show_goodbye()
                    break
                
                # Skip empty inputs
                if not user_input:
                    continue
                
                # Handle special commands
                if self.ui.is_help_command(user_input):
                    self.ui.show_help()
                    continue
                elif self.ui.is_stats_command(user_input):
                    self.ui.show_stats()
                    continue
                elif self.ui.is_clear_command(user_input):
                    self.clear_history()
                    continue
                
                # Show typing indicator and send message to Gemini
                self.ui.show_typing_indicator()
                response = self.chat.send_message(user_input)
                self.ui.show_message(response.text)
                
            except KeyboardInterrupt:
                self.ui.show_goodbye()
                break
            except Exception as e:
                self.ui.show_error(str(e))
    
    def clear_history(self) -> None:
        """Clear conversation history."""
        self.chat = self.model.start_chat(history=[])
        self.ui.show_clear_message()
    
    def get_chat_history(self) -> list:
        """Get the current chat history."""
        return self.chat.history
    
    def get_message_count(self) -> int:
        """Get the number of messages exchanged."""
        return self.ui.message_count
