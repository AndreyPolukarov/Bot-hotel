from api import api_function
import random
from loguru import logger
from loader import bot
from telebot.types import Message, Dict, InputMediaPhoto
from database.models import InfoHotels, db, Command


def full_info(message: Message, hotels_info: Dict, photo_count: int, numbers_hotels: int):
	"""
	Получаем все данные с нужной информацией по отелю, сохраняем в bd файл с нужной информацией, происходит поиск по post запросу,
	формируется информация по отелю в которую дальнейшем отправляем пользователю,
	проверяем сколько фотографий нужно пользователю и отправляем пользователю,
	если фотографий 0, то отправляем без фото, так же формируется рандомный список выбор фотографий,
	: param message : Message.
	: param hotels_info : Dict данные, с нужной информацией по отелю.
	: photo_count: int : сколько фото запросил пользователь.
	: numbers_hotels: int : сколько отелей выбрал пользователь.
	"""

	logger.info('переходим full_info')

	count = 0
	for hotel in hotels_info.values():
		if count < int(numbers_hotels):
			count += 1
			payload = {
				"currency": "USD",
				"eapid": 1,
				"locale": "en_US",
				"siteId": 300000001,
				"propertyId": hotel['id']
			}
			response = api_function.api_request('properties/v2/detail', payload, 'POST')
			full_hotels_info = f"Название: {hotel['name']}\n"\
							   f"Адресс: {response['data']['propertyInfo']['summary']['location']['address']['addressLine']}\n"\
							   f"Растояние до центра: {hotel['distance']}\n"\
							   f"Цены: {hotel['price']} $\n"

			if 'error' in full_hotels_info:
				bot.send_message(message.chat.id, full_hotels_info['error'])
				bot.send_message(message.chat.id, 'Попробуйте осуществить поиск с другими параметрами')
				bot.send_message(message.chat.id, '')

			with db:
				InfoHotels.create(command_id=Command.select(Command.id).order_by(Command.id.desc()).get(),
					hotel_name=hotel['name'],
					address=response['data']['propertyInfo']['summary']['location']['address']['addressLine'],
					distance=hotel['distance'],
					prices=hotel['price']
				)


			photo_num = {'images': [url['image']['url'] for url in response['data']['propertyInfo']['propertyGallery']['images']]}
			logger.info(photo_num)
			medias = []
			logger.info('Поиск фото')
			if int(photo_count) > 0:
				for ilem in range(int(photo_count)):
					random_numbers = random.randint(0, 10)
					for number, imag in enumerate(photo_num['images']):
						if random_numbers == number:
							medias.append(InputMediaPhoto(media=imag))
				bot.send_media_group(message.chat.id, medias)
				bot.send_message(message.chat.id, full_hotels_info)
			else:
				bot.send_message(message.chat.id, full_hotels_info)
	bot.send_message(message.chat.id, 'Поиск окончен!\nЕсли хотите выбрать другой отель то выберите команду\n/low\n/high\n/custom')
	bot.set_state(message.chat.id, None)











