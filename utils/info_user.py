# from telebot.types import Message, Dict
# from loguru import logger
# from loader import bot
#
#
# def information_user(message: Message, data: Dict) -> None:
#     logger.info('Вывод суммарной информации о параметрах запроса пользователем.')
#     print_user = (
#         "Вся информация который ввел пользователь\n"
#         # f"команда - {data['command']}",
#         # f"город - {data['city']}",
#         f"отель - {data['destination_id']}",
#         f"Минимальная цены - {data['price_min']}",
#         f"Максимальная цены - {data['price_max']}",
#         f"Кол-во фото - {data['photo_count']}",
#     )
#     return bot.send_message(message.chat.id, print_user)


