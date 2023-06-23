import discord
import os
import random
import asyncio
import aiosqlite
from Recursos.JsonDef import Ler_Players, salve_json
from discord.ext import commands
from tokenbot import TOKEN

client = commands.Bot(command_prefix="-",intents=discord.Intents.all())

path = ".\\Cogs"
async def load():
    for filename in os.listdir(path):
        if filename.endswith('.py'):
            await client.load_extension(f"Cogs.{filename[:-3]}")

async def main():
    await load()
    await client.start(TOKEN)

@client.event
async def on_ready():
    print("Sou gay e estou on")
    await client.tree.sync()

@client.tree.command(name = "hello", description = "diz olá")
async def hello(interaction: discord.Integration):
    robert = await interaction.response.send_message("hello!")

@client.tree.command(name= "criar", description= "test")
async def criarPlayer(interaction:discord.Integration):
    p = await Criar_player(interaction.user)
    if p == True:
        await interaction.response.send_message("Criado!")
    else:
        await interaction.response.send_message("Já criado!")

async def Criar_player(player):
    alayers = await Ler_Players()
    if not str(player.id) in alayers:
        print('Não está na lista')
        alayers[player.id]={
            'id': player.id,
            'nome': player.display_name,
            'gold': 0,
            'hpMax': 100,
            'hpAtual': 100,
            'level': 1
        }
        await salve_json(alayers)
        return True

#Teste
'''@client.tree.command(name= "mod", description= "test")
async def Mod(interaction:discord.Integration):
    alayers = await Ler_Players()
    player = interaction.user
    if not str(player.id) in alayers:
        await Criar_player(player)
    print("passou")
    alayers[str(player.id)]["Mana"] = "🥵"
    await salve_json(alayers)
    print ('p')'''


@client.tree.command(name= "escolha", description = "Eu faço suas escolhas!")
async def escolha(interaction: discord.Integration, args:str):
    argumentos = args.split(" ")
    choice = random.choice(argumentos)
    pensando = await interaction.response.send_message(":clock1: Pensando...")
    await asyncio.sleep(0.2)
    for i in range(4):
        await interaction.edit_original_response(content=f":clock{i+1}: Pensando...")
        await asyncio.sleep(0.2)
    
    await interaction.edit_original_response(content = choice)

asyncio.run(main())