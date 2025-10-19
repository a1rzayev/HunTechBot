import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from templates import templates

# Load environment variables
load_dotenv()
TOKEN = os.getenv("API_TOKEN")

if not TOKEN:
    raise ValueError("❌ API_TOKEN is missing! Add it to your .env file.")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = templates["start"]["question"]
    buttons = [[b] for b in templates["start"]["buttons"]]
    markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text(question, reply_markup=markup)

# Handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in templates:
        await update.message.reply_text(templates[text])
    else:
        await update.message.reply_text("Bağışlayın, bu suala cavabım yoxdur 🤖")

# Main function
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot işləyir...")
    app.run_polling()

if __name__ == "__main__":
    main()
