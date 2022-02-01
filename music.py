import asyncio 
import discord 
from discord.ext import commands
import youtube_dl

songs = asyncio.Queue()
play_next_song = asyncio.Event()

class music(commands.Cog):
  def __init__(self, client):
    self.client = client
 
  @commands.command() #se une el bot
  async def unete(self, ctx):
    if ctx.author.voice is None:
      await ctx.send("No estas en un canal de voz carnal")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)

  @commands.command() #se apaga el bot 
  async def vete(self, ctx):
      await ctx.voice_client.disconnect()

  @commands.command()  #reproduce una cancion de Youtube 
  async def r(self, ctx, url):
    ctx.voice_client.stop()  
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': "bestaudio"}
    await ctx.send("come popo ratt")
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)

  @commands.command()
  async def stop(self, ctx):
    await ctx.voice_client.pause()
    await ctx.send("Uyyy quieto ⏸︎")

  @commands.command()
  async def resume(self, ctx):
    await ctx.voice_client.resume()
    await ctx.send("y volvemos a la normalidad ... ⏩︎")

def setup(client):
  client.add_cog(music(client))    