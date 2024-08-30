import logging
from telegram.ext import ApplicationBuilder
from config import TOKEN
from bot import start_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(start_handler)

    application.run_polling()