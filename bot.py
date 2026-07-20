from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8955405180:AAHmDJQZjIuuBcm2UnAeArG-r2XFFXxWF6c"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot working!")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
