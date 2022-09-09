from nextcord.ext import commands
import nextcord
from nextcord import Interaction, SlashOption, slash_command
from datetime import datetime, timedelta
import asyncio
class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(name='kick', description='Kick a member')
    async def kick(self, ctx:Interaction, member: nextcord.Member = SlashOption(name='member', description='Please select a member'), reason: str = nextcord.SlashOption(name = 'reason', description = 'Please provide a reason', required = False)):
        if ctx.user.guild_permissions.kick_members or ctx.user.guild_permissions.administrator:
            if member.id == ctx.user.id:
                await ctx.response.send_message("You can't kick yourself!", ephemeral=True)
                return
            if not reason: reason='No reason'
            embed = nextcord.Embed(description = ":airplane: **User ** "+f"**{member.mention}**"+" **has been kicked from the server** ", colour=0xed0000, timestamp=datetime.utcnow())
            embed.add_field(name = 'Reason: ', value = f"{reason}", inline = False)
            await ctx.send(embed=embed)
            await member.kick(reason=reason)
        else:
            return await ctx.response.send_message('You are not allowed to use this command.', ephemeral=True)
 
    @slash_command(name='ban', description='Ban a member')
    async def ban(self, ctx:Interaction,  member: nextcord.Member = SlashOption(name='member', description='Please select a member'), reason: str = nextcord.SlashOption(name = 'reason', description = 'Please provide a reason', required = False)):
        if ctx.user.guild_permissions.ban_members or ctx.user.guild_permissions.administrator:
            if member.id == ctx.user.id:
                await ctx.response.send_message("You can't ban yourself!", ephemeral=True)
                return
            if not reason: reason='No reason'
            embed = nextcord.Embed(description = ":airplane: **User ** "+f"**{member.mention}**"+" **has been banned from the server** ", colour=0xed0000, timestamp=datetime.utcnow())
            embed.add_field(name = 'Reason: ', value = f"{reason}", inline = False)
            await ctx.send(embed=embed)
            await member.ban(reason=reason)
        else:
            await ctx.response.send_message("You are not allowed to use this command.", ephemeral=True)
 
    @slash_command(name='clear', description='Purge a channel')
    async def clear(self, ctx:Interaction,  amount: int = SlashOption(name = 'amount', description = 'Please enter amount to purge')):
        if ctx.user.guild_permissions.manage_messages or ctx.user.guild_permissions.administrator:
            embed = nextcord.Embed(description = ':wastebasket: **Cleared ** '+f'**{amount}**'+' **messages**', colour=0xed0000, timestamp=datetime.utcnow())
            await ctx.channel.purge(limit=amount)
            await ctx.send(embed=embed)
        else:
            await ctx.response.send_message("You are not allowed to use this command.", ephemeral=True)
 
    @slash_command(name='timeout', description='Timeout a member')
    async def timeout(self, ctx:Interaction, member: nextcord.Member = SlashOption(name = 'member', description = ' Please select a member', required = True), reason: str = SlashOption(name = 'reason', description = 'Please provide a reason', required = False), days: int = SlashOption(max_value = 30, default = 0, required = False), hours: int = SlashOption(default = 0, required = False), minutes: int = SlashOption(default = 0, required = False), seconds: int = SlashOption(default = 0, required = False)):
        if ctx.user.guild_permissions.moderate_members:
            if member.id == ctx.user.id:
                await ctx.response.send_message("You can't timeout yourself!", ephemeral=True)
                return
            if member.guild_permissions.moderate_members:
                await ctx.response.send_message("You can't do this, this person is a moderator!")
                return
            duration = timedelta(days = days, hours = hours, minutes = minutes, seconds = seconds)
            if duration >= timedelta(days = 30): #added to check if time exceeds 28 days
                await ctx.response.send_message("I can't mute someone for more than 30 days!", ephemeral = True) #responds, but only the author can see the response
                return
            if reason == None:
                await member.timeout(duration)
                t1embed = nextcord.Embed(description = ":hourglass: **User ** "+f"**{member.mention}**"+" **has been timed out** ", colour=0xed0000, timestamp=datetime.utcnow())
                t1embed.add_field(name = 'Time: ', value = f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds')
                t1embed.set_footer(icon_url = ctx.user.avatar.url, text = f'Requested by {ctx.user.name}')
                await ctx.response.send_message(embed=t1embed)
            else:
                await member.timeout(duration, reason = reason)
                t2embed = nextcord.Embed(description = ":hourglass: **User ** "+f"**{member.mention}**"+" **has been timed out** ", colour=0xed0000, timestamp=datetime.utcnow())
                t2embed.add_field(name = 'Time: ', value = f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds')
                t2embed.add_field(name = 'Reason: ', value = f"{reason}", inline = False)
                t2embed.set_footer(icon_url = ctx.user.avatar.url, text = f'Requested by {ctx.user.name}')
                await ctx.response.send_message(embed=t2embed)
        else:
            await ctx.response.send_message("You are not allowed to use this command.", ephemeral=True)
    @slash_command(name='untimeout', description='Untimeout a member')
    async def untimeout(self, ctx:Interaction, member: nextcord.Member = SlashOption(name='member', description='Please select a member'), reason: str = SlashOption(name = 'reason', description = 'Please provide a reason', required = False)):
        if ctx.user.guild_permissions.moderate_members:
            if reason == None:
                await member.edit(timeout=None)
                ut1embed = nextcord.Embed(description = ':white_check_mark: **User ** '+f'{member.mention}'+' **has been untimed out** ', colour = 0xed0000, timestamp =datetime.utcnow())
                ut1embed.set_footer(icon_url = ctx.user.avatar.url, text = f'Requested by {ctx.user.name}')
                await ctx.response.send_message(embed=ut1embed)
            else:
                await member.edit(timeout=None, reason=reason)
                ut2embed = nextcord.Embed(description = ':white_check_mark: **User ** '+f'{member.mention}'+' **has been untimed out** ', colour = 0xed0000, timestamp =datetime.utcnow())
                ut2embed.add_field(name = 'Reason: ', value = f'{reason}', inline = False)
                ut2embed.set_footer(icon_url = ctx.user.avatar.url, text = f'Requested by {ctx.user.name}')
                await ctx.response.send_message(embed=ut2embed)
        else:
            await ctx.response.send_message("You are not allowed to use this command.", ephemeral=True)
