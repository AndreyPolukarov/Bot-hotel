from loader import bot
from telebot.types import Message
from states.contact_information import UserInfoState
from keyboards.inline import inline_locations, photo_buttons
from loguru import logger
from post_and_get import proprties_v2_list
from keyboards.calendar.bot_calendar import Calendar


@bot.message_handler(commands=['low', 'high', 'custom'])
def low_high_custom(message: Message) -> None:
    """ Спрашивает у пользователя город в котором будем искать """

    bot.set_state(message.chat.id, UserInfoState.command)
    logger.info('Запоминаем выбранную команду: ' + message.text)
    with bot.retrieve_data(message.chat.id) as data:
        data["command"] = message.text
        data['sort'] = check_command(message.text)
    bot.set_state(message.from_user.id, UserInfoState.city, message.chat.id)
    bot.send_message(message.from_user.id, 'Давай начнем с города,\nВ каком городе ищем?')


@bot.message_handler(state=UserInfoState.city)
def get_city(message: Message) -> None:
    """ Запоминаем город, и выводим кнопки с поиском геопозиции  """

    with bot.retrieve_data(message.chat.id) as data:
        data["city"] = message.text
        logger.info('Пользователь ввел город: ' + message.text)
    bot.send_message(message.from_user.id, 'Выполняю поиск в городе:  {}'.format(data['city']))
    if ''.join(message.text.split()).isalpha():
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
        bot.send_message(message.chat.id,
                         "Отлично, запомнил!\nТеперь напишите максимальную стоимость в $")
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
                photo_buttons.choice_photo_buttons(message)
            else:
                bot.send_message(message.chat.id,
                                 "Максимальная сумма должна быть больше, чем минимальная сумма\nВведите еще раз:")
    else:
        bot.send_message(message.chat.id, 'Ошибка!\nЧисло должно содержать только цифры.\nВведите еще раз:')


@bot.message_handler(state=UserInfoState.photo_count)
def input_photo_quantity(message: Message) -> None:
    """ Ввод количества фотографий и проверка на число и на соответствие заданному диапазону от 1 до 10 """

    if message.text.isdigit():
        if 0 < int(message.text) <= 10:
            logger.info('Ввод и запись количества фотографий: ' + message.text)
            with bot.retrieve_data(message.chat.id) as data:
                data['photo_count'] = message.text
            my_calendar(message, 'заезда')
        else:
            bot.send_message(message.chat.id, 'Число фотографий должно быть в диапазоне от 1 до 10! Повторите ввод!')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(state=UserInfoState.landmark_in)
def input_landmark_in(message: Message) -> None:
    """ Ввод начала диапазона расстояния до центра """

    if message.text.isdigit():
        with bot.retrieve_data(message.chat.id) as data:
            data['landmark_in'] = message.text
        bot.set_state(message.chat.id, UserInfoState.landmark_out)
        bot.send_message(message.chat.id, 'Введите конец диапазона расстояния от центра (в милях).')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(state=UserInfoState.landmark_out)
def input_landmark_out(message: Message) -> None:
    """ Ввод конца диапазона расстояния до центра """

    if message.text.isdigit():
        with bot.retrieve_data(message.chat.id) as data:
            data['landmark_out'] = message.text
            proprties_v2_list.info_post_list(message, data)
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


def check_command(command: str):
    """ Проверка команды и назначение параметра сортировки """

    if command == '/custom':
        return 'DISTANCE'
    elif command == '/low' or command == '/high':
        return 'PRICE_LOW_TO_HIGH'


bot_calendar = Calendar()


def my_calendar(message: Message, word: str) -> None:
    """ Запуск инлайн-клавиатуры (календаря) для выбора дат заезда и выезда """

    bot.send_message(message.chat.id, f'Выберите дату: {word}',
                     reply_markup=bot_calendar.create_calendar(), )












