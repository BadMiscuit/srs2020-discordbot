# General cog imports
import discord

from discord.ext import commands

# Specific cog imports
import random

from discord.ext.commands import has_permissions
from utils.util import guild_only, members_only, logtrace
from utils.config import NULL_ID, WRONG_CHANNEL, RIGHT_CHANNEL
from utils.emojis import pepelove, zoglu, zoglon

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cursed = [ "uwu", "UwU", "owo", "0w0", "OwO", "'w'", ":3", "^w^" ]
        self.goodbot = [ "good bot", "good robot", "bon robot", "bon bot" ]
        self.badbot = [ "bad bot", "méchant bot", "sale bot", "mauvais bot" ]


    @commands.Cog.listener()
    @members_only()
    @guild_only()
    async def on_message(self, ctx):
        if (ctx.channel.id == WRONG_CHANNEL):
            if (ctx.content.startswith("-play")
                    or ctx.content.startswith(">>play")
                    or ctx.content.startswith("--play")):
                try:
                    await ctx.channel.send("""Le bon canal c'est celui là {0}""".format(\
                        self.bot.get_channel(RIGHT_CHANNEL).mention))
                except Exception as e:
                    await logtrace(ctx, e)
        elif (ctx.content.lower().startswith("je suis ")):
            try:
                nickname = ctx.content.replace("Je suis ", "", 1).replace("je suis ", "", 1)
                await ctx.author.edit(nick=nickname)
                await ctx.add_reaction("\N{White Heavy Check Mark}")
            except Exception as e:
                await logtrace(ctx, e)
                await ctx.add_reaction("\N{Cross Mark}")
        elif (bool(set(self.cursed).intersection(ctx.content.split()))):
            try:
                await ctx.reply("Pas de weeb autorisé.")
                await ctx.add_reaction("\N{Hammer}")
            except Exception as e:
                await logtrace(ctx, e)
        elif (ctx.content.lower() in self.goodbot):
            try:
                await ctx.reply("Merci")
                await ctx.add_reaction(self.bot.get_emoji(random.choice([pepelove, zoglu, zoglon])[1]))
            except Exception as e:
                await logtrace(ctx, e)
        elif (ctx.content.lower() in self.badbot):
            try:
                await ctx.reply("Pourquoi <:{0}:{1}> ?".format(pepecry[0], pepecry[1]))
                await ctx.add_reaction(self.bot.get_emoji(pepecry[1]))
            except Exception as e:
                await logtrace(ctx, e)

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


def setup(bot):
    bot.add_cog(GeneralCog(bot))
