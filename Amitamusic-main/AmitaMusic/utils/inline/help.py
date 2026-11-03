# ─────────────────────────────────────────────────────────────
#  AmitaMusic
#  Source fixed & made public by: Dilchor
#  Copyright (c) 2026 Dilchor | MIT License (see LICENSE file)
# ─────────────────────────────────────────────────────────────
from pyrogram.enums import ButtonStyle
from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AmitaMusic import app

def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=ButtonStyle.DANGER)]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settingsback_helper", style=ButtonStyle.PRIMARY,
        ),
    ]
    mark = second if START else first
    
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_2"], callback_data="help_callback hb2", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_3"], callback_data="help_callback hb3", style=ButtonStyle.PRIMARY),
            ],
            [
                InlineKeyboardButton(text=_["H_B_4"], callback_data="help_callback hb4", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_5"], callback_data="help_callback hb5", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_6"], callback_data="help_callback hb6", style=ButtonStyle.PRIMARY),
            ],
            [
                InlineKeyboardButton(text=_["H_B_7"], callback_data="help_callback hb7", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_8"], callback_data="help_callback hb8", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_9"], callback_data="help_callback hb9", style=ButtonStyle.PRIMARY),
            ],
            [InlineKeyboardButton(text=_["C_B_3"], callback_data="help_callback cbot", style=ButtonStyle.PRIMARY),],
            mark,
        ]
    )
    return upl

def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="settings_back_helper", style=ButtonStyle.PRIMARY,
                ),
            ]
        ]
    )
    return upl

def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help", style=ButtonStyle.SUCCESS,
            ),
        ],
    ]
    return buttons


def first_page(_):
    controll_button = [
        InlineKeyboardButton(text="๏ ᴍᴇɴᴜ ๏", callback_data=f"settingsback_helper", style=ButtonStyle.PRIMARY),
        InlineKeyboardButton(text="๏ ɴᴇxᴛ ๏", callback_data=f"dilXaditi", style=ButtonStyle.PRIMARY),
    ]
    first_page_menu = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_2"], callback_data="help_callback hb2", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_3"], callback_data="help_callback hb3", style=ButtonStyle.PRIMARY),
            ],
            [
                InlineKeyboardButton(text=_["H_B_11"], callback_data="help_callback hb11", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_8"], callback_data="help_callback hb8", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_6"], callback_data="help_callback hb6", style=ButtonStyle.PRIMARY),
            ],
            [
                InlineKeyboardButton(text=_["H_B_13"], callback_data="help_callback hb13", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_12"], callback_data="help_callback hb12", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_9"], callback_data="help_callback cloghelp", style=ButtonStyle.PRIMARY),
            ],
            [
                InlineKeyboardButton(text=_["H_B_10"], callback_data="help_callback hb10", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_14"], callback_data="help_callback hb14", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_15"], callback_data="help_callback hb15", style=ButtonStyle.PRIMARY),
            ],
            [
                InlineKeyboardButton(text=_["C_B_1"], callback_data="help_callback chelp", style=ButtonStyle.PRIMARY),
            ],
            [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=ButtonStyle.DANGER)]
        ]
    )
    return first_page_menu

def second_page(_):
    controll_button = [
        InlineKeyboardButton(text="๏ ʙᴀᴄᴋ ๏", callback_data=f"settings_back_helper", style=ButtonStyle.PRIMARY)
    ]
    second_page_menu = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_7"], callback_data="help_callback hb7", style=ButtonStyle.PRIMARY
                ),
                InlineKeyboardButton(
                    text=_["H_B_19"], callback_data="help_callback hb19", style=ButtonStyle.PRIMARY
                ),
                InlineKeyboardButton(
                    text=_["H_B_14"], callback_data="help_callback hb14", style=ButtonStyle.PRIMARY
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_15"], callback_data="help_callback hb15", style=ButtonStyle.PRIMARY
                ),
                InlineKeyboardButton(
                    text=_["H_B_16"], callback_data="help_callback hb16", style=ButtonStyle.PRIMARY
                ),
                InlineKeyboardButton(
                    text=_["H_B_17"], callback_data="help_callback hb17", style=ButtonStyle.PRIMARY
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_18"], callback_data="help_callback hb18", style=ButtonStyle.PRIMARY
                ),
                InlineKeyboardButton(
                    text=_["H_B_13"], callback_data="help_callback hb13", style=ButtonStyle.PRIMARY
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_20"], callback_data="help_callback hb20", style=ButtonStyle.PRIMARY
                ),
                InlineKeyboardButton(
                    text=_["H_B_22"], callback_data="help_callback hb22", style=ButtonStyle.PRIMARY
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_21"], callback_data="help_callback hb21", style=ButtonStyle.PRIMARY
                )
            ],
            controll_button,
        ]
    )
    return second_page_menu