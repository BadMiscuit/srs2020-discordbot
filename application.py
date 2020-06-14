from announcer import *
from config import *
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(client))
    return

@client.event
async def on_voice_state_update(member, before, after):
    if (not member.bot and member.id != CLIENT_ID):
        if (after.channel != None and before.channel != after.channel):
            await leave(client)
            filename = tts(member.display_name)
            try:
                print("Joining {0}".format(after.channel))
                voice = await after.channel.connect()
                print("Joined {0}".format(after.channel))
                await play(voice, filename)
                await leave(client, voice)
            except discord.ClientException:
                print("Already in voice")
                await leave(client)
    return

client.run(TOKEN)
