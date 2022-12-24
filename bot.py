import os
import re
from dotenv import load_dotenv
from helper import generator
import discord
from discord.ext import commands, tasks
from datetime import datetime
import random
import sys


print(r'''
  ______         _    _      _       
 |  ____|       | |  | |    (_)      
 | |__ ___  _ __| | __ | ___ _ _ __  
 |  __/ _ \| '__| |/ / |/ _ \ | '_ \ 
 | | | (_) | |  |   <| |  __/ | | | |
 |_|  \___/|_|  |_|\_\_|\___|_|_| |_|

''')

load_dotenv()


TOKEN_DISCORD = os.getenv('TOKEN_DISCORD')
PROFILE_URL = os.getenv('PROFILE_URL')
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="Forklein Generator"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    userMessage = message.content
    
    if(userMessage.startswith('!generateAI')):
        checkString = re.split('! |, |-', userMessage)
        if(checkString[0].strip() == '!generateAI'):
            await message.channel.send(f"Ciao **{message.author}** sto generando l\'immagine!")
            embed = discord.Embed(description="Ecco l\'immagine fanne buon uso!", timestamp=datetime.utcnow(), colour=13434624)
            embed.set_image(url=generator.generateImage(checkString[1]))
            embed.set_author(name=bot.user)
            embed.set_thumbnail(url=PROFILE_URL)
            embed.set_footer(text=bot.user, icon_url=PROFILE_URL)
            await message.channel.send(embed=embed)
            print('Embed inviato correttamente')
        else:
            await message.channel.send(f"Ciao **{message.author}** digita correttamente il comando!")

bot.run(TOKEN_DISCORD)
