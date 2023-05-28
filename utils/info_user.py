# from telebot.types import Message, Dict
# from loguru import logger
# from loader import bot
#
#
# def information_user(message: Message, data: Dict) -> None:
#     logger.info('Вывод суммарной информации о параметрах запроса пользователем.')
#     print_user = (
#         "Вся информация который ввел пользователь\n"
#         f"команда - {data['command']}",
#         f"город - {data['city']}",
#         f"Выбран город с id - {data['destination_id']}",
#         f'Количество отелей: {data["numbers_hotels"]}\n'
#         f"Минимальная цены - {data['price_min']}",
#         f"Максимальная цены - {data['price_max']}",
#         f"Кол-во фото - {data['photo_count']}",
#     )
#
#     if data['sort'] == 'DISTANCE':
#         bot.send_message(message.chat.id, print_user +
#                      f'Начало диапазона от центра: {data["landmark_in"]}\n'
#                      f'Конец диапазона от центра: {data["landmark_out"]}')
#     else:
#         bot.send_message(message.chat.id, print_user)




