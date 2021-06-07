import os
import discord
import random

client = discord.Client()

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
    if message.author == client.user: 
        return
    #if message.author.id == 216992464328851456 and random.randint(1,10) >= 9:
    #    return
    if message.author.id == 364860521419243520 and random.randint(1,101) <= 5:
        await message.channel.send("You 810 yet Beefus?")
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
        await message.channel.send(f"Meet me in stormhaven {nick}")
    #Bashing Baboon thing
    if "<@&824122867859587072>" in message.content:
        await message.channel.send(f"C'mon man, everyone makes mistakes")
    if "based" in message.content.lower():
        await message.add_reaction(r":SmackPilled:828833530414628864") #SmackPilled
    if "cringe" in message.content.lower():
        await message.add_reaction(r":SirpzPilled:828833060950376448") #SirpzPilled


client.run("ODI1MTc3NDc2ODg3MjE2MTQ5.YF6IaQ.5_myI33vkbjZ0auZl8A9I13M2Q0")
