from api import api_function
from telebot.types import Message, Dict
from post_and_get import full_info_hotel
from loguru import logger
from database.models import *
def info_post_list(message: Message, data: Dict) -> Dict:
	logger.info('Переходим в properties/v2/list')
	logger.info(data)

	with db:
		UserCommand.create(command=data['command'],
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


	with db:
		History.create(history_id=UserCommand.select(UserCommand.id).order_by(UserCommand.id.desc()).get(),
						   command=data['command'],
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
			"day": 10,
			"month": 10,
			"year": 2022
		},
		"checkOutDate": {
			"day": 15,
			"month": 10,
			"year": 2022
		},
		"rooms": [
			{
				"adults": 2,
				"children": [{"age": 5}, {"age": 7}]
			}
		],
		"resultsStartingIndex": 0,
		"resultsSize": 200,
		"sort": "PRICE_LOW_TO_HIGH",
		"filters": {"price": {
			"max": data["price_max"],
			"min": data["price_min"]
		}}
	}

	response = api_function.api_request('properties/v2/list', payload, 'POST')

	if data['command'] == '/low' or data['command'] == '/high':
		logger.info('переходим в /low и ищем подходящие отели')
		hotels_info = {}
		for hotel in response['data']['propertySearch']['properties']:
			if float(data['price_min']) <= hotel['price']['lead']['amount'] <= float(data["price_max"]):
				hotels_info[hotel['id']] = {
					'name': hotel['name'], 'id': hotel['id'],
					'distance': hotel['destinationInfo']['distanceFromDestination']['value'],
					"price": hotel['price']['lead']['amount']
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





