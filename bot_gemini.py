import discord 
import os
from discord.ext import commands
from dotenv import load_dotenv
from google import genai
import requests


#! tokens/Api's
load_dotenv()
token_discord = os.getenv("token_bot")
token_IA = os.getenv("token_gemini")

ai_client = genai.Client(api_key=token_IA)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)
#*  EVENTOS.........................................................................

#*  COMANDOS........................................................................./
#! comando $hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name='ia')
async def ia(ctx, *, pregunta):
    command_ia = await ai_client.aio.models.generate_content(
        model ="gemini-3.6-flash",
        contents = pregunta
        )
    await ctx.send(command_ia.text)
    #*............................................................................................./


bot.run(token_discord)
