from telebot.types import Message
from loguru import logger
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message) -> None:
    logger.info('Выбор команды start - приветствие')
    bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ бот  - {1.first_name}, "
                                      "помогу тебе выбрать отель!\nВыбери подходящие действия для поиска".format(message.from_user, bot.get_me()))
