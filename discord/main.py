import discord
from discord.ext import commands
import music


client = commands.Bot(command_prefix = '*', intents = discord.Intents.all())

cogs = [music]
for i in range(len(cogs)):
	cogs[i].setup(client)


@client.command()
async def about(ctx):
	embed = discord.Embed(
		title = 'About geekMusic',
		description = 'Am a music bot created using python and am hosted in Heroku Server',
		colour = discord.Colour.blue()
	)
	embed.set_footer(text = 'Happy Music 🎵')
	embed.set_image(url = 'https://lh3.googleusercontent.com/AQK9TbvW13eNrlGNmAWD3g_osRSLofDn42VIFLYxkh6go_rHScOAB6ZDLEpn1EEconN-aw=s85')
	embed.set_author(name = 'geekMusic', icon_url = 'https://icon-library.com/images/music-bot-icon/music-bot-icon-14.jpg')
	embed.add_field(name = 'commands',value = 'below',inline = False)
	embed.add_field(name = 'To join bot to VC',value = '*join',inline = False)
	embed.add_field(name = 'To play song',value = '*play name of the song',inline = False)
	embed.add_field(name = 'To pause ⏸︎',value = '*pause',inline = False)
	embed.add_field(name = 'To continue ⏵︎',value = '*resume',inline = False)
	embed.add_field(name = 'To kick bot out of VC',value = '*disconnect',inline = False)
	await ctx.send(embed = embed)


client.run("TOKEN")
