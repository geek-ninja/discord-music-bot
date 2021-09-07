import discord
from discord.ext import commands
import youtube_dl
import ffmpeg
from youtube_search import YoutubeSearch

class music(commands.Cog):

	def __init__(self,client):
		self.client = client

	@commands.command()
	async def join(self,ctx):
		welcom = discord.Embed(
			title = 'geekMusic joined the VC 🎉',
			description = 'hello guys lets make some fun 🔥',
			colour = discord.Colour.blue()
			)
		error = discord.Embed(
			title = 'geekMusic facing some error ❌',
			description = 'Make sure to add the bot to VC',
			colour = discord.Colour.blue()
			)
		if ctx.author.voice is None:
			await ctx.send(embed = error)
		voice_channel = ctx.author.voice.channel
		if ctx.voice_client is None:
			await voice_channel.connect()
			await ctx.send(embed = welcom)
		else:
			await voice_client.move_to(voice_channel)
			await ctx.send(embed = welcom)

	@commands.command()
	async def disconnect(self,ctx):
		embed = discord.Embed(
		title = 'geekMusic left 😔',
		description = 'See you again ! bye 👋',
		colour = discord.Colour.blue()
		)
		try:
			await ctx.voice_client.disconnect()
			await ctx.send(embed = embed)
		except:
			await ctx.send(embed = embed)

	@commands.command()
	async def play(self,ctx,*song_name):
		song_name = list(song_name)
		song_name = ' '.join(song_name)
		result = YoutubeSearch(song_name,max_results = 1).to_dict()
		result = result[0]
		song_title = result['title']
		song_thumbnail = result['thumbnails']
		song_thumbnail_url = song_thumbnail[0]
		prefix = 'https://www.youtube.com'
		url = result['url_suffix']
		url = prefix + url
		
		ctx.voice_client.stop()
		FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
		YDL_OPTIONS = {
		    'format': 'bestaudio/best',
		    'reactrictfilenames': True,
		    'noplaylist': True,
		    'nocheckcertificate': True,
		    'ignoreerrors': False,
		    'logtostderr': False,
		    'quiet': True,
		    'no_warnings': True,
		    'default_search': 'auto',
		    # bind to ipv4 since ipv6 addreacses cause issues sometimes
		    'source_addreacs': '0.0.0.0',
		    'output': r'youtube-dl',
		    'postprocessors': [{
		        'key': 'FFmpegExtractAudio',
		        'preferredcodec': 'mp3',
		        'preferredquality': '320',
		    }]
		}
		vc = ctx.voice_client
		with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
			info = ydl.extract_info(url,download=False)
			url2 = info['formats'][0]['url']
			source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
			vc.play(source)
		embed = discord.Embed(
		title = 'geekMusic 🎵',
		description = 'You are playing 🎶 ' +' '+song_title,
		colour = discord.Colour.blue()
		)
		embed.set_thumbnail(url = song_thumbnail_url)
		await ctx.send(embed = embed)

	@commands.command()
	async def pause(self,ctx):
		embed = discord.Embed(
		title = 'geekMusic Paused ⏸︎',
		description = 'Type *resume to continue ▶️',
		colour = discord.Colour.blue()
		)
		try:
			await ctx.voice_client.pause()
			await ctx.send("Your Song is Paused ⏸︎ ")
		except:
			await ctx.send(embed = embed)

	@commands.command()
	async def resume(self,ctx):
		embed = discord.Embed(
		title = 'geekMusic Resumed ▶️',
		description = 'Enjoy your song 😊',
		colour = discord.Colour.blue()
		)
		try:
			await ctx.voice_client.resume()
			await ctx.send("resume ▶️")
		except:
			await ctx.send(embed = embed)

def setup(client):
	client.add_cog(music(client))
