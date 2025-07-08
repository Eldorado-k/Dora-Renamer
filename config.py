import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "24817837")  # ⚠️ Requis
    API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")  # ⚠️ Requis
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8183564006:AAGi1AA-F9KayRBReMosL3M0tM1HkJd1kcU")  # ⚠️ Requis

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "Antiflix")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Aniflix:Lipun123@aniflix.q2wina5.mongodb.net/?retryWrites=true&w=majority&appName=Aniflix")  # ⚠️ Requis

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://envs.sh/Ag8.jpg")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '1740287480 7428552084').split()]  # ⚠️ Requis
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "BotZFlix") # ⚠️ Requis Nom d'utilisateur sans @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002757788052"))  # ⚠️ Requis
    FLOOD = int(os.environ.get("FLOOD", '105'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Salut {} ♡゙,Jᴇ sᴜɪs ʟᴇ ʀᴇɴᴀᴍᴇʀ ʙᴏᴛ 🦜 ᴄᴀᴘᴀʙʟᴇ ᴅ'ᴀʟʟᴇʀ à ᴜɴᴇ ᴠɪᴛᴇssᴇ ᴅᴇ 9Mᴏ/s 🚀

Lᴀ ғᴀçᴏɴ ᴅᴏɴᴛ ᴊᴇ ᴍᴇ sᴀᴄʀɪғɪᴇ ᴘᴏᴜʀ ᴍᴏɴ éǫᴜɪᴘᴀɢᴇ ⚓, Jᴇ ғᴇʀᴀɪ ᴅᴇ ᴍêᴍᴇ ᴘᴏᴜʀ ᴛᴇs ғɪᴄʜɪᴇʀs 📂. Sᴏɪᴛ ᴇɴ sûʀ. Mêᴍᴇ sɪ ᴍᴏɴ ᴇsᴛᴏᴍᴀᴄ ғᴀɪᴛ ᴅᴇs ʙʀᴜɪᴛs ᴅᴇ ᴍᴏᴛᴇᴜʀ, sᴀᴄʜᴇᴢ Qᴜᴇ, 

Jᴇ ᴛʀᴏᴜᴠᴇʀᴀɪ ʟᴇ Oɴᴇ ᴘɪᴇᴄᴇ 🏴‍☠️ ᴅᴇ ᴠᴏs ғɪᴄʜɪᴇʀs, ᴇᴛ Lᴇ ᴘʀᴏᴄʜᴀɪɴ ʀᴏɪ ᴅᴇs Pɪʀᴀᴛᴇs 🏆, ᴄᴇ sᴇʀᴀ Mᴏɪ 🍖.</b>\n\nCréé par ©<a href='t.me/BotZFlix>😜 BotZFlix</a>"""

    ABOUT_TXT = """<b>Bot ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃Mon Nom : {}
║┣⪼👼Créateur : <a href='t.me/ZFlixteamBot>🇰ιηg¢єу</a>
║┣⪼🤖Mise à Jour : <a href='t.me/BotZFlix'>BᴏᴛZFʟɪx</a>
║┣⪼📡 Hébergé Sur: Super Rapide
║┣⪼🗣️Langage : <a href='python.org'>Python3</a>
║┣⪼📚 Librairie : <a href='pyrogram.org'>Pyrogram</a>
║┣⪼🗒️Version : [𝟶.𝟷𝟾.3]
║╰━━━━━━━━━━━━━━━➣"""

    HELP_TXT = """
<b><blockquote>Ceci est le Menu d'aide. clique sur ses boutons ci-dessous pour voir l'aide.


<b>➜ propulsé par :</b> <a href=https://t.me/BotZFlix>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ ꭙ 𝐁ᴏᴛs</a>
"""

    LEG_TXT = """📑 <b><u>Comment configurer une légende personnalisée</u></b>

<b>•></b> /set_caption - Utiliser cette commande pour définir une légende personnalisée
<b>•></b> /see_caption - Utiliser cette commande pour voir votre légende personnalisée
<b>•></b> /del_caption - Utiliser cette commande pour supprimer votre légende personnalisée
Exemple:- <code> /set_caption 📕 Nom du fichier : {filename}
💾 Taille : {filesize}
⏰ Durée : {duration} </code>

✏️ <b><u>Comment renommer un fichier</u></b>
<b>•></b> Envoyer un fichier et taper le nouveau nom \nEt sélectionner le format [ document, video, audio ]."""

    ZFLIX_TXT = """<b><u>⛔️⛔️⛔️MESSAGE URGENT‼️‼️‼️ </u>

Rejoignez Notre Groupe de film & de séries. Dans ce groupe, il faut juste écrire le nom du film ou de la série, pour le recevoir

<u>EXEMPLE:</u>

<code>Loki 
Warrior
Hulk
Squid Game</code>

En écrivant le nom, Un bot va vous l'envoyé. il faut et seulement écrire le nom du film.


<a href='t.me/ZFlixTeam'>Rejoindre le groupe</a>
<a href='t.me/ZFlixTeam'>Rejoindre le groupe</a>
<a href='t.me/ZFlixTeam'>Rejoindre le groupe</a>


pour tout Problème contactez moi : <a href='t.me/ZFlixTeamBot'>@◡̈⃝ㅤ🇰ιηg¢єу</a></b>"""

    DEV_TXT = """ɪᴄɪ ᴄ'ᴇsᴛ Kɪɴɢᴄᴇʏ 😌. ᴜɴ ᴘᴇᴛɪᴛ ᴅéᴠᴇʟᴏᴘᴘᴇᴜʀs ᴄᴏᴍᴍᴇɴçᴀɴᴛ à ᴀᴘᴘʀᴇɴᴅʀᴇ ʟᴀ ᴘʀᴏɢʀᴀᴍᴍᴀᴛɪᴏɴ ᴇɴ 🐍Pʏᴛʜᴏɴ ᴇᴛ HTML.
    
    ᴊᴜsᴛᴇ ᴘᴏᴜʀ ᴅɪʀᴇ ǫᴜᴇ, sɪ ᴠᴏᴜs ᴠᴏᴜʟɪᴇᴢ ʟᴇ ᴄᴏᴅᴇ sᴏᴜʀᴄᴇ ᴅᴜ ʙᴏᴛ, ɪʟ ᴠᴀ ғᴀʟʟᴏɪʀ ᴘᴀʏé. ʟᴇ ᴄᴏᴅᴇ sᴏᴜʀᴄᴇ ᴇsᴛ ᴘᴀʏᴀɴᴛ."""

    THUMB_TXT = """🌌 <b><u>Comment configurer la miniature</u></b>
  
<b>•></b> /start Démarrer le bot et envoyer une photo pour définir automatiquement la miniature.
<b>•></b> /del_thumb Utiliser cette commande pour supprimer votre ancienne miniature.
<b>•></b> /view_thumb Utiliser cette commande pour voir votre miniature actuelle."""

    SEND_METADATA = """
❪ CONFIGURER LES MÉTADONNÉES PERSONNALISÉES ❫

☞ Par Exemple :-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Propulsé par :- @BotZFlix" -metadata author="@BotZFlix" -metadata:s:s title="Sous-titré par :- @BotZFlix" -metadata:s:a title="Par :- @BotZFlix" -metadata:s:v title="Par :- @BotZFlix" </code>

📥 Pour aide contactez <a href='t.me/ZFlixTeam>@ZFlix-Team</a>
"""

    PROGRESS_BAR = """<b>\n
╔━━━━❰ Gᴏᴍᴜ Gᴏᴍᴜ Nᴏ🔥 ❱━╗ 
 ➜ 🗃️ Tᴀɪʟʟᴇ : {1} | {2}
 ➜ ⏳ Tᴇʀᴍɪɴé : {0}%
 ➜ 🚀 Vɪᴛᴇssᴇ : {3}/s
 ➜ ⏰ Rᴇsᴛᴀɴᴛ : {4}
╚━━━━━━━━━━━━━━━╝
<blockquote><a href='t.me/ZFlixTeam'>𒄆  ZFʟɪx-Tᴇᴀᴍ</a></blockquote></b>"""