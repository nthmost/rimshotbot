import os

from discord import FFmpegOpusAudio, FFmpegPCMAudio
from discord.ext.commands import Bot
from discord.ext.commands.errors import CommandInvokeError


TOKEN = os.getenv("DISCORD_RIMSHOTBOT_TOKEN")         # collected from Discord Bot setup process.
PREFIX = os.getenv("DISCORD_RIMSHOTBOT_PREFIX")       # recommended: "%"
ENCODING = "ogg"                                      # options: ogg, mp3  (default: ogg)


# oneoff sounds
SOUNDS = {"wrong": "https://instantrimshot.com/audio/priceiswrong.mp3",
          "rim": "https://instantrimshot.com/audio/rimshot.mp3",
          "crickets": "https://instantrimshot.com/audio/crickets.mp3",
          "gong": "http://instantrimshot.com/audio/gong.mp3",
          "reveille": "http://instantrimshot.com/audio/reveille.mp3",
          "rainbow": "http://instantrimshot.com/audio/readingrainbow.mp3",
          "slide": "http://instantrimshot.com/audio/slidewhistle.mp3",
          "csi": "http://instantrimshot.com/audio/csi.mp3",
         }


client = Bot(command_prefix=list(PREFIX))

player = None


@client.event
async def on_ready():
    print('RimshotBot Ready')


@client.command(name="menu")
async def menu(ctx):
    out = "Menu of Commands\n\n"
    tmpl = "\t{PREFIX}{key}"
    for key, val in SOUNDS.items():
        out += tmpl.format(PREFIX=PREFIX, key=key)
    out += "\n"
    await ctx.send(out)


async def do_play(ctx, src):
    global player
    try:
        channel = ctx.message.author.voice.channel
    except AttributeError:
        # user is not in a Voice Channel
        await ctx.send(f"You need to join a Voice Channel first!")
        return

    try:
        player = await channel.connect()
    except CommandInvokeError:
        print("Attempt to play without user in channel")
    except Exception as err:
        print(err)
        pass
    if player:
        if ENCODING == "mp3":
            player.play(FFmpegPCMAudio(src))
        else:
            player.play(FFmpegOpusAudio(src))
    else:
        print("Could not initialize player.")


@client.command(aliases=['c', 'cri'])
async def crickets(ctx):
    await do_play(ctx, SOUNDS["crickets"])

@client.command(aliases=['g'])
async def gong(ctx):
    await do_play(ctx, SOUNDS["gong"])

@client.command(aliases=['r', 'ri'])
async def rim(ctx):
    await do_play(ctx, SOUNDS["rim"])

@client.command(aliases=['w', 'wro', 'priceiswrong', 'womp'])
async def wrong(ctx):
    await do_play(ctx, SOUNDS["wrong"])

@client.command(aliases=['rev', 'trumpet'])
async def reveille(ctx):
    await do_play(ctx, SOUNDS["reveille"])

@client.command(aliases=['rain', 'reading'])
async def rainbow(ctx):
    await do_play(ctx, SOUNDS["rainbow"])

@client.command(aliases=['s', 'sli'])
async def slide(ctx):
    await do_play(ctx, SOUNDS["slide"])

@client.command(aliases=['cs', 'yeah', 'thewho'])
async def csi(ctx):
    await do_play(ctx, SOUNDS["csi"])



# Remove bot from channel if it's sitting unused.
async def on_voice_state_update(member, before, after):
    voice_state = member.guild.voice_client
    # Checking if the bot is connected to a channel and if there is only 1 member connected to it (the bot itself)
    if voice_state is not None and len(voice_state.channel.members) == 1:
        # You should also check if the song is still playing
        await voice_state.disconnect()


client.run(TOKEN)

