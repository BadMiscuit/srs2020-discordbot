import discord
from config import POLL_CHANNEL, TEST_CHANNEL, PEPECRY
from classes import *

alphabet = ['\N{REGIONAL INDICATOR SYMBOL LETTER A}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER B}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER C}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER D}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER E}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER F}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER G}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER H}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER I}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER J}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER K}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER L}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER M}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER N}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER O}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER P}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER Q}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER R}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER S}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER T}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER U}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER V}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER W}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER X}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER Y}',
        '\N{REGIONAL INDICATOR SYMBOL LETTER Z}']

async def send_poll(ctx, *args, msg=""):
    if (ctx.message.channel.id != POLL_CHANNEL
            and ctx.message.channel.id != TEST_CHANNEL):
        return
    if (len(args) == 0):
        await ctx.send(embed=man_poll())
        return
    try:
        if (len(args) > 27):
            await ctx.send("Arrête d'essayer de me casser {0}".format(PEPECRY))
            return
        poll = create_poll(args)
        if (len(poll.options) == 1):
            await ctx.send("Crée un sondage avec des options différentes")
            return
        msg = await ctx.send(content=msg, embed=poll.to_embed())
        set_poll(msg.id, poll)
        for option in poll.options:
            await msg.add_reaction(option.emoji)
    except Exception as e:
        print(str(e))
        await ctx.send("Arrête d'essayer de me casser {0}".format(PEPECRY))
        print(PEPECRY)

def create_poll(args):
    poll = Poll(title=args[0])
    #Simple Poll
    if (len(args) == 1):
        poll.add_option(Option(emoji="\N{Thumbs Up Sign}"))
        poll.add_option(Option(emoji="\N{Thumbs Down Sign}"))
    #Simple Poll 2
    elif (len(args) == 2):
        poll.title = ""
        poll.add_option(Option(emoji=alphabet[0], option=args[0]))
        poll.add_option(Option(emoji=alphabet[1], option=args[1]))
    #Multiple options Poll
    else:
        j = 0
        for i in range (0, len(args) - 1):
            option = Option(emoji=alphabet[j], option=args[i + 1])
            if (option_exists(poll, option)):
                continue
            poll.add_option(option)
            j += 1
    return poll

async def poll_add_option(ctx, *args):
    if (ctx.message.channel.id != POLL_CHANNEL
            and ctx.message.channel.id != TEST_CHANNEL):
        return
    # Man
    if (len(args) == 0):
        await ctx.send(embed=man_poll_add())
        return
    try:
        poll_id, poll = get_poll()
        if (poll is None):
            await ctx.send("Il n'y a pas de dernier sondage")
            return
        msg = await ctx.fetch_message(poll_id)
        if (msg == None):
            await ctx.send("Je ne trouve pas le dernier sondage")
            return
        if (poll.options[0].option == "" and poll.options[1].option == ""):
            poll.clear_options()
            remove_options(poll_id)
            for reaction in msg.reactions:
                await reaction.clear()
        #if (msg.channel != ctx.channel):
        #    await ctx.send("Impossible d'éditer un poll d'un autre channel")
        #    return
        options = [x.option for x in poll.options]
        new_options = [x for x in args if x not in options]
        #FIXME
        if (len(poll.options) + len(new_options) > 26):
            await ctx.send("Arrête d'essayer de me casser {0}".format(PEPECRY))
            return
        # Option exists
        if (len(new_options) == 0):
            await ctx.send("Rien à ajouter")
            return
        for opt in new_options:
            emoji = alphabet[len(poll.options)]
            add_new_option(poll_id, emoji, opt)
            poll.add_option(Option(option=opt, emoji=emoji))
            await msg.add_reaction(emoji)
        await msg.edit(embed=poll.to_embed())
        await ctx.message.add_reaction("\N{White Heavy Check Mark}")
    except Exception as e:
        print(str(e))
        await ctx.message.add_reaction("\N{Cross Mark}")
        await ctx.send("Arrête d'essayer de me casser {0}".format(PEPECRY))

def option_exists(poll, option):
    for o in poll.options:
        if (o.option == option.option):
            return True
    return False

def man_poll():
    return discord.Embed(colour=discord.Colour.from_rgb(254, 254, 254),
        title="Manuel d'utilisation",
        description="" \
        + "**Sondage simple \N{Thumbs Up Sign}/\N{Thumbs Down Sign}:**\n" \
        + "/poll \"Suis-je un bon bot ?\"\n" \
        + "ou\n" \
        + "/poll \"Vim\" \"Emacs\"\n\n" \
        + "**Sondage avec plusieurs propositions**\n" \
        + "/poll \"Pain au chocolat ou chocolatine ?\"" \
        + "\"Pain au chocolat\" \"Pain au chocolat\"")

def man_poll_add():
    return discord.Embed(colour=discord.Colour.from_rgb(254, 254, 254),
        title="Manuel d'utilisation",
        description="""**Pour ajouter une option au dernier sondage**
        /poll_add \"Option 1\" \"Option 2\" \"Option 3\" ... """)
