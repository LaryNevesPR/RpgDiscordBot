import discord
import os
import random
import asyncio
import aiosqlite
from discord.ext import commands
from tokenbot import TOKEN

client = commands.Bot(command_prefix="-",intents=discord.Intents.all())

async def load():
    for filename in os.listdir('./Cogs'):
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