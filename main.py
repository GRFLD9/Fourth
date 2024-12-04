import sys

from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        self.tableView.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
