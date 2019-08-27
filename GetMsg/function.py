from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, QEventLoop

import mainwindow
import checkmail
#from blacklist import blacklist


class UI_MainWindow(QtWidgets.QWidget, mainwindow.Ui_MainWindow):
    def __init__(self,mailusr):
        super(UI_MainWindow, self).__init__()
        self.setupUi(self)
        self.connectButtons()
        self.mailusr=mailusr

    def clickNormal(self):
        self.mailList.clear()
        normallist = self.mailusr.get_normalmail()
        self.mailList.addItems(normallist)

    def clickTrash(self):
        self.mailList.clear()
        trashlist = self.mailusr.get_badmail()
        self.mailList.addItems(trashlist)

    def clickBlackConfirm(self):
        print(self.getBlackList())
        self.blacklist.clear()

    def clickWhiteConfirm(self):
        print(self.getWhiteList())
        self.whitelist.clear()

    def setUserName(self, str):
        self.username.setText(str)

    def logOut(self):
        QCoreApplication.instance().quit()

    def locateEachMail(self):
        textlist = self.mailList.selectedItems() #返回的是列表，用迭代器访问
        indexlist = self.mailList.selectedIndexes()
        for item in textlist:
            print(item.text())
        for index in indexlist:
            print(index.row())

    def checkMail(self):
        checkwindow = UI_CheckMail()
        checkwindow.show()
        qe = QEventLoop()
        qe.exec()
        # self.locateEachMail()

    def getBlackList(self):
        return self.blacklist.text()

    def getWhiteList(self):
        return self.whitelist.text()

    def connectButtons(self):
        self.normal.clicked.connect(self.clickNormal)
        self.trash.clicked.connect(self.clickTrash)
        self.logout.clicked.connect(self.logOut)
        self.checkmail.clicked.connect(self.checkMail)
        self.blackconfirm.clicked.connect(self.clickBlackConfirm)
        self.whiteconfirm.clicked.connect(self.clickWhiteConfirm)


class UI_CheckMail(QtWidgets.QWidget, checkmail.Ui_CheckMail):
    def __init__(self):
        super(UI_CheckMail, self).__init__()
        self.setupUi(self)


# class UI_BlackList(QtWidgets.QWidget, blacklist.Ui_BlackList):
#     def __init__(self):
#         super(UI_BlackList, self).__init__()
#         self.setupUi(self)
#
#     def deleteBlackListItem(self):
#         pass

if __name__ == "__main__":
    import sys
    mailusr=''
    app = QtWidgets.QApplication(sys.argv)
    a = UI_MainWindow(mailusr)
    a.show()
    sys.exit(app.exec_())