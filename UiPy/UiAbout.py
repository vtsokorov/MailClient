# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 160)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setText("")
        self.label_1.setPixmap(QtGui.QPixmap(r".\img\app.png"))
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 2, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.pb_ok = QtWidgets.QPushButton(Dialog)
        self.pb_ok.setObjectName("pb_ok")
        self.gridLayout.addWidget(self.pb_ok, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        self.pb_ok.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "О программе"))
        self.label_2.setText(_translate("Dialog", "Примитивный почтовый клиент (IMAP/SMTP) \n"
            "Написан на Python и PyQt\n"
            "Протестирован в работе с Yandex.Почта\n"
            "Copyright ® 2016 gfreeice@gmail.com\n"""))
        self.pb_ok.setText(_translate("Dialog", "OK"))

