from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView

import blackwhitelist


class UI_BlackWhiteList(QtWidgets.QWidget, blackwhitelist.Ui_BlackWhiteList):


    def __init__(self,list,usr,clisock):

        super(UI_BlackWhiteList, self).__init__()
        self.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        #self.blackwhitelist.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.testAdd(list)
        self.deletebutton.clicked.connect(self.deleteBlackWhiteListItem)
        self.usr=usr
        self.clisock=clisock

    def testAdd(self,list):
        # blacklist = ["black list1", "black list2", "black list3", "black list4", "black list5", "black list6", "black list7"]
        self.blackwhitelist.addItems(list)

    def deleteBlackWhiteListItem(self):
        # selectedItems = self.blacklist.selectedItems()
        # for item in selectedItems:
        #     print(item.row()) #item没有row()函数！！！！
        # selectedIndexs = self.blacklist.selectedIndexes()
        # for index in selectedIndexs:
        #     print(index.row()) #index才有row()函数！！！
        selectedIndexs = self.blackwhitelist.selectedIndexes()
        usr=self.usr
        windowtitle = self.windowTitle()
        if len(selectedIndexs)==1:
            for index in selectedIndexs:
                name=self.blackwhitelist.item(index.row()).text()
                if windowtitle=='黑名单':
                    self.clisock.deleteblack(usr,name)
                elif windowtitle=='白名单':
                    self.clisock.deletewhite(usr, name)
                self.blackwhitelist.removeItemWidget(self.blackwhitelist.takeItem(index.row()))

        if len(selectedIndexs)>1:
            count = 0
            for index in selectedIndexs:
                self.blackwhitelist.removeItemWidget(self.blackwhitelist.takeItem(index.row() - count))
                count+=1

        # if len(selectedIndexs)>1:
        #     count = 0
        #     for index in selectedIndexs:
        #         name = self.blackwhitelist.item(index.row()).text()
        #         if windowtitle == '黑名单':
        #             self.clisock.deleteblack(usr, name)
        #         elif windowtitle == '白名单':
        #             self.clisock.deletewhite(usr, name)
        #         self.blackwhitelist.removeItemWidget(self.blackwhitelist.takeItem(index.row()-count))
        #         count+=1
