import discord
from discord.ext import commands
import os, random
import requests
from model import get_class
from checkname import check_extention, Random_Question, Quiz #Answering


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')



@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def news(ctx):
    await ctx.send(f"Oto losowa ciekawostka:\n{Random_Question()}")


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if check_extention(attachment.filename) == True :
                name = attachment.filename
                url = attachment.url
                await attachment.save(name)
                await ctx.send("....Saved:)")
                await ctx.send(get_class(model="keras_model.h5", labels="labels.txt", image = name))
    else :
        await ctx.send("Nothing here")

@bot.command()
async def quiz(ctx):
    await ctx.send(f"Oto losowe pytanie\n{Quiz()}")
    # if ctx.message.attachments :
    #     answer = ctx.message.attachments 
    #     Answering(answer)
    
@bot.command()
async def comands(ctx):
    await ctx.send("komendy:\n hello - przywitaj się z botem \n news - losowe ciekawostki \n quiz - chce wziąść udział w quizie z ciekawostek \n check - możesz zrobić zdięcie elektrowni por ekologicznej a sztuczna inteligencja powiadomi się co to za elektrownia:)")







bot.run("SECRET TOKEN")

