#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 18826274
API_HASH = "88581e87d99b41033450bbb53a026792"
BOT_TOKEN = "6675948261:AAEvzgVndBO0DhlBWOfgUvJiBImpLHDkoLA"
SESSION = "BQAVUUFUZ5pHVzQs4dsUbbECa41cExOa8JzfXR07aAWOpHZD303wlje-Gp_wsCsgUCV7ct-YCLaUhrn3JjBYU658cu75FQGhUBT15DYoHjEuRFEyBvtReVqS-aSwNzNTqGYcAf4r-nuoZcgrOIRcNOEvkptyBwVF3dtA3BHbcRtDtToAdN0PFjfrV6Dby6ri9RLcW98O7kc08EayEXVE67n58x26uTzo7V7dxPTONWGZy769urcN54vixuEx7S8rAW7jWi-uM8ycpt0aiaCRoc5stXqK8U-uDANum1HHwhr4HA34u3Tf34ydtInSbvwah3KyQDyknsF_zTTWCKcbJPZQAAAAAWhEDsAA"
FORCESUB = "saverbhaba"
AUTH = 6044257984

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
