from api import api_function
from telebot.types import Message, Dict
from post_and_get import full_info_hotel
from loguru import logger

# TODO: пока не придумал как сделать сортировку цен
def info_post_list(message: Message, data: Dict) -> Dict:
	logger.info('Переходим в properties/v2/list')

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
			"max": 150,
			"min": 100
		}}
	}

	response = api_function.api_request('properties/v2/list', payload, 'POST')

	if data['command'] == '/low' or data['command'] == '/high':
		logger.info('переходим в /low и ищем подходящие отели')
		hotels_info = {}
		for hotel in response['data']['propertySearch']['properties']:
			hotels_info[hotel['id']] = {'name': hotel['name'], 'id': hotel['id'],
										'distance': hotel['destinationInfo']['distanceFromDestination']['value'],
										"price": hotel['price']['lead']['amount']
										}

	elif data['command'] == '/custom':
		logger.info('переходит /custom функцию и ищет отели')
		hotels_info = {}
		for hotel in response['data']['propertySearch']["properties"]:
			if float(data['landmark_in']) <= hotel['destinationInfo']['distanceFromDestination'][
				'value'] <= float(
				data['landmark_out']):
				hotels_info[hotel['id']] = {
					'name': hotel['name'], 'id': hotel['id'],
					'distance': hotel['destinationInfo']['distanceFromDestination']['value'],
					'price': hotel['price']['lead']['amount']
				}



	return full_info_hotel.full_info(message, hotels_info, data['photo_count'], data['numbers_hotels'])





