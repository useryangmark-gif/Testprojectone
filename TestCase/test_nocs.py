#此模块文件存放不需要传参的接口
import unittest ,requests ,json,time,ddt

from requests import post
from  Common.Global  import *
from Common.get_excel import  *
import unittest,os, json
from ddt import ddt,data,unpack

class Test_users(unittest.TestCase):

    def set_up(self):
        pass


    def test_users(self):

        url = "https://test.api.vodeshop.com/api/v1/users"
        headers = headerss()
        result = requests.get(url=url, headers=headers, verify=False)
        self.assertEqual(result.status_code,200,"响应码断言失败")

    @unittest.skip("test_test_hotsearch")
    def test_hotsearch(self):
        url = "https://test.api.vodeshop.com/api/v1/goods/hot-search"
        headers = headerss()
        result = requests.get(url=url, headers=headers, verify=False)
        self.assertEqual(result.status_code, 200, "响应码断言失败")
    def test_good_show(self):
        '''
        测试接口：商品详情
        '''
        url = server_id()+"/api/v1/goods/show"
        headers = headerss()
        params={
            "goods_id":10012
        }
        result = requests.get(url=url, headers=headers,params=params ,verify=False)
        self.assertEqual(result.status_code, 200, "响应码断言失败")
    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()