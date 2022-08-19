import nextcord
from nextcord.ext import commands
from googleapiclient.discovery import build
import asyncio
from datetime import datetime
api_key = 'Your google search api key, available to get on https://console.cloud.google.com/'
class Img(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Command
    async def img(self, ctx,*,search):
        resource = build('customsearch', 'v1', developerKey=api_key).cse()
        result = resource.list(q=f'{search}', cx = 'Your custom search engine ID, https://cse.google.com/', searchType='image').execute()
#         I know it is possible to do in fewer lines but im still learning
        embed1 = nextcord.Embed(title=f'**{search.title()}, Page 1**',colour=0x62008f, timestamp=datetime.utcnow())
        embed1.set_image(url=result['items'][0]['link'])
        embed1.set_footer(icon_url = 'Your avatar URL',text = f'Page 1/10 | Requested by {ctx.author.name}')
        embed2 = nextcord.Embed(title=f'**{search.title()}**, Page 2',colour=0x62008f, timestamp=datetime.utcnow())
        embed2.set_image(url=result['items'][1]['link'])
        embed2.set_footer(icon_url = 'Your avatar URL',text = f'Page 2/10 | Requested by {ctx.author.name}')
        embed3 = nextcord.Embed(title=f'**{search.title()}**, Page 3',colour=0x62008f, timestamp=datetime.utcnow())
        embed3.set_image(url=result['items'][2]['link'])
        embed3.set_footer(icon_url = 'Your avatar URL',text = f'Page 3/10 | Requested by {ctx.author.name}')
        embed4 = nextcord.Embed(title=f'**{search.title()}**, Page 4',colour=0x62008f, timestamp=datetime.utcnow())
        embed4.set_image(url=result['items'][3]['link'])
        embed4.set_footer(icon_url = 'Your avatar URL',text = f'Page 4/10 | Requested by {ctx.author.name}')
        embed5 = nextcord.Embed(title=f'**{search.title()}**, Page 5',colour=0x62008f, timestamp=datetime.utcnow())
        embed5.set_image(url=result['items'][4]['link'])
        embed5.set_footer(icon_url = 'Your avatar URL',text = f'Page 5/10 | Requested by {ctx.author.name}')
        embed6 = nextcord.Embed(title=f'**{search.title()}, Page 1**',colour=0x62008f, timestamp=datetime.utcnow())
        embed6.set_image(url=result['items'][0]['link'])
        embed6.set_footer(icon_url = 'Your avatar URL',text = f'Page 1/10 | Requested by {ctx.author.name}')
        embed7 = nextcord.Embed(title=f'**{search.title()}**, Page 2',colour=0x62008f, timestamp=datetime.utcnow())
        embed7.set_image(url=result['items'][1]['link'])
        embed7.set_footer(icon_url = 'Your avatar URL',text = f'Page 2/10 | Requested by {ctx.author.name}')
        embed8 = nextcord.Embed(title=f'**{search.title()}**, Page 3',colour=0x62008f, timestamp=datetime.utcnow())
        embed8.set_image(url=result['items'][2]['link'])
        embed8.set_footer(icon_url = 'Your avatar URL',text = f'Page 3/10 | Requested by {ctx.author.name}')
        embed9 = nextcord.Embed(title=f'**{search.title()}**, Page 4',colour=0x62008f, timestamp=datetime.utcnow())
        embed9.set_image(url=result['items'][3]['link'])
        embed9.set_footer(icon_url = 'Your avatar URL',text = f'Page 4/10 | Requested by {ctx.author.name}')
        embed10 = nextcord.Embed(title=f'**{search.title()}**, Page 5',colour=0x62008f, timestamp=datetime.utcnow())
        embed10.set_image(url=result['items'][4]['link'])
        embed10.set_footer(icon_url = 'Your avatar URL',text = f'Page 5/10 | Requested by {ctx.author.name}')
        img_pages = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10]
        message = await ctx.send(embed=embed1)
        buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
        current = 0
 
        for button in buttons:
            await message.add_reaction(button)
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check = lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)
            except asyncio.TimeoutError:
                return print('test')
            else:
                previous_page = current

                if reaction.emoji == u"\u23EA":
                    current = 0
                elif reaction.emoji == u"\u25C0":
                    if current > 0:
                        current -=1
                elif reaction.emoji == u"\u25B6":
                    if current < len(img_pages)-1:
                        current +=1
                elif reaction.emoji == u"\u23E9":
                    current = len(img_pages)-1
    
                for button in buttons:
                    await message.remove_reaction(button, ctx.author)
                if current != previous_page:
                    await message.edit(embed=img_pages[current])
