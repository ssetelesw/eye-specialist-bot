import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time

# Replace 'YOUR_TOKEN_HERE' with the token from BotFather
TOKEN = '7678417799:AAHUaC_DGHQagFYbbDYkWinlLrC9qMOhvg4'

# Function to handle the /start command
def start(update, context):
    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Hello {user}! I'm your Eye Care Bot. Use /tips for eye care advice or /remind to set a reminder to rest your eyes."
    )

# Function to provide eye care tips
def tips(update, context):
    tips_message = (
        "Here are some eye care tips:\n"
        "1. Follow the 20-20-20 rule: Every 20 minutes, look at something 20 feet away for 20 seconds.\n"
        "2. Blink often to keep your eyes moist.\n"
        "3. Wear blue-light glasses if you use screens a lot.\n"
        "4. Visit an eye doctor annually."
    )
    update.message.reply_text(tips_message)

# Function to set a simple eye rest reminder
def remind(update, context):
    update.message.reply_text("I'll remind you to rest your eyes in 20 minutes!")
    time.sleep(20 * 60)  # Wait 20 minutes (for testing, you can change to 20 seconds with `20`)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Time to rest your eyes! Look away from the screen.")

# Function to handle unknown commands or messages
def unknown(update, context):
    update.message.reply_text("Sorry, I didn’t understand that. Try /start, /tips, or /remind.")

# Main function to set up the bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("tips", tips))
    dp.add_handler(CommandHandler("remind", remind))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()