import discord
from config import *
import asyncio
from datetime import datetime
from gtts import gTTS
import random
import os
import glob

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(client))
    return

async def play(voice, filename):
    voice.play(discord.FFmpegPCMAudio(filename))
    while (True):
        if not voice.is_playing():
            remove(filename)
            await leave(voice)
            break
    return

def remove(filename=None):
    if (filename == None):
        fileList = glob.glob('voice_*.mp3')
        for f in fileList:
            try:
                os.remove(f)
            except:
                continue
    else:
        try:
            os.remove(filename)
        except:
            pass
    return

async def leave(voice=None):
    if (voice == None):
        for c in client.voice_clients:
            if (c.is_playing()):
                c.stop()
            if (c.is_connected()):
                await e.disconnect()
                break
    else:
        if (voice.is_playing()):
            voice.stop()
        await voice.disconnect(force=True)
    return


def tts(name):
    msg = "{0} a rejoint le canal".format(name)
    sound = gTTS(text=msg, lang='fr', slow=False)
    filename = "voice_{0}.mp3".format(random.randint(0, 16))
    sound.save(filename)
    return filename

@client.event
async def on_voice_state_update(member, before, after):
    if (not member.bot and member.id != CLIENT_ID):
        if (after.channel != None and before.channel != after.channel):
            await leave()
            remove()
            filename = tts(member.display_name)
            try:
                voice = await after.channel.connect()
                await play(voice, filename)
            except discord.ClientException:
                await leave()
    return

client.run(TOKEN)
