from loader import bot
from database.models import *
from telebot.types import Message
from loguru import logger
from states.contact_information import UserInfoState

# TODO: хочу вывести информауию по поиску отелей по запросам пользователя,
#  но не могу обратиться к command_id(ползователь ввел 2 отеля, потом ввел 3) и я хочу вывести какая была информация
#  у того или иного запроса(когда обращаюсь к id b другим то информ. выводится, а именно к command_id нет, как это можно исправить?)


@bot.message_handler(commands=['history'])
def history(message: Message) -> None:
    bot.send_message(message.from_user.id, "История запросов: ")
    query = UserCommand.select()
    if query:
        logger.info("Получаем запись из таблицы")
        for i_elem in query:
            bot.send_message(message.chat.id, f"({i_elem.num_requests}).Дата и время: {i_elem.time} .Вы вводили город: {i_elem.city}")
        bot.set_state(message.from_user.id, UserInfoState.history_select, message.chat.id)
        bot.send_message(message.chat.id, "Выберите номер интересующего вас варианта: ")
    else:
        bot.send_message(message.chat.id, "В базе данных нет записей")

@bot.message_handler(state=UserInfoState.history_select)
def history_hotel_info(message: Message) -> None:
    logger.info("Получаем историю отелей")
    with bot.retrieve_data(message.chat.id) as data:
        data["history_select"] = message.text
    logger.info(data["history_select"])
    for i_elem in InfoHotels.select():
        logger.info(i_elem.num_requests)
        if int(data["history_select"]) == i_elem.command_id: # дальше код не идет
            bot.send_message(message.chat.id, f"Название отеля: {i_elem.hotel_name}"
                                              f"\nАдрес: {i_elem.address}"
                                              f"\nЦена: {i_elem.prices}")

        # 2 идея но тоже не работает
        # for i_elem in UserCommand.select():
        # name_hotels = [hotel.hotel_name for hotel in InfoHotels.select().where(InfoHotels.command_id == i_elem.id)]
        # address_hotels = [hotel.address for hotel in InfoHotels.select().where(InfoHotels.command_id == i_elem.id)]
        # price_hotels = [hotel.prices for hotel in InfoHotels.select().where(InfoHotels.command_id == i_elem.id)]
        #
        # bot.send_message(message.chat.id, f"Название отеля: {name_hotels}"
        #                                   f"\nАдрес: {address_hotels}"
        #                                   f"\nЦена: {price_hotels}")













