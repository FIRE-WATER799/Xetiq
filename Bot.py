import discord, os
from discord.ext import commands

PREFIX="!"

client = commands.Bot(command_prefix=PREFIX, pm_help=True, owner_id=702954010008748174, case_insensitive=True)

client.remove_command("help")
client._uptime = None

@client.event
async def on_connect():
	if client._uptime is None:
		print(f"Connected to Discord. Getting ready...")
		print(f'-----------------------------')

if({message.content}=="How do I join Xetiq"):
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
		
client.run("NzQzNTUyNDcyMzQ5NTQwNDUy.XzWVMw.6CpqvEJIAA7LNTbgNw6MtVYOzVw")