#__author: Administrator
#data:2020/6/26
import smtplib     #发送邮件及链接邮件服务器
from email.mime.text import MIMEText #构建邮件格式
class SendEmail:
    global send_user
    global email_host
    global password
    password="13819719342Aa"
    send_user= "2194095015@qq.com"                       #发件人
    email_host = "smtp.qq.com"
    def send_mail(self,user_list,sub,content):
        user = "清风扬"+"<"+send_user+">"               #发件人昵称
        message = MIMEText(content,_subtype="plain",_charset="utf-8")  #y邮件格式
        message["sbuject"]=sub   #主题
        message["from"]  =user
        message["To"]=";".join(user_list)
        server =smtplib.SMTP()
        server.connect(email_host)
        server.login("2194095015@qq.com","dpyftipjftugdjcb")
        server.sendmail(user,user_list,message.as_string())
        server.close()
if __name__=="__main__":
    sen = SendEmail()
    user_list = ["2194095015@qq.com"]
    sub = "这是测试邮件"
    content="好好加油学习提高工资呀"
    sen.send_mail(user_list,sub,content)
