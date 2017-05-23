# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from UiPy.UiNewMessage import Ui_Dialog
from loadsettings import Settings
from Core.smtpclient import *

class NewMessahe(QtWidgets.QDialog):
    def __init__(self, configure, parent = None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.config = configure
        self.ui.pb_send.clicked.connect(self.sendMessage)
        self.ui.pb_cencel.clicked.connect(self.closeWindow)

    def sendMessage(self):
        obj = SMTPClient(self.config["smtp_server"], self.config["smtp_port"], self.config["ssl"])
        if obj.login(self.config["mail"], self.config["pwd"]):
            obj.sender = self.config["mail"]
            obj.recipient = self.ui.le_mail.text()
            obj.subject = self.ui.le_subject.text()
            obj.body = self.ui.te_content.toPlainText()
            obj.send()
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Ощибка отправки письма", QtWidgets.QMessageBox.Ok)

    def closeWindow(self):
        self.close()
