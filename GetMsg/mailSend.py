# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:32:31 2019

@author: adminster
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SendMail:
    def __init__(self,sender,receivers,subject,lisence,txt):
        self.Sender = sender
        self.Receivers = receivers
        self.Subject = subject
        self.Lisence = lisence
        self.Txt = txt
    def send_mail_txt(self):
        # print("1111111")
        message = MIMEText(self.Txt)   # 邮件内容
        message['From'] = Header(self.Sender)   # 邮件发送者名字
        message['To'] = Header(self.Receivers)   # 邮件接收者名字
        message['Subject'] = Header(self.Subject)   # 邮件主
             
        mail = smtplib.SMTP()
        mail.connect("smtp.qq.com")   # 连接 qq 邮箱
        mail.login(self.Sender, self.Lisence)   # 账号和授权码
        mail.sendmail(self.Sender, [self.Receivers], message.as_string())   # 发送账号、接收账号和邮件信息
        if smtplib.SMTPException:
            return True
        else:
            return False
            
if __name__ == "__main__":           
             mailTest =SendMail('879180233@qq.com','445396420@qq.com','test','idrbvinoknuhbdfj','hello')
             mailTest.send_mail_txt()
