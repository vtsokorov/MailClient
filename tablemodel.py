
from PyQt5 import QtCore, QtGui


column_count = int(4)
class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, parent = None):
        super(TableModel, self).__init__(parent)
        self.mail = []
        self.rowCountMail = 0

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index, role = QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        row = index.row(); column = index.column()
        if row < 0 or row > self.rowCountMail-1:
            return None

        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            if column == 0:
                return self.mail[row].send_from
            if column == 1:
                return self.mail[row].send_to
            if column == 2:
                return self.mail[row].subject
            if column == 3:
                return self.mail[row].date
        return None

    def headerData(self, section, orientation, role = QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            if section == 0:
                return "От кого"
            if section == 1:
                return "Для кого"
            if section == 2:
                return "Тема письма"
            if section == 3:
                return "Дата"
        return None

    def rowCount(self, index = QtCore.QModelIndex()):
        return  0 if index.isValid() else self.rowCountMail

    def columnCount(self, index = QtCore.QModelIndex()):
        return 0 if index.isValid() else column_count

    def updateModel(self, data = list(), count = 0):
        self.beginResetModel()
        self.rowCountMail = count
        self.mail = data
        self.endResetModel()

    def uid(self, index):
        return self.mail[index.row()].uid
