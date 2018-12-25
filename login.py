# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from homepage import Ui_Homepage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 571)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(207, 138, 0, 255), stop:0.0113636 rgba(255, 211, 76, 255), stop:0.443182 rgba(173, 115, 0, 255), stop:1 rgba(207, 138, 0, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 500))
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setStyleSheet("background-color: rgba(152, 171, 255, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.rememberPasswordCheckBox = QtWidgets.QCheckBox(self.frame)
        self.rememberPasswordCheckBox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.rememberPasswordCheckBox.setFont(font)
        self.rememberPasswordCheckBox.setStyleSheet("selection-background-color: rgb(248, 250, 215);")
        self.rememberPasswordCheckBox.setObjectName("rememberPasswordCheckBox")
        self.gridLayout.addWidget(self.rememberPasswordCheckBox, 8, 0, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.frame)
        self.passwordLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet("")
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setEnabled(False)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.userNameLabel = QtWidgets.QLabel(self.frame)
        self.userNameLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.userNameLabel.setFont(font)
        self.userNameLabel.setStyleSheet("")
        self.userNameLabel.setObjectName("userNameLabel")
        self.gridLayout.addWidget(self.userNameLabel, 3, 0, 1, 1)
        self.loginLabel = QtWidgets.QLabel(self.frame)
        self.loginLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.loginLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet("")
        self.loginLabel.setObjectName("loginLabel")
        self.gridLayout.addWidget(self.loginLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 50))
        self.loginButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color: rgba(90, 228, 255, 0);\n"
"background-color: rgba(197, 115, 21, 220);")
        self.loginButton.setObjectName("loginButton")
        
        #############login click event############
        self.loginButton.clicked.connect(self.loginCheck)
        ##########################################
        
        self.gridLayout.addWidget(self.loginButton, 9, 0, 1, 1)
        self.usernameInput = QtWidgets.QLineEdit(self.frame)
        self.usernameInput.setMinimumSize(QtCore.QSize(0, 40))
        self.usernameInput.setStyleSheet("background-color: rgb(248, 250, 215);")
        self.usernameInput.setObjectName("usernameInput")
        self.gridLayout.addWidget(self.usernameInput, 4, 0, 1, 1)
        self.passwordInput = QtWidgets.QLineEdit(self.frame)
        self.passwordInput.setMinimumSize(QtCore.QSize(0, 40))
        self.passwordInput.setStyleSheet("background-color: rgb(248, 250, 215);\n"
"background-color: rgb(248, 250, 215);")
        self.passwordInput.setObjectName("passwordInput")
        self.gridLayout.addWidget(self.passwordInput, 7, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
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
        self.homepage = QtWidgets.QMainWindow()
        self.ui = Ui_Homepage()
        self.ui.setupUi(self.homepage)
        self.homepage.show()
        #
        # this line closes main window
        MainWindow.close()
        # or
        #MainWindow.hide()

    def errorMsg(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rememberPasswordCheckBox.setText(_translate("MainWindow", "Remember My Password"))
        self.passwordLabel.setText(_translate("MainWindow", "Password:"))
        self.userNameLabel.setText(_translate("MainWindow", "Username:"))
        self.loginLabel.setText(_translate("MainWindow", "LOGIN"))
        self.loginButton.setText(_translate("MainWindow", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

















