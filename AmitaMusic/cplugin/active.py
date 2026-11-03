# ─────────────────────────────────────────────────────────────
#  AmitaMusic
#  Source fixed & made public by: Dilchor
#  Copyright (c) 2026 Dilchor | MIT License (see LICENSE file)
# ─────────────────────────────────────────────────────────────
from pyrogram.enums import ButtonStyle
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from unidecode import unidecode

from AmitaMusic import app
from AmitaMusic.misc import SUDOERS
from AmitaMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@Client.on_message(filters.command(["ac", "activevc", "activevoice"]))
async def start(client: Client, message: Message):
    ac_audio = str(len(await get_active_chats()))
    ac_video = str(len(await get_active_video_chats()))
    await message.reply_text(
        f"✫ <b><u>ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ</u></b> :\n\nᴠᴏɪᴄᴇ : {ac_audio}\nᴠɪᴅᴇᴏ  : {ac_video}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✯ ᴄʟᴏsᴇ ✯", callback_data=f"close", style=ButtonStyle.DANGER)]]
        ),
    )
