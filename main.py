import os
import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")

class MeuPrimeiroBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",intents=discord.Intents.all())

    async def setup_hook(self):
        sincronizados = await self.tree.sync()
        print(f"🔄 {len(sincronizados)} comando(s) sincronizado(s) globalmente")

bot = MeuPrimeiroBot()

@bot.event
async def on_ready():
    print(f"✅ {bot.user} está online!")

@bot.tree.command(name="ola",description="O bot te da um Oi, simples assim.")
async def ola(interaction:discord.Interaction):
    await interaction.response.send_message("Olá mundo!")

bot.run(TOKEN)
        