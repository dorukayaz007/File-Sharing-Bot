import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1974633520:AAEKrSoK3tMMMgzH791vS_q9iQHY1vS-Pu8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7882914"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "83283e0c2ae722adb9567a5319259d88")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001596916369"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1371278429"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001301222803"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Merhaba {first}\n\nKanallarımızdan aldığın linklerle sana içerikleri sunabilirim.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1371278429").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Merhaba {first}\n\n<b>Botu kullanabilmek ve içeriklere ulaşabilmek için kanalımızın üyesi olman gerekli\n\nButona tıklayıp kanala katılabilirsin</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1023154009)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
