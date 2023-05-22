from loader import bot
from telebot.types import Message, CallbackQuery
from states.contact_information import UserInfoState
from keyboards.inline import inline_locations

@bot.message_handler(commands=['low', 'high', 'custom'])
def low_high_custom(message: Message) -> None:
    """ Спрашивает у пользователя город в котором будем искать """

    bot.set_state(message.from_user.id, UserInfoState.city, message.chat.id)
    bot.send_message(message.from_user.id, 'Давай начнем с города,\nВ каком городе ищем?')


@bot.message_handler(state=UserInfoState.city)
def get_city(message: Message) -> None:
    """ Запоминаем город, и выводим кнопки с поиском геопозиции  """

    with bot.retrieve_data(message.chat.id) as data:
        data["city"] = message.text
    bot.send_message(message.from_user.id, 'Выполняю поиск в городе:  {}'.format(data['city']))
    if any(i_elem.isalpha() for i_elem in message.text) and any(i_elems.isspace() for i_elems in message.text):
        bot.send_message(message.from_user.id, 'Уточните местоположение:', reply_markup=inline_locations.city_markup(message.text))
    else:
        bot.send_message(message.from_user.id, 'Город может содержать только буквы')


@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def destination_id_callback(call: CallbackQuery) -> None:

    """
    Пользователь нажал кнопку города, который ему нужен. Записываем id
    этого города и переходим к следующему шагу. Запрашиваем количество отелей для вывода в чат.
    """

    if call.data:
        bot.set_state(call.message.chat.id, UserInfoState.destination_id)
        with bot.retrieve_data(call.message.chat.id) as data:
            data['destination_id'] = call.data
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.set_state(call.message.chat.id, UserInfoState.numbers_hotels)
        bot.send_message(call.message.chat.id, 'Сколько вывести отелей в чат? Не более 25!')


@bot.message_handler(state=UserInfoState.numbers_hotels)
def quantity_hotels(message: Message) -> None:
    """
    Спрашиваем у пользователя количество отель сколько нужно вывести на экран,
    проверяем на число и на диапазон, запоминаем число
    """

    if message.text.isdigit():
        if 0 < int(message.text) <= 25:
            with bot.retrieve_data(message.chat.id) as data:
                data['numbers_hotels'] = message.text
            bot.set_state(message.from_user.id, UserInfoState.price_min, message.chat.id)
            bot.send_message(message.chat.id, "Отлично, запомнил!\nТеперь напишите минимальную стоимость в $")
        else:
            bot.send_message(message.chat.id, 'Ошибка!\nЧисло должно быть не более 25.\nВведите еще раз:')
    else:
        bot.send_message(message.chat.id, 'Ошибка!\nЧисло должно содержать только цифры.\nВведите еще раз:')

@bot.message_handler(state=UserInfoState.price_min)
def quantity_hotels(message: Message) -> None:

    """ Ввод минимальной стоимости отеля и проверка чтобы это было число. """

    if message.text.isdigit():
        with bot.retrieve_data(message.chat.id) as data:
            data['price_min'] = message.text
        bot.set_state(message.from_user.id, UserInfoState.price_max, message.chat.id)
        bot.send_message(message.chat.id, "Отлично, запомнил!\nТеперь напишите максимальную стоимость в $")
    else:
        bot.send_message(message.chat.id, "Ошибка!\nЧисло должно содержать только цифры.\nВведите еще раз:")


@bot.message_handler(state=UserInfoState.price_max)
def quantity_hotels(message: Message) -> None:

    """
    Ввод максимальной стоимости отеля и проверка чтобы это было число.
    Максимальное число не может быть меньше минимального.
    """

    if message.text.isdigit():
        with bot.retrieve_data(message.chat.id) as data:
            if int(data['price_min']) < int(message.text):
                data['price_max'] = message.text
                bot.set_state(message.from_user.id, UserInfoState.price_min, message.chat.id)
                bot.send_message(message.chat.id, "Хорошо")
            else:
                bot.send_message(message.chat.id, "Максимальная сумма должна быть больше, чем минимальная сумма\nВведите еще раз:")
    else:
        bot.send_message(message.chat.id, 'Ошибка!\nЧисло должно содержать только цифры.\nВведите еще раз:')


@bot.message_handler(commands=['help'])
def help(message: Message) -> None:
    """ Команды при вызове /help """
    bot.send_message(message.from_user.id, "/low - Самые дешевые отели")
    bot.send_message(message.from_user.id, "/high - Самые дорогие отели")
    bot.send_message(message.from_user.id, "/custom - Лучшие по цене и расположению")
    bot.send_message(message.from_user.id, "/history - Истории поиска")

    #  привет ->
    # bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ бот  - {1.first_name}, "
    #                                   "помогу тебе выбрать подходящий отель!".format(message.from_user, bot.get_me()))








