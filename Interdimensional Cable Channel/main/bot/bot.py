# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from storyboard import callai
import shutil

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def cable(ctx):
    # Buffer time
    await ctx.send("```Finding a great channel...```")
    # Calls ChatGPT to find image
    prompt = callai()
    message = "```\n" + prompt + "\n```"
    # Sends message to discord  
    await ctx.send(message)


    folder = 'main/bot/images'


    # Searches google images for images of the characters and the setting
    for file in os.listdir(folder):
        f = os.path.join(folder, file)

        if os.path.isfile(f):
            # Sends images to discord
            await ctx.send(file=discord.File(r'main/bot/images/' + file))


    # Clears folder of all the images of the search
    
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
             os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
        
client.run(TOKEN)
