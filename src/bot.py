import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='#')


@bot.command(name='hello', help='Displays a friendly message')
async def hello(context):
    await context.send('Hello to you!')


@bot.command(name='echo', help='Echoes the message back')
async def echo(context, message : str):
    await context.send(message)


@commands.has_role('camarada')
@bot.command(name='comrade', help='Comrades unite!')
async def comrade(context):
    await context.send('Hello comrade!')



bot.run(TOKEN)
