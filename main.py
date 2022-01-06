import os
import discord
from keep_alive import keep_alive
from discord.ext import commands

client = discord.Client()

cuss = {
  #list of words goes here 
}

cuss1=list(cuss.keys())
meaning=list(cuss.values())
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content.lower()
  x=len(cuss1)
  if message.content.startswith("!hello"):
    await message.channel.send("Hey!")
  
  if message.content.startswith("!list"):
    myEmbed=discord.Embed(title="French",description="",color=0x00ff00)
    for i in range(0,24): 
      myEmbed.add_field(name=cuss1[i],value=meaning[i],inline='true')
    await message.channel.send(embed=myEmbed)

  if message.content.startswith("!list"):
    myEmbed=discord.Embed(title="SG",description="",color=0x00ff00)
    for i in range(24,45): 
      myEmbed.add_field(name=cuss1[i],value=meaning[i],inline='true')
    await message.channel.send(embed=myEmbed)

  if message.content.startswith("!list"):
    myEmbed=discord.Embed(title="SG",description="",color=0x00ff00)
    for i in range(45,65): 
      myEmbed.add_field(name=cuss1[i],value=meaning[i],inline='true')
    await message.channel.send(embed=myEmbed)

  if message.content.startswith("!list"):
    myEmbed=discord.Embed(title="SG",description="",color=0x00ff00)
    for i in range(65,85): 
      myEmbed.add_field(name=cuss1[i],value=meaning[i],inline='true')
    await message.channel.send(embed=myEmbed)
  if message.content.startswith("!list"):
    myEmbed=discord.Embed(title="SG",description="",color=0x00ff00)
    for i in range(85,87): 
      myEmbed.add_field(name=cuss1[i],value=meaning[i],inline='true')
    await message.channel.send(embed=myEmbed)

  if any(word in msg for word in cuss1):
    for i in range(x):
      
        if(msg.find(cuss1[i])==0):
          y=i
    print(meaning[y])
    await message.channel.send('Translation:'+ meaning[y])
    
   

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
