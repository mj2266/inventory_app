import os
from PyQt5 import QtGui, uic, QtWidgets
from functools import partial
from addSupplier import addSupplierDialog
from main import MainWidget

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "UI FILES/login.ui"))


class loginWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.loginButton.clicked.connect(self.loginCheck)

    def loginCheck(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        if(username == "admin" and password == "admin"):
            self.homepageopen()
        else:
            self.errorMsg("Warning", 'Invalid Username and Password')

    def homepageopen(self):
        self.homepage = MainWidget()
        self.homepage.show()
        self.close()

    def errorMsg(self , title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = loginWindow()
    w.show()
    sys.exit(app.exec_())
    