from PyQt5 import QtWidgets
import checkmail


class UI_CheckMail(QtWidgets.QWidget, checkmail.Ui_CheckMail):
    def __init__(self, senderStr, subStr, contentStr):
        super(UI_CheckMail, self).__init__()
        self.setupUi(self)
        self.displayMail(senderStr, subStr, contentStr)

    def displayMail(self,senderStr, subStr, contentStr):
        self.senderName.setText(senderStr)
        self.title.setText(subStr)
        self.content.setText(contentStr)