import discord
from config import *
import asyncio
from datetime import datetime
from gtts import gTTS
import random
import os

client = discord.Client()

async def play(voice, filename):
    voice.play(discord.FFmpegPCMAudio(filename))
    while (True):
        if not voice.is_playing():
            await voice.disconnect()
            break
    os.remove(filename)
    return

async def leave():
    for e in client.voice_clients:
        try:
            if (e.is_playing()):
                e.stop()
            await e.disconnect()
            break
        except:
            continue

def tts(name):
    msg = "{0} a rejoint le canal".format(name)
    sound = gTTS(text=msg, lang='fr', slow=False)
    filename = "voice_{0}.mp3".format(random.randint(0, 16))
    sound.save(filename)
    return filename

@client.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(client))

@client.event
async def on_voice_state_update(member, before, after):
    if (member.id != CLIENT_ID):
        if (after.channel != None and before.channel != after.channel):
            print("{0}: {1} joined {2}".format(
                datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 
                member.display_name, after.channel.name))
            await leave()
            filename = tts(member.display_name)
            try:
                voice = await after.channel.connect()
                await play(voice, filename)
            except discord.ClientException:
                await leave()
        elif (before.channel != None and after.channel != before.channel):
            print("{0}: {1} left {2}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), member.name, before.channel.name))
    return

client.run(TOKEN)
