from nextcord.ext import commands
import nextcord
import sqlite3
from nextcord import slash_command, Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from datetime import datetime

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS logs(guild_id INT, channel_id INT, toggle BOOL)')
        cursor.close()
        db.close()
        print('LOGS ONLINE!')
    @slash_command(name = "logs", description = "Enable or disable server logs")
    async def logstoggle(
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
                cursor.execute("SELECT guild_id FROM logs WHERE guild_id = ?", (ctx.user.guild.id,))
                data = cursor.fetchone()
                if data is None:
                    cursor.execute("INSERT INTO logs(guild_id, toggle) VALUES(?, ?)", (ctx.user.guild.id, toggle))
                else:
                    cursor.execute("UPDATE logs SET toggle = ? WHERE guild_id = ?", (toggle, ctx.user.guild.id))
                await ctx.send('Logs turned ON', ephemeral=True)
                db.commit()
                cursor.close()
                db.close()
            else:
                db = sqlite3.connect("database.db")
                cursor = db.cursor()
                cursor.execute("DELETE FROM logs WHERE guild_id = ?", (ctx.user.guild.id,))
                await ctx.send('Logs turned OFF', ephemeral=True)
                db.commit()
                cursor.close()
                db.close()
        else:
            await ctx.response.send_message("You are not allowed to use this command.", ephemeral=True)
    @slash_command(name = 'logchannel', description = 'select a channel to send log messages')
    async def setlog(self, ctx:Interaction, channel:GuildChannel = SlashOption(channel_types=[ChannelType.text], name = 'channel', description = 'Please mention a channel')):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('SELECT guild_id FROM logs WHERE guild_id = ?', (ctx.user.guild.id,))
        result = cursor.fetchone()
        if result:
            cursor.execute('UPDATE logs SET channel_id = ? WHERE guild_id = ?', (channel.id, ctx.user.guild.id))
        else:
            cursor.execute('INSERT INTO logs(guild_id, channel_id) VALUES(?, ?)', (ctx.user.guild.id, channel.id))
        await ctx.send(f'Log channel was set on {channel.mention}')
        db.commit()
        cursor.close()
        db.close()
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('SELECT toggle FROM logs WHERE guild_id = ?', (message.guild.id,))
        data = cursor.fetchone()
        if data:
            toggle = data
        else:
            toggle = 0
        cursor.close()
        db.close()
        if toggle == data:
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute("SELECT channel_id FROM logs WHERE guild_id = ?", (message.guild.id,))
            result = cursor.fetchone()
            if result:
                result = int(result)
                log_channel = self.bot.get_channel(result)
                embed = nextcord.Embed(description = ":wastebasket: **Message sent by** "+f"**{message.author.mention}**"+" **was deleted on channel ** "+f"**{message.channel.mention}**",colour=0xed0000, timestamp=datetime.utcnow())
                embed.set_author(name = message.author.name+"#"+message.author.discriminator)
                embed.add_field(name = 'Message deleted', value = f"{message.content}", inline = False)
                await log_channel.send(embed=embed)
            else:
                pass
