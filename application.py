#!/usr/bin/env python3

from announcer import *
from poll import send_poll
from config import *
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(bot))


@bot.event
async def on_voice_state_update(member, before, after):
    if (not member.bot and member.id != CLIENT_ID):
        if (after.channel != None and before.channel != after.channel):
            await leave(bot.voice_clients)
            filename = tts(member.display_name)
            try:
                print("Joining {0}".format(after.channel))
                voice = await after.channel.connect()
                print("Joined {0}".format(after.channel))
                await play(voice, filename)
                await leave(bot.voice_clients)
            except discord.ClientException:
                print("Already in voice")
                await leave(bot.voice_clients)
            except Exception as e:
                print(str(e))
                await leave(bot.voice_clients)
    return

@bot.command()
async def test(ctx, *args):
    msg = await ctx.send(content="\N{SLIGHTLY SMILING FACE}")
    await msg.add_reaction("\N{REGIONAL INDICATOR SYMBOL LETTER D}")

@bot.command()
async def poll(ctx, *args):
    await send_poll(ctx, *args)

bot.run(TOKEN)
