import discord
from discord.ext import commands
from discord import app_commands
from utils import config

class ConfigReload(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="config_reload", description="Lädt die config.yaml neu (nur Owner).")
    async def config_reload(self, interaction: discord.Interaction):
        owner_id = self.bot.owner_id or 0
        if interaction.user.id != owner_id:
            await interaction.response.send_message("❌ Du darfst diesen Befehl nicht nutzen.", ephemeral=True)
            return

        try:
            config.reload_config()
            await interaction.response.send_message("✅ config.yaml wurde erfolgreich neu geladen.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Fehler beim Neuladen: {e}", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(ConfigReload(bot))
