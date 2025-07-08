from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import Config
from helper.database import db

async def not_subscribed(_, client, message):
    await db.add_user(client, message)
    if not Config.FORCE_SUB:
        return False
    try:             
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id) 
        if user.status == enums.ChatMemberStatus.BANNED:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [[InlineKeyboardButton(text="🔻Rᴇᴊᴏɪɴs ʟ'Éǫᴜɪᴘᴀɢᴇ🔺", url=f"https://t.me/{Config.FORCE_SUB}") ]]
    text = "**Hᴇʏ Hᴇʏ Hᴇʏ, 😕\nTᴜ ᴠᴀ ᴏù ᴄᴏᴍᴍᴇ çᴀ ?. Pᴏᴜʀ ᴍ'ᴜᴛɪʟɪsé ɪʟ ғᴀᴜᴛ ᴅ'ᴀʙᴏʀᴅ ғᴀɪʀᴇ ᴘᴀʀᴛɪᴇ ᴅᴇ ᴍᴏɴ Éǫᴜɪᴘᴀɢᴇ ᴇᴛ ᴄᴇʟʟᴇ ᴅᴜ Mᴀîᴛʀᴇ.\n\nRᴇᴊᴏɪɴs ʟᴇ ᴠᴏᴛᴇ ᴇᴛ ᴄʟɪǫᴜᴇ sᴜʀ /start à ɴᴏᴜᴠᴇᴀᴜ**"
    try:
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="Désolé mais tu as été banni")  
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          



