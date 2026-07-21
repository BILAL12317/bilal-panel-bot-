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