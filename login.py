import os
from PyQt5 import QtGui, uic, QtWidgets
from main import MainWidget
import rec_rc

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "login.ui"))


class loginWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        
        # Setting Focus on username Input
        self.usernameInput.setFocus()

        # Login Button Pressed Event
        self.loginButton.clicked.connect(self.loginCheck)
        
        # Enter button press on Line Edit event
        self.passwordInput.returnPressed.connect(self.loginButton.click)
        self.usernameInput.returnPressed.connect(self.loginButton.click)
        
        # Enter Button pressed on Login button
        self.loginButton.setAutoDefault(True)

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
    