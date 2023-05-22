import requests
from dotenv import load_dotenv
import os
load_dotenv()

def api_request(method_endswith, params, method_type):
    url = f"https://hotels4.p.rapidapi.com/{method_endswith}"

    if method_type == 'GET':
        return get_request(
            url=url,
            params=params
        )

    else:
        return requests.post_request(
            url=url,
            params=params
        )

def get_request(url, params):
    try:
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
    except Exception as ex:
        print("ошибка: ", ex)



