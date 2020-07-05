import requests ,json,time
import unittest ,requests ,json,time,ddt

from Common.ts import *
import unittest, requests, json, time, ddt
from requests import post
from Common.Global import *
from Common.get_excel import *
import unittest, os, json
from ddt import ddt, data, unpack
from Common.ts import *

list1 = getData(r"E:\Autoapi\VodeZbapi\File\Datalogin_pwd.xlsx", "address")


@ddt
class Test_Adress(unittest.TestCase):
    def setUp(self):
        pass

    @data(*tuple(list1))
    @unpack
    def test_adress(self, test_num, test_mingchen, data, res):
        ''''
        该接口为添加收货地址的接口
        '''
        url = server_id() + "/api/v1/users/addresses"
        self.test_num = test_num
        self.test_mingchen = test_mingchen
        self.data = eval(data)
        self.res = res
        headers = headerss()

        run = RunMain()
        RES = run.run_main(url, "POST", self.data)
        print(RES)
        # try:
        self.assertEqual(a, self.res)

        # except  Exception as e:
        def tearDown(self):
            pass


if __name__ == '__main__':
    unittest.main()




