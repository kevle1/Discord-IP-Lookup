import os
import requests
import discord
import json
import re
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # Privileged intent must be enabled in Developer Portal

client = discord.Client(intents=intents)
weather_api_key = os.environ["WEATHER_API_KEY"]
discord_api_key = os.environ["DISCORD_TOKEN"]

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="admin"))

@client.event
async def on_message(message):
    # Check if message contains an IP
    regex = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    result_list = re.findall(regex, message.content)

    result_list = list(set(result_list)) # Remove duplicates

    if result_list and len(result_list) <= 10:
        print(result_list)

        for ip in result_list:
            print(ip)
            ip_api_response = requests.get(f"http://ip-api.com/json/{ip}")
            json_ip_data = json.loads(ip_api_response.text)

            try:
                if json_ip_data["status"] == "success":
                    lat = str(json_ip_data["lat"])
                    lon = str(json_ip_data["lon"])
                    coords = lat + ", " + lon

                    embed = discord.Embed(title="IP Info", description=ip, color=0xcccccc) #Build embed
                    embed.add_field(name="Country: ", value=json_ip_data["country"], inline=False)
                    embed.add_field(name="Region/ State: ", value=json_ip_data["regionName"], inline=True)
                    embed.add_field(name="City: ", value=json_ip_data["city"], inline=True)
                    embed.add_field(name="ZIP Code: ", value=json_ip_data["zip"], inline=True)
                    embed.add_field(name="Coordinates: ", value=coords, inline=True)
                    embed.add_field(name="ISP: ", value=json_ip_data["isp"], inline=False)

                    try: #Get temperature
                        weather_api_response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={weather_api_key}&units=metric")
                        json_weather_data = json.loads(weather_api_response.text)
                        temp = str(json_weather_data["main"]["temp"]) + "°C"

                        embed.add_field(name="Temp: ", value=temp, inline=False)
                    except Exception:
                        print("Error retrieving temperature")

                    embed.set_footer(text="Powered by ip-api.com and openweathermap.org")
                    await message.channel.send(embed=embed) #Send embed
            except KeyError:
                print("Partial IP result")
            except Exception:
                print("Error")

client.run(discord_api_key) 

