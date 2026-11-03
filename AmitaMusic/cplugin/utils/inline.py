# ─────────────────────────────────────────────────────────────
#  AmitaMusic
#  Source fixed & made public by: Dilchor
#  Copyright (c) 2026 Dilchor | MIT License (see LICENSE file)
# ─────────────────────────────────────────────────────────────
from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton(text="II", callback_data="pause_cb", style=ButtonStyle.DANGER),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb", style=ButtonStyle.DANGER),
            InlineKeyboardButton(text="▢", callback_data="end_cb", style=ButtonStyle.DANGER),
        ]
    ]
)

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close", style=ButtonStyle.DANGER)]]
)
