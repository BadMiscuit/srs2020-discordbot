#!/usr/bin/env python3

from announcer import *
from poll import send_poll
from config import *
from announcer import announce
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(bot))

@bot.event
async def on_voice_state_update(member, before, after):
    await announce(bot.voice_clients, member, before, after)

@bot.command()
async def poll(ctx, *args):
    await send_poll(ctx, *args)

bot.run(TOKEN)
