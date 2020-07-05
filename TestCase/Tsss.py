
import zipfile
import os
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase #附件
from email.mime.text import MIMEText
from email import encoders #转码
# from datetime import date
#
#
# def getToday():
#     '''获得今天的日期，并把名字改成0901这样的格式'''
#     today = date.today()
#     date_today = today.strftime("%y%m%d")
#     return date_today
#
#
# def zipDir(dirpath, outFullName):
#     '''
#     压缩指定文件夹
#     :param dirpath: 目标文件夹路径
#     :param outFullName:  压缩文件保存路径+XXXX.zip
#     :return: 无
#     '''
#     zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
#     for path, dirnames, filenames in os.walk(dirpath):
#         #去掉目标和路径，只对目标文件夹下边的文件及文件夹进行压缩（包括父文件夹本身）
#         this_path = os.path.abspath('.')
#         fpath = path.replace(this_path, '')
#         for filename in filenames:
#             zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
#     zip.close()
# print(zipDir("D:\Autoapi\VodeZbapi\Run\report\各有所爱接口自动化报告第三版.html","D:\Autoapi"))
#


# ! python 3
# -*- coding:utf-8 -*-
# Autor: Li Rong Yang
'''
Copy指定格式的文件到新文件夹
'''
import os
import shutil
import time
start_time = time.time()
# 需要被复制的文件夹

old_path = r'D:\mywenjian'
new_path = r'F:\mysql'
all_list=os.listdir(old_path)
