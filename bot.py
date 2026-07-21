import os

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "Use /products to view all products."
    )

async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🛒 PRODUCTS

🔹 BR MOD PC VERSION
• 1 Day - ₹100
• 10 Days - ₹350
• 30 Days - ₹650

🔹 DRIP CLIENT PROXY NON ROOT
• 1 Day - ₹90
• 3 Days - ₹120
• 7 Days - ₹230
• 30 Days - ₹549

🔹 PATO TEAM
• 3 Days - ₹300
• 7 Days - ₹450
• 15 Days - ₹600
• 30 Days - ₹800

🔹 BR MODS ROOT + NON ROOT
• 1 Day - ₹90
• 7 Days - ₹230
• 15 Days - ₹399
• 30 Days - ₹499

🔹 REAPER X PRO ROOT + NON ROOT
• 10 Days - ₹300

🔹 PRIME HOOK NON ROOT
• 1 Day - ₹90
• 3 Days - ₹120
• 7 Days - ₹210
• 30 Days - ₹300

🔹 HEX BLADE CHEATS ROOT
• 1 Day - ₹100
• 3 Days - ₹300
• 7 Days - ₹390
• 10 Days - ₹490
• 15 Days - ₹590
• 30 Days - ₹690

🔹 HG CHEAT ROOT + NON ROOT
• 1 Day - ₹100
• 7 Days - ₹300
• 10 Days - ₹400
• 30 Days - ₹500

🔹 HG CHEAT PROXY
• 1 Day - ₹100
• 3 Days - ₹200
• 10 Days - ₹300
• 30 Days - ₹500

🔹 FLUORITE IOS FF
• 1 Day - ₹300
• 7 Days - ₹900
• 30 Days - ₹1600

🔹 DRIP CLIENT PC AIM KILL
• 1 Day - ₹150
• 7 Days - ₹300
• 15 Days - ₹500
• 30 Days - ₹600

🔹 DRIP CLIENT NON ROOT
• 1 Day - ₹90
• 3 Days - ₹150
• 7 Days - ₹230
• 15 Days - ₹350
• 30 Days - ₹550
"""
    await update.message.reply_text(text)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("products", products))

    app.run_polling()

if __name__ == "__main__":
    main()
