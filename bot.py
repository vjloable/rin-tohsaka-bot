import discord
from discord.ext import commands
import os
import random
import asyncio

def mudae_randomize():
	container = [("a"*1),("h"*2),("g"*4),("k"*5),("c"*6),("b"*8),("d"*9),("e"*11),("f"*16),("j"*18),("i"*20)]
	string = ""
	while(len(container)>0):
		string += container.pop(random.randint(0,len(container)-1))
	string = list(string)
	return string.pop(random.randint(0,99))

mudae_events_list = {
		"a":["UNLUCKY EVENT","Server-wide Thanos Snap"],								# 1%
		"b":["UNLUCKY EVENT","Force-divorce all firstmarries"],						# 8%
		"c":["UNLUCKY EVENT","Force-divorce the highest-kakera character"],			# 6%
		"d":["UNLUCKY EVENT","Force-divorce 2 random characters (500-ka below)"],		# 9%
		"e":["NEUTRAL EVENT","Send any character to someone (Must be 250-ka above)"], # 11%
		"f":["UNLUCKY EVENT","Pay 1500 kakera"],										# 16%
		"g":["UNLUCKY EVENT","Thanos Snap (2 random players)"],						# 4%
		"h":["LUCKY EVENT","Earn 1x Trading Power (Random player)"],				# 2%
		"i":["LUCKY EVENT","Earn 200 kakera"],										# 20%
		"j":["LUCKY EVENT","Earn 100 daily kakera for 7 days (Random player)"],		# 18%
		"k":["LUCKY EVENT","Next event immunity (random player)"]					# 5%
	}
		#BURN THE FIRST THING YOU ROLL
		#

client = commands.Bot(command_prefix = 'r!')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.dnd, activity=discord.Game("with the Events | r!help"))
	print('Logged on as')
	print(client.user.name)
	print(client.user.id)

@client.command()
async def mudae_event(ctx, number=1):
	embed = discord.Embed(
		title=':heart_exclamation: **Mudae Event** :heart_exclamation:',
		colour=discord.Colour.red()
		)
	if number > 4:
		number = 4
	if number < 1:
		number = 1
	for _ in range(number):
		embed.add_field(name='📍| '+mudae_events_list[mudae_randomize()][0], value=mudae_events_list[mudae_randomize()][1], inline=False)

	await ctx.send(embed=embed)
    #await ctx.send(":heart_exclamation: **Mudae Event** :heart_exclamation: \n```📍 | " + events[randomize()] + "\n```")

@client.command()
async def arena_event(ctx):
	embed = discord.Embed(
		title=':trophy: **Arena Event** :trophy:',
		description='Hosted by: <@336068309789310979>',
		colour=discord.Colour.gold()
		)
	first = '<@!273035462996918273>\n10,000 Tatsumaki Credits | 10,000 IdleRPG Credits | 1000 kakera'
	second = '<@!487935377219256343>\n5,000 Tatsumaki Credits | 5,000 IdleRPG Credits | 500 kakera'
	third = '<@!523701663937200134>\n1,000 Tatsumaki Credits | 1,000 IdleRPG Credits | 100 Kakera'
	embed.add_field(name='Eligible to:', value='Mudae and IdleRPG players', inline=False)
	embed.add_field(name='Rewards and Winners:', value='-', inline=False)
	embed.add_field(name=':first_place: ', value=first, inline=True)
	embed.add_field(name=':second_place: ', value=second, inline=True)
	embed.add_field(name=':third_place: ', value=third, inline=True)
	embed.add_field(name='Score Tally:', value='https://controlc.com/6b6f4fab', inline=False)
	join = 'Use `$skills` and set the skills for each of your 6 waifus/husbandos to the following divisions:' 
	embed.add_field(name='How to join:', value=join, inline=False)
	embed.add_field(name=':small_orange_diamond:| +10 :crossed_swords: stats', value='Yandere Division', inline=True)
	embed.add_field(name=':small_orange_diamond:| +5 :crossed_swords: +5 :shield: stats', value='Tsundere Division', inline=True)
	embed.add_field(name=':small_orange_diamond:| +10 :shield: stats', value='Kuudere Division', inline=True)
	embed.add_field(name=':small_orange_diamond:| +8 :notebook_with_decorative_cover: stats', value='Dandere Division', inline=True)
	embed.add_field(name=':small_orange_diamond:| +40% :heartpulse: stats', value='Deredere Division', inline=True)
	embed.add_field(name=':small_orange_diamond:| Any stats', value='Combo Division', inline=True)
	
	embed.add_field(name='Where:', value='<#745137728793870366>', inline=True)
	embed.set_footer(text='When: COMPLETED ~~Friday, Aug-28-2020, 9:00 PM Local Time~~')
	await ctx.send(embed=embed)
    #await ctx.send(":heart_exclamation: **Mudae Event** :heart_exclamation: \n```📍 | " + events[randomize()] + "\n```")

@client.command()
async def baog(ctx):
	await ctx.send(content='<a:baoggif:746755743809667193>')
	print(ctx.message)

count = 0
@client.command()
async def ex(ctx):
	if count < 1:
		if ctx.message.author.id == 336068309789310979 or ctx.message.author.id == 487935377219256343:
			count += 1
			await ctx.send('Wished by <@487935377219256343>')
			embed = discord.Embed(
				description='**Monkey D. Luffy** \n\nOne Piece\n**565**<:kakera:748810456671453296>',
				colour=discord.Colour.green()
				)
			embed.set_image(url='https://i.imgur.com/9UVKIr1.png')
			msg = await ctx.send(embed=embed)
			await msg.add_reaction('\U0001F496')
			
			new_embed = discord.Embed(
				description='**Monkey D. Luffy** \n\nOne Piece\n**565**<:kakera:748810456671453296>',
				colour=discord.Colour.red()
				)
			new_embed.set_image(url='https://i.imgur.com/9UVKIr1.png')
			new_embed.set_footer(text='Belongs to Reinn_sama', icon_url='https://cdn.discordapp.com/avatars/487935377219256343/2656f554ae5e6ff7d703512f29414984.png')

			def check(reaction, user):
				print(str(user.id))
				id_list = [336068309789310979,487935377219256343]
				return (reaction.message.id == msg.id and user.id in id_list) #487935377219256343
			try:
				reaction, user = await client.wait_for("reaction_add", check=check, timeout=15)
			except asyncio.TimeoutError:
				print('Timeout')
			else:
				print('Rheana reacted')
				await msg.edit(embed=new_embed)
				await ctx.send('Welcome to the Kingdom of ♕ **Reinn_sama, Monkey D. Luffy**! :european_castle:')

@client.command()
async def rules(ctx):
	rules = [
		'**1** ►   Same rules as any righteous groups or servers.',
		'**2** ►   Please be respectful towards everyone. This means __**NO HATE**__ and whatever variant of this rule applies.',
		'**3** ►   No self-promotion without admin permission.',
		'**4** ►   Yeah have fun.'
	]
	flatrules = ''
	for rule in rules:
		flatrules += rule + '\n\n'
	embed = discord.Embed(
		title=':round_pushpin: **SERVER RULES** :round_pushpin:\n',
		description=flatrules,
		colour=discord.Colour.from_rgb(102, 255, 153)
		)
	await ctx.send(embed=embed)

@client.command()
async def campus(ctx):
	description = 'React to give yourself a role.'
	reacts = [
		':white_circle:',
		':black_circle:',
		':red_circle:',
		':blue_circle:',
		':brown_circle:',
		':purple_circle:',
		':green_circle:',
		':yellow_circle:',
		':orange_circle:',
		':white_large_square:',
		':black_large_square:',
		':orange_square:',
		':blue_square:',
		':red_square:',
		':brown_square:',
		':purple_square:'
	]
	roles = [
		': IRC',
		': CLC',
		': EVC',
		': CVisC',
		': CVC',
		': WVC',
		': MRC',
		': MC',
		': CBZRC',
		': ZPRC',
		': CARC',
		': CMC',
		': CRC',
		': SMC',
		': BRC',
		': SRC'
	]
	embed = discord.Embed(
		title=':round_pushpin: **ROLE MENU: Campus** :round_pushpin:\n',
		description=description,
		colour=discord.Colour.from_rgb(102, 255, 153)
		)
	for react, role in zip(reacts, roles):
		embed.add_field(name=react, value='***'+role+'***', inline=True)
	await ctx.send(embed=embed)

client.run(os.environ['TOKEN'])
