import HTMLReport
import time
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

sender = '2194095015@qq.com'
receivers = '2194095015@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
mail_pass = "poscbyuqfxqoecij"  # 授权码

file_new = r"D:\Autoapi\oth\VodeZbapi\Run\report\reports.html"
f = open(file_new, 'rb')
mail_body = f.read()
f.close()

# 构造MIMEMultipart对象做为根容器
msgRoot = MIMEMultipart()
text_msg = MIMEText(mail_body, 'html', 'utf-8')
msgRoot.attach(text_msg)
file_msg = MIMEText(mail_body, 'base64', 'utf-8')
file_msg["Content-Type"] = 'application/octet-stream'

# 设置附件头
basename = os.path.basename(file_new)
file_msg["Content-Disposition"] = 'attachment; filename=''' + basename + ''
msgRoot.attach(file_msg)

# 设置根容器属性
msgRoot['Subject'] = Header(sender, 'utf-8')
msgRoot['From'] = sender
msgRoot['To'] = receivers      # 发送多个邮件时逗号（,）隔开 ['接收邮箱']

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com"  ) #['邮箱服务器'])
smtp.login(sender, mail_pass)
smtp.sendmail(msgRoot['From'], msgRoot['To'].split(','), msgRoot.as_string())
smtp.quit()
print('测试报告发送成功！')