
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN:", TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot working!")
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
• 30 Days - ₹690🔹 HG CHEAT ROOT + NON ROOT
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
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
