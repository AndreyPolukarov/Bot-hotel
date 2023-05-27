# from api import api_function
#
# def info_user(destination_id):
# 	payload = {
# 		"currency": "USD",
# 		"eapid": 1,
# 		"locale": "en_US",
# 		"siteId": 300000001,
# 		"destination": {"regionId": destination_id},
# 		"checkInDate": {
# 			"day": 10,
# 			"month": 10,
# 			"year": 2022
# 		},
# 		"checkOutDate": {
# 			"day": 15,
# 			"month": 10,
# 			"year": 2022
# 		},
# 		"rooms": [
# 			{
# 				"adults": 2,
# 				"children": [{"age": 5}, {"age": 7}]
# 			}
# 		],
# 		"resultsStartingIndex": 0,
# 		"resultsSize": 200,
# 		"sort": "PRICE_LOW_TO_HIGH",
# 		"filters": {"price": {
# 			"max": 150,
# 			"min": 100
# 		}}
# 	}
# 	response = api_function.api_request('properties/v2/list', payload, 'POST')
# 	if response:
# 		hotels_info = list()
# 		for hotel in response['data']['propertySearch']['properties']:
# 			name = hotel['name']
# 			unit = hotel['destinationInfo']['distanceFromDestination']['value']
# 			price = hotel['price']['lead']['amount']
# 			hotels_info.append({"Название отеля": name,
# 								"айди": id,
# 								"дистанция": unit,
# 								"Цена": price
# 								})
# 		return hotels_info
# 	if not response:
# 		raise LookupError('Запрос пуст...')
# 	elif 'errors' in response.keys():
# 		return {'error': response['errors'][0]['message']}











