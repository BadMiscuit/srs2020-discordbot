import discord
from discord.ext import commands

from .config import GUILD_ID, POLL_CHANNEL, TEST_CHANNEL, LOGTRACE_CHANNEL


def srs_only():
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == GUILD_ID
    return commands.check(predicate)

def poll_only():
    async def predicate(ctx):
        return ctx.channel.id == POLL_CHANNEL or ctx.channel.id == TEST_CHANNEL
    return commands.check(predicate)

async def logtrace(ctx, msg):
    channel = ctx.guild.get_channel(LOGTRACE_CHANNEL)
    await channel.send("Error: {0}".format(msg))
