# ─────────────────────────────────────────────────────────────
#  AmitaMusic
#  Source fixed & made public by: Dilchor
#  Copyright (c) 2026 Dilchor | MIT License (see LICENSE file)
# ─────────────────────────────────────────────────────────────
from pyrogram.enums import ButtonStyle
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, Message
import config
from AmitaMusic.repo_link import REPO_LINK
import asyncio
from AmitaMusic import app


# Start panel for inline buttons
def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SO_B_1"], url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.PRIMARY
            )],
        [
           

InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL, style=ButtonStyle.PRIMARY),

InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT, style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text="💻 sᴏᴜʀᴄᴇ", url=REPO_LINK, style=ButtonStyle.SUCCESS),
        ],
    ]
    return buttons



# Private panel for inline buttons
def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL, style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT, style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text="💻 sᴏᴜʀᴄᴇ", url=REPO_LINK, style=ButtonStyle.SUCCESS),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID, style=ButtonStyle.PRIMARY),
InlineKeyboardButton(text="📨ʏᴛ-ᴀᴘɪ", callback_data=f"oapi", style=ButtonStyle.PRIMARY),
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper", style=ButtonStyle.PRIMARY)],
    ]
    return buttons


def private_panell(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID, style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT, style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text="💻 sᴏᴜʀᴄᴇ", url=REPO_LINK, style=ButtonStyle.SUCCESS),
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper", style=ButtonStyle.PRIMARY)],
    ]
    return buttons







#-----------------------------+-------------##



import sys
import platform
from time import time
from datetime import datetime
import pyrogram
from pyrogram import filters
from pyrogram.types import CallbackQuery
  

# Pyrogram version
pver = pyrogram.__version__

# Bot start time (uptime ke liye)
BOT_START_TIME = datetime.now()

def get_uptime():
    uptime = datetime.now() - BOT_START_TIME
    hours, remainder = divmod(int(uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"


@app.on_callback_query(filters.regex("oapi"))
async def show_bot_info(c: app, q: CallbackQuery):
    start = time()
    m = await c.send_message(q.message.chat.id, "🧾ᴀᴘɪ sᴛᴀᴛᴜs........")
    delta_ping = (time() - start) * 1000
    await m.delete()

    # Short popup text (under 200 chars)
    short_txt = f"""
🧾ᴀᴘɪ sᴛᴀᴛᴜs

ᴅʙ : ᴏɴʟɪɴᴇ
lunabots ᴀᴘɪ : ʀᴇsᴘᴏɴsɪᴠᴇ
ᴀᴘɪ ᴘɪɴɢ : {delta_ping:.2f} ms
ᴀᴘɪ ᴜᴘᴛɪᴍᴇ : {get_uptime()}

✅ ᴇᴠᴇʀʏᴛʜɪɴɢ ғɪɴᴇ
"""

    await q.answer(short_txt.strip(), show_alert=True)
