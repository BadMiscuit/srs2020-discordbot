#!/usr/bin/env python3

import discord
import modules.shifumi.shifumi, modules.poll.poll, modules.announcer.announcer

from discord.ext import commands
from discord.ext.commands import has_permissions
from utils.config import NULL_ID, TOKEN, WRONG_CHANNEL, RIGHT_CHANNEL
from utils.emojis import *


bot = commands.Bot(command_prefix='/')

extensions = ['modules.shifumi.shifumi',
        'modules.poll.poll',
        'modules.announcer.announcer']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

@bot.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(bot))


@bot.listen()
async def on_message(message):
    for role in message.author.roles:
        if (role.id == NULL_ID):
            return
    if (message.channel.id == WRONG_CHANNEL):
        if (message.content.startswith("-play")
                or message.content.startswith(">>play")
                or message.content.startswith("--play")):
            try:
                await message.channel.send("""Mauvais canal {0} {1}""".format(\
                    bot.get_channel(RIGHT_CHANNEL).mention, PEPEANGRY))
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
