import discord, os, random, time, json
from discord import Embed, Colour, Member, User
from discord.ext import commands
from typing import Union

config = json.load(open('config.json'))

client = commands.Bot(command_prefix=config["prefix"], pm_help=True, owner_id=702954010008748174, case_insensitive=True)

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
  if(config["embed_toggle"]==0):
    await ctx.send(join)
  if(config["embed_toggle"]==1):
    join_embed=discord.Embed(color=0x0000, title="How to join", description=join)
    join_embed.set_footer(text="Created by fire#7010") 
    await ctx.send(embed=join_embed)

  
@client.command(usage="Gives help about commands")
async def help(ctx):
    help= "**"
    for command in client.commands:
        help+=f"{command}- `{command.usage}`\n"
    help+="**"   
    if(config["embed_toggle"]==0):
      await ctx.send(help)
    if(config["embed_toggle"]==1):
      help_embed=discord.Embed(color=0x0000, title="My Commands", description=help)
      help_embed.set_footer(text="Created by fire#7010") 
      help_embed.set_thumbnail(url='https://image.ibb.co/caM2BK/help.gif')
      help_embed.set_image(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')

      await ctx.send(embed=help_embed)
    
		
client.run(config["token"])