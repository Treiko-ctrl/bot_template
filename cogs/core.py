import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class Core(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # ✅ /ping-Befehl
    @app_commands.command(name="ping", description="Zeigt die Latenz des Bots.")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"🏓 Pong! Latenz: `{latency}ms`", ephemeral=True)

    # 👤 /userinfo-Befehl
    @app_commands.command(name="userinfo", description="Zeigt Informationen über ein Mitglied.")
    @app_commands.describe(member="Das Mitglied, über das du Infos sehen willst")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user
        roles = ", ".join(r.mention for r in member.roles[1:]) or "Keine Rollen"
        created = member.created_at.strftime("%d.%m.%Y")
        joined = member.joined_at.strftime("%d.%m.%Y") if member.joined_at else "unbekannt"

        embed = discord.Embed(
            title=f"👤 Informationen über {member.display_name}",
            color=discord.Color.blurple(),
            timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Account erstellt", value=created, inline=True)
        embed.add_field(name="Beigetreten am", value=joined, inline=True)
        embed.add_field(name="Rollen", value=roles, inline=False)

        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Core(bot))
