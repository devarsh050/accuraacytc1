import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix=',' )

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='BY CRO'))
	print("hey cro im ready")
	
	
@client.event
async def on_message(message):
	if message.content.lower().startswith(',a'):
		if "509298564527292416" in [role.id for role in message.author.roles]:
			args = message.content.split(" ")
			await client.send_message(message.channel,"%s" % (" ".join(args[1:])))
		else:
				await client.send_message(message.channel, "YOU DO NOT HAVE PERMISSION")
	

client.run("NTUyMDk5MjAyNzIxOTA2NzA1.D2FmIQ.HNtuW_UFRiwPxNuDRex3rsOhIu8")
