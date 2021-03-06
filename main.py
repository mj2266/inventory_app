import os
from PyQt5 import QtGui, uic, QtWidgets
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "main.ui"))


class MainWidget(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.homepage.suppliersButton.clicked.connect(self.foo)
        self.homepage.ordersButton.clicked.connect(self.doo)
        self.supplier.actionBack.triggered.connect(self.boo)
        self.order.generateByIdButton.clicked.connect(self.boo)
        self.stackedWidget.setCurrentIndex(0)
        
    def foo(self):
        self.stackedWidget.setCurrentIndex(1)

    def doo(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def boo(self):
        self.stackedWidget.setCurrentIndex(0)
    


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = MainWidget()
    w.show()
    sys.exit(app.exec_())
