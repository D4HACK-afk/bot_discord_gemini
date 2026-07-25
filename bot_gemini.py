import discord 
import os
from discord.ext import commands
from dotenv import load_dotenv
from google import genai


#*............................................................................................./
load_dotenv()
token_discord = os.getenv("token_bot")
token_IA = os.getenv("token_gemini")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
#*............................................................................................./




client.run(token_discord)
