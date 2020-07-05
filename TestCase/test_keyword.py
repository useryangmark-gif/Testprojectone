#__author: Administrator
#data:2020/6/21

import unittest ,requests ,json,time,ddt

from requests import post
from  Common.Global  import *
from Common.get_excel import  *
import unittest,os, json
from ddt import ddt,data,unpack
list1=getData(r"E:\Autoapi\VodeZbapi\File\Datalogin_pwd.xlsx","keywords")
@ddt

class Test_users(unittest.TestCase):

    def set_up(self):
        pass

    @data(*tuple(list1))
    @unpack
    def test_keywordgoods(self,test_num,params,goods_id):
        '''
        接口说明：该接口是通过搜索平台设置的关键字返回绑定的关键字商品
        '''
        self.params=eval(params)
        self.goods_id=goods_id
        self.test_num=test_num

        url = "https://test.api.vodeshop.com/api/v1/os/keyword-goods"
        headers = headerss()
        result = requests.get(url=url, params=self.params, headers=headers, verify=False)

        self.assertEqual(self.goods_id,result.json()['data'][0]['id'],self.test_num+"测试不通过")


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()