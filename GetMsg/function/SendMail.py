from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from mailSend import SendMail
import sendmail


class UI_SendMail(QtWidgets.QWidget, sendmail.Ui_SendMail):
    def __init__(self):
        super(UI_SendMail, self).__init__()
        self.setupUi(self)
        self.connectButtons()

    def clickSend(self):
        addressee = self.receiver.text()
        mailtitle = self.title.text()
        mailcontent = self.content.toPlainText()
        # # mail = [addressee, mailtitle, mailcontent]
        # print(mailcontent)
        sendMail = SendMail('879180233@qq.com',addressee,mailtitle,'idrbvinoknuhbdfj',mailcontent)
        if (sendMail.send_mail_txt()):
            QMessageBox.information(self, "提示", "发送成功！")
        else:
            QMessageBox.information(self, "提示", "发送失败！")
        self.close()


    def connectButtons(self):
        self.sendButton.clicked.connect(self.clickSend)
