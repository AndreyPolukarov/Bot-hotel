from loader import bot
from telebot.types import Message
from states.contact_information import UserInfoState
from keyboards.inline import inline_locations
from loguru import logger

# TODO: Тут не очень понимаю как переключить command == "/custom", что бы если команда введена /custom,
#  то дополнительно должны заданы вопросы про дистанцию до центра (landmark_in, landmark_out)


@bot.message_handler(commands=['low', 'high', 'custom'])
def low_high_custom(message: Message) -> None:
    """ Спрашивает у пользователя город в котором будем искать """

    bot.set_state(message.chat.id, UserInfoState.command)
    logger.info('Запоминаем выбранную команду: ' + message.text)
    with bot.retrieve_data(message.chat.id) as data:
        data["command"] = message.text
    bot.set_state(message.from_user.id, UserInfoState.city, message.chat.id)
    bot.send_message(message.from_user.id, 'Давай начнем с города,\nВ каком городе ищем?')


@bot.message_handler(state=UserInfoState.city)
def get_city(message: Message) -> None:
    """ Запоминаем город, и выводим кнопки с поиском геопозиции  """

    with bot.retrieve_data(message.chat.id) as data:
        data["city"] = message.text
        logger.info('Пользователь ввел город: ' + message.text)
    bot.send_message(message.from_user.id, 'Выполняю поиск в городе:  {}'.format(data['city']))
    if any(i_elem.isalpha() for i_elem in message.text) and any(i_elems.isspace() for i_elems in message.text):
        bot.send_message(message.from_user.id, 'Уточните местоположение:', reply_markup=inline_locations.city_markup(message.text))
    else:
        bot.send_message(message.from_user.id, 'Город может содержать только буквы')

@bot.message_handler(state=UserInfoState.numbers_hotels)
def numbers_hotels(message: Message) -> None:
    """
    Спрашиваем у пользователя количество отель сколько нужно вывести на экран,
    проверяем на число и на диапазон, запоминаем число
    """

    if message.text.isdigit():
        if 0 < int(message.text) <= 25:
            logger.info('Ввод и запись количества отелей: ' + message.text)
            with bot.retrieve_data(message.chat.id) as data:
                data['numbers_hotels'] = message.text
            bot.set_state(message.from_user.id, UserInfoState.price_min, message.chat.id)
            bot.send_message(message.chat.id, "Отлично, запомнил!\nТеперь напишите минимальную стоимость в $")
        else:
            bot.send_message(message.chat.id, 'Ошибка!\nЧисло должно быть не более 25.\nВведите еще раз:')
    else:
        bot.send_message(message.chat.id, 'Ошибка!\nЧисло должно содержать только цифры.\nВведите еще раз:')

@bot.message_handler(state=UserInfoState.price_min)
def price_min(message: Message) -> None:

    """ Ввод минимальной стоимости отеля и проверка чтобы это было число. """

    if message.text.isdigit():
        logger.info('Ввод и запись максимальной стоимости отеля, сравнение с price_min: ' + message.text)
        with bot.retrieve_data(message.chat.id) as data:
            data['price_min'] = message.text
        bot.set_state(message.from_user.id, UserInfoState.price_max, message.chat.id)
        bot.send_message(message.chat.id, "Отлично, запомнил!\nТеперь напишите максимальную стоимость в $")
    else:
        bot.send_message(message.chat.id, "Ошибка!\nЧисло должно содержать только цифры.\nВведите еще раз:")


@bot.message_handler(state=UserInfoState.price_max)
def price_max(message: Message) -> None:

    """
    Ввод максимальной стоимости отеля и проверка чтобы это было число.
    Максимальное число не может быть меньше минимального.
    """

    if message.text.isdigit():
        logger.info('Ввод и запись максимальной стоимости отеля, сравнение с price_max: ' + message.text)
        with bot.retrieve_data(message.chat.id) as data:
            if int(data['price_min']) < int(message.text):
                data['price_max'] = message.text
            else:
                bot.send_message(message.chat.id, "Максимальная сумма должна быть больше, чем минимальная сумма\nВведите еще раз:")
    else:
        bot.send_message(message.chat.id, 'Ошибка!\nЧисло должно содержать только цифры.\nВведите еще раз:')






# if command == "/custom":
# def check_command(command: str) -> str:
#     @bot.message_handler(states=UserInfoState.landmark_in)
#     def info_landmark_in(message: Message) -> None:
#         logger.info('Начальный диапазон' + message.text)
#         bot.send_message(message.chat.id, 'Напишите начало диапазона расстояния от центра')
#         bot.set_state(message.from_user.id, UserInfoState.landmark_out, message.chat.id)
#
#     @bot.message_handler(states=UserInfoState.landmark_out)
#     def info_landmark_out(message: Message) -> None:
#         logger.info('Конечный диапазон' + message.text)
#         bot.send_message(message.chat.id, 'Напишите конец диапазона расстояния от центра')











