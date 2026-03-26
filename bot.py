from hctvwrapper import Bot 
import os # for env
from dotenv import load_dotenv, dotenv_values
import random #coinflip
import requests #zapi aka zach quotes



load_dotenv()
bot = Bot(command_prefix="?")
coin = ["heads", "tails"]

@bot.event
async def on_ready(session):
    print("67")

@bot.command()
async def ping(ctx):
    await ctx.reply(f"its on buddy")
    print(f"online check made ")


@bot.command()
async def coinflip(ctx):
    await ctx.reply(random.choice(coin))


@bot.command()
async def zachquote(ctx):
    quote = requests.get("https://zapi-seven.vercel.app/quote/random")
    await ctx.reply(quote.text)

@bot.command()
async def flavortownproject(ctx):
    await ctx.reply("this is a flavortown project :D feel free to follow (https://flavortown.hackclub.com/projects/18266)")


@bot.command()
async def help(ctx):
    await ctx("Heres a list of our commands,?ping check if the bots online,?coinflip does a coinflip, ?zachquote pulls a random zach latta quote, ?flavortownproject shares the link to the flavortown project.")

bot.run(os.getenv("token"),channel="hack-bot")