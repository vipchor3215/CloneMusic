# ─────────────────────────────────────────────────────────────
#  AmitaMusic
#  Source fixed & made public by: Dilchor
#  Copyright (c) 2026 Dilchor | MIT License (see LICENSE file)
# ─────────────────────────────────────────────────────────────
import os
from typing import List

import yaml

import config

languages = {}
languages_present = {}


def get_string(lang: str):
    return languages[lang]


for filename in os.listdir(r"./strings/langs/"):
    if "en" not in languages:
        languages["en"] = yaml.safe_load(
            open(r"./strings/langs/en.yml", encoding="utf8")
        )
        languages_present["en"] = languages["en"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]
    try:
        languages_present[language_name] = languages[language_name]["name"]
    except:
        print("There is some issue with the language file inside bot.")
        exit()


# Show the links set in config (SUPPORT_CHANNEL / SUPPORT_CHAT / OWNER_USERNAME)
# instead of the "@YourChannel" style placeholders written in the language files.
def _wanted():
    w = {
        "@YourChannel": "@" + config.tg_name(config.SUPPORT_CHANNEL),
        "@YourSupportChat": "@" + config.tg_name(config.SUPPORT_CHAT),
    }
    if config.OWNER_USERNAME:
        w["@YourOwner"] = "@" + config.OWNER_USERNAME.lstrip("@")
    return w


_applied = {}


def refresh_links():
    """Replace placeholders (first call) or the previous values (later calls)."""
    global _applied
    wanted = _wanted()
    for key, new in wanted.items():
        old = _applied.get(key, key)
        if old == new:
            continue
        for _lang in languages.values():
            for _k, _v in list(_lang.items()):
                if isinstance(_v, str) and old in _v:
                    _lang[_k] = _v.replace(old, new)
    _applied = wanted


refresh_links()
