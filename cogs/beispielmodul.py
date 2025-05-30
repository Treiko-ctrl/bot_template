import discord
from discord.ext import commands
from discord import app_commands

class BeispielModul(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Antwortet mit Pong und zeigt die Latenz.")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! 🏓 `{latency}ms`")

async def setup(bot):
    await bot.add_cog(BeispielModul(bot))
