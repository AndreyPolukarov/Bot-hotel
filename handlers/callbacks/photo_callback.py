from loader import bot
from telebot.types import CallbackQuery
from states.contact_information import UserInfoState
from loguru import logger
from handlers.custom_handlers import survey


@bot.callback_query_handler(func=lambda call: call.data.isalpha())
def photo_callback(call: CallbackQuery) -> None:
    """ Пользователь нажал кнопку "ДА" или "НЕТ" """

    if call.data == 'yes':
        logger.info('Нажата кнопка "ДА"')
        with bot.retrieve_data(call.message.chat.id) as data:
            data['photo_need'] = call.data
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.set_state(call.message.chat.id, UserInfoState.photo_count)
        bot.send_message(call.message.chat.id, 'Сколько вывести фотографий? От 1 до 10!')
    elif call.data == 'no':
        logger.info('Нажата кнопка "НЕТ"')
        with bot.retrieve_data(call.message.chat.id) as data:
            data['photo_need'] = call.data
            data['photo_count'] = '0'
        bot.delete_message(call.message.chat.id, call.message.message_id)
        survey.my_calendar(call.message, 'заезда')


