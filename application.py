from announcer import *
from poll import *
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
            await leave(bot)
            filename = tts(member.display_name)
            try:
                print("Joining {0}".format(after.channel))
                voice = await after.channel.connect()
                print("Joined {0}".format(after.channel))
                await play(voice, filename)
                await leave(bot, voice)
            except discord.ClientException:
                print("Already in voice")
                await leave(bot)
    return

@bot.command()
async def poll(ctx, *args):
    if (ctx.message.channel.id != POLL_CHANNEL):
        return
    embed = create_poll(args)
    msg = await ctx.send(embed=embed)
    if (len(args) - 1 == 0):
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
    else:
        for i in range (0, len(args) - 1):
            await msg.add_reaction(alphabet[i])

bot.run(TOKEN)
