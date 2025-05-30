# Template Discord Bot

**Template Discord Bot** ist ein vielseitiges Startprojekt für moderne Discord-Bots.  
Mit klarer Struktur, modularer Erweiterbarkeit und systemd-/Webhook-Integration eignet sich dieses Projekt perfekt für produktionsreife Bots.

---

## 🚀 Schnellstart

### 1. Projekt klonen

```bash
git clone https://github.com/dein-nutzername/template-discord-bot.git
cd template-discord-bot
```

### 2. Abhängigkeiten installieren

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. `.env` einrichten

```env
# .env Datei
TOKEN=dein_bot_token
GUILD_ID=123456789012345678
STATUS_CHANNEL_ID=123456789012345678
WEBHOOK_URL=https://discord.com/api/webhooks/...
```

### 4. Konfiguration anpassen

```yaml
# config.yaml
bot:
  guild_id: 123456789012345678
  status_channel_id: 987654321098765432
  webhook_url: "https://discord.com/api/webhooks/..."

features:
  enable_reminders: true
```

---

## 🔁 systemd Autostart (optional)

```bash
sudo cp systemd-template.service /etc/systemd/system/templatebot.service
sudo systemctl daemon-reload
sudo systemctl enable templatebot
sudo systemctl start templatebot
```

---

## 💡 Slash-Befehle

| Befehl              | Beschreibung                                        |
|---------------------|-----------------------------------------------------|
| `/ping`             | Zeigt die aktuelle Bot-Latenz                       |
| `/userinfo [user]`  | Zeigt Informationen über ein Mitglied               |
| `/erinnerung`       | Zeigt, speichert oder löscht deine Notizen          |
| `/hilfe`            | Übersicht über alle verfügbaren Befehle             |
| `/config_reload`    | Lädt die `config.yaml` neu (nur für Owner)          |

---

## 📚 Lizenz

Dieses Projekt steht unter der [MIT License](LICENSE).  
Du darfst es frei verwenden, verändern und veröffentlichen.

---

## 🤝 Mitmachen

Pull Requests, Vorschläge & neue Module sind willkommen!  
Starte z. B. mit einer eigenen `cogs/meinmodul.py` und ergänze `config.yaml` um deine Features.

---

## 🛠 Kontakt & Hilfe

Erstellt von [Treiko](https://github.com/Treiko-ctrl)  
Für Fragen: Issues öffnen oder Discord verlinken
