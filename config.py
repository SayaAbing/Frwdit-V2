#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa

import os
import logging

class Config:
#Get this value from https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", "21879629"))
 #Get this value from https://my.telegram.org  
    API_HASH = os.environ.get("API_HASH", "dcb6bfd6d51a8ff5f6aadb01b9fdd11b")
 #Your bot token from @BotFather   
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6135992497:AAHkETqeVK7q7cvkDLL_sWMAXVWrPlVo99U") 
#leave-it
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
#If you want to add a caption to the forwarded file, enter it here
    CAPTION = os.environ.get("CAPTION", "")
#Type Of filters (document , audio , photo , video , animation) else type empty to forward almost everything 
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "empty")
#Enter Your Telegram id
    OWNER_ID = os.environ.get("OWNER_ID", "1105331049")
#Pyrogram string Seccion - https://replit.com/@KindKobra/Pyrogram-String-Gen?v=1 or any updated pyrogram string session 
    SESSION = os.environ.get("SESSION", "BAFN200AByliJ5XijOxLL47FSpctPxIk8EHloEcxYfjgrexr6-SpbfrWqztbd0o6QB_LEocroL6yBxDnIQilaJK32lp7ayQzOe2v0swPdxjTphyW3YNHnGpT5hPi3LTJSRw5ohtfqkq7b1fq1rDgLGMf1j5PlbGCPM5a3Q0Xwc6DMBDPq7YJ0bV9I17w88HyKZOsMCyxpSK1KMgmL7-T1PL7kX9rWuPYKAdKdHUulB_GTaAk6rXK7XsJjQGGlDV68PpMuRfubCSUXGzSCccfGyEcAKimCIPW4Ww5skpLv6mu_y6kRGEaz2hJ49ylw-IIetaLME4dhaCt5ITwzvSoWiJJceclKAAAAAFNQAAoAA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
