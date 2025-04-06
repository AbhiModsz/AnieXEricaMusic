import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

KEY = getenv("KEY", "47dcbf3d6a62ebb6b4e8ad88edcb9b03fe6f4432a675eff2af6037c84008969d")
API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
#BOT_TOKEN = getenv("BOT_TOKEN", "7732030577:AAEpqfiwdOnFa7S-uDRAazyEcPWduPy_YHY")
BOT_TOKEN = getenv("BOT_TOKEN", "7546434205:AAG6sBTOai4R5Z5guYqv6bN-5gHIUk90yF4")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://jay:jay@jay.r2lxx.mongodb.net/?retryWrites=true&w=majority&appName=jay")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1001741141734))

OWNER_ID = int(getenv("OWNER_ID", 5265276618))

OWNER = int(getenv("OWNER", 5265276618))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME",None)

HEROKU_API_KEY = getenv("HEROKU_API_KEY",None)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AbhiModsz/AnieXEricaMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Resso_music_group")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Hindi_English_singing_group_chat")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION", "BQFmQ5kAjQLtpmG7rSgbu2o6nz8WECd3Ws6G9KRQIuw5ZGsonlHYKKb0zEMeCUWHW-Haexsu8QkAaM9CawEyhHoSPjLAMiqxzXyQcj1v8LDANlyA_gHtXaRffYO495yfCUO7MPzVAOEigbKApMDVGXHNZ_8mWLZ2-h0P-lhv1ui9Re1S6ToVqHh-hgZL_Urdy1Pc1EhbQ1kY9nZxTd9xkbL4BYEFdvOt5sfFuYY-qXdRg3LGYInJb3dNHEvmCTD9XmpXCTlhOON6G5lg7-9aEJ_LIwzw8VZJX5RFeCsjWprvZj15AuUWX9xo6udEeECMzDx_xb_u9-HEzIdzD3uaHQ-NSqOJ-AAAAAB9d6iMAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://envs.sh/WJm.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://envs.sh/WJm.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://envs.sh/WJm.jpg")
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
