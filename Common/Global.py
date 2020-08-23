#该文件存放全局变量信息
import  requests,json
def server_id():
    '''
    test_ip 测试环境的服务器ip地址
    '''

    test_ip="https://test.api.vodeshop.com"
    return test_ip

from requests import post
host = "https://test.api.vodeshop.com"
login_url = host + "/api/auth/login/mobile-pwd"
gouwu_url = host + "/api/v1/carts"
def login(mobile,password):
    data = {
        "login_type": "mobile-pwd",
        "mobile": mobile,
        "password": password
    }
    response = post(login_url, data)
    # print(response.content.decode('unicode_escape'))
    return response.json()["data"]["access_token"]
def headerss():
    headers = {
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */* ",
        "User-Agent": "vodeApp/2 CFNetwork/1121.2.2 Darwin/19.2.0 ",
        "Accept-Language": "zh-cn",
        "x-request-from": "XMLHttpRequest ",
        "Authorization": f"bearer{login(18370381111, 123456)}"
    }
    return headers


def logins(mobile, password):
    data = {
        "login_type": "mobile-pwd",
        "mobile": mobile,
        "password": password
    }
    session = requests.session()
    response = session.post(login_url, data)
    token = "bearer" + response.json()["data"]["access_token"]
    session.headers['Authorization'] = token
    return session
