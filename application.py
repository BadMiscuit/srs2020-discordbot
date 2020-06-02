import discord
from config import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_voice_state_update(member, before, after):
    if (before.channel == None  and after.channel != None):
        print(member.name + " just connected to " + after.channel.name)
    else:
        print("foo")
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
