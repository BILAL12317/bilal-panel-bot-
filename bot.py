import os

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🛒 Products"],
        ["💳 Payment", "📞 Contact"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "👋 Welcome!\n\nSelect an option:",
        reply_markup=reply_markup
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
📞 CONTACT

👤 Telegram: @BILALPANEL3

💬 Need help? Contact me on Telegram.

⏰ Support: 24/7
"""
    await update.message.reply_text(text)
async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔹 BR MOD PC VERSION", callback_data="brmod")],
        [InlineKeyboardButton("🔹 DRIP CLIENT PROXY NON ROOT", callback_data="dripproxy")],
        [InlineKeyboardButton("🔹 PATO TEAM", callback_data="pato")],
        [InlineKeyboardButton("🔹 BR MODS ROOT + NON ROOT", callback_data="brmods")],
        [InlineKeyboardButton("🔹 REAPER X PRO", callback_data="reaper")],
        [InlineKeyboardButton("🔹 PRIME HOOK NON ROOT", callback_data="prime")],
        [InlineKeyboardButton("🔹 HEX BLADE CHEATS", callback_data="hex")],
        [InlineKeyboardButton("🔹 HG CHEAT", callback_data="hg")],
        [InlineKeyboardButton("🔹 HG CHEAT PROXY", callback_data="hgproxy")],
        [InlineKeyboardButton("🔹 FLUORITE IOS FF", callback_data="ios")],
        [InlineKeyboardButton("🔹 DRIP CLIENT PC AIM KILL", callback_data="aim")],
        [InlineKeyboardButton("🔹 DRIP CLIENT NON ROOT", callback_data="nonroot")],
    ]

    await update.message.reply_text(
        "🛒 Choose a Product:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "brmod":
        await query.edit_message_text("BR MOD PC VERSION")

    elif query.data == "dripproxy":
        await query.edit_message_text("DRIP CLIENT PROXY NON ROOT")

    elif query.data == "pato":
        await query.edit_message_text("PATO TEAM")
async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💳 Payment details - Contact me")

async def receive_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        "✅ Payment screenshot received.\nOur admin will verify it soon."
    )

    await context.bot.forward_message(
        chat_id=5053534694,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id,
    )

    await context.bot.send_message(
        chat_id=5053534694,
        text=(
            f"📥 New Payment Screenshot\n\n"
            f"👤 Name: {user.full_name}\n"
            f"🆔 User ID: {user.id}\n"
            f"📛 Username: @{user.username if user.username else 'None'}"
        ),
    )
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("products", products))
    app.add_handler(CommandHandler("payment", payment))
    app.add_handler(CallbackQueryHandler(button))

    app.add_handler(MessageHandler(filters.Regex("^🛒 Products$"), products))
    app.add_handler(MessageHandler(filters.Regex("^💳 Payment$"), payment))
    app.add_handler(MessageHandler(filters.Regex("^📞 Contact$"), contact))
    app.add_handler(MessageHandler(filters.PHOTO, receive_screenshot))

    app.run_polling()


if __name__ == "__main__":
    main()
    