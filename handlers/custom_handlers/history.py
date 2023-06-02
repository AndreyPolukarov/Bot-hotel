from loader import bot
from database.models import UserCommand, InfoHotels, Command
from telebot.types import Message
from loguru import logger
from states.contact_information import UserInfoState


@bot.message_handler(commands=['history'])
def history(message: Message) -> None:
    """ Выводим пользователю историю запросов, должен ввести нужную команду """

    bot.send_message(message.from_user.id, "История запросов: ")
    query = UserCommand.select(UserCommand).order_by(UserCommand.id.desc()).limit(10)
    if query:
        logger.info("Получаем запись из таблицы")
        for element in query:
            bot.send_message(message.chat.id, f"({element.num_requests}). Дата и время: {element.time}. Вы вводили город: {element.city}")
        bot.set_state(message.from_user.id, UserInfoState.history_select, message.chat.id)
        bot.send_message(message.chat.id, "Выберите номер интересующего вас варианта: ")
    else:
        bot.send_message(message.chat.id, "В базе данных нет записей")


@bot.message_handler(state=UserInfoState.history_select)
def history_hotel_info(message: Message) -> None:
    """ Выводим всю информацию об отеле, которую ранее запрашивал пользователь"""

    logger.info("Получаем историю отелей")
    with bot.retrieve_data(message.chat.id) as data:
        data["history_select"] = message.text
    query = InfoHotels.select().join(Command).where(Command.id == int(data["history_select"]))
    for element in query:
        bot.send_message(message.chat.id, f"Название отеля: {element.hotel_name}" 
                                          f"\nАдрес: {element.address}" 
                                          f"\nЦена: {element.prices}")















