# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from UiPy.UiLogin import Ui_Dialog

from loadsettings import Settings
from settingsdialog import SettingsDialog
from Core.imapclient import *


class LoginDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.isWork = 0
        self.config = Settings()
        self.config.load()
        self.settingsDlg = SettingsDialog(self.config)
        self.ui.le_mail.setText(self.config["mail"])
        self.ui.pb_settings.clicked.connect(self.showSettings)
        self.ui.pb_cancel.clicked.connect(self.closeMethod)
        self.ui.pb_ok.clicked.connect(self.acceptMethod)

    @QtCore.pyqtSlot()
    def showDialog(self):
        self.exec_ ()
        return self.isWork

    @QtCore.pyqtSlot()
    def acceptMethod(self):
        self.settingsDlg.config.set("mail", self.ui.le_mail.text())
        self.settingsDlg.config.save()
        self.imap = IMAPClient(self.config["imap_server"], self.config["imap_port"], self.config["ssl"])
        if self.imap.login(self.ui.le_mail.text(), self.ui.le_passwd.text()):
            self.isWork = 1
            self.config["pwd"] = self.ui.le_passwd.text()
        else:
            self.isWork = 2
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Не корректная аутентификация", QtWidgets.QMessageBox.Ok)
        self.accept()

    @QtCore.pyqtSlot()
    def closeMethod(self):
         self.isWork = 0
         self.close()

    @QtCore.pyqtSlot()
    def showSettings(self):
         self.settingsDlg.exec_()

    @property
    def connection(self):
        pass

    @connection.getter
    def connection(self):
        return self.imap

    @property
    def configure(self):
        pass

    @configure.getter
    def configure(self):
        return self.config