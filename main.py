import discord, os
from discord.ext import commands
from classes.Database import Database
from classes.Shop import Shop

client = commands.Bot(command_prefix = "$", intents = discord.Intents.all())
db = Database("server.db", client)
shop = Shop("server.db", client)

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        client.load_extension(f"cogs.{file[:-3]}")

@client.event
async def on_ready():
    db.create_tables()
    await client.change_presence(status = discord.Status.online, activity = discord.Game("$help"))
    print(f'{client.user} запущен и готов к работе!')

@client.command(aliases = ['profile',])
async def _profile(ctx):
    embed = discord.Embed(title = f"Профиль игрока {ctx.message.author}", color=0x8dc3bd)
    embed.set_thumbnail(url = ctx.message.author.avatar_url)
    embed.add_field(name = "Кол-во майнеров", value = db.getUserInformation(ctx.message.author.id)[0], inline = False)
    embed.add_field(name = "Баланс", value = db.getUserInformation(ctx.message.author.id)[1], inline = False)
    embed.add_field(name = "Уровень", value = db.getUserInformation(ctx.message.author.id)[2], inline = False)
    embed.add_field(name = "Опыт", value = db.getUserInformation(ctx.message.author.id)[3], inline = False)
    embed.set_footer(text = client.user, icon_url = client.user.avatar_url)
    await ctx.send(embed = embed)



if __name__ == "__main__":
    with open('token.txt', 'r') as file:
        client.run(file.readline())  