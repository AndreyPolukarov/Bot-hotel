from api import api_function
from telebot.types import Message, Dict
from post_and_get import full_info_hotel
from loguru import logger
from database.models import Command, UserCommand, db
import datetime

def info_post_list(message: Message, data: Dict) -> Dict:
	"""
	Получаем все данные и сохраняем в bd файл информацию, которую вводил пользователь,
	происходит поиск по post запросу, создается словарь с нужной информацией по отелю,
	так же проверяем какую команду вводил пользователь.
	: param message : Message.
	: param data : Dict данные, собранные от пользователя.
	: return : Dict данные, с нужной информацией по отелю
	"""

	logger.info('Переходим в properties/v2/list')

	with db:
		Command.create(command=data['command'])

	with db:
		UserCommand.create(num_requests=Command.select(Command.id).order_by(Command.id.desc()).get(),
			time=datetime.datetime.now(),
			city=data['city'],
			hotel_id=data['destination_id'],
			numbers_hotels=data['numbers_hotels'],
			price_min=data['price_min'],
			price_max=data['price_max'],
			photo_need=data['photo_need'],
			photo_count=data['photo_count'],
			distance_min=data['landmark_in'],
			distance_max=data['landmark_out']
			)

	payload = {
		"currency": "USD",
		"eapid": 1,
		"locale": "en_US",
		"siteId": 300000001,
		"destination": {"regionId": data['destination_id']},
		"checkInDate": {
			'day': int(data['checkInDate']['day']),
			'month': int(data['checkInDate']['month']),
			'year': int(data['checkInDate']['year'])
		},
		"checkOutDate": {
			'day': int(data['checkOutDate']['day']),
			'month': int(data['checkOutDate']['month']),
			'year': int(data['checkOutDate']['year'])
		},
		"rooms": [
			{
				"adults": 2,
				"children": [{"age": 5}, {"age": 7}]
			}
		],
		"resultsStartingIndex": 0,
		"resultsSize": 30,
		"sort": data['sort'],
		"filters": {"price": {
			"max": int(data['price_max']),
			"min": int(data['price_min'])
		}}
	}

	response = api_function.api_request('properties/v2/list', payload, 'POST')
	if not response:
		raise LookupError('Запрос пуст...')

	if 'errors' in response.keys():
		return {'error': response['errors'][0]['message']}

	hotels_info = {}
	for hotel in response['data']['propertySearch']['properties']:
		if float(data['price_min']) <= hotel['price']['lead']['amount'] <= float(data["price_max"]):
			hotels_info[hotel['id']] = {
				'name': hotel['name'], 'id': hotel['id'],
				'distance': hotel['destinationInfo']['distanceFromDestination']['value'],
				"price": hotel['price']['lead']['amount']
			}

	if data['command'] == '/high':
		logger.info('Переходит в /high')
		hotels_info = {
			key: value for key, value in
			sorted(hotels_info.items(), key=lambda hotel_id: hotel_id[1]['price'], reverse=True)
		}

	elif data['command'] == '/custom':
		logger.info('переходит /custom функцию и ищет отели')
		hotels_info = {}
		for hotel in response['data']['propertySearch']["properties"]:
			if float(data['landmark_in']) <= hotel['destinationInfo']['distanceFromDestination'][
				'value'] <= float(data['landmark_out']):
				hotels_info[hotel['id']] = {
					'name': hotel['name'], 'id': hotel['id'],
					'distance': hotel['destinationInfo']['distanceFromDestination']['value'],
					'price': hotel['price']['lead']['amount']
				}

	return full_info_hotel.full_info(message, hotels_info, data['photo_count'], data['numbers_hotels'])





