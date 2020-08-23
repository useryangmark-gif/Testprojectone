import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '2194095015@qq.com'
receivers = ['2194095015@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
mail_pass = "ptceczcskgewdibj"  # 授权码

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('这是qq,邮箱的内容     你说有问题么，这是qq,邮箱的内容     你说有问题么这是qq,邮箱的内容     你说有问题么', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')  # 接收的邮件 发送者栏 展示信息
message['To'] = Header("测试", 'utf-8')  # 接收者

subject = '我这个应该是邮件内容把'  #邮件内容
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect('smtp.qq.com', 25)
    smtpObj.login(sender, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
