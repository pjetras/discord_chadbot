import nextcord
from nextcord import Interaction, SlashOption, ButtonStyle, slash_command
from nextcord.ext import commands
from nextcord.ui import Button, View
from datetime import datetime
 
class Dropdown(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='Moderation', description = 'Moderation commands help', emoji = '🔰'
            ),
            nextcord.SelectOption(
                label = 'Utillity', description = 'Utillity commands help', emoji = '🌐'
            ),
        ]
        super().__init__(
            placeholder = "❔ Select your help category",
            min_values = 1,
            max_values = 1,
            options=options,
        )
class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(name = 'help', description = 'ChadBot help')
    async def help(self, ctx:Interaction):
        current = 0
        moderationembed1 = nextcord.Embed(title = '**Moderation help**', colour=0xed0000)
        moderationembed1.set_author(name = 'ChadBot help', icon_url = self.bot.user.avatar)
        moderationembed1.add_field(name = '/kick or -kick', value = 'Kicks a member out of the server, Usage:\n```/kick [member mention] (reason)```', inline = False)
        moderationembed1.add_field(name = '/ban or -ban', value = 'Bans a member on the server, Usage:\n```/ban [member mention] (reason)```', inline = False)
        moderationembed1.add_field(name = '/clear or -clear', value = 'Purges a channel, Usage:\n```/clear [amount of messages]```', inline = False)
        moderationembed1.set_footer(icon_url = self.bot.user.avatar, text = 'Page 1/2 |  © pjetras')
        moderationembed2 = nextcord.Embed(title = '**Moderation help**', colour=0xed0000)
        moderationembed2.set_author(name = 'ChadBot help', icon_url = self.bot.user.avatar)
        moderationembed2.add_field(name = '/timeout', value = 'Timing out a member, Usage:\n```/timeout [member mention] [timestamp] (reason)```', inline = False)
        moderationembed2.add_field(name = '/ban or -ban', value = 'Untiming out a member, Usage:\n```/untimeout [member mention] (reason)```', inline = False)
        moderationembed2.set_footer(icon_url = self.bot.user.avatar, text = 'Page 2/2 |  © pjetras')
        moderation_pages = [moderationembed1, moderationembed2]
        utillityembed1 = nextcord.Embed(title = '**Utillity help**', colour=0xed0000)
        utillityembed1.set_author(name = 'ChadBot help', icon_url = self.bot.user.avatar)
        utillityembed1.add_field(name = '/img', value = 'Searches an Image in google and sends it for you, Usage:\n```/img [keyword]```', inline = False)
        utillityembed1.add_field(name = '/avatar', value = "Sends a member's avatar for you, Usage:\n```/avatar [member mention]```", inline = False)
        utillityembed1.add_field(name = '/userinfo', value = 'Sends informations of mentioned user, Usage:\n```/userinfo [member mention]```', inline = False)
        utillityembed1.set_footer(icon_url = self.bot.user.avatar, text = 'Page 1/2 |  © pjetras')
        utillityembed2 = nextcord.Embed(title = '**Utillity help**', colour=0xed0000)
        utillityembed2.set_author(name = 'ChadBot help', icon_url = self.bot.user.avatar)
        utillityembed2.add_field(name = '/serverinfo', value = 'Sends informations about the server, Usage:\n```/serverinfo```', inline = False)
        utillityembed2.add_field(name = '/roles', value = "Sends the server role list, Usage:\n```/roles```", inline = False)
        utillityembed2.set_footer(icon_url = self.bot.user.avatar, text = 'Page 2/2 |  © pjetras')
        util_pages = [utillityembed1, utillityembed2]
        modpreviousButton = Button(label='<', style = ButtonStyle.blurple)
        modnextButton = Button(label = '>', style = ButtonStyle.blurple)
        utilpreviousButton = Button(label='<', style = ButtonStyle.blurple)
        utilnextButton = Button(label = '>', style = ButtonStyle.blurple)
        async def modnext_callback(interaction):
            nonlocal current, message
            if current < 1:
                current += 1
                await message.edit(embed=moderation_pages[current])
            else:
                return
        async def modprevious_callback(interaction):
            nonlocal current, message
            if current > 0:
                current -= 1
                await message.edit(embed=moderation_pages[current])
            else:
                return
        async def utilnext_callback(interaction):
            nonlocal current, message
            if current < 1:
                current += 1
                await message.edit(embed=util_pages[current])
            else:
                return
        async def utilprevious_callback(interaction):
            nonlocal current, message
            if current > 0:
                current -= 1
                await message.edit(embed=util_pages[current])
            else:
                return
        modpreviousButton.callback = modprevious_callback
        modnextButton.callback = modnext_callback
        utilpreviousButton.callback = utilprevious_callback
        utilnextButton.callback = utilnext_callback
        moderationview = View(timeout=0)
        moderationview.add_item(modpreviousButton)
        moderationview.add_item(modnextButton)
        moderationview.add_item(Dropdown())
        utilview = View(timeout=0)
        utilview.add_item(utilpreviousButton)
        utilview.add_item(utilnextButton)
        utilview.add_item(Dropdown())
        myview1 = View(timeout=0)
        # myview1.add_item(add_bot)
        myview1.add_item(Dropdown())
        hembed = nextcord.Embed(title = '**ChadBot commands**',colour=0xed0000, timestamp=datetime.utcnow())
        hembed.add_field(name = '**» Help menu**', value = 'Help menu has `2` categories and `8` commands in them.', inline = False)
        hembed.add_field(name = '**» Categories**', value = '`🔰 Moderation`\n`🌐 Utillity`\n`🔞 NSFW - Soon`', inline = False)
        hembed.add_field(name = '**» Useful links**', value = '[Invite bot](https://discord.com/api/oauth2/authorize?client_id=888483961838370876&permissions=8&scope=bot%20applications.commands) | [Support server](https://discord.gg/K9saZevd98)')
        hembed.set_footer(icon_url = self.bot.user.avatar, text = '© pjetras')
        message = await ctx.response.send_message(embed=hembed, ephemeral=True, view=myview1)
        async def callback(self, ctx:Interaction):
            if self.values[0] == 'Moderation':
                return await message.edit(embed=moderationembed1, view=moderationview)
            if self.values[0] == 'Utillity':
                return await message.edit(embed=utillityembed1, view=utilview)
        nextcord.ui.Select.callback = callback
