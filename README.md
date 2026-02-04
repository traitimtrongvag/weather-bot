# Weather Bot

Weather Bot is a simple bot that helps you check current weather information and forecasts for cities worldwide. The bot uses the OpenWeatherMap API to fetch weather data and provides information in Vietnamese.

## Features

- **Current weather**: Get current weather information for a specific city.
- **Weather forecast**: Get a 5-day weather forecast for a specific city.
- **Set default city**: Set a default city so you don't need to enter the city name each time you check the weather.

## Usage

1. **Start**: Send the `/start` command to begin using the bot.
2. **Current weather**: Send `/weather <city name>` to view current weather. If you've set a default city, just send `/weather`.
3. **Weather forecast**: Send `/forecast <city name>` to view the 5-day forecast. If you've set a default city, just send `/forecast`.
4. **Set default city**: Send `/setcity <city name>` to set your default city.

## Installation

1. **Requirements**:
   - Python 3.7 or higher
   - Required libraries: `aiohttp`, `python-telegram-bot`

2. **Install dependencies**:
   ```bash
   pip install aiohttp python-telegram-bot
   ```

3. **Configuration**:
   - Create a `.env` file with these environment variables:
     ```plaintext
     API_KEY=<YOUR_OPENWEATHERMAP_API_KEY>
     BOT_TOKEN=<YOUR_TELEGRAM_BOT_TOKEN>
     ```
   - Replace `<YOUR_OPENWEATHERMAP_API_KEY>` and `<YOUR_TELEGRAM_BOT_TOKEN>` with your actual OpenWeatherMap API key and Telegram bot token.

4. **Run the bot**:
   ```bash
   python Main.py
   ```

## Contribution

If you want to contribute to the project, please create a pull request. All contributions are welcome!
