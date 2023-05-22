# from typing import Dict
# import requests
#
# def _make_response(method: str, url: str, headers: Dict, params: Dict, timeout: int, success=200):
#     response = requests.request(
#         method,
#         url,
#         headers=headers,
#         params=params,
#         timeout=timeout
#     )
#
#     status_code = response.status_code
#
#     if status_code == success:
#         return response
#
#     return status_code
#
# def get_date(method: str, url: str, headers: Dict, params: Dict, date_day: str, date_month: str,
#              timeout: int, func=_make_response()):
#
#     url = "{}/{}/{}/date".format(url, date_month, date_day)
#
#     respense = func(method, url, handlers=headers, params=params, timeout=timeout)
#
#     return respense