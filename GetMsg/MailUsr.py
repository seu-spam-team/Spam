import poplib
import time
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

class Mail:
    def __init__(self,sen,sub,tex):
        self.send=sen
        self.subject=sub
        self.text=tex
    def out(self):
        print(self.send+"..."+self.subject+"..."+self.text)

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
        elif '@qq.com' in pwd:
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
        self.server.set_debuglevel(1)
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
            # if indent == 0:
            for header in ['From', 'To', 'Subject']:
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

            if msg is None:
                return None
            for part in msg.walk():
                if not part.is_multipart():
                    text = self.get_content(part)
                    print("emailcontent:\r\n" + text)
                    break;
            mail = Mail(sender, sub, text)
            mail.out()
            return mail



    def checknew(self):
        resp, mails, octets = self.server.list()
        currentnumber = len(mails)
        while True:
            time.sleep(10)
            self.server.quit()
            self.server = poplib.POP3(self.pop3_server)
            self.server.set_debuglevel(1)
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
            currentnumber = newnum
    def quit(self):
        self.server.quit()


def get_mail_content(msg):
    if msg == None:
        return None
    for part in msg.walk():
        if not part.is_multipart():
            data = part.get_payload(decode=True)
            data=data.decode()
            print("emailcontent:\r\n"+data)
            break
    return data



if __name__ == "__main__":
    mailusr=MailUser('haonan_0204@163.com','123456789asd')
    str=mailusr.login('haonan_0204@163.com','123456789')
    print(str)

    mailusr.getmails()
    mailusr.mail_info()
    # mailusr.checknew()
    mailusr.quit()









