import pytest,unittest
'''
测试文件以test_开头 （或_test 结尾）
测试类以Test 开头，不能带有init 方法
测试函数以test_ 开头
断言使用assert即可
'''
if __name__=="__main__":
  #d单个文件运行，运行添加，对应的文件的地址，地址要用相对路径
    # pytest.main([r"E:\ApiAuto\Projects\VodeZbapi\TestCase\test_Cart.py"])
  #多个文件 放多个列表 放多个文件
   # pytest.main([r"E:\ApiAuto\Projects\VodeZbapi\TestCase\test_Cart.py",r"E:\ApiAuto\Projects\VodeZbapi\TestCase\test_login.py"])
  #运行整个目录
   # pytest.main(["../TestCase"])
  #生成html报告
  pytest.main(["../TestCase","--html=../report/report.html"])

