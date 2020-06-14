import discord
import re


alphabet = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲',
        '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿']

def create_poll(args):
    embed = discord.Embed(colour=discord.Colour.from_rgb(254, 254, 254))
    title = ""
    description = ""
    if (len(args) == 2 or len(args) == 0):
        title = "man /poll"
        description = """
        **Sondage simple :thumbsup:/:thumbsdown:**
        poll \"Suis-je un bon bot ?\"\n
        **Sondage avec plusieurs propositions**
        /poll \"Pain au chocolat ou chocolatine ?\" \"Pain au chocolat\" \"Pain au chocolat\" """
    else:
        title = ":bar_chart: {0}".format(args[0])
        for i in range (0, len(args) - 1):
            description += "{0} {1}\n".format(alphabet[i], args[i + 1])
    embed.title, embed.description = title, description
    return embed


