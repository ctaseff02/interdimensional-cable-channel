# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from storyboard import callai

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

print(TOKEN)
print(GUILD)
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def prompt(ctx):
    prompt = callai()
    message = "```\n" + prompt + "\n```"  
    await ctx.send(message)

client.run(TOKEN)