from loader import bot
from telebot import types
from telebot.types import Message


def choice_photo_buttons(message: Message) -> None:
    """
    Вызов в чат инлайн-кнопок с вопросом - нужны ли пользователю фотографии?
    : param message : Message
    : return : None
    """
    # logger.info('Вывод кнопок о необходимости фотографий пользователю. ')
    markup_yes_no = types.InlineKeyboardMarkup()
    markup_yes_no.add(types.InlineKeyboardButton(text='ДА', callback_data='yes'))
    markup_yes_no.add(types.InlineKeyboardButton(text='НЕТ', callback_data='no'))
    bot.send_message(message.chat.id, "Нужно вывести фотографии?", reply_markup=markup_yes_no)











