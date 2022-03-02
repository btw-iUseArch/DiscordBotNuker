import discord
from discord.ext import commands

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
    try:
        await ctx.channel.purge(limit=amount+1)
        if amount == 1:
            await ctx.send(f"Deleted 1 message :+1:")
        else:
            await ctx.send(f"Deleted {amount} messages :+1:")
    except:
        print("aa")

@clear.error
async def clear_error(ctx, error):
    await ctx.send(":negative_squared_cross_mark: You don't have permission to do that!")


@client.command()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx, channel: discord.TextChannel=None):
    try:
        channel = channel or ctx.channel
        count = 0
        async for _ in channel.history(limit=None):
            count += 1
        await ctx.channel.purge(limit=count)
        await ctx.send(f"Nuked {channel.mention}")
    except Exception as e:
        print(e)
        await ctx.send("You don't have permission!")

@nuke.error
async def nuke_error(ctx, error):
    await ctx.send(":negative_squared_cross_mark: You don't have permission to do that!")

client.run("OTQ4MjcwNDY1NjcwMDUzOTk5.Yh5XsQ.9r7L083Tsfg7r39_S26o_RW6FvU")
