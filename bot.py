import discord
from discord import player
from discord import colour
from discord.ext import commands
from discord.ext.commands.errors import BadArgument, CommandNotFound, MissingRequiredArgument
from discord import app_commands
from discord import File
from discord.utils import get
import random
import json
import typing

with open('config.json', 'r') as f:
    config = json.load(f)
TOKEN = config['token']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.moderation = True

client = commands.Bot(command_prefix="-", help_command=None, intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Blahaj World"))
    print("We Are Ready Now")

@client.event
async def on_message(message):
    if client.user.mentioned_in(message) and message.reference is None:
        await message.reply("🎆 The Haj is here! 🦈")
    elif message.reference is not None and "shark" in message.content.lower() and client.user.mentioned_in(message):
        await message.reply("shark")
    elif message.reference is not None and "yokoso" in message.content.lower() and client.user.mentioned_in(message):
        await message.reply("<:YOKOSO:1167289778190946334>")
    await client.process_commands(message)

@client.command(name='blahaj')
async def blahaj(ctx):
    def random_blahaj():
        with open('blahaj.json') as dt:
            data = json.load(dt)
            random_index = random.randint(0, len(data) - 1)
            return data[random_index]["url"], data[random_index]["name"]

    blahajImageLink, blahajImageName = random_blahaj()
    embed = discord.Embed(
        description=f"Here is a **{blahajImageName}** 🦈", color=discord.Color.from_rgb(178, 208, 250))
    embed.set_image(url=blahajImageLink)
    await ctx.reply(embed=embed)

@client.command(name='shark')
async def blahaj(ctx):
    def random_blahaj():
        with open('blahaj.json') as dt:
            data = json.load(dt)
            random_index = random.randint(0, len(data) - 1)
            return data[random_index]["url"], data[random_index]["name"]

    blahajImageLink, blahajImageName = random_blahaj()
    embed = discord.Embed(
        description=f"Here is a **{blahajImageName}** 🦈", color=discord.Color.from_rgb(178, 208, 250))
    embed.set_image(url=blahajImageLink)
    await ctx.reply(embed=embed)

testServerId = 713322963193167913

@client.command(name= "domain_expansion")
@commands.has_permissions(manage_roles=True)
async def domain_expansion(ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, id=(1187353451735289897))
    await ctx.send(file=File("Domain Expansion.mp4"))
    await member.add_roles(role)

@client.command(name= "release")
@commands.has_permissions(manage_roles=True)
async def release(ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, id=(1187353451735289897))
    await ctx.send(file=File("Domain Reversal.mp4"))
    await member.remove_roles(role)

client.run(TOKEN)
