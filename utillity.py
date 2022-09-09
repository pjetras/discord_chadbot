import nextcord
from nextcord.ext import commands
from googleapiclient.discovery import build
from nextcord import ButtonStyle, SlashOption, ButtonStyle, slash_command
from nextcord.ui import Button, View
# import random
from datetime import datetime
api_key = 'Your google search api key, available to get on https://console.cloud.google.com/'
class Img(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(name = 'img', description = 'Searching image and sending it for you.')
    async def slashimg(self, ctx, *, search: str = nextcord.SlashOption(name = 'keyword', description = 'Type a keyword to search.')):
        current = 0
        google_icon = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/120px-Google_%22G%22_Logo.svg.png?20210618182606.nextcordapp.com/attachments/1010156138978869360/1010156205437632512/chadbot.png'
        resource = build('customsearch', 'v1', developerKey=api_key).cse()
        result = resource.list(q=f'{search}', cx = 'Your custom search ID', searchType='image').execute()
        embed1 = nextcord.Embed(title=f'**{search.title()}**',colour=0xed0000, timestamp=datetime.utcnow())
        embed1.set_image(url=result['items'][0]['link'])
        embed1.set_footer(icon_url = google_icon,text = f'Page 1/10')
        embed2 = nextcord.Embed(title=f'**{search.title()}**',colour=0xed0000, timestamp=datetime.utcnow())
        embed2.set_image(url=result['items'][1]['link'])
        embed2.set_footer(icon_url = google_icon,text = f'Page 2/10')
        embed3 = nextcord.Embed(title=f'**{search.title()}**',colour=0xed0000, timestamp=datetime.utcnow())
        embed3.set_image(url=result['items'][2]['link'])
        embed3.set_footer(icon_url = google_icon,text = f'Page 3/10')
        embed4 = nextcord.Embed(title=f'**{search.title()}**',colour=0xed0000, timestamp=datetime.utcnow())
        embed4.set_image(url=result['items'][3]['link'])
        embed4.set_footer(icon_url = google_icon,text = f'Page 4/10')
        embed5 = nextcord.Embed(title=f'**{search.title()}**',colour=0xed0000, timestamp=datetime.utcnow())
        embed5.set_image(url=result['items'][4]['link'])
        embed5.set_footer(icon_url = google_icon,text = f'Page 5/10')
        embed6 = nextcord.Embed(title=f'**{search.title()}**',colour=0xed0000, timestamp=datetime.utcnow())
        embed6.set_image(url=result['items'][5]['link'])
        embed6.set_footer(icon_url = google_icon,text = f'Page 6/10')
        embed7 = nextcord.Embed(title=f'**{search.title()}**',colour=0xed0000, timestamp=datetime.utcnow())
        embed7.set_image(url=result['items'][6]['link'])
        embed7.set_footer(icon_url = google_icon,text = f'Page 7/10')
        embed8 = nextcord.Embed(title=f'**{search.title()}**',colour=0xed0000, timestamp=datetime.utcnow())
        embed8.set_image(url=result['items'][7]['link'])
        embed8.set_footer(icon_url = google_icon,text = f'Page 8/10')
        embed9 = nextcord.Embed(title=f'**{search.title()}**',colour=0xed0000, timestamp=datetime.utcnow())
        embed9.set_image(url=result['items'][8]['link'])
        embed9.set_footer(icon_url = google_icon,text = f'Page 9/10')
        embed10 = nextcord.Embed(title=f'**{search.title()}**',colour=0xed0000, timestamp=datetime.utcnow())
        embed10.set_image(url=result['items'][9]['link'])
        embed10.set_footer(icon_url = google_icon,text = f'Page 10/10')
        img_pages = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10]
        previousButton = Button(label='<', style = ButtonStyle.blurple)
        nextButton = Button(label = '>', style = ButtonStyle.blurple)
        deleteButton = Button(label = '🗑️', style = ButtonStyle.danger)
        async def next_callback(interaction):
            nonlocal current, message
            current += 1
            await message.edit(embed=img_pages[current])
        async def previous_callback(interaction):
            nonlocal current, message
            current -= 1
            await message.edit(embed=img_pages[current])
        async def delete_callback(interaction):
            await message.delete()
        previousButton.callback = previous_callback
        nextButton.callback = next_callback
        deleteButton.callback = delete_callback
        myview = View(timeout=180)
        myview.add_item(previousButton)
        myview.add_item(nextButton)
        myview.add_item(deleteButton)
        message = await ctx.send(embed=embed1, view=myview)
class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(name = 'avatar', description = 'Sending an mentioned user avatar for you.')
    async def avatar(self, ctx:nextcord.Interaction, member: nextcord.Member = SlashOption(name = 'member', description='Please select a member', required = True)):
        memberAvatar = member.avatar.url
        avaEmbed = nextcord.Embed(title = f"{member.name}'s Avatar", colour=0xed0000, timestamp=datetime.utcnow())
        avaEmbed.set_image(url = memberAvatar)
        await ctx.send(embed=avaEmbed)
class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(name = 'userinfo', description = 'Sends informations of mentioned user')
    async def userinfo(self, ctx:nextcord.Interaction, member: nextcord.Member = SlashOption(name = 'member', description =' Please select a member', required = True)):
        memberNick = member.nick
        if memberNick == None:
            memberNick = 'No nickname'
        rlist = []
        for role in member.roles:
            rlist.append(role.mention)

        b = ','.join(rlist)
        uembed = nextcord.Embed(colour=0xed0000, timestamp=datetime.utcnow())
        uembed.set_thumbnail(url = member.avatar.url)
        uembed.add_field(name = '**User informations**', value = f'**User: ** {member.name}#{member.discriminator}\n**Nick:** {memberNick}\n**ID:** {member.id}', inline = False)
        uembed.add_field(name = '**Joined discord**', value = member.created_at.strftime("%b %d, %Y, %T"), inline = False)
        uembed.add_field(name = f'**Joined {member.guild.name}**', value = member.joined_at.strftime("%b %d, %Y, %T"), inline = False)
        uembed.add_field(name = f'**Roles: **({len(rlist)})', value = ''.join([b]), inline = False)
        uembed.set_footer(icon_url = self.bot.user.avatar, text = 'ChadBot')
        await ctx.send(embed=uembed)
class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(name = 'serverinfo', description = 'Sends information about server')
    async def serverinfo(self, ctx:nextcord.Interaction):
        vclist = []
        for channel in ctx.guild.voice_channels:
            vclist.append(channel.mention)
        tclist = []
        rlist = []
        for role in ctx.guild.roles:
            rlist.append(role.mention)
        for channel in ctx.guild.text_channels:
            tclist.append(channel.mention)
        sembed = nextcord.Embed(colour=0xed0000, timestamp=datetime.utcnow())
        sembed.set_author(icon_url = ctx.guild.icon.url, name = ctx.guild.name)
        sembed.set_thumbnail(url = ctx.guild.icon.url)
        sembed.add_field(name = '**Server ID:**', value = f'{ctx.guild.id}')
        sembed.add_field(name = '**Created on**', value = f'{ctx.guild.created_at.strftime("%b %d, %Y, %T")}')
        sembed.add_field(name = '**Owned by**', value = f'{ctx.guild.owner.mention}')
        sembed.add_field(name = f'**Members ({(ctx.guild.member_count)})**', value = f'**{ctx.guild.premium_subscription_count}** Boosts')
        sembed.add_field(name = f'**Channels ({len(vclist+tclist)})**', value = f'**{len(vclist)}** Voice | **{len(tclist)}** Text')
        sembed.add_field(name = f'**Roles ({len(rlist)}**)', value = 'To see a role list use **/roles**')
        sembed.set_footer(icon_url = self.bot.user.avatar, text = 'ChadBot')
        await ctx.send(embed=sembed)
class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(name = 'roles', description = 'Sends a list of server roles')
    async def roles(self, ctx:nextcord.Interaction):
        rlist = []
        for role in ctx.guild.roles:
            if role.name != "@everyone":
                rlist.append(role.mention)
        b = ','.join(rlist)
        rembed = nextcord.Embed(colour=0xed0000, timestamp=datetime.utcnow())
        rembed.set_author(icon_url = ctx.guild.icon.url, name = f'{ctx.guild.name} role list')
        rembed.add_field(name = f'**{ctx.guild.name} roles ({len(rlist)})**', value = f''.join([b]), inline = False)
        rembed.set_footer(icon_url = self.bot.user.avatar, text = 'ChadBot')
        await ctx.send(embed=rembed)
