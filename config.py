#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa

import os
import logging

class Config:
#Get this value from https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", "1945966"))
 #Get this value from https://my.telegram.org  
    API_HASH = os.environ.get("API_HASH", "6b73197f50512e26f5ebd42e73c3315f")
 #Your bot token from @BotFather   
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5322382737:AAGWqY21L-mw_hPIbUF8sze_HrT9wEdDtGw") 
#leave-it
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
#If you want to add a caption to the forwarded file, enter it here
    CAPTION = os.environ.get("CAPTION", "")
#Type Of filters (document , audio , photo , video , animation) else type empty to forward almost everything 
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "empty")
#Enter Your Telegram id
    OWNER_ID = os.environ.get("OWNER_ID", "1105331049")
#Pyrogram string Seccion - https://replit.com/@KindKobra/Pyrogram-String-Gen?v=1 or any updated pyrogram string session 
    SESSION = os.environ.get("SESSION", "BQAexKqM7vVe5JQ0SWySuFp8Sflw_gjEUD8vZRQSxESkTOIAzVndiiza9CiIEw-jDTKQwLiqlWPG_YQ17mc9wy66kiTnT9P2yA0k1qNIchJWODrLRiCuuFyuYBH01uTVc0ERp0LB_R7YS5-HyvtPKN_5jOkGr7rveq1tJQXrV0aNmee4qxqhTP4zzvDG4aH0F69tQnTSyzf59fBs_xGilWInOMqnPxwl2Y-m2wGeGxzlpzOe-SwkGExU__UBgTnRU_77n4rgCU9q-j2-BCxEvNsTmIDLEFI4IqziPEyrklAMKurgc2OfU2Vugtumg_hCgfOtKABan6kge2qkfo_SpS6ZAAAAAWuYknoA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
