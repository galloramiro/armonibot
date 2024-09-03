import logging
import os
from logging import config
from pathlib import Path


# SHARED VARIABLES
SRC_PATH = Path(__file__).parent.resolve()
DATA_FOLDER = f"{SRC_PATH.parent}/data"

# ENVIRONMENT VARIABLES
TOKEN = os.getenv("TOKEN", "")
USERNAME = os.getenv("USERNAME")
BOT_LINK = f"https://t.me/{USERNAME}"

# LOGGER CONFIG
# config.fileConfig(f"{SRC_PATH.parent}/logging.conf")
LOGGER = logging.getLogger("armoni-bot")
