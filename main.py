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

@client.command()
async def help(ctx):
    embedVar = discord.Embed(title="Commands", description="_ _", color=0x00bfff)
    embedVar.add_field(name="?clear number", value="Deletes the specified number of messages. If the number is not"
                                                   "specified, it deletes the last 20 messages", inline=False)
    embedVar.add_field(name="?nuke", value="Deletes all the messages in the channel.", inline=False)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=20):
    await ctx.channel.purge(limit=amount+1)
    if amount == 1:
        message1 = await ctx.send(f"Deleted 1 message :+1:")
        await asyncio.sleep(5)
        await message1.delete()
    else:
        message2 = await ctx.send(f"Deleted {amount} messages :+1:")
        await asyncio.sleep(5)
        await message2.delete()

@clear.error
async def clear_error(ctx, error):
    message = await ctx.send(":negative_squared_cross_mark: You don't have permission to do that!")
    await asyncio.sleep(5)
    await message.delete()


@client.command()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx, channel: discord.TextChannel=None):
    channel = channel or ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.channel.purge(limit=count)
    message = await ctx.send(f"Nuked {channel.mention}")
    await asyncio.sleep(5)
    await message.delete()

@nuke.error
async def nuke_error(ctx, error):
    message = await ctx.send(":negative_squared_cross_mark: You don't have permission to do that!")
    await asyncio.sleep(5)
    await message.delete()

client.run(os.getenv("DISCORD_TOKEN"))
