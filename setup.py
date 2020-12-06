#!/usr/bin/env python3

from announcer import *
from poll import send_poll, poll_add_option
from config import *
from announcer import *
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


import random
import rstr

import cogs.shifumi

bot = commands.Bot(command_prefix='/')

if __name__ == '__main__':
    bot.load_extension('cogs.shifumi')

@bot.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(bot))

@bot.event
async def on_voice_state_update(member, before, after):
    if (not member.bot and member.id != CLIENT_ID):
        if (after.channel != None and before.channel != after.channel):
            await leave(bot.voice_clients)
            filename = tts(member.display_name)
            print("File created")
            try:
                voice = await after.channel.connect()
                print("Joined {0}".format(after.channel))
                await play(voice, filename)
                await leave(bot.voice_clients, voice)
            except discord.ClientException:
                print("Error trying to join {0}: Already in voice".format(after.channel))
                await leave(bot.voice_clients)
            except Exception as e:
                print("Foo " + str(e))
                await leave(bot.voice_clients)

@bot.command()
async def poll_all(ctx, *args):
    try:
        if (len(args) != 0):
            await send_poll(ctx, *args, msg="@here")
        else:
            await send_poll(ctx, *args)
    except Exception as e:
        print(str(e))
        await ctx.message.add_reaction(\
                ctx.guild.get_emoji("pepeangry:702518264332550156"))

@bot.command()
async def poll_add(ctx, *args):
    try:
        await poll_add_option(ctx, *args)
    except Exception as e:
        print(str(e))
        await ctx.message.add_reaction(\
                ctx.guild.get_emoji("pepeangry:702518264332550156"))

@bot.command()
async def poll(ctx, *args):
    try:
        await send_poll(ctx, *args)
    except Exception as e:
        print(str(e))
        await ctx.message.add_reaction(\
                ctx.guild.get_emoji("pepeangry:702518264332550156"))

@bot.listen()
async def on_message(message):
    for role in message.author.roles:
        if (role.id == NULL_ID):
            return
    if (message.channel.id == WRONG_CHAN):
        if (message.content.startswith("-play")
                or message.content.startswith(">>play")
                or message.content.startswith("--play")):
            try:
                await message.channel.send("""Mauvais canal {0} {1}""".format(\
                    bot.get_channel(RIGHT_CHAN).mention, PEPEANGRY))
            except Exception as e:
                print(str(e))
    elif (message.content.startswith("Je suis ")):
        try:
            nickname = message.content.replace("Je suis ", "", 1)
            await message.author.edit(nick=nickname)
            await message.add_reaction("\N{White Heavy Check Mark}")
        except Exception as e:
            print("Error in Je suis : {0}".format(str(e)))
            await message.add_reaction("\N{Cross Mark}")

'''
async def random_ping():
    await bot.wait_until_ready()
    random_delay = random.randint(120,2700)
    guild = bot.get_guild(GUILD_ID)
    member = guild.get_member(PING_USER)
    offline_delay = 300
    while not bot.is_closed():
        try:
            if (member.status == "offline"):
                offline_delay += 100
                await asyncio.sleep(offline_delay)
            else:
                offline_delay = 300
                random_delay = random.randint(120,1200)

                overwrites = {
                        guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        guild.me: discord.PermissionOverwrite(read_messages=True),
                        member: discord.PermissionOverwrite(read_messages=True)
                        }

                channel = await guild.create_text_channel(\
                        name=rstr.xeger(r'[a-z0-9\-]{15}'),\
                        overwrites=overwrites)

                await channel.send("<@{0}> t puni".format(PING_USER))

                await asyncio.sleep(5)

                await channel.delete()
        except Exception as e:
            print(str(e))
        await asyncio.sleep(random_delay)

bot.loop.create_task(random_ping())
'''
bot.run(TOKEN)
