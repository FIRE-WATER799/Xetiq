import discord, os
from discord.ext import commands

PREFIX="!"

client = commands.Bot(command_prefix=PREFIX, pm_help=True, owner_id=702954010008748174, case_insensitive=True)

client.remove_command("help")

@client.event
async def on_connect():
	if client._uptime is None:
		print(f"Connected to Discord. Getting ready...")
		print(f'-----------------------------')
		
client.run("NzQzNTUyNDcyMzQ5NTQwNDUy.XzWVMw.6CpqvEJIAA7LNTbgNw6MtVYOzVw")