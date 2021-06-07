#!/usr/bin/env python3

import discord
import modules.shifumi.shifumi, modules.poll.poll, modules.announcer.announcer, modules.general.general, modules.webm.webm

from discord.ext import commands
from utils.config import TOKEN
from utils.emojis import *


bot = commands.Bot(command_prefix='/')

extensions = ['modules.shifumi.shifumi',
        'modules.poll.poll',
        'modules.announcer.announcer',
        'modules.general.general',
        'modules.webm.webm']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

@bot.event
async def on_ready():
    print('We have logged in as {0.user.name}:{0.user.id}'.format(bot))

bot.run(TOKEN)
