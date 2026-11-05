# ─────────────────────────────────────────────────────────────
#  AmitaMusic
#  Source fixed & made public by: Dilchor
#  Copyright (c) 2026 Dilchor | MIT License (see LICENSE file)
# ─────────────────────────────────────────────────────────────
import time
import random
import asyncio
from pyrogram import filters, Client
from pyrogram.enums import ChatType, ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, InputMediaPhoto
from py_yt import VideosSearch
from AmitaMusic import app

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import config
from AmitaMusic.repo_link import REPO_LINK
from AmitaMusic.misc import _boot_
from AmitaMusic.plugins.sudo.sudoers import sudoers_list
from AmitaMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from AmitaMusic.utils import bot_sys_stats
from AmitaMusic.utils.database import (
    add_served_chat_clone,
    add_served_user_clone,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from AmitaMusic.utils.decorators.language import LanguageStart
from AmitaMusic.utils.formatters import get_readable_time
from AmitaMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS, OWNER_ID, STREAMI_PICS
from strings import get_string

from AmitaMusic.utils.database.clonedb import get_owner_id_from_db, get_cloned_support_chat, get_cloned_support_channel

from AmitaMusic.cplugin.setinfo import get_logging_status, get_log_channel


@Client.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    a = await client.get_me()
    bot_id = a.id
    await add_served_user_clone(message.from_user.id, bot_id)

    loading_1 = await message.reply_text("⚡")
    C_BOT_OWNER_ID = get_owner_id_from_db(a.id)
    
    await loading_1.edit_text("<b>ʟᴏᴀᴅɪɴɢ</b>")
    C_BOT_SUPPORT_CHAT = await get_cloned_support_chat(a.id)
    C_SUPPORT_CHAT = f"https://t.me/{C_BOT_SUPPORT_CHAT}"
    await loading_1.edit_text("<b>ʟᴏᴀᴅɪɴɢ.</b>")
    C_BOT_SUPPORT_CHANNEL = await get_cloned_support_channel(a.id)
    C_SUPPORT_CHANNEL = f"https://t.me/{C_BOT_SUPPORT_CHANNEL}"
    await loading_1.edit_text("<b>ʟᴏᴀᴅɪɴɢ..</b>")
    await asyncio.sleep(0.1)
    await loading_1.edit_text("<b>ʟᴏᴀᴅɪɴɢ...</b>")
    await asyncio.sleep(0.1)
    await loading_1.delete()

    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                random.choice(STREAMI_PICS),
                caption=_["help_1"].format(C_SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, a.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link, style=ButtonStyle.DANGER),
                        InlineKeyboardButton(text=_["S_B_9"], url=C_SUPPORT_CHAT, style=ButtonStyle.PRIMARY),
                    ],
                ]
            )
            await m.delete()
            await client.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                has_spoiler=True,
                caption=searched_text,
                reply_markup=key,
            )
    
    else:
        out = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{a.username}?startgroup=true",
                style=ButtonStyle.SUCCESS,
            )
        ],
        [
            InlineKeyboardButton(text=_["C_B_2"], user_id=C_BOT_OWNER_ID, style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text=_["S_B_6"], url=C_SUPPORT_CHANNEL, style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text="📦 sᴏᴜʀᴄᴇ", url=REPO_LINK, style=ButtonStyle.SUCCESS),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper", style=ButtonStyle.PRIMARY),
        ],
    ]
        
        app_name = app.name
        app_link = f"https://t.me/{app.username}"

        await message.reply_photo(
            random.choice(STREAMI_PICS),
            has_spoiler=True, 
            caption=_["c_start_2"].format(message.from_user.mention, a.mention, app_name, app_link, app_name, app_link, C_SUPPORT_CHANNEL, C_SUPPORT_CHAT),
            reply_markup=InlineKeyboardMarkup(out),
        )

        C_LOG_STATUS = get_logging_status(bot_id)
        C_LOGGER_ID = get_log_channel(bot_id)

        if C_LOG_STATUS:
            if str(C_LOGGER_ID) == "-100":
                C_LOGGER_ID = C_BOT_OWNER_ID

            try:
                await client.send_message(
                    chat_id=int(C_LOGGER_ID),
                    text=f"✦ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n"
                        f"✦ <b>ᴜsᴇʀ ɪᴅ ➠</b> <code>{message.from_user.id}</code>\n"
                        f"✦ <b>ᴜsᴇʀɴᴀᴍᴇ ➠</b> @{message.from_user.username}",
                )
            except Exception as e:
                print(f"[ERROR] Failed to send log message: {e}")


@Client.on_callback_query(filters.regex("clone_start_back") & ~BANNED_USERS)
@LanguageStart
async def clone_start_back_callback(client, CallbackQuery: CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    
    a = await client.get_me()
    C_BOT_OWNER_ID = get_owner_id_from_db(a.id)
    C_BOT_SUPPORT_CHAT = await get_cloned_support_chat(a.id)
    C_SUPPORT_CHAT = f"https://t.me/{C_BOT_SUPPORT_CHAT}"
    C_BOT_SUPPORT_CHANNEL = await get_cloned_support_channel(a.id)
    C_SUPPORT_CHANNEL = f"https://t.me/{C_BOT_SUPPORT_CHANNEL}"

    out = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{a.username}?startgroup=true",
                style=ButtonStyle.SUCCESS,
            )
        ],
        [
            InlineKeyboardButton(text=_["C_B_2"], user_id=C_BOT_OWNER_ID, style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text=_["S_B_6"], url=C_SUPPORT_CHANNEL, style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text="💻 sᴏᴜʀᴄᴇ", url=REPO_LINK, style=ButtonStyle.SUCCESS),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper", style=ButtonStyle.DANGER),
        ],
    ]
    
    app_name = app.name
    app_link = f"https://t.me/{app.username}"

    await CallbackQuery.edit_message_media(
        InputMediaPhoto(
            media=random.choice(STREAMI_PICS), 
            caption=_["c_start_2"].format(CallbackQuery.from_user.mention, a.mention, app_name, app_link, app_name, app_link, C_SUPPORT_CHANNEL, C_SUPPORT_CHAT)
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


@Client.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    a = await client.get_me()
    C_BOT_SUPPORT_CHAT = await get_cloned_support_chat(a.id)
    C_SUPPORT_CHAT = f"https://t.me/{C_BOT_SUPPORT_CHAT}"
    C_BOT_SUPPORT_CHANNEL = await get_cloned_support_channel(a.id)
    C_SUPPORT_CHANNEL = f"https://t.me/{C_BOT_SUPPORT_CHANNEL}"
    
    out = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], 
                url=f"https://t.me/{a.username}?startgroup=true",
                style=ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=C_SUPPORT_CHAT, style=ButtonStyle.PRIMARY),
        ],
    ]
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        random.choice(STREAMI_PICS),
        has_spoiler=True, 
        caption=_["start_1"].format(a.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    
    bot_id = a.id
    return await add_served_chat_clone(message.chat.id, bot_id)
