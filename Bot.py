import discord, os
from discord.ext import commands
from discord import member
from discord.ext.commands import Bot

PREFIX="$"

client = commands.Bot(command_prefix=PREFIX, pm_help=True, owner_id=702954010008748174, case_insensitive=True)

client.remove_command("help")
client._uptime = None

@client.event
async def on_connect():
	if client._uptime is None:
		print(f"Connected to Discord. Getting ready...")
		print(f'-----------------------------')
		
@client.command(usage="Learn how to join a role")
async def How_do_I_join_Xetiq(ctx):
  join=""
  join+="1. What server are you \n"
  join+="-NAE \n"
  join+="-NAW \n"
  join+="-EU \n"
  join+="-ASIA \n"
  join+="-OCE \n \n"
  join+="2. What do you want to join as \n \n"
  join+="Cretive Warrior: U need to know to do retakes and edit good. \n \n"
  join+="Comp Player: U need at least 1k in arena. Play alot of solos/duos/squads \n \n"
  join+="TrickShotter: Need to do good trickshots or insane trickshots to join as a Trickshotter \n \n"
  join+="Content Creator: U need atleast 100+ subs to be a content creator \n \n"
  join+="GFX/VFX: U have to make good work and dm staff or owners ur work \n \n"
  join+="And thats how u Join Xetiq so try to join this clan and be apart with the members in the clan!"
  embed=discord.Embed(color=0x0000, title="How to join", description=join)
  embed.set_footer(text="Created by fire#7010") 
  await ctx.send(embed=embed)
		
client.run("NzQzNTUyNDcyMzQ5NTQwNDUy.XzWVMw.6CpqvEJIAA7LNTbgNw6MtVYOzVw")