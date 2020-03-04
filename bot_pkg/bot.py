def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello I'm a bot, talk to me!!!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
