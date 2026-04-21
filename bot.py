from hctvwrapper import Bot 
import os # for env
from dotenv import load_dotenv, dotenv_values
import random #coinflip
import requests #zapi aka zach quotes
import json


load_dotenv()
with open("channels.json","r") as f:
    connectchannels = json.load(f)
bot = Bot(command_prefix="?")
flavorkey = os.getenv("flavortown")

@bot.event
async def on_ready(session):
    print("67")
    

@bot.command()
async def flavorstore(ctx,text):
    url = "https://flavortown.hackclub.com/api/v1/store/"+ text
    headers = {
        "content-type": 'application/json',
        "Authorization": f"Bearer {flavorkey}"
    }
    getstore = requests.get(url, headers=headers)
    print(getstore)
    alldata = getstore.json()
    print(alldata)
    name = alldata.get("name")
    description = alldata.get("description")

    finaldata = f"Name:{name}\nDescription: {description}"
    
    await ctx.send(finaldata)

@bot.command()
async def flavorcookies(ctx,text):
    url = "https://flavortown.hackclub.com/api/v1/users/"+ text
    headers = {
        "content-type": "application/json",
        "Authorization": f"Bearer {flavorkey}"
    }
    cookiesdata = requests.get(url, headers=headers)
    print(cookiesdata)
    cookiedatajson = cookiesdata.json()
    print(cookiedatajson)
    dacookies = cookiedatajson.get("cookies")
    name = cookiedatajson.get("display_name")
    msg = f"User:{name} has {dacookies} cookies."
    await ctx.reply(msg)


@bot.command()
async def flavorinfo(ctx,text):
    url = f"https://flavortown.hackclub.com/api/v1/users/"+text
    headers = {
        "content-type": "application/json",
        "Authorization": f"Bearer {flavorkey}"
    }
    userinfodata = requests.get(url,headers=headers)
    userdatajson = userinfodata.json()
    print(userdatajson)
    name = userdatajson.get("display_name")
    liked = userdatajson.get("like_count")
    cookies = userdatajson.get("cookies")
    msg = f"User:{name} has liked {liked} projects and has {cookies} cookies!"
    print(msg)
    await ctx.reply(msg)
    
@bot.command()
async def ping(ctx):
    await ctx.reply(f"pong 🏓!")


@bot.command()
async def coinflip(ctx):
    coin = ["heads", "tails"]
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
    await ctx.reply("Heres a list of our commands,?ping check if the bots online,?coinflip does a coinflip, ?zachquote pulls a random zach latta quote, ?flavortownproject shares the link to the flavortown project.?flavorinfo id get data about a user,?flavorcookies id  get a users cookies,?flavorstore get info about a flavortown store item  " )

bot.run(os.getenv("token"),channels=connectchannels)