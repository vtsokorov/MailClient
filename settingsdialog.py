# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from UiPy.UiSettings import Ui_Dialog
from loadsettings import Settings

class SettingsDialog(QtWidgets.QDialog):
    def __init__(self, config, parent = None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.config = config
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.ui.le_imap_server.setText(self.config["imap_server"])
        self.ui.le_smtp_server.setText(self.config["smtp_server"])
        self.ui.sp_imap_port.setValue(self.config["imap_port"])
        self.ui.sp_smtp_port.setValue(self.config["smtp_port"])
        self.ui.cb_ssl.setChecked(self.config["ssl"])
        self.ui.pb_ok.clicked.connect(self.saveSettings)

    @QtCore.pyqtSlot()
    def saveSettings(self):
        self.config.set("imap_server", self.ui.le_imap_server.text())
        self.config.set("smtp_server", self.ui.le_smtp_server.text())
        self.config.set("imap_port", str(self.ui.sp_imap_port.value()))
        self.config.set("smtp_port", str(self.ui.sp_smtp_port.value()))
        self.config.set("ssl", "Yes" if self.ui.cb_ssl.isChecked() else "No")
        self.config.save()
        self.accept()
