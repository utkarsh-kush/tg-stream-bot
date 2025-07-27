import os
import nest_asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

nest_asyncio.apply()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Send me a video and I’ll give you a streamable link!")

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        file = await context.bot.get_file(update.message.video.file_id)
        stream_link = file.file_path
        await update.message.reply_text(f"🎬 Stream Link: {stream_link}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VIDEO, handle_video))
    app.run_polling()

if __name__ == "__main__":
    main()