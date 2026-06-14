# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

# Login feature, if you want then True , if you don't want then False
LOGIN_SYSTEM = bool(os.environ.get('LOGIN_SYSTEM', True)) # True or False

if LOGIN_SYSTEM == False:
    # if login system is False then fill your tg account session below 
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQFitqsAWeTf7LogHW7ZhnRQHyHz6noSazYH-KKVfI7o4t-3wPEFFYeGKwY6RndkzirjKcg6NY97DNjzHiSKP97GPxRdRdGXFPDs45oYSgDzNivALiWg3yHqkUyj1wu-aZiq9doKP2ENhxFUfIQ9A7GVlOa_cdKvzPzduFWmSwkyhBNMFPSNMwXD1ZjPEeCjX5Sa74pCPr6XwOb-clS_LkkCea-p2wxyVLmavtz_RYb2IRCc0EXtDTaNYWn2ayYOMO9P2xHDdiG1J39wMcyx06ZBk-9AcYTeRMBUW-syZzbmepZlWAlRUepX83btrqWFJi06LP5JAtVCiqaOoDZuKVOzn0Ti6gAAAABWMo9zAA")
else:
    STRING_SESSION = None

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "34346182"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6a4f3d575c6b236ae9a152e95771e7a6")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1446154099"))

# Your Channel Id In Which Bot Upload Downloaded Video/File/Message etc.
# And Make Your Bot Admin In this channel with full rights.
# if you don't want to upload in channel then leave it blank don't fill anything.
CHANNEL_ID = os.environ.get("CHANNEL_ID", "")

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://souravyadav:2230@cluster0.kalstao.mongodb.net/?appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# Increase time as much as possible to avoid floodwait, spamming and tg account ban issues.
WAITING_TIME = int(os.environ.get("WAITING_TIME", "10")) # time in seconds

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
