import nextcord
from nextcord.ext import commands
from music_cog import music_cog
from mod import Mod
from utillity import Img, Avatar, Userinfo, Serverinfo, Roles
from help import Help
from automod import Automod
from logs import Logs


TOKEN = 'Your bot token here'
# Importing commands from other files
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix = 'Your bot prefix here', intents=intents)
client.remove_command('help')
client.add_cog(music_cog(client))
client.add_cog(Mod(client))
client.add_cog(Img(client))
client.add_cog(Avatar(client))
client.add_cog(Userinfo(client))
client.add_cog(Serverinfo(client))
client.add_cog(Roles(client))
client.add_cog(Automod(client))
client.add_cog(Help(client))
client.add_cog(Logs(client))
# Custom status
@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name =f'{len(client.guilds)} servers | /help'))
@client.event
async def on_connect():
    print("Bot is on!")

keep_alive()
client.run(TOKEN)
