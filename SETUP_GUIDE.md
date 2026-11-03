# 📖 AmitaMusic — Setup Guide (Bina Coding Ke)

Ye guide un logon ke liye hai jinhe coding nahi aati. Bas neeche diye steps follow karein, koi dikkat nahi aayegi.

---

## Step 1: Zaroori cheezein (jo aapko chahiye)

Deploy karne se pehle ye 5 cheezein tayyar rakhein:

| Naam | Kya hai | Kahan se milega |
|---|---|---|
| `API_ID` aur `API_HASH` | Telegram app ki ek secret chaabi | [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | Aapke bot ka password | Telegram par [@BotFather](https://t.me/BotFather) |
| `MONGO_DB_URI` | Database link (users/settings save karne ke liye) | [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register) (free) |
| `OWNER_ID` | Aapki Telegram numeric ID | Telegram par [@userinfobot](https://t.me/userinfobot) |
| `STRING_SESSION` | Assistant account ka login (music stream karne ke liye) | Neeche Step 5 me bataya hai |

Koi cheez samajh na aaye, koi baat nahi — bas aage padhte jayein, har step me bataya hai.

---

## Step 2: API_ID aur API_HASH lein

1. Browser me [my.telegram.org](https://my.telegram.org) kholein.
2. Apna Telegram number daalein aur login karein (OTP aayega).
3. **API development tools** par click karein.
4. Koi bhi App title aur Short name daal kar **Create application** dabayein.
5. Ab aapko `api_id` (numbers) aur `api_hash` (letters+numbers) dikhega. Dono copy kar lein.

---

## Step 3: Bot Token lein

1. Telegram me [@BotFather](https://t.me/BotFather) ko kholein.
2. `/newbot` type karein.
3. Bot ka ek naam dein (jaise `Amita Music`).
4. Bot ka ek username dein, jo `bot` se khatam hona chahiye (jaise `AmitaMusicBot`).
5. BotFather aapko ek **token** dega, kuch aisa: `123456789:ABCdefGhIJklmNoPQRstuVWXyz`. Isse copy kar lein — ye `BOT_TOKEN` hai.

---

## Step 4: Database (MongoDB) banayein

1. [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register) par free account banayein.
2. **Create a Cluster** par click karein, **Free (M0)** option chunein.
3. Cluster ban jaye to **Database Access** me jaakar ek username/password banayein (yaad rakhein, baad me chahiye hoga).
4. **Network Access** me jaakar **Allow access from anywhere** (`0.0.0.0/0`) add karein.
5. **Connect** button dabayein → **Drivers** chunein → wahan jo link milega (`mongodb+srv://...`), usme apna username/password daal kar copy kar lein. Ye `MONGO_DB_URI` hai.

---

## Step 5: Assistant Account Session banayein

Ye ek "helper" account hai jo asli music stream karta hai (aapka bot sirf control karta hai).

1. [replit.com](https://replit.com) ya apne computer par Python chalayein.
2. Ye command chalayein:
   ```
   pip install pyrofork
   ```
3. Phir ye Python code chalayein (ek naya file bana kar):
   ```python
   from pyrogram import Client
   api_id = input("API_ID: ")
   api_hash = input("API_HASH: ")
   with Client("my_session", api_id=int(api_id), api_hash=api_hash) as app:
       print(app.export_session_string())
   ```
4. Ye aapse phone number, OTP aur (agar 2-step verification on hai to) password maangega.
5. Jo lamba text milega, wahi `STRING_SESSION` hai. Isse kisi ke saath share mat karein — ye aapke Telegram account ka password jaisa hai.

---

## Step 5.5: Spotify Keys (optional, Spotify songs ke liye)

Agar aap chahte hain ki bot Spotify ke links/songs bhi samjhe, to ye free keys le lein (nahi to skip kar sakte hain, bot phir bhi YouTube se chalega):

1. [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard) par jaakar login karein.
2. **Create app** dabayein, koi bhi naam aur description dein.
3. **Redirect URI** me kuch bhi daal dein, jaise `https://localhost`.
4. App ban jaye to **Settings** me `Client ID` aur `Client Secret` dikhega. Dono copy kar lein — ye `SPOTIFY_CLIENT_ID` aur `SPOTIFY_CLIENT_SECRET` hain.

⚠️ Ye bhi code me kabhi mat likhein — sirf Step 6 wale deploy form me daalein.

---

## Step 6: Bot Deploy karein

Sabse aasan tarika **Heroku** hai (free/paid dono):

1. README me diya **"Deploy to Heroku"** button dabayein.
2. Heroku account banayein (agar nahi hai).
3. App ka naam dein.
4. Jo form khulega, usme Step 1-5 wali sari values daal dein:
   - `API_ID`
   - `API_HASH`
   - `BOT_TOKEN`
   - `MONGO_DB_URI`
   - `OWNER_ID`
   - `STRING_SESSION`
5. **Deploy App** dabayein. 2-5 minute lagenge.
6. Deploy hone ke baad apne bot ko Telegram par kholein aur `/start` karein.

---

## Step 7: Apna naam/channel set karein (zaroori)

Public karne se pehle README, `config.py` aur language files me jahan `YourChannel`, `YourSupportChat`, `YourOwner`, `YourUsername` likha hai, usko apne asli Telegram channel/group/username se badal dein. Agar coding nahi aati, to is bot ko dene wale (ya humse) madad maang sakte hain.

---

## ❓ Common Problems

| Problem | Solution |
|---|---|
| Bot start nahi ho raha | `BOT_TOKEN` ya `API_ID`/`API_HASH` galat ho sakta hai, dobara check karein |
| "Database Error" aa raha hai | `MONGO_DB_URI` me password galat hai, ya Network Access me `0.0.0.0/0` add nahi kiya |
| Gana play nahi ho raha | `STRING_SESSION` expire ho gaya hoga, Step 5 dobara karein aur naya session lein |
| Bot deploy hi nahi ho raha | Heroku logs check karein (`heroku logs --tail`), ya humse screenshot ke saath poochein |

---

## 🔒 Dhyan Rakhein

- `BOT_TOKEN`, `STRING_SESSION`, aur `MONGO_DB_URI` kabhi kisi ke saath share na karein, na hi GitHub par public code me paste karein.
- Ye saari values sirf **Heroku ke Environment Variables / Config Vars** me daali jaati hain, code file me nahi.

---

Agar is guide ke baad bhi koi step samajh na aaye, bot ke Support group me pooch sakte hain (README me link hai).
