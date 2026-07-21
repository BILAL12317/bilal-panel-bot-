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
ADMIN_ID = 5053534694


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🛒 Products"],
        ["💳 Payment", "📞 Contact"],
    ]
    await update.message.reply_text(
        "👋 Welcome!\n\nSelect an option:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 CONTACT\n\n"
        "👤 Telegram: @BILALPANEL3\n\n"
        "💬 Need help? Contact me on Telegram."
    )
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

    products = {
        "brmod": "🔹 BR MOD PC VERSION",
        "dripproxy": "🔹 DRIP CLIENT PROXY NON ROOT",
        "pato": "🔹 PATO TEAM",
        "brmods": "🔹 BR MODS ROOT + NON ROOT",
        "reaper": "🔹 REAPER X PRO",
        "prime": "🔹 PRIME HOOK NON ROOT",
        "hex": "🔹 HEX BLADE CHEATS",
        "hg": "🔹 HG CHEAT",
        "hgproxy": "🔹 HG CHEAT PROXY",
        "ios": "🔹 FLUORITE IOS FF",
        "aim": "🔹 DRIP CLIENT PC AIM KILL",
        "nonroot": "🔹 DRIP CLIENT NON ROOT",
    }

    product = products.get(query.data, "Unknown Product")

    await query.edit_message_text(
        f"🛒 {product}\n\n"
        "💰 Contact admin for price.\n\n"
        "Click Payment from the menu after payment."
    )


async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 PAYMENT\n\n"
        "Send your payment screenshot here after payment."
    )


async def receive_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        "✅ Payment screenshot received.\n"
        "Admin will verify it soon."
    )

    await context.bot.forward_message(
        chat_id=ADMIN_ID,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id,
    )

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            f"📥 New Payment Screenshot\n\n"
            f"👤 Name: {user.full_name}\n"
            f"🆔 User ID: {user.id}\n"
            f"📛 Username: @{user.username if user.username else 'None'}"
        ),
    )