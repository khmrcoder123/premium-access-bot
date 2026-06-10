import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_ID = 7626989173

CHANNEL_LINK = "https://t.me/+S5BAFd-s7a1iM2Q1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=open("aba_qr.jpg", "rb"),
        caption="""
💎 Premium Membership

Price: $3 / Month

1. Scan ABA QR
2. Pay $3
3. Send payment screenshot here

Admin will verify and grant access.
"""
    )

async def receive_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    photo = update.message.photo[-1].file_id

    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo,
        caption=f"""
New payment proof

Name: {user.first_name}
Username: @{user.username}
User ID: {user.id}

Approve manually and send channel link:
{CHANNEL_LINK}
"""
    )

    await update.message.reply_text(
        "✅ Screenshot received.\nPlease wait for admin approval."
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, receive_photo))

app.run_polling()
