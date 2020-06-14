from datetime import datetime
from gtts import gTTS
import asyncio
import discord
import os
import time

async def play(voice, filename):
    print("[{0}]: Playing {1}".format(
        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        filename))
    voice.play(discord.FFmpegPCMAudio(filename))
    while True:
        await asyncio.sleep(0.1)
        if not (voice.is_playing()):
            break
    print("[{0}]: Stopped {1}".format(
        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        filename))
    return

async def leave(client, voice=None):
    if (len(client.voice_clients) < 1):
        print("Not in voice")
        return
    if (voice == None and len(client.voice_clients) > 0):
        voice = client.voice_clients[0]
    if (voice.is_playing()):
        voice.stop()
    await voice.disconnect(force=True)
    print("Left {0}".format(voice))
    return

def tts(name):
    filename = "files/voice_{0}.mp3".format(name)
    if os.path.exists(filename):
        return filename
    msg = "Bonjour {0}".format(name)
    sound = gTTS(text=msg, lang='fr', slow=False)
    sound.save(filename)
    return filename


