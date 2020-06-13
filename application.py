import discord
from config import *
import asyncio
from gtts import gTTS
import os
import time
from datetime import datetime

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(client))
    return

async def play(voice, filename):
    time.sleep(0.5)
    print("[{0}]: Playing {1}".format(
        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        filename))
    voice.play(discord.FFmpegPCMAudio(filename))
    while (voice.is_playing()):
        time.sleep(0.5)
    print("[{0}]: Played {1}".format(
        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        filename))
    return

async def leave(voice=None):
    if (len(client.voice_clients) < 1):
        return
    if (voice == None and len(client.voice_clients) > 0):
        voice = client.voice_clients[0]
    if (voice.is_playing()):
        voice.stop()
    await voice.disconnect(force=True)
    return

def tts(name):
    filename = "files/voice_{0}.mp3".format(name)
    if os.path.exists(filename):
        return filename
    msg = "Bonjour {0}".format(name)
    sound = gTTS(text=msg, lang='fr', slow=False)
    sound.save(filename)
    return filename


@client.event
async def on_voice_state_update(member, before, after):
    if (not member.bot and member.id != CLIENT_ID):
        if (after.channel != None and before.channel != after.channel):
            await leave()
            filename = tts(member.display_name)
            try:
                print("Joining {0}".format(after.channel))
                voice = await after.channel.connect()
                print("Joined {0}".format(after.channel))
                await play(voice, filename)
                await leave(voice)
            except discord.ClientException:
                print("Already in voice")
                await leave()
    return

client.run(TOKEN)
