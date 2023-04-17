import discord
from discord.ext import commands

TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_member_join(member):
    message = 'Bem-vindo ao servidor, membro!'
    await member.send(message)

bot.run(TOKEN)
