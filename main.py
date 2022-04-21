import discord
from discord.ext import commands
from keep_alive import keep_alive
from music_cog import music_cog
from mod import Mod


TOKEN = 'Your bot token here'

client = commands.Bot(command_prefix = 'Your bot prefix here')
client.remove_command('help')
client.add_cog(music_cog(client))
client.add_cog(Mod(client))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Your bot status'))

@client.event
async def on_connect():
    print("Bot is on!")

keep_alive()
client.run(TOKEN)
