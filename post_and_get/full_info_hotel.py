from api import api_function
import random
from loader import bot
from telebot.types import Message, Dict, InputMediaPhoto

# TODO: примерно накидал код по поиску отелей(потом через функию напишу параметры от пользователя), в первый запрос мы должны вытянуть инфу,
#  подставляю destination_id и выдает пустой словарь так же и со вторым запросом выдает ошибку,
#  так же всю инфу которую в дальнейшем получим надо в bd или только историю поиска? или можно сразу пользователюотрпавить
#  .И как потом прислать ползователю фото не могу найти нигде

# Выводим информацию из properties/v2/list

destination_id = '2621' # айди из первого запроса пользователя, какую локацию выбрал он

payload = {
	"currency": "USD",
	"eapid": 1,
	"locale": "en_US",
	"siteId": 300000001,
	"destination": { "regionId": destination_id }, # подставляем для поиска айди из первого запроса
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
			"children": [{ "age": 5 }, { "age": 7 }]
		}
	],
	"resultsStartingIndex": 0,
	"resultsSize": 200,
	"sort": "PRICE_LOW_TO_HIGH",
	"filters": { "price": {
			"max": 150,
			"min": 100
		} }
}
landmark_in = 1  # начало диапазона расстояния от центра
landmark_out = 4  # конец диапазона расстояния от центра
price_min = 50  # минимальная стоимость отеля
price_max = 130  # конец диапазона расстояния от центра

response = api_function.api_request('properties/v2/list', payload, 'POST')
hotels_info = {}
for hotel in response['data']['propertySearch']['properties']:
	if float(landmark_in) < hotel['destinationInfo']['distanceFromDestination']['value'] < float(landmark_out):
		hotels_info[hotel['id']] = {'destination': hotel['destinationInfo']['distanceFromDestination']['value'],
									'name': hotel['name'],
									"price": hotel['price']['lead']['amount']
									}

print(hotels_info)


# Выводим информацию из properties/v2/detail

payload = {
    "currency": "USD",
    "eapid": 1,
    "locale": "en_US",
    "siteId": 300000001,
    "propertyId": destination_id # тут если подставляем то ошибка
}
response = api_function.api_request('properties/v2/detail', payload, 'POST')

photo_num = {
	'images': [url['image']['url'] for url in response['data']['propertyInfo']['propertyGallery']['images']]
}
full_hotels_info = {
	'address': response['data']['propertyInfo']['summary']['location']['address']['addressLine'],
}

photo_count = int(input("Numder: ")) # тоже вводит пользователь
photo_hotel = []
medias = []
if photo_hotel > 0:
	for ilem in range(photo_count):
		random_numbers = random.randint(0, 31)
		for number, imag in enumerate(photo_num['images']):
			if random_numbers == number:
				photo_hotel.append(imag)
	# 	medias.append(InputMediaPhoto(medias=photo_hotel)) -> думаю как-то так выводить фото пользователю
	# bot.send_media_group(message.chat.id, medias)
# else:
# 	bot.send_message(message.chat.id, full_hotels_info) -> вся информация кроме фото

# bot.send_message(message.chat.id, full_hotels_info) -> Либо сначало фото потом вся остальная информация

print(full_hotels_info)












