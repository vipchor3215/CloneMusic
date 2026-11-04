# ─────────────────────────────────────────────────────────────
#  AmitaMusic
#  Source fixed & made public by: Dilchor
#  Copyright (c) 2026 Dilchor | MIT License (see LICENSE file)
# ─────────────────────────────────────────────────────────────
FROM nikolaik/python-nodejs:python3.11-nodejs19

RUN rm -f /etc/apt/sources.list.d/yarn.list && \
    sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i '/security.debian.org/d' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg aria2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Other packages (pykeyboard, SafoneAPI...) pull in plain "pyrogram", which overwrites the
# fork. Remove all pyrogram variants and reinstall the fork last so ButtonStyle exists.
RUN pip3 uninstall -y pyrogram kurigram pyrofork pyrotgfork || true
RUN pip3 install --no-cache-dir --no-deps "pyrotgfork>=2.2.24"
RUN python -c "from pyrogram.enums import ButtonStyle; print('ButtonStyle OK')"

CMD bash start
