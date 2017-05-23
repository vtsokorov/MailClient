# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from UiPy.UiAbout import Ui_Dialog

class AboutDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

