# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui
from standarditem import StandardItem

class TreeModel(QtGui.QStandardItemModel):
    def __init__(self, parent = None):
        super(QtGui.QStandardItemModel, self).__init__(parent)
        self.initialize()

    def initialize(self):
        self.setHorizontalHeaderLabels(["Почтовый ящик"])
        self.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.setup()

    def setup(self):
        root = self.invisibleRootItem()
        item0 = self.createItem(root,  r".\img\mail.png", "Письма", "root")
        item1 = self.createItem(item0, r".\img\unread.png", "Не прочитанные" , "unread")
        item2 = self.createItem(item0, r".\img\all.png", "Все письма", "all")


    def createItem(self, root, path, text, arg = str()):
        item = StandardItem(QtGui.QIcon(path), text, arg)
        root.appendRow(item)
        return item

    def dataForIndex(self, index):
        item = self.itemFromIndex(index)
        return item.value