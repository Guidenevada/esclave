import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

token = "OTUwNTAxMzAwOTg1MDEyMjU2.YiZ1UQ.NPnIHwHd4EVFPtdaUBn8R7eEVXI"

#bot = commands.Bot(command_prefix='>')

async def on_message(message, channel):
    if message.author == discord.Client().user:
        return
    try:
        table = str(channel.message.content()).replace(" ", ";")
        os.system("echo '" + table + "' >> table.csv")
        channel.send("sauvegarde effectuée")
    except:
        channel.send("erreur")

discord.Client.on_message = on_message
discord.Client.run(token)    

channel = discord.Client.get_channel(channel_id)
discord.Client().run(token)
