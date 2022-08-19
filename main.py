import nextcord
from nextcord.ext import commands
import asyncio
from keep_alive import keep_alive
from music_cog import music_cog
from mod import Mod
from imgsrch import Img


TOKEN = 'Your bot token here'
# Importing commands from other files
client = commands.Bot(command_prefix = 'Your bot prefix here')
client.remove_command('help')
client.add_cog(music_cog(client))
client.add_cog(Mod(client))
client.add_cog(Img(client))
# Custom status
@client.event
async def on_ready():
    statuses = ['You | -help', f'{len(client.guilds)} servers | -help']

    while not client.is_closed():
        status = random.choice(statuses)

        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name = status))

        await asyncio.sleep(10)
    client.loop.create_task(on_ready())
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="Pornhub VR"))
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name =f'{len(client.guilds)} servers'))

@client.event
async def on_connect():
    print("Bot is on!")

keep_alive()
client.run(TOKEN)
