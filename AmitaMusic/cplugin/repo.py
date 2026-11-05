# ─────────────────────────────────────────────────────────────
#  AmitaMusic
#  Source fixed & made public by: Dilchor
#  Copyright (c) 2026 Dilchor | MIT License (see LICENSE file)
# ─────────────────────────────────────────────────────────────
from pyrogram import Client, filters
from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from AmitaMusic.repo_link import REPO_LINK
from config import BANNED_USERS


@Client.on_message(filters.command(["repo", "source"]) & ~BANNED_USERS)
async def repo_clone(client: Client, message: Message):
    await message.reply_text(
        "🔑 <b>sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ</b>\n\nᴛᴀᴘ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴏᴘᴇɴ ᴛʜᴇ ʀᴇᴘᴏ.",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🎐 sᴏᴜʀᴄᴇ", url=REPO_LINK, style=ButtonStyle.SUCCESS)]]
        ),
        disable_web_page_preview=True,
    )
