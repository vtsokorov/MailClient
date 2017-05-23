# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from UiPy.UiMainWindow import Ui_MainWindow
from loadsettings import Settings
from settingsdialog import SettingsDialog
from newmessage import NewMessahe
from aboutdialog import AboutDialog
from threading import Thread
import tablemodel


class MailHeader:
    def __init__(self, uid = None, send_from = None, send_to = None, subject = None, date = None):
        self.uid = uid
        self.send_from = send_from
        self.send_to = send_to
        self.subject = subject
        self.date = date

class MainWindow(QtWidgets.QMainWindow):

    threadInfoText = QtCore.pyqtSignal()
    threadInfoStatus = QtCore.pyqtSignal(str)
    threadInfoMessage = QtCore.pyqtSignal(str)

    def __init__(self, connection, config, parent = None):
        super(QtWidgets.QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.isWork = 0
        self.config = config
        self.connection = connection
        self.typeView = None
        self.body = None

        self.ui.closeAct.triggered.connect(self.closeMethod, QtCore.Qt.QueuedConnection)
        self.ui.exitAct.triggered.connect(self.exitMethod, QtCore.Qt.QueuedConnection)
        self.ui.newMail.triggered.connect(self.showDialogNewMessage, QtCore.Qt.QueuedConnection)
        self.ui.settingsAct.triggered.connect(self.showSettingsDialog, QtCore.Qt.QueuedConnection)
        self.ui.aboutAct.triggered.connect(self.showAboutDialog, QtCore.Qt.QueuedConnection)
        self.ui.updateAct.triggered.connect(self.updateModel, QtCore.Qt.QueuedConnection)

        self.threadInfoText.connect(self.showBody, QtCore.Qt.BlockingQueuedConnection)
        self.threadInfoStatus[str].connect(self.showStatus, QtCore.Qt.BlockingQueuedConnection)
        self.threadInfoMessage[str].connect(self.showMessage, QtCore.Qt.BlockingQueuedConnection)

        self.ui.tv_mailbox.selectObject.connect(self.showModel)
        self.ui.tv_mailbox.expandAll()
        self.ui.tv_maillist.clicked.connect(self.getBody)

        self.model = tablemodel.TableModel(self)
        self.ui.tv_maillist.setModel(self.model)

        self.treadLoadHeader = Thread()
        self.treadLoadBody = Thread()

        self.exitThread = False
        self.exit = False

    def closeEvent(self, enent = QtGui.QCloseEvent()):
        self.exitThread = True
        if not self.exit:
            self.connection.logout()

    @QtCore.pyqtSlot()
    def closeMethod(self):
        self.exitThread = True
        self.exit = True
        self.connection.logout()
        self.isWork = 0
        self.close()

    @QtCore.pyqtSlot()
    def exitMethod(self):
        self.exitThread = True
        self.exit = True
        self.connection.logout()
        self.isWork = 2
        self.close()

    def windowStatus(self):
        return self.isWork

    @QtCore.pyqtSlot(str)
    def showModel(self, typeView):
        self.typeView = typeView
        self.model.updateModel()
        self.initTable()

    @QtCore.pyqtSlot()
    def updateModel(self):
        self.model.updateModel()
        self.initTable()

    def initTable(self):
        if not self.treadLoadHeader.is_alive():
            del self.treadLoadHeader
            self.treadLoadHeader = Thread(target = self.loadHeader, args=(self.typeView, ), daemon = False)
            self.treadLoadHeader.start()
        self.ui.te_content.setHtml("")
        self.ui.tv_maillist.setColumnWidth(0, 150)
        self.ui.tv_maillist.setColumnWidth(1, 150)
        self.ui.tv_maillist.setColumnWidth(2, 270)
        self.ui.tv_maillist.setColumnWidth(3, 120)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def getBody(self, index):
        if not self.treadLoadBody.is_alive():
            del self.treadLoadBody
            self.treadLoadBody = Thread(target = self.loadBody, args=(index,), daemon = False)
            self.treadLoadBody.start()
        self.showStatus("Количество писем: " + str(self.model.rowCount()))

    def loadBody(self, index):
        self.body = "Загрузка содержания письма..."
        self.threadInfoText.emit()
        uid = self.model.uid(index)
        item = self.connection.fetch_body_by_uid(uid)
        self.body = item["body"]["plain"][0] if item["body"]["plain"] else item["body"]["html"][0]
        self.threadInfoText.emit()
        if self.typeView == "unread":
            self.connection.mark_seen(uid)

    def loadHeader(self, view):
        typeView = view
        recursive = False
        self.threadInfoStatus[str].emit("Запрос получения писем из почтового ящика...")
        rowCountMail = 0; mail = []; headers = []

        if typeView == "unread":
            rowCountMail = self.connection.count(unread=True)
            headers = self.connection.headers(unread=True)
        elif typeView == "all":
            rowCountMail = self.connection.count()
            headers = self.connection.headers()

        for item in headers:
            if self.exitThread : return
            if typeView != self.typeView: recursive = True; break
            uid = item[0]
            sent_from = item[1]["sent_from"][0]["email"]  # if item["sent_from"] else None
            sent_to = item[1]["sent_to"][0]["email"] if item[1]["sent_to"] else None
            subject = item[1].get("subject", None)
            date = item[1].get("date", None)
            mail.append(MailHeader(uid, sent_from, sent_to, subject, date))

        if not recursive:
            mail.reverse()
            self.model.updateModel(mail, rowCountMail)
            self.threadInfoStatus[str].emit("Готово.")
        else:
            self.threadInfoStatus[str].emit("Стоп.")
            self.threadInfoMessage[str].emit("Смена перспективы вовремя загрузки данных. Обновите почтовый ящик.")


    @QtCore.pyqtSlot(str)
    def showBody(self):
        self.ui.te_content.setHtml(self.body)

    @QtCore.pyqtSlot(str)
    def showStatus(self, text):
        self.ui.statusbar.showMessage(text)

    @QtCore.pyqtSlot(str)
    def showMessage(self, test):
        QtWidgets.QMessageBox.information(self, "Внимание", test, QtWidgets.QMessageBox.Ok)

    @QtCore.pyqtSlot()
    def showDialogNewMessage(self):
        dialog = NewMessahe(self.config)
        dialog.exec_()

    @QtCore.pyqtSlot()
    def showSettingsDialog(self):
        self.settingsDlg = SettingsDialog(self.config)
        self.settingsDlg.exec_()

    @QtCore.pyqtSlot()
    def showAboutDialog(self):
        self.aboutDlg = AboutDialog()
        self.aboutDlg.exec_()




