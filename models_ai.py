import os
from discord.ext import commands
from dotenv import load_dotenv
from google import genai
import openai
import anthropic
import ollama 
import requests
#*............................................................................../
load_dotenv()
gemini = os.getenv("token_gemini")
deepseek = os.getenv("deepseek_api_key")
grock = os.getenv("grock_api_key")
claude = os.getenv("claude_api_key")
open_ai = os.getenv("openai_api_key")
#*............................................................................./