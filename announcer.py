from datetime import datetime
from gtts import gTTS
import asyncio
import discord
import os
import time

async def play(voice, filename):
    time.sleep(0.5)
    print("[{0}]: Start playing {1}".format(
        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        filename))
    voice.play(discord.FFmpegPCMAudio(filename))
    try:
        i = 0.0
        while True:
            if (not voice.is_playing() or not voice.is_connected()):
                break
            time.sleep(0.1)
            print("[{0}] Playing in {1}...".format(i, voice.channel))
            i += 0.1
    except Exception as e:
        print("Error playing {0}".format(filename))
    print("[{0}]: Stopped {1}".format(
            datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            filename))
    return

async def leave(voices):
    if (len(voices) < 1):
        print("Not in voice")
        return
    if (voices[0].is_playing()):
        voices[0].stop()
    await voices[0].disconnect(force=True)
    print("Left {0}".format(voices[0].channel))
    return

def tts(name):
    filename = "files/voice_{0}.mp3".format(name)
    if os.path.exists(filename):
        return filename
    msg = "Bonjour {0}".format(name)
    sound = gTTS(text=msg, lang='fr', slow=False)
    sound.save(filename)
    return filename


