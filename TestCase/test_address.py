#__author: Administrator
#data:2020/6/23
import unittest ,requests ,json,time,ddt
from requests import post
from Common.Global import  *
from Common.get_excel  import *
import unittest,os, json
from ddt import ddt,data,unpack
list1=getData(r"E:\apptool\testproject\File\Datalogin_pwd.xlsx","address")
@ddt
class Test_Adress(unittest.TestCase):
    def setUp(self):
        pass

    @data(*tuple(list1))
    @unpack
    def test_adress(self,test_num,test_mingchen,data,res):
        ''''
        该接口为添加收货地址的接口
        '''
        url=server_id()+"/api/v1/users/addresses"
        self.test_num=test_num
        self.test_mingchen =test_mingchen
        self.data = eval(data)
        self.res = res
        headers=headerss()
        response = post(url=url, data=self.data, headers=headers)
        a=response.json()[ 'msg']
        # try:
        self.assertEqual(a, self.res)
        # except  Exception as e:
        def tearDown(self):
            pass
if __name__ == '__main__':
     unittest.main()
