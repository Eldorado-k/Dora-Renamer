import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from helper.database import db
from config import Config, Txt
import humanize
from time import sleep


@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):

    if message.from_user.id in Config.BANNED_USERS:
        await message.reply_text("Désolé, vous êtes banni.")
        return

    user = message.from_user
    await db.add_user(client, message)
    
    # Liste des stickers et messages intermédiaires
    sequence = [
        {"type": "message", "text": "✨ Sᴀʟᴜᴛ. Jᴇ sᴜɪs Lᴜғғʏ. Lᴇ ᴄʜᴇғ ᴅᴇ ʟ'éǫᴜɪᴘᴀɢᴇ ᴀᴜ ᴄʜᴀᴘᴇᴀᴜ ᴅᴇ ᴘᴀɪʟʟᴇ😁...."},
        {"type": "sticker", "id": "CAACAgQAAxkBAAI5Qmhr8zPYWMTtfvRgZoZh7rJhivIMAAKLDgACWE4wUg3rP9wbFJPmHgQ"},  # ID du 1er sticker
        {"type": "message", "text": " Mᴏɴ ʀêᴠᴇ à ᴍᴏɪ, ᴄ'ᴇsᴛ ᴅᴇ ᴛʀᴏᴜᴠᴇʀ ʟᴇ Oɴᴇ Pɪᴇᴄᴇ ǫᴜᴇʟ ǫᴜ'ᴇɴ sᴏɪᴛ ʟᴇ Pʀɪx💥 ..."},
        {"type": "sticker", "id": "CAACAgQAAxkBAAI5UGhr8-Slyzo23zWEZ1tnjFkpDevvAAKxEQACaFsZUgyBRaS2kd6WHgQ"},  # ID du 2ème sticker
        {"type": "message", "text": " Eᴛ ᴊᴇ ᴅᴇᴠɪᴇɴᴅʀᴀɪ ʟᴇ Rᴏɪ ᴅᴇs Pɪʀᴀᴛᴇs ..."},
        {"type": "sticker", "id": "CAACAgQAAxkBAAI5VGhr9FeRoiJLXb2fojC1I4dVAkGXAAIpEAAC95ooUlcZZo3Owm9CHgQ"}   # ID du 3ème sticker
    ]
    
    # Envoyer et supprimer les éléments un par un
    for item in sequence:
        if item["type"] == "message":
            sent_item = await message.reply_text(item["text"])
        else:
            sent_item = await message.reply_sticker(item["id"])
        
        await asyncio.sleep(2)  # Attendre 2 secondes
        await sent_item.delete()
        await asyncio.sleep(0.3)  # Petit délai entre les éléments
    
    # Ces messages en commentaire, est là pour vous aider à bien comprendre 😜😁. C'est kingcey. j'ai modifié le Renamer bot de codeflix pour donner ceci
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton('Mɪsᴇs à Jᴏᴜʀ', url='https://t.me/BotZFlix'),
        InlineKeyboardButton('Aɪᴅᴇ', url='https://t.me/BTZF_CHAT')
    ], [
        InlineKeyboardButton('À Pʀᴏᴘᴏs', callback_data='about'),
        InlineKeyboardButton('Aɪᴅᴇ', callback_data='help')
    ]])
    
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)

    if not Config.STRING_SESSION:
        if file.file_size > 4000 * 1024 * 1024:
            return await message.reply_text("Désolé, ce bot ne prend pas en charge les fichiers de plus de 4Go")

    try:
        text = f"""**__Qᴜᴇ ᴠᴏᴜʟᴇᴢ-ᴠᴏᴜs ǫᴜᴇ ᴊᴇ ғᴀssᴇ ᴀᴠᴇᴄ ᴄᴇ ғɪᴄʜɪᴇʀ ?__**\n\n**Nᴏᴍ ᴅᴜ ғɪᴄʜɪᴇʀ** :- `{filename}`\n\n**Tᴀɪʟʟᴇ ᴅᴜ ғɪᴄʜɪᴇʀ** :- `{filesize}`"""
        buttons = [[InlineKeyboardButton("📝 Cᴏᴍᴍᴇɴᴄᴇʀ ʟᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ 📝", callback_data="rename")],
                   [InlineKeyboardButton("✖️ Aɴɴᴜʟᴇʀ ✖️", callback_data="close")]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__Qᴜᴇ ᴠᴏᴜʟᴇᴢ-ᴠᴏᴜs ǫᴜᴇ ᴊᴇ ғᴀssᴇ ᴀᴠᴇᴄ ᴄᴇ ғɪᴄʜɪᴇʀ ?__**\n\n**Nᴏᴍ ᴅᴜ ғɪᴄʜɪᴇʀ** :- `{filename}`\n\n**Tᴀɪʟʟᴇ ᴅᴜ ғɪᴄʜɪᴇʀ** :- `{filesize}`"""
        buttons = [[InlineKeyboardButton("📝 Cᴏᴍᴍᴇɴᴄᴇʀ ʟᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ 📝", callback_data="rename")],
                   [InlineKeyboardButton("✖️ Aɴɴᴜʟᴇʀ ✖️", callback_data="close")]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Cᴏɴᴛᴀᴄᴛ Dᴇᴠ", callback_data='dev')
            ],[
                InlineKeyboardButton(
                    'Mɪsᴇs à Jᴏᴜʀ', url='https://t.me/BotZFlix'),
                InlineKeyboardButton(
                    'Sᴜᴘᴘᴏʀᴛ', url='https://t.me/BTZF_CHAT')
            ],[
                InlineKeyboardButton('À Pʀᴏᴘᴏs', callback_data='about'),
                InlineKeyboardButton('Aɪᴅᴇ', callback_data='help')
            ]])
        )
    elif data == "dev":
        await query.message.edit_text(
            text=Txt.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Pᴀʏᴇʀ ʟᴇ Cᴏᴅᴇ Sᴏᴜʀᴄᴇ", url="https://t.me/Kingcey")
                ],[
                InlineKeyboardButton("🎌 Anime Terr", url="https://t.me/Anime_Terr")
                ],[
                InlineKeyboardButton("✘ Fᴇʀᴍᴇʀ", callback_data="close"),
                InlineKeyboardButton("⟪ Rᴇᴛᴏᴜʀ", callback_data="start")
            ]])          
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Légendes", callback_data="leg")
                ],[
                InlineKeyboardButton("Vignettes", callback_data='thumb')
                ],[
                InlineKeyboardButton("✘ Fᴇʀᴍᴇʀ", callback_data="close"),
                InlineKeyboardButton("⟪ Rᴇᴛᴏᴜʀ", callback_data="start")
            ]])
        )
    elif data == "thumb":
        await query.message.edit_text(
            text=Txt.THUMB_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✘ Fᴇʀᴍᴇʀ", callback_data="close"),
                InlineKeyboardButton("⟪ Rᴇᴛᴏᴜʀ", callback_data="help")
            ]])
        )
    elif data == "zft":
        await query.message.edit_text(
            text=Txt.ZFLIX_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ZFʟɪx-Tᴇᴀᴍ", url="t.me/ZFlixTeam"),
                InlineKeyboardButton("⟪ Rᴇᴛᴏᴜʀ", callback_data="about")
            ]])
        )
    elif data == "leg":
        await query.message.edit_text(
            text=Txt.LEG_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✘ Fᴇʀᴍᴇʀ", callback_data="close"),
                InlineKeyboardButton("⟪ Rᴇᴛᴏᴜʀ", callback_data="help")
            ]])
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ZFʟɪx-Tᴇᴀᴍ", callback_data="zft")
                ],[
                InlineKeyboardButton("✘ Fᴇʀᴍᴇʀ", callback_data="close"),
                InlineKeyboardButton("⟪ Rᴇᴛᴏᴜʀ", callback_data="start")
            ]])
        )

    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()
