# Telegram Bot for Group Notifications

This project is a Telegram bot that sends messages to users who join a specified group. It utilizes the `python-telegram-bot` library to interact with the Telegram API.

## Project Structure

```
telegram-bot
├── src
│   ├── bot.py          # Main entry point for the Telegram bot
│   ├── handlers
│   │   └── __init__.py # Contains handler functions for bot events
│   └── config.py       # Configuration settings for the bot
├── requirements.txt     # Lists dependencies required for the project
└── README.md            # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd telegram-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the bot:
   - Open `src/config.py` and set your bot token and group ID.

4. Run the bot:
   ```
   python src/bot.py
   ```

## Usage

Once the bot is running, it will monitor the specified group for new members. When a user joins, the bot will send a welcome message or any other specified notification.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the bot.

## License

This project is licensed under the MIT License.