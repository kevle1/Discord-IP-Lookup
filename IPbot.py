import discord
import asyncio
import re
# IP Geolocation API from ipinfo.io
import ipinfo

token = 'apikey' # Requires API key from ipinfo.io. 
handler = ipinfo.getHandler(token)

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Check if the message containts an IP 
    regex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    result = re.search(regex, message.content)
    # If the message contains an IP. Print to terminal and look it up 
    if result:
        ip = result.group()
        print(ip)
        
        # Embed Message containing result
        result = handler.getDetails(ip)
        # print(result.all)
        embed = discord.Embed(title="IP Info", description=ip, color=0xcccccc)
        embed.add_field(name="Country: ", value=result.country_name, inline=True)
        embed.add_field(name="ISP: ", value=result.org, inline=True)
        embed.add_field(name="City: ", value=result.city, inline=True)
        embed.add_field(name="Region: ", value=result.region, inline=True)
        embed.add_field(name="Postcode: ", value=result.postal, inline=True)
        embed.add_field(name="Coords: ", value=result.loc, inline=True)
        await client.send_message(message.channel, embed=embed)


client.run('apikey') # Discord Bot API key 