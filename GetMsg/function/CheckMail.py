from PyQt5 import QtWidgets
import checkmail


class UI_CheckMail(QtWidgets.QWidget, checkmail.Ui_CheckMail):
    def __init__(self):
        super(UI_CheckMail, self).__init__()
        self.setupUi(self)