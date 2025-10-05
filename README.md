# Gemini Chatbot

A modular, interactive chatbot powered by Google's Gemini AI.

## Features

- 🤖 Interactive conversation with Gemini AI
- 📊 Conversation statistics tracking
- 🧹 Clear conversation history
- 💬 Typing indicators for better UX
- 🎯 Multiple exit commands
- 📚 Built-in help system
- 🏗️ Modular, maintainable codebase

## Project Structure

```
gemini_chatbot/
├── src/
│   └── chatbot/
│       ├── __init__.py      # Package initialization
│       ├── chatbot.py       # Main chatbot logic
│       ├── config.py        # Configuration management
│       └── ui.py           # User interface handling
├── main.py                 # Application entry point
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Setup

1. Make sure you have Python 3.7+ installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. The API key is already configured in the code

## Usage

Run the chatbot:
```bash
python main.py
```

### Available Commands

- `help` - Show available commands
- `stats` - Display conversation statistics
- `clear` - Clear conversation history
- `quit`, `exit`, `bye`, or `q` - End the conversation
- `Ctrl+C` - Force exit

### Example Conversation

```
🤖================================================🤖
🤖           GEMINI CHATBOT v1.0           🤖
🤖================================================🤖
🤖 Powered by Google's Gemini AI
🤖 Type 'help' for available commands
🤖 Type 'quit', 'exit', or 'bye' to end the conversation
🤖================================================🤖

👤 You: Hello!
🤖 Gemini: ... Hello! How can I help you today?

👤 You: help
📚 Available Commands:
  • help     - Show this help message
  • stats    - Show conversation statistics
  • clear    - Clear conversation history
  • quit/exit/bye - End the conversation
  • Just type normally to chat with Gemini!

👤 You: quit
🤖 Gemini: Goodbye! Have a great day!
```

## Architecture

The application is built with a modular architecture:

- **`chatbot.py`**: Core chatbot logic and Gemini AI integration
- **`config.py`**: Configuration management and settings
- **`ui.py`**: User interface handling and display logic
- **`main.py`**: Application entry point

## Configuration

The API key and model configuration are managed in `src/chatbot/config.py`. The chatbot uses the Gemini 2.5 Flash model for optimal performance.

## Requirements

- `google-generativeai>=0.8.0`
