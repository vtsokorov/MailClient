# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from mainwindow import MainWindow
from logindialog import LoginDialog

def main():
    app = QtWidgets.QApplication(sys.argv)
    result = 0; isOk = 1
    while isOk == 1 or isOk == 2:
        loginDlg = LoginDialog()
        isOk = loginDlg.showDialog()
        if isOk == 1:
            window = MainWindow(loginDlg.connection, loginDlg.configure)
            window.show()
            result = app.exec_()
            isOk = window.windowStatus()
            del window
    sys.exit(result)

if __name__ == "__main__":
    main()

