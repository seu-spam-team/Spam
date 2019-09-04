from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAbstractItemView

import blackwhitelist


class UI_BlackWhiteList(QtWidgets.QWidget, blackwhitelist.Ui_BlackWhiteList):
    def __init__(self,list, userName):
        super(UI_BlackWhiteList, self).__init__()
        self.setupUi(self)
        self.blackwhitelist.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.testAdd(list)
        self.deletebutton.clicked.connect(self.deleteBlackWhiteListItem)

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
        if len(selectedIndexs)==1:
            for index in selectedIndexs:
                self.blackwhitelist.removeItemWidget(self.blackwhitelist.takeItem(index.row()))
        if len(selectedIndexs)>1:
            count = 0
            for index in selectedIndexs:
                self.blackwhitelist.removeItemWidget(self.blackwhitelist.takeItem(index.row() - count))
                count+=1
