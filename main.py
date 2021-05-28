import os
import discord
from dotenv import load_dotenv
import random
from keep_alive import keep_alive
load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds,name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# welcoming message
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

# bot functionalities
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.upper() == '!IB KIDS':
        response = random.choice(list(open('kids.txt')))
        embedVar = discord.Embed(title ='Ice breaker question for kids... 😁',description= response,color=0x7EFD95) 
        await message.channel.send(embed=embedVar) 

    elif message.content.upper() == '!IB WORK':
        response = random.choice(list(open('work.txt')))
        embedVar = discord.Embed(title ='Ice breaker question for coworkers... 🤝',description= response,
        color=0x1538D5) 
        await message.channel.send(embed=embedVar)

    elif message.content.upper() == '!IB SPICY' :
        response = random.choice(list(open('spicy.txt')))
        embedVar = discord.Embed(title ='Ice breaker question to spice up your friendship... 🔥',description= response,color=0xFD5F24) 
        await message.channel.send(embed=embedVar)

    elif message.content.upper() == '!IB WYR' :
        response = random.choice(list(open('wouldyourather.txt')))
        embedVar = discord.Embed(title ='Would you rather... 🤔',description= response,color=0xFDE02A)
        await message.channel.send(embed=embedVar)

    elif message.content.upper() == '!IB NEVER' :
        response = random.choice(list(open('neverhaveiever.txt')))
        embedVar = discord.Embed(title ='Never have I ever... 🚫',description= response,color=0xC81B07)
        await message.channel.send(embed=embedVar)

    elif message.content.upper() == '!IB TRUTH' :
        response = random.choice(list(open('truth.txt')))
        embedVar = discord.Embed(title ='One truth... 🤥',description= response,color=0x4FCD43)
        await message.channel.send(embed=embedVar)

    elif message.content.upper() == '!IB DARE' :
        response = random.choice(list(open('dare.txt')))
        embedVar = discord.Embed(title ='One dare... 😈',description= response,color=0x7A2F8F)
        await message.channel.send(embed=embedVar)

    elif message.content.upper() == '!IB TOT' :
        response = random.choice(list(open('thisorthat.txt')))
        embedVar = discord.Embed(title ='Choose between... 😏',description= response,color=0xFA82CF)
        await message.channel.send(embed=embedVar)
  
    elif message.content.upper() == '!IB HELP':
       embedVar = discord.Embed(title ='Hi, I am Ice Breaker Bot!',description= 'I will make your Discord conversations less boring. 🧊\nHere are the available question packs and their commands:\n \n!ib kids : Ice breaker question for kids 😁\n!ib spicy : Ice breaker question to spice up your friendship 🔥\n!ib work : Ice breaker question for coworkers 🤝\n!ib wyr : "Would you rather?" question 🤔\n!ib never : "Never have I ever" question 🚫\n!ib truth : One truth for truth or dare 🤥\n!ib dare : One dare for truth or dare 😈\n!ib tot : This or That question 😏',color=discord.Color.blue())
       await message.channel.send(embed=embedVar)

    elif '!IB' in message.content.upper():
        embedVar = discord.Embed(title ="Oops",description='There\'s a command error... Try " !ib help " ', color=discord.Color.blue())
        await message.channel.send(embed=embedVar)
    
    else:
      for i in ['ICEBREAKER', 'ICE BREAKER']:
        if i in message.content.upper():
          embedVar = discord.Embed(title ="Hi, I am Ice Breaker Bot!",description='I will make your Discord conversations less boring. 🧊\nAre you looking for me? Try " !ib help "', color=discord.Color.blue())
          await message.channel.send(embed=embedVar)
          
keep_alive()
client.run(TOKEN)
