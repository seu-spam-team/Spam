import poplib
import time
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import sys
import chilkat2
class Mail:
    def __init__(self,sen,sub,tex):
        self.send=sen
        self.senderIP=None
        self.subject=sub
        self.text=tex
        self.ifnormal=None
        self.pre_list=[]

    def getmail(self):
        text=self.text[0:10]
        return self.subject+" "+text

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
        self.pre_list=pre
    def get_pretest(self):
        return self.pre_list
    def get_test(self):
        return self.subject+' '+self.text
    def getmailinfo(self):
        str = '发件人：' + self.send + '\n' + '主题：' +self.subject + '\n' + '正文：' + self.text
        return str


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

    def get_html(self, msg):
            content = ''
            content_type = msg.get_content_type()
            # print('content_type:',content_type)
            if content_type == 'text/html':  # or
                content = msg.get_payload(decode=True)
                charset = guess_charset(msg)
                if charset:
                    content = content.decode(charset)
            return content

    def parsemsg(self, msg):
            pre=[]
            for header in [ 'Received', 'X-Originating-IP', 'Date','From', 'To','Subject',  'X-Mailer', 'Message-ID']:
                value = msg.get(header, '')
                if value:
                    if header == 'Subject':
                        value = decode_str(value)
                        sub = value
                    elif header == 'From':
                        hdr, addr = parseaddr(value)
                        name = decode_str(hdr)
                        value = name+'<'+addr+'>'
                        sender = value
                    elif header=='To':
                        hdr, addr = parseaddr(value)
                        name = decode_str(hdr)
                        value = u'%s <%s>' % (name, addr)
                    elif header == 'X-Originating-IP':
                        value = decode_str(value)
                        ip = value
                    else:
                        value = decode_str(value)
                else:
                    value=''
                pre.append(value)
            #print(pre)

            if msg is None:
                return None
            for part in msg.walk():
                if not part.is_multipart():
                    text = self.get_content(part)
                    #print("emailcontent:" + text)
                    break
            # for part in msg.walk():
            #     if not part.is_multipart():
            #         html = self.get_html(part)
            #         print(html)
            #         if html !='':
            #           break
            mail = Mail(sender, sub, text)
            #mail.out()
            return mail



    def checknew(self,signal,sock):
        glob = chilkat2.Global()
        success = glob.UnlockBundle("Anything for 30-day trial")

        status = glob.UnlockStatus

        # The LastErrorText can be examined in the success case to see if it was unlocked in
        # trial more, or with a purchased unlock code.

        # This example assumes the Chilkat API to have been previously unlocked.
        # See Global Unlock Sample for sample code.
        imap = chilkat2.Imap()
        # Connect to an IMAP server.
        # Use TLS
        imap.Ssl = True
        imap.Port = 993
        if '@163.com' in self.user:
          success = imap.Connect("imap.163.com")
        if '@qq.com' in self.user:
            success = imap.Connect("imap.qq.com")
        if (success != True):
            print(imap.LastErrorText)
            sys.exit()
        # Login
        success = imap.Login(self.user, self.password)
        if (success != True):
            print(imap.LastErrorText)
            sys.exit()
            # Select an IMAP mailbox
        success = imap.SelectMailbox("Inbox")
        if (success != True):
            print(imap.LastErrorText)
            sys.exit()
        currentnumber = imap.NumMessages
        while True:
            time.sleep(1)
            success = imap.SelectMailbox("Inbox")
            if (success != True):
                print(imap.LastErrorText)
                sys.exit()
            newnum = imap.NumMessages
            if(newnum>currentnumber):
                self.server.quit()
                self.server = poplib.POP3(self.pop3_server)
                self.server.set_debuglevel(0)
                self.server.user(self.user)
                self.server.pass_(self.password)
                index = newnum
                resp, lines, octets = self.server.retr(index)
                # lines存储了邮件的原始文本的每一行,
                # 可以获得整个邮件的原始文本:
                msg_content = b'\r\n'.join(lines).decode('utf-8')
                # 稍后解析出邮件:
                msg = Parser().parsestr(msg_content)
                # 可以根据邮件索引号直接从服务器删除邮件:
                # server.dele(index)
                mail = self.parsemsg(msg)
                send = mail.get_sender()
                sock.sendfrom(self.user, send)
                rs = sock.get_sender()
                print(rs)
                if rs == '1':
                    print(1)
                    mail.set_normal(False)
                    self.maillist.append(mail)
                elif rs == '2':
                    print(2)
                    mail.set_normal(True)
                    self.maillist.append(mail)
                elif rs == '3':
                    print(3)
                    test = mail.get_test()
                    sock.sendmail(test)
                    label = sock.getresult()
                    mail.set_normal(label)
                    self.maillist.append(mail)
                if mail.get_label()==True:
                    signal.run('正常')
                else:
                    signal.run('垃圾')
            currentnumber=newnum


    #得到邮件数量
    def getmailnum(self):
         return len(self.maillist)


    #得到第几封邮件的内容
    def mailtext(self,num):
        t=num
        str=self.maillist[t].get_sub()+"    "+self.maillist[t].get_text()
        return str


    def mailsender(self,num):
        t = num
        str = self.maillist[t].get_sender()
        return str


    def mail_pretest(self,num):
        list=self.maillist[num].get_pretest()
        return list

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
              str = '发件人：' + send +'\n' +'主题：'+ sub + '\n' +'正文：'+text
              list.append(str)
        return list



    def get_normalmail(self):
        list = []
        for mail in self.maillist:
            if mail.get_label():
              send = mail.get_sender()
              sub = mail.get_sub()
              text=mail.get_text()
              str = '发件人：' + send + '\n' + '主题：' + sub + '\n' + '正文：' + text
              list.append(str)
        return list


    def setlabel(self,num,label):
         self.maillist[num].set_normal(label)


    def getname(self):
        return self.user
    def getpwd(self):
        return self.password


    def quit(self):
        self.server.quit()

    def mailnum(self,str):
        l=len(self.maillist)
        num=None
        for i in range(0,l):
            mailinfo=self.maillist[i].getmailinfo()
            if str==mailinfo:
                num=i
                break
        print(num)
        return num


    def getkey(self,i):
        return self.maillist[i].getmail()



    def maildic(self):
        l = len(self.maillist)
        maildic={}
        for i in range(0, l):
            text=self.maillist[i].getmail()
            label=self.maillist[i].get_label()
            dic={text:label}
            maildic.update(dic)
        return maildic




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








