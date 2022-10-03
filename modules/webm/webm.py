# General cog imports
import discord

from discord.ext import commands

# Specific cog imports
import re
from discord.ext.commands import has_permissions
from utils.util import guild_only, members_only, logtrace, owner_dm_only

class WebmCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    @members_only()
    @guild_only()
    async def on_message(self, ctx):
        if (str(ctx.author) == "Uptime#0761"):
            return
        try:
            regex = re.compile("^https://img-9gag-fun\.9cache\.com/photo/[a-zA-Z0-9]+_460sv")
            match = regex.findall(ctx.content)
            if (len(match) > 0 and match[0] != ctx.content[:-4]):
                await ctx.channel.send(match[0] + ".mp4")
                await ctx.add_reaction("\N{White Heavy Check Mark}")
        except Exception as e:
            await logtrace(ctx, e)
            await ctx.add_reaction("\N{Cross Mark}")


async def setup(bot):
    await bot.add_cog(WebmCog(bot))
