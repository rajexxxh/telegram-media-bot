from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "7868526712:AAGh13i6flGhYTg2hGaNHRMQMizHIDXEyGE"

def start_bot():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    def echo(update, context):
        update.message.reply_text("Bot chal raha hai, bolo kya chahiye?")

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    print("Bot starting...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    start_bot()
