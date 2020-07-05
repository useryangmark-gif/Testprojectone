import unittest

import  unittest
from Run.HTMLReport import *

#加载用例
testsuite=unittest.defaultTestLoader.discover(r"E:\Autoapi\VodeZbapi\TestCase",pattern="test*.py")
#创建一个执行器






runner = HTMLReport.TestRunner(report_file_name='各有所爱接口自动化报告第四版',  # 报告文件名，如果未赋值，将采用“test+时间戳”
                               output_path='report',  # 保存文件夹名，默认“report”
                               title='vode测试报告',  # 报告标题，默认“测试报告”
                               description='第一版报告描述',  # 报告描述，默认“测试描述”
                               thread_count=3,  # 并发线程数量（无序执行测试），默认数量 1
                               thread_start_wait=3,  # 各线程启动延迟，默认 0 s
                               sequential_execution=False,  # 是否按照套件添加(addTests)顺序执行，
                               # 会等待一个addTests执行完成，再执行下一个，默认 False
                               # 如果用例中存在 tearDownClass ，建议设置为True，
                               # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                               # lang='en'
                               lang='cn'  # 支持中文与英文，默认中文
                               )
# 执行测试用例套件
runner.run(testsuite)

