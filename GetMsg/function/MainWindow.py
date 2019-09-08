import qtawesome
from PyQt5 import QtWidgets, QtCore, sip
from PyQt5.QtCore import QCoreApplication, QEventLoop, QSize

from function.BlackWhiteList import UI_BlackWhiteList
from function.CheckMail import UI_CheckMail
from function.SendMail import UI_SendMail
import mainwindow
import re
import mailwrite
from PyQt5.Qt import *
import sys
class UI_MainWindow(QtWidgets.QWidget, mainwindow.Ui_MainWindow):

    signOut = pyqtSignal()

    def __init__(self,mailusr,clisock):
        super(UI_MainWindow, self).__init__()
        self.setAutoFillBackground(True)
        self.setupUi(self)
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.hideCheckMailWidget()
        self.connectButtons()
        self.mailusr = mailusr
        self.clisock = clisock
        self.UI()
        self.usePalette()

    def sendMail(self):
        sendmail = UI_SendMail(self.mailusr)
        sendmail.show()
        self.deleteWidget()
        qe = QEventLoop()
        qe.exec()

    def clickNormal(self): #查看收件箱
        self.mailList.clear()
        self.moveto.setText("移至垃圾箱")
        normallist = self.mailusr.get_normalmail()
        self.mailList.addItems(normallist)
        # self.checkMail()

    def clickTrash(self): #查看垃圾箱
        self.mailList.clear()
        self.moveto.setText("移至收件箱")
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
        usr = self.username.text()
        dict=self.mailusr.maildic()
        mailwrite.write(usr,dict)
        self.signOut.emit()


    def locateEachMail(self):
        # textlist = self.mailList.selectedItems() #返回的是列表，用迭代器访问
        indexItems = self.mailList.selectedIndexes()
        # for item in textlist:
        #     print(item.text())
        return indexItems[0].row()

    def checkMail(self):  # 查看邮件(正常和垃圾)
        selectedItems = self.mailList.selectedItems()
        if len(selectedItems) == 0:
            return
        # op = QtWidgets.QGraphicsOpacityEffect()
        # op.setOpacity(0.5)
        # self.content.setGraphicsEffect(op)
        num = self.locateEachMail()
        t = self.mailList.item(num).text()
        #print(t)
        num=self.mailusr.mailnum(t)
        mail=self.mailusr.rtmail(num)
        sender=mail.get_sender()
        sub=mail.get_sub()
        text=mail.get_text()
        self.displayMail(sender, sub, text)
        self.showCheckMailWidget()
        # checkwindow = UI_CheckMail(sender, sub, text)
        # checkwindow.show()
        # qe = QEventLoop()
        # qe.exec()

    def displayMail(self,senderStr, subStr, contentStr):
        self.senderName.setText(senderStr)
        self.title.setText(subStr)
        self.content.setText(contentStr)

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

    def clickmoveto(self):
        selectedItems = self.mailList.selectedItems()
        if len(selectedItems) == 0:
            return
        act=self.moveto.text()
        n=self.locateEachMail()
        text = self.mailList.item(n).text()
        mailnum=self.mailusr.mailnum(text)
        if act=='移至垃圾箱':
            self.mailusr.setlabel(mailnum,False)
        if act=='移至收件箱':
            self.mailusr.setlabel(mailnum, True)
        self.mailList.removeItemWidget(self.mailList.takeItem(n))

    def UI(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.normal.setIconSize(QSize(20,20))
        self.normal.setIcon(qtawesome.icon("mdi.mailbox", color="black"))
        self.sendmail.setIconSize(QSize(16,16))
        self.sendmail.setIcon(qtawesome.icon("fa5s.pen", color="black"))
        self.trash.setIcon(qtawesome.icon("fa5s.trash-alt", color="black"))
        self.checkblacklist.setIcon(qtawesome.icon("fa5s.list-alt", color="black"))
        self.checkwhitelist.setIcon(qtawesome.icon("fa.list-alt", color="black"))
        self.blackconfirm.setIcon(qtawesome.icon("fa5s.plus", color="black"))
        self.whiteconfirm.setIcon(qtawesome.icon("fa5s.plus", color="black"))
        self.checkmail.setIcon(qtawesome.icon("fa.eye", color="black"))
        self.moveto.setIcon(qtawesome.icon("fa5s.exchange-alt", color="black"))
        self.logout.setIcon(qtawesome.icon("fa5s.sign-out-alt", color="black"))
        self.userlabel.setFont(qtawesome.font("fa5s", 50))
        self.userlabel.setText(chr(0xf007))
        self.setButtonCursor()
        self.mailList.setStyleSheet(
            "QListWidget{background-color:whitesmoke;border:none;color:#696969;font:75 16pt 'Microsoft YaHei UI';font-size:16px;font-weight:bold;}"
            'QListWidget::Item{padding-top:-2px; padding-bottom:-1px;}'
            "QListWidget::Item:hover{background:silver;padding-top:0px; padding-bottom:0px; }"
            "QListWidget::item:selected{background:lightgray; color:black; }")

    def setButtonCursor(self):
        self.logout.setCursor(QCursor(QPixmap('mid.png').scaled(25, 29)))
        self.normal.setCursor(QCursor(QPixmap('mid.png').scaled(25, 29)))
        self.sendmail.setCursor(QCursor(QPixmap('mid.png').scaled(25, 29)))
        self.trash.setCursor(QCursor(QPixmap('mid.png').scaled(25, 29)))
        self.checkblacklist.setCursor(QCursor(QPixmap('mid.png').scaled(25, 29)))
        self.checkwhitelist.setCursor(QCursor(QPixmap('mid.png').scaled(25, 29)))
        self.blackconfirm.setCursor(QCursor(QPixmap('mid.png').scaled(25, 29)))
        self.whiteconfirm.setCursor(QCursor(QPixmap('mid.png').scaled(25, 29)))
        self.moveto.setCursor(QCursor(QPixmap('mid.png').scaled(25, 29)))
        self.checkmail.setCursor(QCursor(QPixmap('mid.png').scaled(25, 29)))


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
        self.moveto.clicked.connect(self.clickmoveto)

    def hideCheckMailWidget(self):
        self.title.hide()
        self.senderName.hide()
        self.content.hide()
        self.titlelabel.hide()
        self.senderlabel.hide()

    def showCheckMailWidget(self):
        self.title.show()
        self.senderName.show()
        self.content.show()
        self.titlelabel.show()
        self.senderlabel.show()

    def usePalette(self):
        # pass
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.5)
        self.mailList.setGraphicsEffect(op)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAutoFillBackground(False)
        # self.setAttribute(Qt.WA_NoSystemBackground)
        # self.setWindowOpacity(0)
        # self.checkmailwidget.setWindowOpacity(0)
        self.leftwidget.setAttribute(Qt.WA_TranslucentBackground, True)
        self.checkmailwidget.setAttribute(Qt.WA_TranslucentBackground, True)
        self.leftwidget.setAutoFillBackground(False)
        # leftpalette = self.leftwidget.palette()
        # leftpalette.setColor(leftpalette.Window, QColor(85, 170, 255))
        # self.leftwidget.setPalette(leftpalette)
        self.checkmailwidget.setAutoFillBackground(False)
        # palette = self.checkmailwidget.palette()
        # palette.setColor(palette.Window, QColor(85, 170, 255))
        # self.checkmailwidget.setPalette(palette)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton or Qt.MidButton or Qt.RightButton:
            pass

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton or Qt.MidButton or Qt.RightButton:
            pass

    def mouseMoveEvent(self, event):
        pass

    def deleteWidget(self):
        pass
        # self.checkmailwidget.remove(self.content)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    a = UI_MainWindow()
    a.show()
    sys.exit(app.exec_())