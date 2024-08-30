import logging
import os
from logging import config

# ENVIRONMENT VARIABLES
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
BOT_LINK = f"https://t.me/{USERNAME}"

# LOGGER CONFIG
config.fileConfig("/app/logging.conf")
LOGGER = logging.getLogger("armoni-bot")
