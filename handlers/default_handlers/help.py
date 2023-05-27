from telebot.types import Message
from loader import bot


@bot.message_handler(commands=['help'])
def bot_help(message: Message) -> None:
    """ Команды при вызове /help """
    bot.send_message(message.from_user.id, "/low - Самые дешевые отели")
    bot.send_message(message.from_user.id, "/high - Самые дорогие отели")
    bot.send_message(message.from_user.id, "/custom - Лучшие по цене и расположению")
    bot.send_message(message.from_user.id, "/history - Истории поиска")