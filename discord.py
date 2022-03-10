

from dis import disco
from email import message
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random
load_dotenv()
bot = commands.Bot(command_prefix='>')

token = "token"
client = discord.Client()
#bot = commands.Bot(command_prefix='>')
@bot.command()
async def test(ctx, *args):
    if args[0] == "test":
        await ctx.send("test")
    channel = client.get_channel(id='921017174481567765')
    channel.send("test du bot")

@client.event
async def on_message(message, channel):
    try:
        channel = client.get_channel(id='921017174481567765')
        channel.send("test du bot")
        if message.author == discord.Client().user:
            return
        channel = client.get_channel(931555646246121542)

        if '>achat' in message.content.lower():

        

            channel = discord.Client.get_channel(id='celui du bot, encore à définir')
            table = str(channel.message.content()).replace(" ", ";")
            table = table.replace(">", "")
            if 'dete' in message.content.lower():
                channel = client.get_channel(id='928702815679971348')
                channel.send(table)

            else:
                table = str(table)
                readable = table.replace(";", " ")
                channel = client.get_channel(id='931555646246121542')
                channel.send(readable)
            os.system("echo '" + table + "' >> table/user.csv")
            channel.send("sauvegarde effectuée")
    
        if '>ajout_produit' in message.content.lower():

            table = str(channel.message.content()).replace(" ", ";")
            table = table.replace(">", "")
            os.system("echo '" + table + "' >> table/produit.csv")
            channel.send("produit ajouté à la base de données")
    
        if '>aide' in message.content.lower():
            message.channel.send("utilisation : >achat nom;produit;argent;dete")
            message.channel.send("utilisation : >ajout_produit nom;quantité;prix")
            message.channel.send("utilisation : >liste_produit   affiche la liste des produits")
            message.channel.send("utilisation : >liste_detes     affiche la liste des detes")
        if '>liste_produit' in message.content.lower():
            channel = client.get_channel(921017174481567765)
            message.channel.send("liste des produits : \n" + os.popen("cat table/produit.csv").read())
        if 'connard' in message.content.lower():
            message.channel.send("faites l'amour pas la guerre!")
        if '>liste_detes' in message.content.lower():
            message.channel.send("liste des detes : \n" + os.system("cat table/user.csv | grep oui").read())
        if '>bug' in message.content.lower():
            bug = str(message.content).replace(">bug", "")
            os.system ("echo '" + bug + "' >> bug.txt")
            message.channel.send("bug reporté : " + bug)

        message.channel.send("tâche effectuée")
    except Exception as e:
        message.channel.send("erreur")
        print("erreur \n " + str(e))



    
    
if __name__ == '__main__':
    client.run(token)
    discord.Client.on_message = on_message
    discord.Client.run(token)    
    client = discord.Client()

    bot.run(token)

