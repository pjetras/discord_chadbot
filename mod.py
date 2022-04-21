from discord.ext import commands
import discord
from datetime import datetime

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Command
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.administrator:
            embed = discord.Embed(description = ":airplane: **Użytkownik ** "+f"**{member.mention}**"+" **został wyrzucony z serwera** ", colour=0x62008f, timestamp=datetime.utcnow())
            embed.set_author(icon_url = member.avatar_url, name = member.name+"#"+member.discriminator)
            embed.add_field(name = 'Powód wyrzucenia: ', value = f"{reason}", inline = False)
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Wykonane przez {ctx.author.name}')
            await member.kick(reason=reason)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description = ":no_entry_sign: **Nie masz wystarczających uprawnień, aby użyć tej komendy ** ", colour=0x62008f, timestamp=datetime.utcnow())
            embed.set_author(icon_url = member.avatar_url, name = member.name+"#"+member.discriminator)
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Wykonane przez {ctx.author.name}')
            embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/907356437808808027/966773714677022780/769591370884055051.png')
            await ctx.send(embed=embed)
            return
    @commands.Command
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.administrator:
            embed = discord.Embed(description = ":airplane: **Użytkownik ** "+f"**{member.mention}**"+" **został zbanowany na tym serwerze** ", colour=0x62008f, timestamp=datetime.utcnow())
            embed.set_author(icon_url = member.avatar_url, name = member.name+"#"+member.discriminator)
            embed.add_field(name = 'Powód bana: ', value = f"{reason}", inline = False)
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Wykonane przez {ctx.author.name}')
            await member.ban(reason=reason)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description = ":no_entry_sign: **Nie masz wystarczających uprawnień, aby użyć tej komendy ** ", colour=0x62008f, timestamp=datetime.utcnow())
            embed.set_author(icon_url = member.avatar_url, name = member.name+"#"+member.discriminator)
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Wykonane przez {ctx.author.name}')
            embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/907356437808808027/966773714677022780/769591370884055051.png')
            await ctx.send(embed=embed)
            return
