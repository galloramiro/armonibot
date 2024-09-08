import logging
from telegram.ext import ApplicationBuilder
from src.config import TOKEN
from src.bot import start_handler, harmonica_by_tone_handler

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(start_handler)
    application.add_handler(harmonica_by_tone_handler)

    application.run_polling()
