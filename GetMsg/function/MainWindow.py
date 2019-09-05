import qtawesome
from PyQt5 import QtWidgets, QtCore
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
    def __init__(self,mailusr,clisock):
        super(UI_MainWindow, self).__init__()
        self.setupUi(self)
        self.connectButtons()
        self.mailusr = mailusr
        self.clisock = clisock
        self.UI()
        # 在系统托盘处显示图标
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(QIcon('timg.jpg'))
        self.tray.show()

        # 设置系统托盘图标的菜单
        # 设定显示和退出两个选项
        self.op1 = QAction('&显示(Show)', triggered=self.show)
        self.op2 = QAction('&退出(Exit)', triggered=self.quitApp)

        # 创建菜单并添加选项
        self.trayMenu = QMenu()
        self.trayMenu.addAction(self.op1)
        self.trayMenu.addAction(self.op2)
        self.tray.setContextMenu(self.trayMenu)

        # 设置后台运行时的提示信息
        self.tray.showMessage('九龙湖邮管', '已在后台运行', icon=0)
        # 鼠标双击点击或左键单击点击会唤出主界面
        self.tray.activated.connect(self.act)

        # 退出程序
    def quitApp(self):
            self.show()  # w.hide() #隐藏
            re = QMessageBox.question(self, "提示", "退出系统", QMessageBox.Yes |
                                      QMessageBox.No, QMessageBox.No)
            if re == QMessageBox.Yes:
                # 关闭窗体程序
                QCoreApplication.instance().quit()
                # 在应用程序全部关闭后，TrayIcon其实还不会自动消失，
                # 直到你的鼠标移动到上面去后，才会消失，
                # 这是个问题，（如同你terminate一些带TrayIcon的应用程序时出现的状况），
                # 这种问题的解决我是通过在程序退出前将其setVisible(False)来完成的。
                self.tray.setVisible(False)

    def act(self, reason):
            # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
            if reason == 2 or reason == 3:
                self.show()


    def sendMail(self):
        sendmail = UI_SendMail(self.mailusr)
        sendmail.show()
        qe = QEventLoop()
        qe.exec()

    def clickNormal(self): #查看收件箱
        self.mailList.clear()
        self.moveto.setText("移至垃圾箱")
        normallist = self.mailusr.get_normalmail()
        self.mailList.addItems(normallist)

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
        QCoreApplication.instance().quit()


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
        num = self.locateEachMail()
        t = self.mailList.item(num).text()
        print((t))
        self.mailusr.mailnum(t)
        sender = (re.findall(r"sender: (.+?)sub", t))
        sender = (sender[0])
        sub = (re.findall(r"subject:(.+?)\ntext", t, re.S))
        sub = (sub[0])
        text = re.findall(r"text:(.+.)", t)
        text = (text[0])
        checkwindow = UI_CheckMail(sender, sub, text)
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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    a = UI_MainWindow()
    a.show()
    sys.exit(app.exec_())