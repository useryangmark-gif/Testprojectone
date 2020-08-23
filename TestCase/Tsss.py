import requests
from requests import post

host = "https://test.api.vodeshop.com"
login_url = host + "/api/auth/login/mobile-pwd"
gouwu_url = host + "/api/v1/carts"
mobile = 18370381111
password = 123456

data = {
    "login_type": "mobile-pwd",
    "mobile": mobile,
    "password": password
}
session = requests.session()
response = session.post(login_url, data)
# print(response.content.decode('unicode_escape'))
token = "bearer" + response.json()["data"]["access_token"]
print(response.json(), "\ntoken的值为=", token)
url = "https://test.api.vodeshop.com/api/v1/users"
#
session.headers['Authorization'] = token
results = session.get(url, verify=False)
print("session的值为=", session.headers)
print(results.json())
#
# headers = {
# #     "Connection": "keep-alive",
# #     "Accept": "application/json, text/plain, */* ",
# #     "User-Agent": "vodeApp/2 CFNetwork/1121.2.2 Darwin/19.2.0 ",
# #     "Accept-Language": "zh-cn",
# #     "x-request-from": "XMLHttpRequest ",
# #     "Authorization": f"bearer{login(18370381111, 123456)}"
# # }

# headers = {
#      "Connection": "keep-alive",
#      "Accept": "application/json, text/plain, */* ",
#      "User-Agent": "vodeApp/2 CFNetwork/1121.2.2 Darwin/19.2.0 ",
#      "Accept-Language": "zh-cn",
#      "x-request-from": "XMLHttpRequest ",
#      "Authorization": token
# }
