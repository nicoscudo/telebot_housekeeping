from bot_pkg import calendar_calls


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello pussy I'm a bot, talk to me!!!")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def calendar(update, context):
    events = calendar_calls.list_events()
    res = ""
    for ev in events:
        tm = ev[0].strftime("%H:%M") + "-" + ev[2].strftime("%H:%M")
        res += tm + ' ' + str(ev[1]) + '\n'
    if len(events) == 0:
        res = "no events found for next 24h"
    context.bot.send_message(chat_id=update.message.chat_id, text=res)
