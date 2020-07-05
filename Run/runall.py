import  unittest,HTMLReport,pytest
#加载用例
testsuite=unittest.defaultTestLoader.discover(r"E:\ApiAuto\Projects\VodeZbapi\TestCase",pattern="test*.py")
#创建一个执行器
runner=unittest.TextTestRunner()


#执行所有用例
runner.run(testsuite)



