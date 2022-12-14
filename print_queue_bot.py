import discord
from discord.ext import commands
import os
import win32api

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    for attachment in message.attachments:
        if attachment.filename.endswith('.pdf'):
            await attachment.save(os.path.join(os.path.dirname(__file__), 'temp.pdf'))
            
            win32api.ShellExecute(0, 'print', os.path.join(os.path.dirname(__file__), 'temp.pdf'), None, '.', 0)

bot.run('YOUR_BOT_TOKEN')