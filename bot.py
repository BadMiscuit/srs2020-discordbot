#!/usr/bin/env python3

import discord
import modules.shifumi.shifumi, modules.poll.poll, modules.announcer.announcer, modules.general.general, modules.webm.webm
import asyncio

from discord.ext import commands
from utils.config import TOKEN
from utils.emojis import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/',
        intents=intents)

extensions = ['modules.shifumi.shifumi',
        'modules.poll.poll',
        'modules.announcer.announcer',
        'modules.general.general',
        'modules.webm.webm']

@bot.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(bot))

@bot.command()
async def load(extension_name: str):
    try:
        await bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        return

async def main():
    async with bot:
        for ext in extensions:
            try:
                await load(ext)
            except Exception as e:
                print(e)
        await bot.start(TOKEN)

asyncio.run(main())
