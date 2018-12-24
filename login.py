# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

# this is to call the homepage
from homepage import Ui_Homepage
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(716, 571)
        MainWindow.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(207, 138, 0, 255), stop:0.0113636 rgba(255, 211, 76, 255), stop:0.443182 rgba(173, 115, 0, 255), stop:1 rgba(207, 138, 0, 255));"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 500))
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgba(152, 171, 255, 0);"))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.rememberPasswordCheckBox = QtGui.QCheckBox(self.frame)
        self.rememberPasswordCheckBox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.rememberPasswordCheckBox.setFont(font)
        self.rememberPasswordCheckBox.setStyleSheet(_fromUtf8("selection-background-color: rgb(248, 250, 215);"))
        self.rememberPasswordCheckBox.setObjectName(_fromUtf8("rememberPasswordCheckBox"))
        self.gridLayout.addWidget(self.rememberPasswordCheckBox, 8, 0, 1, 1)
        self.passwordLabel = QtGui.QLabel(self.frame)
        self.passwordLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet(_fromUtf8(""))
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridLayout.addWidget(self.passwordLabel, 5, 0, 1, 1)
        self.line = QtGui.QFrame(self.frame)
        self.line.setEnabled(False)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.userNameLabel = QtGui.QLabel(self.frame)
        self.userNameLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.userNameLabel.setFont(font)
        self.userNameLabel.setStyleSheet(_fromUtf8(""))
        self.userNameLabel.setObjectName(_fromUtf8("userNameLabel"))
        self.gridLayout.addWidget(self.userNameLabel, 3, 0, 1, 1)
        self.loginLabel = QtGui.QLabel(self.frame)
        self.loginLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.loginLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet(_fromUtf8(""))
        self.loginLabel.setObjectName(_fromUtf8("loginLabel"))
        self.gridLayout.addWidget(self.loginLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.loginButton = QtGui.QPushButton(self.frame)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 50))
        self.loginButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet(_fromUtf8("background-color: rgba(90, 228, 255, 0);\n"
"background-color: rgba(197, 115, 21, 220);"))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))

        #############login click event############
        self.loginButton.clicked.connect(self.loginCheck)
        ##########################################
        
        self.gridLayout.addWidget(self.loginButton, 9, 0, 1, 1)
        self.usernameInput = QtGui.QLineEdit(self.frame)
        self.usernameInput.setMinimumSize(QtCore.QSize(0, 40))
        self.usernameInput.setStyleSheet(_fromUtf8("background-color: rgb(248, 250, 215);"))
        self.usernameInput.setObjectName(_fromUtf8("usernameInput"))
        self.gridLayout.addWidget(self.usernameInput, 4, 0, 1, 1)
        self.passwordInput = QtGui.QLineEdit(self.frame)
        self.passwordInput.setMinimumSize(QtCore.QSize(0, 40))
        self.passwordInput.setStyleSheet(_fromUtf8("background-color: rgb(248, 250, 215);\n"
"background-color: rgb(248, 250, 215);"))
        self.passwordInput.setObjectName(_fromUtf8("passwordInput"))
        self.gridLayout.addWidget(self.passwordInput, 7, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    #### login check#####
    def loginCheck(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        if(username == "admin" and password =="admin"):
            self.homepageopen()
        else:
            self.errorMsg("Warning",'Invalid Username and Password')
    
            
  
    def homepageopen(self):
        #these 4 lines open new page
        self.homepage = QtGui.QMainWindow()
        self.ui = Ui_Homepage()
        self.ui.setupUi(self.homepage)
        self.homepage.show()
        #
        # this line closes main window
        MainWindow.close()
        # or
        #MainWindow.hide()

    def errorMsg(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.rememberPasswordCheckBox.setText(_translate("MainWindow", "Remember My Password", None))
        self.passwordLabel.setText(_translate("MainWindow", "Password:", None))
        self.userNameLabel.setText(_translate("MainWindow", "Username:", None))
        self.loginLabel.setText(_translate("MainWindow", "LOGIN", None))
        self.loginButton.setText(_translate("MainWindow", "LOGIN", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

