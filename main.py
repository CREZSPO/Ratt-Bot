import discord 
from discord.ext import commands
import music
    
cogs = [music]

client = commands.Bot(command_prefix ='-', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("ODkyNjQzNTM5NzIzMzgyNzk1.YVP5FA.wUt4OIBxqFuoikUHGEG7_35QuHs")