import os
import discord
import random
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#Using a .env file to stop discord token from being uploaded to places
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

based_role = 862122776658444349
cringe_role = 862124825550913587

#player role IDs
beefus = 364860521419243520
smack = 82671142287970304
pedaeus = 216992464328851456

@client.event
async def on_ready():
    print("bot conneceted")

@client.event
async def on_message(message):
    #message.author is of type Member
    #print(f"message author is {type(message.author)}")
    #print(f"message nick is {message.author.nick}")
    #print(f"message contents are {message.content}\n")
    #print(discord.Member.nick)
    
    
    #print(based_role in message.author.roles)
    #print(cringe_role in message.author.roles)
    
    
    if message.author == client.user: 
        return
    #if message.author.id == 216992464328851456 and "what if" in message.content:
    #    await message.channel.send("testing <@!216992464328851456>")
    #    return
    if message.author.id == 364860521419243520 and random.randint(1,101) <= 5:
        await message.channel.send("You 1k cp yet Beefus?")
    if "what if" in message.content and message.author.id == 364860521419243520 and random.randint(0,10) >= 3:
        await message.channel.send("<@!364860521419243520> can u stop?")
    if "<@!82671142287970304>" in message.content:
        nick = message.author.nick
        name = message.author.name
        if nick == None:
            nick = name
        await message.channel.send(f"U tryna fite {nick}?")
    #StickToPvP Role
    if "<@&818697316013834262>" in message.content:
        nick = message.author.nick
        name = message.author.name
        if nick == None:
            nick = name
        await message.channel.send(f"I had overload :(")
    #Bashing Baboon thing
    #if "<@&824122867859587072>" in message.content:
    #    await message.channel.send(f"C'mon man, everyone makes mistakes")
    if "based" in message.content.lower():
        await message.add_reaction(r":SmackPilled:828833530414628864") #SmackPilled
    #    if based_role in message.author.roles and random.randint(1,11) <= 5:
    #        await message.channel.send("Super Based")
    if "cringe" in message.content.lower():
        await message.add_reaction(r":SirpzPilled:828833060950376448") #SirpzPilled:
    #    if cringe_role in message.author.roles and random.randint(1,11) <= 5:
    #        await message.channel.send("Super Cringe")

client.run(DISCORD_TOKEN)

