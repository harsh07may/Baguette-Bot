import os
import discord
from keep_alive import keep_alive
from discord.ext import commands

client = discord.Client()

cuss = {
  #french
   "putain":"Son of a bitch",
   "salope":"Bitch",
   "conne":"Fucking idiot",
   "pute":"Slut",
   "connard":"Idiot",
   "va chier":"Fuck you",
   "tu fait chier":"Youre annoying",
   "va te faire foutre":"go fuck yourself",
   "gros connard":"fat fuck",
   "ferme ta geule":"shut the fuck up",
   "stupide":"idiot",
   "putain de merde":"fuck",
   "merde":"shit",
   #french canadian 
   "Tabarnak":"fuck or fucking idiot",
   "Caliss":"fuck",
   "Osti":"fuck",
   "Siboire":"fuck",
   "Mange de la merde":"eat shit",
   "criss":"fucking idiot",
   "caliss":"fucking idiot",
   "osti de cave":"fucking idiot",
   "gros lard":"fat fuck",
   "gros cave":"fucking idiot",
   #SG
   "Gan":"Fuck",
   "Tekkan":"To fuck",
   "Honggan":"Be screwed",
   "CB":"Pussy",
   "Chibai":"Pussy",
   "Cibai":"Pussy",
   "Chaochibai":"Fucking pussy",
   "Caochibai":"Fucking pussy",
   "Caocibai":"Fucking pussy",
   "CCB":"Fucking pussy",
   "Gannina":"Fuck your mom",
   "Kannina":"Fuck your mom",
   "Kanina":"Fuck your mom",
   "KNN":"Fuck your mom",
   "Kan ni nabuei":"Fuck your mom/dad",
   "Kanninabuei":"Fuck your mom/dad",
   "Nabei":"Fuck your dad",
   "Nabu":"Fuck your mom",
   "Lanjiao":"Dick (Also: Bullshit)",
   "LJ":"Dick (Also: Bullshit)",
   "Lampah":"Balls",
   "Kamlan":"Suck dick",
   "Kaobei":"Cause problems (Lit: Cry for dad)",
   "Kaopeh":"Cause problems (Lit: Cry for dad)",
   "KP":"Cause problems (Lit: Cry for dad)",
   "Kaopeh Kaobu":"Cause problems (Lit: Cry for parents)",
   "Kaobei Kaobu":"Cause problems (Lit: Cry for parents)",
   "KPKB":"Cause problems (Lit: Cry for parents)",
   "jiaksua":"Shirker",
   "Kayu":"Retarded",
   "simi lanjiao":"the fuck",
   "similan":"the fuck",
   "SML":"the fuck",
   "neh neh":"boobs",
   "neh neh pok":"boobs",
   "paikia":"bad kid",
   "simi":"what",
   "goondu":"idiot",
   "gundu":"idiot",
   "guailan":"to bother (lit: weird dick)",
   "cheekopek":"geezer",
   "cheekupek":"geezer",
   "bolampah":"no balls",
   #japanese
   "Busu":"ugly",
   "debu":"fatty",
   "ama":"bitch)",
   "kuso ama":"shitty bitch",
   "baka":"idiot",
   "aho":"stupid",
   "kuso gaki":"shitty brat",
   "gaki":"brat",
   "uzai":"annoying",
   "shine":"die/kys",
   "damare":"shut up"
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
