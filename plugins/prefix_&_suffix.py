from pyrogram import Client, filters, enums
from helper.database import db


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Dᴏɴɴᴇᴢ Lᴇ Pʀéғɪxᴇ__\n\nExᴇᴍᴘʟᴇ:- `/set_prefix @Anime_Terr`**")
    prefix = message.text.split(" ", 1)[1]
    Kingcey = await message.reply_text("Vᴇᴜɪʟʟᴇᴢ ᴘᴀᴛɪᴇɴᴛᴇʀ ...", reply_to_message_id=message.id)
    await db.set_prefix(message.from_user.id, prefix)
    await Kingcey.edit("__**✅ Pʀéғɪxᴇ Eɴʀᴇɢɪsᴛʀé**__")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    Kingcey = await message.reply_text("Vᴇᴜɪʟʟᴇᴢ ᴘᴀᴛɪᴇɴᴛᴇʀ ...", reply_to_message_id=message.id)
    prefix = await db.get_prefix(message.from_user.id)
    if not prefix:
        return await Kingcey.edit("__**😔 Vᴏᴜs N'ᴀᴠᴇᴢ Aᴜᴄᴜɴ Pʀéғɪxᴇ**__")
    await db.set_prefix(message.from_user.id, None)
    await Kingcey.edit("__**❌️ Pʀéғɪxᴇ Sᴜᴘᴘʀɪᴍé**__")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    Kingcey = await message.reply_text("Vᴇᴜɪʟʟᴇᴢ ᴘᴀᴛɪᴇɴᴛᴇʀ ...", reply_to_message_id=message.id)
    prefix = await db.get_prefix(message.from_user.id)
    if prefix:
        await Kingcey.edit(f"**Vᴏᴛʀᴇ Pʀéғɪxᴇ:-**\n\n`{prefix}`")
    else:
        await Kingcey.edit("__**😔 Vᴏᴜs N'ᴀᴠᴇᴢ Aᴜᴄᴜɴ Pʀéғɪxᴇ**__")


# SUFFIXE
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Dᴏɴɴᴇᴢ Lᴇ Sᴜғғɪxᴇ__\n\nExᴇᴍᴘʟᴇ:- `/set_suffix @Anime_Terr`**")
    suffix = message.text.split(" ", 1)[1]
    Kingcey = await message.reply_text("Vᴇᴜɪʟʟᴇᴢ ᴘᴀᴛɪᴇɴᴛᴇʀ ...", reply_to_message_id=message.id)
    await db.set_suffix(message.from_user.id, suffix)
    await Kingcey.edit("__**✅ Sᴜғғɪxᴇ Eɴʀᴇɢɪsᴛʀé**__")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    Kingcey = await message.reply_text("Vᴇᴜɪʟʟᴇᴢ ᴘᴀᴛɪᴇɴᴛᴇʀ ...", reply_to_message_id=message.id)
    suffix = await db.get_suffix(message.from_user.id)
    if not suffix:
        return await Kingcey.edit("__**😔 Vᴏᴜs N'ᴀᴠᴇᴢ Aᴜᴄᴜɴ Sᴜғғɪxᴇ**__")
    await db.set_suffix(message.from_user.id, None)
    await Kingcey.edit("__**❌️ Sᴜғғɪxᴇ Sᴜᴘᴘʀɪᴍé**__")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_csuffix(client, message):

    Kingcey = await message.reply_text("Vᴇᴜɪʟʟᴇᴢ ᴘᴀᴛɪᴇɴᴛᴇʀ ...", reply_to_message_id=message.id)
    suffix = await db.get_suffix(message.from_user.id)
    if suffix:
        await Kingcey.edit(f"**Vᴏᴛʀᴇ Sᴜғғɪxᴇ:-**\n\n`{suffix}`")
    else:
        await Kingcey.edit("__**😔 Vᴏᴜs N'ᴀᴠᴇᴢ Aᴜᴄᴜɴ Sᴜғғɪxᴇ**__")