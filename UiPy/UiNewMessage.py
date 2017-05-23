# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(507, 414)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.le_mail = QtWidgets.QLineEdit(Dialog)
        self.le_mail.setObjectName("le_mail")
        self.gridLayout.addWidget(self.le_mail, 0, 0, 1, 1)
        self.le_subject = QtWidgets.QLineEdit(Dialog)
        self.le_subject.setObjectName("le_subject")
        self.gridLayout.addWidget(self.le_subject, 1, 0, 1, 1)
        self.te_content = QtWidgets.QTextEdit(Dialog)
        self.te_content.setObjectName("te_content")
        self.te_content.setFont(QtGui.QFont("Tahoma", 10, QtGui.QFont.Bold))
        self.gridLayout.addWidget(self.te_content, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_send = QtWidgets.QPushButton(Dialog)
        self.pb_send.setObjectName("pb_send")
        self.horizontalLayout.addWidget(self.pb_send)
        self.pb_cencel = QtWidgets.QPushButton(Dialog)
        self.pb_cencel.setObjectName("pb_cencel")
        self.horizontalLayout.addWidget(self.pb_cencel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новое письмо"))
        self.le_mail.setPlaceholderText(_translate("Dialog", "Адрес электронный почты получателя"))
        self.le_subject.setPlaceholderText(_translate("Dialog", "Тема письма"))
        self.pb_send.setText(_translate("Dialog", "Отправить"))
        self.pb_cencel.setText(_translate("Dialog", "Отмена"))

