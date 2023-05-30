from loader import bot
from database.models import *
from telebot.types import Message

@bot.message_handler(commands=['history'])
def history(message: Message) -> None:
    bot.send_message(message.from_user.id, "История запросов: ")
    for i in History.select():
        bot.send_message(message.from_user.id, i.history_id)





