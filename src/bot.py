from telegram import Update
from telegram.ext import ConversationHandler, CommandHandler, ContextTypes

from src.harmonica_drawer import HarmonicaDrawer
from src.repository import HarmonicaRepository


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Hello, i'm ArmoniBot, let me know what can i do for you!"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


async def harmonica_by_tone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user for a harmonica tone."""
    harmonica_tone = context.args[0].upper()
    try:
        harmonica = HarmonicaRepository().load_harmonica_by_american_tone(harmonica_tone)
        harmonica = HarmonicaDrawer(harmonica)
        await update.message.reply_text(harmonica.__str__())
    except:
        await update.message.reply_text(f"Sorry but we didn't find the tone {harmonica_tone}.")
    return ConversationHandler.END


async def tone_by_song_tone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user for a song tone."""
    song_tone = context.args[0]
    circle_of_fifths = ["C", "G", "D", "A", "E", "B", "F#", "Db", "Ab", "Eb", "Bb", "F"]
    try:
        tone_index = circle_of_fifths.index(song_tone)
        order_of_fifths = circle_of_fifths[tone_index+1:] + circle_of_fifths[:tone_index+1]
        harmonica_tone = order_of_fifths[-5]
        harmonica = HarmonicaRepository().load_harmonica_by_american_tone(harmonica_tone)
        harmonica = HarmonicaDrawer(harmonica)
        await update.message.reply_text(harmonica.__str__())
    except:
        await update.message.reply_text(f"Sorry but we didn't find the tone for this song tone {song_tone}.")
    return ConversationHandler.END

start_handler = CommandHandler("start", start)
harmonica_by_tone_handler = CommandHandler("harmonica_by_tone", harmonica_by_tone)
tone_by_song_tone_handler = CommandHandler("tone_by_song_tone", tone_by_song_tone)
