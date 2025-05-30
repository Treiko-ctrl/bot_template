import discord
from discord.ext import commands
from discord import app_commands
from utils import database

class Reminder(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        database.init_db()

    @app_commands.command(name="erinnerung", description="Erinnerung hinzufügen, anzeigen oder löschen.")
    @app_commands.describe(aktion="Was möchtest du tun?", text="Der Text der Erinnerung (nur bei 'hinzufügen')")
    async def erinnerung(self, interaction: discord.Interaction,
                         aktion: app_commands.Choice[str],
                         text: str = None):

        user_id = interaction.user.id

        if aktion.value == "anzeigen":
            reminders = database.get_reminders(user_id)
            if reminders:
                formatted = "\n".join(f"• {r}" for r in reminders)
                await interaction.response.send_message(f"📌 Deine Erinnerungen:\n{formatted}", ephemeral=True)
            else:
                await interaction.response.send_message("❌ Du hast keine gespeicherten Erinnerungen.", ephemeral=True)

        elif aktion.value == "hinzufügen":
            if not text:
                await interaction.response.send_message("⚠️ Bitte gib einen Erinnerungstext an.", ephemeral=True)
                return
            database.add_reminder(user_id, text)
            await interaction.response.send_message(f"✅ Erinnerung gespeichert: `{text}`", ephemeral=True)

        elif aktion.value == "löschen":
            database.delete_reminders(user_id)
            await interaction.response.send_message("🗑️ Alle deine Erinnerungen wurden gelöscht.", ephemeral=True)

    @erinnerung.autocomplete("aktion")
    async def erinnerung_autocomplete(self, interaction: discord.Interaction, current: str):
        options = ["anzeigen", "hinzufügen", "löschen"]
        return [
            app_commands.Choice(name=o.capitalize(), value=o)
            for o in options if current.lower() in o.lower()
        ]

async def setup(bot: commands.Bot):
    await bot.add_cog(Reminder(bot))
