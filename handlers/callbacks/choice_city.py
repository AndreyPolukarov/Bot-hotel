from loader import bot
from telebot.types import CallbackQuery
from states.contact_information import UserInfoState
from loguru import logger

@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def destination_id_callback(call: CallbackQuery) -> None:
    """
    Пользователь нажал кнопку города, который ему нужен. Записываем id
    этого города и переходим к следующему шагу. Запрашиваем количество отелей для вывода в чат.
    """
    logger.info('Пользователь выбрал город.')
    if call.data:
        bot.set_state(call.message.chat.id, UserInfoState.destination_id)
        with bot.retrieve_data(call.message.chat.id) as data:
            data['destination_id'] = call.data
        logger.info(f'Выбрал локацию: {call.data}')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.set_state(call.message.chat.id, UserInfoState.numbers_hotels)
        bot.send_message(call.message.chat.id, 'Сколько вывести отелей в чат? Не более 25!')
