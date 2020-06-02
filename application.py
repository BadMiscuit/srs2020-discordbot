import discord
from config import *
import time
import asyncio
from datetime import datetime
from gtts import gTTS
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(client))

@client.event
async def on_voice_state_update(member, before, after):
    if (member.id != 675345725512613899):
        if (after.channel != None and before.channel != after.channel):
            print("{0}: {1} joined {2}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), member.name, after.channel.name))
            try:
                voice_client = await after.channel.connect()
                msg = "{0} a rejoint le canal".format(member.name)
                sound = gTTS(text=msg, lang='fr', slow=False)
                filename = "voice_{0}.mp3".format(random.randint(0, 1024))
                sound.save(filename)
                try:
                    voice_client.play(discord.FFmpegPCMAudio(filename))
                    print("Ok")
                except Exception as e:
                    print(str(e))
            finally:
                await voice_client.disconnect()
        elif (before.channel != None and after.channel != before.channel):
            print("{0}: {1} left {2}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), member.name, before.channel.name))
    return

'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
'''
client.run(TOKEN)
