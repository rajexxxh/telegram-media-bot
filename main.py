from telegram import Update, InputFile
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

media_store = {}

def handle_messages(update: Update, context: CallbackContext):
    message = update.message

    if message.document or message.photo:
        caption = message.caption if message.caption else "NoCaption"
        file_id = ""
        if message.document:
            file_id = message.document.file_id
        elif message.photo:
            file_id = message.photo[-1].file_id
        media_store[caption.lower()] = file_id
        message.reply_text("Media saved with caption: " + caption)

    elif message.text:
        keyword = message.text.strip().lower()
        if keyword in media_store:
            context.bot.send_document(chat_id=message.chat_id, document=media_store[keyword])
        else:
            message.reply_text("Kuch nahi mila bhai is keyword se.")

def main():
    TOKEN = "7868526712:AAGh13i6flGhYTg2hGaNHRMQMizHIDXEyGE"
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.all, handle_messages))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
