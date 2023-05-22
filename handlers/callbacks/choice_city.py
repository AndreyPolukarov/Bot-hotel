from loader import bot
from telebot.types import CallbackQuery
from states.contact_information import UserInfoState

# TODO: Хотел вывести callback в определенную папку, не знаю так правильно или нет, но код не работает,
#  если его применять в основном коде то такой код работает

@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def destination_id_callback(call: CallbackQuery) -> None:

    if call.data:
        bot.set_state(call.message.chat.id, UserInfoState.destination_id)
        with bot.retrieve_data(call.message.chat.id) as data:
            data['destination_id'] = call.data
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.set_state(call.message.chat.id, UserInfoState.numbers_hotels)
        bot.send_message(call.message.chat.id, 'Сколько вывести отелей в чат? Не более 25!')
