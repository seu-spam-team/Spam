import poplib
import time
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

class Mail:
    def __init__(self,sen,ip,sub,tex):
        self.send=sen
        self.senderIP=ip
        self.subject=sub
        self.text=tex
        self.ifnormal=None
        self.pre_test=None

    def out(self):
        print(self.send+"..."+self.senderIP+'....'+self.subject+"..."+self.text)

    def get_text(self):
        return self.text
    def get_sender(self):
        return self.send
    def get_sub(self):
        return self.subject
    def get_label(self):
        return self.ifnormal
    def get_pretest(self):
        return self.pre_test
    def set_normal(self,label):
        self.ifnormal=label
    def set_pretest(self,pre):
        self.pre_test=pre

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


class MailUser:
    def __init__(self,usr,pwd):

        if '@163.com' in usr:
           self.pop3_server = 'pop.163.com'
        elif '@qq.com' in usr:
            self.pop3_server = 'pop.qq.com'
        # 连接到POP3服务器:
        self.server = None
        self.user=usr
        self.password=pwd
        self.maillist=[]


    def login(self,usr,pwd):

        try:
          self.server = poplib.POP3(self.pop3_server)
        except Exception as e:
            print(e)
            return"not connected"

         # 可以打开或关闭调试信息:
        self.server.set_debuglevel(0)
        # 可选:打印POP3服务器的欢迎文字:
         # print(self.server.getwelcome().decode('utf-8'))


        # 身份认证:
        self.server.user(usr)

        try:
            self.server.pass_(pwd)
        except Exception as e:
            print(e)
            return 'login fail'
        return 'login success'

    def getmsg(self):
        # stat()返回邮件数量和占用空间:
        print('Messages: %s. Size: %s' % self.server.stat())
        # list()返回所有邮件的编号:
        resp, mails, octets = self.server.list()
        # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
        print(mails)
        msglist=[]
        # 获取最新一封邮件, 注意索引号从1开始:
        for i in range(1, len(mails) + 1):
            index = i
            resp, lines, octets = self.server.retr(index)
            # lines存储了邮件的原始文本的每一行,
            # 可以获得整个邮件的原始文本:
            msg_content = b'\r\n'.join(lines).decode('utf-8')
            # 稍后解析出邮件:
            msg = Parser().parsestr(msg_content)
            msglist.append(msg)
        return msglist


    def getmails(self):
       msglist=self.getmsg()
       for i in range(0,len(msglist)):
           mail=self.parsemsg(msglist[i])
           self.maillist.append(mail)

    def mail_info(self):
        for i in self.maillist:
            i.out()

        # 获取邮件内容
    def get_content(self, msg):
            content = ''
            content_type = msg.get_content_type()
            # print('content_type:',content_type)
            if content_type == 'text/plain':  # or content_type == 'text/html'
                content = msg.get_payload(decode=True)
                charset = guess_charset(msg)
                if charset:
                    content = content.decode(charset)
            return content


    def parsemsg(self, msg):
            pre=''
            for header in ['From', 'X-Originating-IP','Date', 'Subject','Received','To','X-Mailer','Message-ID']:
                value = msg.get(header, '')
                if value:
                    if header == 'Subject':
                        value = decode_str(value)
                        sub = value
                    elif header == 'From':
                        hdr, addr = parseaddr(value)
                        name = decode_str(hdr)
                        value = u'%s <%s>' % (name, addr)
                        sender = value
                    elif header == 'To':
                        hdr, addr = parseaddr(value)
                        name = decode_str(hdr)
                        value = u'%s <%s>' % (name, addr)
                        to = value
                    elif header=='X-Originating-IP':
                        value = decode_str(value)
                        ip = value
                    elif header=='Received':
                        value = decode_str(value)
                        Rec = value
                    elif header=='X-Mailer':
                        value = decode_str(value)
                        X_m= value
                    elif header=='Message-ID':
                        value = decode_str(value)
                        mes_id = value
                    elif header=='Date':
                        value = decode_str(value)
                        date = value
            pre='Received: '+Rec+' From: '+sender+' Date: '+date+' To: '+to+' X-Mailer: '+X_m+' Message-ID: '+mes_id
            #print(pre)

            if msg is None:
                return None
            for part in msg.walk():
                if not part.is_multipart():
                    text = self.get_content(part)
                    #print("emailcontent:" + text)
                    break
            mail = Mail(sender, ip,sub, text)
            #mail.out()
            return mail



    def checknew(self,signal):
        resp, mails, octets = self.server.list()
        currentnumber = len(mails)
        while True:
            time.sleep(10)
            self.server.quit()
            self.server = poplib.POP3(self.pop3_server)
            self.server.set_debuglevel(0)
            self.server.user(self.user)
            self.server.pass_(self.password)
            self.server.stat()
            resp, mails, octets = self.server.list()
            newnum = len(mails)
            if (currentnumber != newnum):
                index = newnum
                resp, lines, octets = self.server.retr(index)
                # lines存储了邮件的原始文本的每一行,
                # 可以获得整个邮件的原始文本:
                msg_content = b'\r\n'.join(lines).decode('utf-8')
                # 稍后解析出邮件:
                msg = Parser().parsestr(msg_content)
                # 可以根据邮件索引号直接从服务器删除邮件:
                # server.dele(index)
                mail=self.parsemsg(msg)
                self.maillist.append(mail)
                signal.run()
            currentnumber = newnum

    #得到邮件数量
    def getmailnum(self):
         return len(self.maillist)


    #得到第几封邮件的内容
    def mailtext(self,num):
        t=num
        str=self.maillist[t].get_sub()+"    "+self.maillist[t].get_text()
        return str

    def getmailhead(self):
        list=[]
        for mail in self.maillist:
            send=mail.get_sender()
            sub=mail.get_sub()
            str='sender: '+send+'subject: '+sub
            list.append(str)
        return list


    def get_badmail(self):
        list = []
        for mail in self.maillist:
            if not mail.get_label():
              send = mail.get_sender()
              sub = mail.get_sub()
              text = mail.get_text()
              str = 'sender: ' + send + 'subject: ' + sub + '\n' + 'text: '+text
              list.append(str)
        return list



    def get_normalmail(self):
        list = []
        for mail in self.maillist:
            if mail.get_label():
              send = mail.get_sender()
              sub = mail.get_sub()
              text=mail.get_text()
              str = 'sender: ' + send + 'subject: ' + sub+'\n'+ 'text:'+text
              list.append(str)
        return list


    def setlabel(self,num,label):
         self.maillist[num].set_normal(label)




    def quit(self):
        self.server.quit()



if __name__ == "__main__":
    mailusr=MailUser('haonan_0204@163.com','123456789asd')
    str=mailusr.login('haonan_0204@163.com','123456789asd')
    print(str)

    mailusr.getmails()
    #mailusr.mail_info()
    #mailusr.checknew()

    num=mailusr.getmailnum()
    text=mailusr.mailtext(5)
    print(num)
    print(text)


    mailusr.quit()









