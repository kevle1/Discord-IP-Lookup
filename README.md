# Discord IP Lookup Bot

A Discord bot that detects IPv4 addresses in messages and responds with geolocation details (country, region, city, coordinates, ISP) and the current temperature at that location.

Supports multiple IPs in a single message (up to 10) and deduplicates results.

![Example Embed](https://i.imgur.com/EgmfuUY.png)

## Requirements

- Python 3.8+
- A Discord bot token from the [Developer Portal](https://discord.com/developers/applications)
- An API key from [OpenWeatherMap](https://openweathermap.org/)

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API keys** — copy the example env file and fill in your keys:

   ```bash
   cp .env.example .env
   ```

   Then edit `.env`:
   ```
   DISCORD_TOKEN=your_discord_bot_token
   WEATHER_API_KEY=your_openweathermap_api_key
   ```

3. **Enable privileged intents** in the [Discord Developer Portal](https://discord.com/developers/applications):
   - Select your application > **Bot** > **Privileged Gateway Intents**.
   - Enable **Message Content Intent** — this is required because the bot reads message content to detect IP addresses.

4. **Invite the bot** to your server with the `Send Messages` and `Read Message History` permissions.

5. **Run the bot:**

   ```bash
   python bot.py
   ```

## APIs Used

- [ip-api.com](http://ip-api.com) — IP geolocation (free tier, no key required)
- [OpenWeatherMap](https://openweathermap.org/) — current temperature at coordinates

