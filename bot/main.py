import os
from telegram import Update
from telegram.ext import ApplicationBuilder, filters, MessageHandler, ContextTypes

from rj_converter import convert_link

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        link = convert_link(update.message.text)
        await update.message.reply_audio(link)
        await update.message.reply_text("Enjoy your music!")
    except:
        await update.message.reply_text("Error sending music")


token = os.environ.get("BOT_TOKEN")
if (token == None):
    raise Exception("No token in BOT_TOKEN env")
app = ApplicationBuilder().token(token).build()

app.add_handler(MessageHandler(filters.TEXT, hello))

app.run_polling()
