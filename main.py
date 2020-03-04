import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from bot_pkg import bot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "1136028020:AAFV5w0C5XddIuvFFTLOMKvH4jcVo-KJ7fE"


def run_bot():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', bot.start))
    dispatcher.add_handler(CommandHandler('caps', bot.caps))
    dispatcher.add_handler(MessageHandler(Filters.text, bot.echo))
    dispatcher.add_handler(CommandHandler('calendar', bot.calendar))

    updater.start_polling()
    updater.idle()
    print("telegram bot done")


if __name__ == "__main__":
    run_bot()
