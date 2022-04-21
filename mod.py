from discord.ext import commands
import discord
from datetime import datetime

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Command
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.administrator:
            embed = discord.Embed(description = ":airplane: **User ** "+f"**{member.mention}**"+" **got kicked from this server** ", colour=0x62008f, timestamp=datetime.utcnow())
            embed.set_author(icon_url = member.avatar_url, name = member.name+"#"+member.discriminator)
            embed.add_field(name = 'Powód wyrzucenia: ', value = f"{reason}", inline = False)
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
            await member.kick(reason=reason)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description = ":no_entry_sign: **You dont have permissions to execute this command ** ", colour=0x62008f, timestamp=datetime.utcnow())
            embed.set_author(icon_url = member.avatar_url, name = member.name+"#"+member.discriminator)
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
            await ctx.send(embed=embed)
            return
    @commands.Command
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.administrator:
            embed = discord.Embed(description = ":airplane: **User ** "+f"**{member.mention}**"+" **got banned from this server** ", colour=0x62008f, timestamp=datetime.utcnow())
            embed.set_author(icon_url = member.avatar_url, name = member.name+"#"+member.discriminator)
            embed.add_field(name = 'Powód bana: ', value = f"{reason}", inline = False)
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
            await member.ban(reason=reason)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description = ":no_entry_sign: **You dont have permissions to execute this command ** ", colour=0x62008f, timestamp=datetime.utcnow())
            embed.set_author(icon_url = member.avatar_url, name = member.name+"#"+member.discriminator)
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
            await ctx.send(embed=embed)
            return
