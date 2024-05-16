from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", None))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "tmm_support_chat")
UPDATE_CHNL = getenv("UPDATE_CHNL", "tmm_heroku_world")
OWNER_USERNAME = getenv("OWNER_USERNAME", "moh_maya_official")

# Random Start Images
IMG = [
    "https://graph.org/file/570e6b36b6962d8f369a2.jpg",
    "https://te.legra.ph/file/5bf629d10afd4af953585.jpg",
    "https://te.legra.ph/file/7a321b99fe99d9d8b5117.jpg",
    "https://te.legra.ph/file/c482a7e55b459ffe07502.jpg",
    "https://telegra.ph//file/0879fbdb307005c1fa8ab.jpg",
    "https://telegra.ph//file/19e3a9d5c0985702497fb.jpg",
    "https://telegra.ph//file/b5fa277081dddbddd0b12.jpg",
    "https://telegra.ph//file/96e96245fe1afb82d0398.jpg",
    "https://telegra.ph//file/fb140807129a3ccb60164.jpg",
    "https://telegra.ph//file/09c9ea0e2660efae6f62a.jpg",
    "https://telegra.ph//file/3b59b15e1914b4fa18b71.jpg",
    "https://telegra.ph//file/efb26cc17eef6fe82d910.jpg",
    "https://telegra.ph//file/ab4925a050e07b00f63c5.jpg",
    "https://telegra.ph//file/d169a77fd52b46e421414.jpg",
    "https://telegra.ph//file/dab9fc41f214f9cded1bb.jpg",
    "https://telegra.ph//file/e05d6e4faff7497c5ae56.jpg",
    "https://telegra.ph//file/1e54f0fff666dd53da66f.jpg",
    "https://telegra.ph//file/18e98c60b253d4d926f5f.jpg",
    "https://telegra.ph//file/b1f7d9702f8ea590b2e0c.jpg",
    "https://telegra.ph//file/7bb62c8a0f399f6ee1f33.jpg",
    "https://telegra.ph//file/dd00c759805082830b6b6.jpg",
    "https://telegra.ph//file/3b996e3241cf93d102adc.jpg",
    "https://telegra.ph/file/ff2ddc282fe7868e3cf73.jpg",
    "https://telegra.ph/file/6130ea9373d5f60898a52.jpg",
    "https://telegra.ph/file/45e5da1eab8f5892981ca.jpg",
    "https://graph.org/file/69468bb8508d4fbe37241.jpg",
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
