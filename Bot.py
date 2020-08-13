import discord, os
from discord.ext import commands
from discord import member
from discord.ext.commands import Bot

PREFIX="!"

client = commands.Bot(command_prefix=PREFIX, pm_help=True, owner_id=702954010008748174, case_insensitive=True)

client.remove_command("help")
client._uptime = None

@client.event
async def on_connect():
	if client._uptime is None:
		print(f"Connected to Discord. Getting ready...")
		print(f'-----------------------------')
		
@client.command(usage="Learn how to join a role")
async def How_do_I_join_Xetiq(self):
  join=""
  join+="1. What server are you \n"
  join+="-NAE \n"
  join+="-NAW \n"
  join+="-EU \n"
  join+="-ASIA \n"
  join+="-OCE \n \n"
  join+="2. What do you want to join as \n \n"
  join+=""
  join+=""
  join+=""
  ctx.send(join)
  print("done")
		
client.run("NzQzNTUyNDcyMzQ5NTQwNDUy.XzWVMw.6CpqvEJIAA7LNTbgNw6MtVYOzVw")