# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui
import treemodel
import treeview

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 526)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Дерево писем "Почтовый ящик"
        self.tv_mailbox = treeview.TreeView(self.centralwidget)
        self.tv_mailbox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tv_mailbox.setObjectName("tw_mailbox")
        self.gridLayout.addWidget(self.tv_mailbox, 0, 0, 2, 1)
        self.tv_mailbox.setModel(treemodel.TreeModel())

        # Список писем
        self.tv_maillist = QtWidgets.QTableView(self.centralwidget)
        self.tv_maillist.setObjectName("tw_maillist")
        self.gridLayout.addWidget(self.tv_maillist, 0, 1, 1, 1)
        self.tv_maillist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tv_maillist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tv_maillist.setAlternatingRowColors(True)
        self.tv_maillist.setSortingEnabled(False)

        # Содержимое писмьма
        self.te_content = QtWidgets.QTextEdit(self.centralwidget)
        self.te_content.setObjectName("te_content")
        self.te_content.setFont(QtGui.QFont("Tahoma", 10, QtGui.QFont.Bold))
        self.te_content.setReadOnly(True)
        self.gridLayout.addWidget(self.te_content, 1, 1, 1, 1)
        # Разделитель
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.gridLayout.addWidget(self.splitter, 0, 1, 1, 1)
        self.splitter.addWidget(self.tv_maillist)
        self.splitter.addWidget(self.te_content)

        MainWindow.setCentralWidget(self.centralwidget)

        # Строка меню
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.menuFile = QtWidgets.QMenu("Файл")
        self.settings = QtWidgets.QMenu("Настройка")
        self.menuHelp = QtWidgets.QMenu("Справка")
        self.menubar.addMenu(self.menuFile)
        self.menubar.addMenu(self.settings)
        self.menubar.addMenu(self.menuHelp)

        self.newMail = QtWidgets.QAction("Новое письмо", MainWindow)
        self.newMail.setShortcuts(QtGui.QKeySequence("Ctrl+N"))
        self.newMail.setIcon(QtGui.QIcon(r".\img\new.png"))
        self.newMail.setStatusTip("Написать новое письмо")
        self.menuFile.addAction(self.newMail)

        self.exitAct = QtWidgets.QAction("Выйти", MainWindow)
        self.exitAct.setShortcuts(QtGui.QKeySequence("Alt+F4"))
        self.exitAct.setIcon(QtGui.QIcon(r".\img\exit.png"))
        self.exitAct.setStatusTip("Выйти из программы")
        self.menuFile.addAction(self.exitAct)

        self.closeAct = QtWidgets.QAction("Закрыть", MainWindow)
        self.closeAct.setShortcuts(QtGui.QKeySequence("Ctrl+Q"))
        self.closeAct.setIcon(QtGui.QIcon(r".\img\close.png"))
        self.closeAct.setStatusTip("Закрыть программу")
        self.menuFile.addAction(self.closeAct)

        self.settingsAct = QtWidgets.QAction("IMAP/SMTP", MainWindow)
        self.settingsAct.setShortcuts(QtGui.QKeySequence("Ctrl+S"))
        self.settingsAct.setStatusTip("Настройка серверов почты IMAP/SMTP")
        self.settingsAct.setIcon(QtGui.QIcon(r".\img\settings.png"))
        self.settings.addAction(self.settingsAct)

        self.aboutAct = QtWidgets.QAction("О программе", MainWindow)
        self.aboutAct.setStatusTip("О программе")
        self.aboutAct.setIcon(QtGui.QIcon(r".\img\info.png"))
        self.menuHelp.addAction(self.aboutAct)

        self.updateAct = QtWidgets.QAction("Обновить", MainWindow)
        self.updateAct.setStatusTip("Обновить ящик с письмами")
        self.updateAct.setIcon(QtGui.QIcon(r".\img\refresh.png"))

        # Панель инструментов
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.addAction(self.newMail)
        self.toolBar.addAction(self.updateAct)
        self.toolBar.addAction(self.exitAct)
        self.toolBar.addAction(self.settingsAct)
        self.toolBar.addAction(self.aboutAct)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        # Статус панель
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Почтовый клиент"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Панель"))
        self.tv_mailbox.setWindowTitle(_translate("MainWindow", "Почтовый ящик"))



