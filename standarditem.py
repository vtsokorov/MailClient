from PyQt5 import QtCore, QtGui

class StandardItem(QtGui.QStandardItem):

    def __init__(self, icon, text, arg = str()):
        super(StandardItem, self).__init__(icon, text)
        self.arg = arg

    @property
    def value(self):
        return self.arg
