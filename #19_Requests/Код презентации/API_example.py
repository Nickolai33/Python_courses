import requests
from bs4 import BeautifulSoup

# resp = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
# soup = BeautifulSoup(resp.content, "xml")
# print(soup)

# print(soup.find('CharCode', text='EUR').find_next_sibling('Value').string)

# print(soup.find(ID="R01239").Value.string)


# resp = requests.get(
#     "http://api.openweathermap.org/data/2.5/weather",
#     params={
#         "q": "Moscow",
#         "APPID": "a4ca581bf1870a4c2e39d02980695d94",
#         'mode': 'xml', 'units': 'metric'
# } )
#
# soup = BeautifulSoup(resp.content, "xml")
# print(soup.temperature['value'])

# import requests
# resp = requests.get(
#     "http://api.openweathermap.org/data/2.5/weather",
#     params={
#         "q": "Moscow",
#         "APPID": "a4ca581bf1870a4c2e39d02980695d94",
#         'mode': 'json', 'units': 'metric'
# } )
# data = resp.json()
# print(data)
# print(data['main']['temp'])

# import requests
#
# resp = requests.get(
#     'https://api.vk.com/method/users.get',
#     params={'user_id': '1'}
# )
# print(resp.json())


import vk

session = vk.AuthSession(
    app_id=7967218,
)
api = vk.API(session)
print(api.users.get(user_ids=3, v=5.131))
