#!/usr/bin/env python3

from announcer import *
from poll import send_poll, poll_add_option
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
async def poll_all(ctx, *args):
    try:
        if (len(args) != 0):
            await send_poll(ctx, *args, msg="@here")
        else:
            await send_poll(ctx, *args)
    except Exception as e:
        print(str(e))
        await ctx.message.add_reaction(ctx.guild.get_emoji("pepeangry:702518264332550156"))

@bot.command()
async def poll_add(ctx, *args):
    try:
        await poll_add_option(ctx, *args)
    except Exception as e:
        print(str(e))
        await ctx.message.add_reaction(ctx.guild.get_emoji("pepeangry:702518264332550156"))

@bot.command()
async def poll(ctx, *args):
    try:
        await send_poll(ctx, *args)
    except Exception as e:
        print(str(e))
        await ctx.message.add_reaction(ctx.guild.get_emoji("pepeangry:702518264332550156"))

bot.run(TOKEN)
