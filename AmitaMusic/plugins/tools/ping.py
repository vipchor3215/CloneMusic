# ─────────────────────────────────────────────────────────────
#  AmitaMusic
#  Source fixed & made public by: Dilchor
#  Copyright (c) 2026 Dilchor | MIT License (see LICENSE file)
# ─────────────────────────────────────────────────────────────
from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message
from config import *
from AmitaMusic import app
from AmitaMusic.core.call import PRO
from AmitaMusic.utils import bot_sys_stats
from AmitaMusic.utils.decorators.language import language
from AmitaMusic.utils.inline import supp_markup
from config import BANNED_USERS
from config import PING_IMG_URL


@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await PRO.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
