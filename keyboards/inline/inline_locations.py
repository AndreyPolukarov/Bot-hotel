from api import api_function
from telebot import types


def city_founding(city):
	response = api_function.api_request('locations/v3/search', {"q": f"{city}", "locale": "en_US", "langid": "1033", "siteid": "300000001"}, 'GET')
	if response:
		cities = list()
		for dest in response['sr']:
			city_name = dest['regionNames']['fullName']
			destination = dest['essId']['sourceId']
			cities.append({city_name: destination})
	return cities

def city_markup(city):
    cities = city_founding(city)
    destinations = types.InlineKeyboardMarkup()
    for city in cities:
        for key, value in city.items():
            destinations.add(types.InlineKeyboardButton(text=key,
                          callback_data=value))
    return destinations