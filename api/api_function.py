import requests
from dotenv import load_dotenv
import os
load_dotenv()


def api_request(method_endswith, params, method_type):
    """
    Получаем данные, проверяет,
    если get, то работает get_request(), если post, то post_request()
    """

    url = f"https://hotels4.p.rapidapi.com/{method_endswith}"

    if method_type == 'GET':
        return get_request(
            url=url,
            params=params
        )

    else:
        return post_request(
            url=url,
            params=params
        )

def get_request(url, params):
    """ Отправка запроса серверу на поиск отелей и достает всю нужную информацию """
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPID_API_KEY", None),
        "X-RapidAPI-Host": os.getenv("HOST_API", None),
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=10
    )

    if response.status_code == requests.codes.ok:
        return response.json()


def post_request(url, params):
    """ Отправка запроса серверу на поиск отелей и достает всю нужную информацию """
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.getenv("RAPID_API_KEY", None),
        "X-RapidAPI-Host": os.getenv("HOST_API", None),
    }

    response = requests.post(
        url,
        json=params,
        headers=headers
    )
    print(response.status_code)

    if response.status_code == requests.codes.ok:
        return response.json()




