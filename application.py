import discord
from config import *
import asyncio
from datetime import datetime
from gtts import gTTS
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(client))
    return

async def play(voice, filename):
    voice.play(discord.FFmpegPCMAudio(filename))
    while (True):
        if not voice.is_playing():
            try:
                os.remove(filename)
            except:
                pass
            await voice.disconnect()
            break
    return

async def leave(voice=None):
    if (voice == None):
        for e in client.voice_clients:
            try:
                if (e.is_playing()):
                    e.stop()
                    os.remove('voice_*.mp3')
                await e.disconnect(force=True)
                break
            except:
                continue
    else:
        if (voice.is_playing()):
            voice.stop()
            os.remove('voice_*.mp3')
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
            filename = tts(member.display_name)
            try:
                voice = await after.channel.connect()
                await play(voice, filename)
            except discord.ClientException:
                await leave(voice)
    return

client.run(TOKEN)
