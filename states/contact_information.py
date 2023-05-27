from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    command = State()  # команда, которую выбрал пользователь
    city = State()  # город, который ввел пользователь
    destination_id = State()  # запись id города
    numbers_hotels = State()  # количество отелей, нужное пользователю
    price_min = State()  # минимальная стоимость отеля
    price_max = State()  # максимальная стоимость отеля
    photo_count = State()  # количество фотографий
    input_date = State()  # ввод даты (заезда, выезда)
    landmark_in = State()  # начало диапазона расстояния от центра
    landmark_out = State()  # конец диапазона расстояния от центра
    history_select = State()  # выбор истории поиска



