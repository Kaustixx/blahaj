import discord
from discord import player
from discord import colour
from discord import SlashCommandGroup
from discord import File
from discord import default_permissions
from discord import commands
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

bot = discord.Bot(command_prefix='-', intents = intents)
testingservers = [713322963193167913]

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Blahaj World"))
    print("We Are Ready Now")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and message.reference is None:
        await message.reply("🎆 The Haj is here! 🦈")
    elif "shark" in message.content.lower() and message.author.id != bot.user.id:
        await message.reply("shark")
    elif "yokoso" in message.content.lower() and message.author.id != bot.user.id:
        await message.reply("<:YOKOSO:1167289778190946334>")
    await bot.process_application_commands(message)

@bot.message_command(guild_ids = testingservers, name='Blåhaj says')
async def blahaj_says(ctx, message: discord.Message):
    await ctx.respond("Initializing speech bubble", ephemeral=True)
    await message.reply(file=File("blahaj_says.png"))

@bot.slash_command(guild_ids = testingservers, name='help', description='list of commands')
async def help(ctx):
    embed = discord.Embed(description="Blahaj commands", color=discord.Color.from_rgb(178, 208, 250))
    embed.add_field(name="Fun commands", value="`-blahaj` >Show a random blahaj \n `-shark` >Show a random blahaj")
    embed.add_field(name = chr(173), value = chr(173))
    embed.add_field(name="Moderation commands", value="`-domain_expansion` >Send someone to a domain. Specify a number to to specify the number of domain. \n `-release` >Release someone from domains.")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = testingservers, name='blahaj', description='show a random blahaj')
async def blahaj(ctx):
    def random_blahaj():
        with open('blahaj.json') as dt:
            data = json.load(dt)
            random_index = random.randint(0, len(data) - 1)
            return data[random_index]["url"], data[random_index]["name"]

    blahajImageLink, blahajImageName = random_blahaj()
    embed = pycord.Embed(
        description=f"Here is a **{blahajImageName}** 🦈", color=pycord.Color.from_rgb(178, 208, 250))
    embed.set_image(url=blahajImageLink)
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = testingservers, name='shark', description='show a random blahaj')
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
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = testingservers, name='domain_expansion', description ='send a user to a domain')
@default_permissions(manage_roles=True)
async def domain_expansion(ctx, domain_number: discord.Option(int, choices=[1, 2, 3]), member: discord.Member):
    if domain_number == 1:
        role = discord.utils.get(member.guild.roles, id=(1187353451735289897))
    elif domain_number == 2:
        role = discord.utils.get(member.guild.roles, id=(1201105937876914309))
    elif domain_number == 3:
        role = discord.utils.get(member.guild.roles, id=(1201106063487926322))
    await ctx.respond(file=File("Domain Expansion.mp4"))
    await member.add_roles(role)

@bot.slash_command(guild_ids = testingservers, name="release", description='release a user from a domain')
@default_permissions(manage_roles=True)
async def release(ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, id=(1187353451735289897))
    role2 = discord.utils.get(member.guild.roles, id=(1201105937876914309))
    role3 = discord.utils.get(member.guild.roles, id=(1201106063487926322))
    await ctx.respond(file=File("Domain Reversal.mp4"))
    await member.remove_roles(role, role2, role3)

@bot.slash_command(guild_ids = testingservers, name="kill", description='kill someone')
async def kill(ctx, target: discord.Member):
    if target != ctx.author:
        def random_kill():
            with open('kill.json') as dt:
                data = json.load(dt)
                random_index = random.randint(0, len(data) - 1)
                return data[random_index]["url"]

        killImageLink = random_kill()
        embed = discord.Embed(
            description=f"**{ctx.author}** ended **{target}**'s life!!", color=discord.Color.from_rgb(160, 0, 0))
        embed.set_image(url=killImageLink)

        role = discord.utils.get(target.guild.roles, id=(713714211552886875))
        await ctx.respond(embed=embed)
    else:
        def random_kill():
            with open('suicide.json') as dt:
                data = json.load(dt)
                random_index = random.randint(0, len(data) - 1)
                return data[random_index]["url"]

        killImageLink = random_kill()
        embed = discord.Embed(
            description=f"**{ctx.author}** committed suicide.", color=discord.Color.from_rgb(160, 0, 0))
        embed.set_image(url=killImageLink)

        role = discord.utils.get(target.guild.roles, id=(713714211552886875))
        await ctx.respond(embed=embed)

bot.run(TOKEN)