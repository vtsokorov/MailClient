# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(376, 147)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.le_mail = QtWidgets.QLineEdit(Dialog)
        self.le_mail.setObjectName("le_mail")
        self.gridLayout.addWidget(self.le_mail, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.le_passwd = QtWidgets.QLineEdit(Dialog)
        self.le_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_passwd.setObjectName("le_passwd")
        self.gridLayout.addWidget(self.le_passwd, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_settings = QtWidgets.QPushButton(Dialog)
        self.pb_settings.setAutoDefault(False)
        self.pb_settings.setObjectName("pb_settings")
        self.horizontalLayout.addWidget(self.pb_settings)
        self.pb_ok = QtWidgets.QPushButton(Dialog)
        self.pb_ok.setAutoDefault(False)
        self.pb_ok.setObjectName("pb_ok")
        self.horizontalLayout.addWidget(self.pb_ok)
        self.pb_cancel = QtWidgets.QPushButton(Dialog)
        self.pb_cancel.setObjectName("pb_cancel")
        self.horizontalLayout.addWidget(self.pb_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация"))
        self.label_1.setText(_translate("Dialog", "Логин"))
        self.label_2.setText(_translate("Dialog", "Пароль"))
        self.pb_settings.setText(_translate("Dialog", "Настройки"))
        self.pb_ok.setText(_translate("Dialog", "OK"))
        self.pb_cancel.setText(_translate("Dialog", "Отмена"))

