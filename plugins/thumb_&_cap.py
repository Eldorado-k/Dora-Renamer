from pyrogram import Client, filters
from helper.database import db


@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
        return await message.reply_text("**__Dᴏɴɴᴇᴢ Lᴀ Léɢᴇɴᴅᴇ__\n\nExᴇᴍᴘʟᴇ:- `/set_caption {filename}\n\n💾 Tᴀɪʟʟᴇ: {filesize}\n\n⏰ Dᴜʀéᴇ: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__**✅ Léɢᴇɴᴅᴇ Eɴʀᴇɢɪsᴛʀéᴇ**__", reply_to_message_id=message.id)


@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)
    if not caption:
        return await message.reply_text("__**😔 Vᴏᴜs N'ᴀᴠᴇᴢ Aᴜᴄᴜɴᴇ Léɢᴇɴᴅᴇ**__")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("__**❌️ Léɢᴇɴᴅᴇ Sᴜᴘᴘʀɪᴍéᴇ**__")


@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption']))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)
    if caption:
        await message.reply_text(f"**Vᴏᴛʀᴇ Léɢᴇɴᴅᴇ:-**\n\n`{caption}`")
    else:
        await message.reply_text("__**😔 Vᴏᴜs N'ᴀᴠᴇᴢ Aᴜᴄᴜɴᴇ Léɢᴇɴᴅᴇ**__")


@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
        await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("😔 __**Vᴏᴜs N'ᴀᴠᴇᴢ Aᴜᴄᴜɴᴇ Mɪɴɪᴀᴛᴜʀᴇ**__")


@Client.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("❌️ __**Mɪɴɪᴀᴛᴜʀᴇ Sᴜᴘᴘʀɪᴍéᴇ**__")


@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    SnowDev = await message.reply_text("Vᴇᴜɪʟʟᴇᴢ Pᴀᴛɪᴇɴᴛᴇʀ ...", reply_to_message_id=message.id)
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)
    await SnowDev.edit("✅️ __**Mɪɴɪᴀᴛᴜʀᴇ Eɴʀᴇɢɪsᴛʀéᴇ**__")