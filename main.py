from bot_pkg import bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token="1136028020:AAFV5w0C5XddIuvFFTLOMKvH4jcVo-KJ7fE", use_context = True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start',bot.start)
caps_handler = CommandHandler('caps', bot.caps)
echo_handler = MessageHandler(Filters.text, bot.echo)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(echo_handler)
updater.start_polling()
