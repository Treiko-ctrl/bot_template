import discord
from discord.ext import commands
from discord import app_commands

class Hilfe(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="hilfe", description="Zeigt eine Übersicht aller verfügbaren Befehle.")
    async def hilfe(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="📘 Hilfe – Befehlsübersicht",
            description="Hier sind alle verfügbaren Slash-Befehle:",
            color=discord.Color.blue()
        )

        embed.add_field(
            name="🏓 `/ping`",
            value="→ Zeigt die aktuelle Latenz des Bots.",
            inline=False
        )

        embed.add_field(
            name="👤 `/userinfo`",
            value="→ Zeigt Informationen über ein Mitglied.",
            inline=False
        )

        embed.add_field(
            name="📌 `/erinnerung`",
            value="→ Erstelle, zeige oder lösche persönliche Erinnerungen.",
            inline=False
        )

        embed.add_field(
            name="📖 `/hilfe`",
            value="→ Diese Übersicht anzeigen.",
            inline=False
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Hilfe(bot))
