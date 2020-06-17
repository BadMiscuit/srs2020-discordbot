from datetime import datetime
from gtts import gTTS
import asyncio
import discord
import os
import time

async def play(voice, filename):
    print("[{0}]: Start playing {1}".format(
        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        filename))
    voice.play(discord.FFmpegPCMAudio(filename))
    try:
        i = 0.0
        while (voice.is_playing() and voice.is_connected()):
            time.sleep(0.1)
            i += 0.1
            if (voice.is_playing() and voice.is_connected()):
                print("[{0}] Playing in {1}...".format(i, voice.channel))
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


