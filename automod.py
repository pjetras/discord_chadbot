import nextcord
from nextcord.ext import commands
from googleapiclient.discovery import build
from nextcord import ButtonStyle, SlashOption, ButtonStyle, slash_command
from nextcord.ui import Button, View
# import random
from datetime import datetime
import sqlite3
class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS automod(guild_id INT, toggle INT)")
        cursor.close()
        db.close()
        print('DB ONLINE!')
    @slash_command(name = "automod", description = "Enable or disable automod")
    async def amtoggle(
        self, ctx:nextcord.Interaction,
        toggle: int = SlashOption(
            name = 'toggle', 
            choices={"ON":1, "OFF":0},
    ),
):
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute("SELECT guild_id FROM automod WHERE guild_id = ?", (ctx.user.guild.id,))
        data = cursor.fetchone()
        if data is None:
            cursor.execute("INSERT INTO automod(guild_id, toggle) VALUES(?, ?)", (ctx.user.guild.id, toggle))
        else:
            cursor.execute("UPDATE automod SET toggle = ? WHERE guild_id = ?", (toggle, ctx.user.guild.id))
        await ctx.send('automod toggle test', ephemeral=True)
        db.commit()
        cursor.close()
        db.close()
    @commands.Cog.listener()
    async def on_message(self, message):
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT toggle FROM automod WHERE guild_id = ?", (message.guild.id,))
        data = cursor.fetchone()
        if data is None:
            toggle = 0
        else:
            toggle = data
        cursor.close()
        db.close()
        blwords = ["test", "test2"]
        if toggle == data:
            if message.content in blwords:
                await message.delete()
                await message.channel.send("You've typed a blacklisted keyword!!!")
        else:
            pass
