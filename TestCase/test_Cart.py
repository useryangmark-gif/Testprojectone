import unittest ,requests ,json,time,ddt
from requests import post
from Common.Global import  *
from Common.get_excel  import *
import unittest,os, json
from ddt import ddt,data,unpack
list1=getData(r"E:\apptool\testproject\File\Datalogin_pwd.xlsx","ts")
@ddt
class Test_Carts(unittest.TestCase):
    def setUp(self):
        pass

    @data(*tuple(list1))
    @unpack
    def test_guowu(self,Test_bianhao,Test_mingchen,data,jg):
        ''''
        该接口为将商品接入购物车的接口
        '''
        self.data=eval(data)
        self.Test_bianhao=Test_bianhao
        self.jg=jg                    #将文本转化为字典
        # print(f"data={self.data}\njg={self.jg}")
        headers = {
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */* ",
            "User-Agent": "vodeApp/2 CFNetwork/1121.2.2 Darwin/19.2.0 ",
            "Accept-Language": "zh-cn",
            "x-request-from": "XMLHttpRequest ",
            "Authorization": f"bearer{login(18370384170,1234567)}"
        }
        response = post(gouwu_url, data=self.data, headers=headers)
        a=response.json()[ 'msg']
        self.assertEqual(a, self.jg)
        def tearDown(self):
            pass
if __name__ == '__main__':
     unittest.main()
