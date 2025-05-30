import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
import aiohttp
import subprocess
from datetime import datetime
import pytz
from utils.database import init_db
from utils.config import load_config, get_config

# 🔐 .env laden
load_dotenv()
config = load_config()

# ✅ Konfiguration
TOKEN = os.getenv("TOKEN")
GUILD_ID = int(config["bot"]["guild_id"])
STATUS_CHANNEL_ID = int(config["bot"]["status_channel_id"])
WEBHOOK_URL = config["bot"]["webhook_url"]
guild_object = discord.Object(id=GUILD_ID)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# 📦 On Ready
@bot.event
async def on_ready():
    print(f"✅ Bot ist bereit! Eingeloggt als {bot.user}")
    try:
        await bot.tree.sync(guild=guild_object)
        print(f"✅ Slash Commands nur für GUILD {GUILD_ID} registriert")
    except Exception as e:
        print(f"❌ Fehler beim Slash Command Sync: {e}")

    latency_rounded = round(bot.latency, 2)
    print(f"❱ Started as:\n『 {bot.user.name} 』")
    print("❱ Ping:\n『 {}s 』".format(latency_rounded))

    asyncio.create_task(rotierender_status())
    await send_startup_notification()

# 🔄 Status wechselt automatisch
async def rotierender_status():
    await bot.wait_until_ready()
    statustexte = [
        lambda: f"Ping: {round(bot.latency * 100)}ms",
        lambda: "📘 Template Discord Bot aktiv!",
        lambda: "/hilfe für alle Befehle",
    ]
    while True:
        for eintrag in statustexte:
            try:
                text = eintrag() if callable(eintrag) else eintrag
                await bot.change_presence(
                    activity=discord.CustomActivity(name=text),
                    status=discord.Status.dnd
                )
                await asyncio.sleep(60)
            except Exception as e:
                print(f"❌ Fehler beim Status-Update: {e}")
                await asyncio.sleep(60)

# 🌐 Startmeldung per Webhook
async def send_startup_notification():
    try:
        commit_message = subprocess.check_output(['git', 'log', '-1', '--pretty=%s'], text=True).strip()
        commit_author = subprocess.check_output(['git', 'log', '-1', '--pretty=%an'], text=True).strip()
    except Exception as e:
        commit_message = "❌ Kein Commit gefunden"
        commit_author = f"Fehler: {e}"

    timezone = pytz.timezone("Europe/Berlin")
    now = datetime.now(timezone).strftime("%d.%m.%Y %H:%M:%S Uhr")

    embed = {
        "title": "🔁 Bot-Neustart erfolgreich!",
        "description": f"**Letzter Commit:** `{commit_message}`\n"
                       f"**Autor:** `{commit_author}`\n"
                       f"**Startzeit:** `{now}`",
        "color": 0x2ecc71
    }

    if WEBHOOK_URL:
        async with aiohttp.ClientSession() as session:
            try:
                await session.post(WEBHOOK_URL, json={"embeds": [embed]})
            except Exception as e:
                print(f"❌ Fehler beim Senden der Webhook-Nachricht: {e}")

# 🧠 Alle Cogs automatisch laden
async def load_extensions():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py") and not filename.startswith("_"):
            ext_name = f"cogs.{filename[:-3]}"
            try:
                await bot.load_extension(ext_name)
                print(f"✅ Geladen: {ext_name}")
            except Exception as e:
                print(f"❌ Fehler beim Laden von {ext_name}: {e}")

# ▶️ Einstiegspunkt
async def main():
    init_db()
    await load_extensions()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
