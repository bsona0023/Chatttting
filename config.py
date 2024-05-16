from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", None))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "FRIENDSHIP_CHAT_GROUP0")
UPDATE_CHNL = getenv("UPDATE_CHNL", "LOVE_ME_BABBY")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@virat_0011")

# Random Start Images
IMG = [
    "https://graph.org/file/463c8991912d1676cf62a.jpg",
    "https://graph.org/file/463c8991912d1676cf62a.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
    "CAACAgUAAx0CfLoeOQACKgNmDlwwnocs9yVbS-G5zYz7U9pZKwAC4RAAAkzCcVSCoM-aLK5MsR4E",

]

EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
    "🦋",
    "🥀",
    
]
