import discord 
from discord.ext import commands

from apikeys import *


intents = discord.Intents.all()  # Create an instance of Intents

intents.all()  # Enable all the intents

client = commands.Bot(command_prefix='!', intents=intents)             #Bot is summoned


@client.event
async def on_ready():                                   #Bot is getting ready for commands
    print("The bot is now ready for use!")
    print("-----------------------------")


@client.command()
async def hello(ctx):
    await ctx.send('Hello, {0.author}'.format(ctx.message))
    
    
@client.event
async def on_member_join(member):
    channel = client.get_channel(1187254085083205643)
    await channel.send("Welcome to the server!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1187254085083205643)
    await channel.send("Goodbye")

@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice): #if user is in voice channel
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else: #if user not in voice channel
        await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command")

@client.command(pass_context = True)
async def leave(ctx): #if command is run then bot will leave the server
    if(ctx.voice_client): 
        await ctx.guild.voice_client.disconnect() #bot leaves server
        await ctx.send("I left the voice channel") #updates user
    else:
        await ctx.send("I am not currently connected to any voice channels.") #updates user

client.run(BOTTOKEN)