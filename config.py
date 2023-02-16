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
    SESSION = os.environ.get("SESSION", "BQBAI9oY5ef_SAj0OF6qJqGgPw_WgjlHryyrMEsjdifVHFQRgodP7eiX2vHtWZIIweulrUyNmUMupKg1R3SXMd_gbNPjeI3GHAMHYmxX41-3tezHJQf_yDhgz430Mcc9fdG-OGM4d0qEYjlsC0G4o4nu4WMrfSnB9s1F3_aEki5Fx04ZsN54K4BdI4xgn3CLMGX0GJZKH9AwQbNzH1unnBqczRACuJP0zP_BgrxL2ycvODK4DIjWVYcyPGxevmPNV4vkZ6yrHV7wiOoY5RFRAWLL82c5QU9RhLst_8Fp2-N7NxafFjFUnSU2YO4UUKPBLza3W2bKOSvvwvj99CidNOovAAAAAWuYknoA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
