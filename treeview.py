# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
import treemodel

class TreeView(QtWidgets.QTreeView):

    selectObject = QtCore.pyqtSignal(str)

    def __init__(self, parent = 0):
        super(QtWidgets.QTreeView, self).__init__(parent)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.dataModel = treemodel.TreeModel()
        self.clicked["QModelIndex"].connect(self.selectItem)

    def setModel(self, model):
        self.dataModel = model
        QtWidgets.QTreeView.setModel(self, model)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def selectItem(self, index):
        self.selectObject.emit(self.dataModel.dataForIndex(index))

