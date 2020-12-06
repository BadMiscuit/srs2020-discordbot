import discord
from discord.ext import commands

from config import *

def srs_only():
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == GUILD_ID
    return commands.check(predicate)
