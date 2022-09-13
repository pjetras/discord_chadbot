import nextcord
from nextcord.ext import commands
from googleapiclient.discovery import build
from nextcord import ButtonStyle, SlashOption, ButtonStyle, slash_command
from nextcord.ui import Button, View
import time
# import random
from datetime import datetime
import sqlite3
import bad_words
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
        if ctx.user.guild_permissions.administrator:
            if toggle == 1:
                db = sqlite3.connect("database.db")
                cursor = db.cursor()
                cursor.execute("SELECT guild_id FROM automod WHERE guild_id = ?", (ctx.user.guild.id,))
                data = cursor.fetchone()
                if data is None:
                    cursor.execute("INSERT INTO automod(guild_id, toggle) VALUES(?, ?)", (ctx.user.guild.id, toggle))
                else:
                    cursor.execute("UPDATE automod SET toggle = ? WHERE guild_id = ?", (toggle, ctx.user.guild.id))
                await ctx.send('Automod turned ON', ephemeral=True)
                db.commit()
                cursor.close()
                db.close()
            else:
                db = sqlite3.connect("database.db")
                cursor = db.cursor()
                cursor.execute("DELETE FROM automod WHERE guild_id = ?", (ctx.user.guild.id,))
                await ctx.send('Automod turned OFF', ephemeral=True)
                db.commit()
                cursor.close()
                db.close()
        else:
            await ctx.response.send_message("You are not allowed to use this command.", ephemeral=True)
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
        
        if toggle == data:
            for word in bad_words.blwords:
                if word in message.content:
                    await message.delete()
                    res = await message.channel.send(f"{message.author.mention}, You've typed a blacklisted keyword!!!")
                    time.sleep(5)
                    await res.delete()
        else:
            pass
