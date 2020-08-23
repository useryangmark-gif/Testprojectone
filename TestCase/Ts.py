import requests ,json,time
import unittest ,requests ,json,time,ddt
from Common.Global import *

logins(18370381111, 123456)

url = "https://test.api.vodeshop.com/api/v1/users"
#

results = session.get(url, verify=False)
print("session的值为=", session.headers)
print(results.json())
