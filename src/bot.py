from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Hello, i'm ArmoniBot, let me know what can i do for you!"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


start_handler = CommandHandler("start", start)
