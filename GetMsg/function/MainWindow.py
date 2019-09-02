from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, QEventLoop

from function.BlackWhiteList import UI_BlackWhiteList
from function.CheckMail import UI_CheckMail
from function.SendMail import UI_SendMail
import mainwindow


class UI_MainWindow(QtWidgets.QWidget, mainwindow.Ui_MainWindow):
    def __init__(self,mailusr,clisock):
        super(UI_MainWindow, self).__init__()
        self.setupUi(self)
        self.connectButtons()
        self.mailusr = mailusr
        self.clisock = clisock

    def sendMail(self):
        sendmail = UI_SendMail(self.mailusr)
        sendmail.show()
        qe = QEventLoop()
        qe.exec()

    def clickNormal(self): #查看收件箱
        self.mailList.clear()
        normallist = self.mailusr.get_normalmail()
        self.mailList.addItems(normallist)

    def clickTrash(self): #查看垃圾箱
        self.mailList.clear()
        trashlist = self.mailusr.get_badmail()
        self.mailList.addItems(trashlist)

    def clickBlackConfirm(self):  # 添加黑名单
        str = self.username.text() + ' ' + self.getBlackList()
        self.clisock.sendBlack(str)
        self.blacklist.clear()

    def clickWhiteConfirm(self):  # 添加白名单
        str = self.username.text() + ' ' + self.getWhiteList()
        self.clisock.sendWhite(str)
        self.whitelist.clear()

    def setUserName(self, str):  # 设置用户名
        self.username.setText(str)

    def logOut(self):
        QCoreApplication.instance().quit()

    def locateEachMail(self):
        # textlist = self.mailList.selectedItems() #返回的是列表，用迭代器访问
        indexItems = self.mailList.selectedIndexes()
        # for item in textlist:
        #     print(item.text())
        return indexItems[0].row()

    def checkMail(self):  # 查看邮件(正常和垃圾)
        print(self.locateEachMail())
        checkwindow = UI_CheckMail()
        checkwindow.show()
        qe = QEventLoop()
        qe.exec()

    def checkBlackList(self):
        usr=self.username.text()
        self.clisock.sendgetblack(usr)
        list=self.clisock.getlist()
        blacklistwindow = UI_BlackWhiteList(list,usr,self.clisock)
        blacklistwindow.setWindowTitle("黑名单")
        blacklistwindow.show()
        qe = QEventLoop()
        qe.exec()

    def checkWhiteList(self):
        usr = self.username.text()
        self.clisock.sendgetwhite(usr)
        list = self.clisock.getlist()
        blacklistwindow = UI_BlackWhiteList(list,usr,self.clisock)
        blacklistwindow.setWindowTitle("白名单")
        blacklistwindow.show()
        qe = QEventLoop()
        qe.exec()

    def getBlackList(self):
        return self.blacklist.text()

    def getWhiteList(self):
        return self.whitelist.text()

    def connectButtons(self):
        self.sendmail.clicked.connect(self.sendMail)
        self.normal.clicked.connect(self.clickNormal)
        self.trash.clicked.connect(self.clickTrash)
        self.logout.clicked.connect(self.logOut)
        self.checkmail.clicked.connect(self.checkMail)
        self.blackconfirm.clicked.connect(self.clickBlackConfirm)
        self.whiteconfirm.clicked.connect(self.clickWhiteConfirm)
        self.checkblacklist.clicked.connect(self.checkBlackList)
        self.checkwhitelist.clicked.connect(self.checkWhiteList)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    a = UI_MainWindow()
    a.show()
    sys.exit(app.exec_())