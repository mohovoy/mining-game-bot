import discord
from discord.ext import commands
from main import shop


class Shop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Класс [Shop] активен")

    @commands.command(aliases = ['shop',])
    async def __Shop(self, ctx):
        embed = discord.Embed(title = f"Магазин", color=0x8dc3bd)
        embed.set_footer(text = self.client.user, icon_url = self.client.user.avatar_url)

        items = [item for item in shop.getAllMashines()]
        # for items in shop.getAllMashines():
        for item in items:
            embed.add_field(name = f"{item[0]} | {item[1]}", value = f"Стоимость: **{item[2]}**\nМощность: **{item[3]}**\nРек-ый уровень: **{item[4]}**", inline = True)

        await ctx.send(embed = embed)

    @commands.command(aliases = ['add',])
    async def __addMashine(self, ctx, cost: int = None, power: int = None, req_lvl: int = None, *, name: str = None):
        shop.addMashine(name, cost, power, req_lvl)
        await ctx.message.add_reaction('✅')
        # if name or cost or power or req_lvl is None:
        #     pass
        # else:
        #     shop.addMashine(name, cost, power, req_lvl)
        #     await ctx.message.add_reaction('✅')

def setup(client):
    client.add_cog(Shop(client))