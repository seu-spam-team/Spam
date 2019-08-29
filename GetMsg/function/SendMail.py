from PyQt5 import QtWidgets
import sendmail


class UI_SendMail(QtWidgets.QWidget, sendmail.Ui_SendMail):
    def __init__(self):
        super(UI_SendMail, self).__init__()
        self.setupUi(self)
        self.connectButtons()

    def clickSend(self):
        addressee = self.receiver.text()
        title = self.title.text()
        content = self.content.text()
        mail = [addressee, title, content]
        print(addressee)

    def connectButtons(self):
        self.sendButton.clicked.connect(self.clickSend)
