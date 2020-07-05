import xlrd
import unittest ,requests ,json,time,xlrd
from Common.Global import *
class Test_login(unittest.TestCase):

    def set_up(self):
          pass
    def test_loginby_pwd(self):
        '''
        该接口是通过密码登录的接口
        '''
        excel = xlrd.open_workbook(r"E:\Autoapi\VodeZbapi\File\Datalogin_pwd.xlsx")  # 打开文件地址   最好绝对路径
        table = excel.sheets()[0]
        for i in range(1, table.nrows):
            num = table.row_values(i)[0]
            pwd = table.row_values(i)[1]
            jg = table.row_values(i)[2]
            test_num=table.row_values(i)[3]
            url = server_id()+"/api/auth/login/mobile-pwd"
            data = {
                "mobile": num,
                "password": pwd,
                "open_merchant_id": 1
            }
            result = requests.post(url, data, verify=False)
            results = json.loads(result.text)
            resultT = results['msg']

            # try:
            self.assertEqual(jg,resultT)
            # except Exception as e:
            #     print(test_num+"测试不通过" )

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()


