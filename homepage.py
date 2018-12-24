# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Homepage(object):
    def setupUi(self, Homepage):
        Homepage.setObjectName(_fromUtf8("Homepage"))
        Homepage.resize(895, 511)
        Homepage.setStyleSheet(_fromUtf8("QMainWindow{\n"
"background-color: rgb(191, 191, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"font-size:28px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(Homepage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.billingButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.billingButton.setStyleSheet(_fromUtf8("background-image: url(:/Homepage/Homepage/Billing.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
""))
        self.billingButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Homepage/background.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.billingButton.setIcon(icon)
        self.billingButton.setObjectName(_fromUtf8("billingButton"))
        self.gridLayout.addWidget(self.billingButton, 3, 4, 1, 1)
        self.customerLabel = QtGui.QLabel(self.centralwidget)
        self.customerLabel.setStyleSheet(_fromUtf8("font-size: 28px;"))
        self.customerLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.customerLabel.setObjectName(_fromUtf8("customerLabel"))
        self.gridLayout.addWidget(self.customerLabel, 2, 2, 1, 1)
        self.ordersButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.ordersButton.setStyleSheet(_fromUtf8("background-image: url(:/Homepage/Homepage/Orders.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
""))
        self.ordersButton.setText(_fromUtf8(""))
        self.ordersButton.setIcon(icon)
        self.ordersButton.setDescription(_fromUtf8(""))
        self.ordersButton.setObjectName(_fromUtf8("ordersButton"))
        self.gridLayout.addWidget(self.ordersButton, 1, 6, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 8, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 8, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 8, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 7, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 7, 1, 1)
        self.userNameLabel = QtGui.QLabel(self.centralwidget)
        self.userNameLabel.setStyleSheet(_fromUtf8("font-size:20px;"))
        self.userNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userNameLabel.setObjectName(_fromUtf8("userNameLabel"))
        self.gridLayout.addWidget(self.userNameLabel, 0, 8, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 6, 0, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 8, 0, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 6, 7, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 6, 8, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 6, 1, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 3, 7, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 2, 0, 1, 1)
        self.varunEnterprisesLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.varunEnterprisesLabel.setFont(font)
        self.varunEnterprisesLabel.setStyleSheet(_fromUtf8("font-size:35px;"))
        self.varunEnterprisesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.varunEnterprisesLabel.setObjectName(_fromUtf8("varunEnterprisesLabel"))
        self.gridLayout.addWidget(self.varunEnterprisesLabel, 0, 2, 1, 5)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 8, 8, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 2, 5, 1, 1)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 6, 5, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 6, 3, 1, 1)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 0, 1, 1, 1)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 8, 2, 1, 5)
        spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem22, 2, 3, 1, 1)
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem23, 0, 0, 1, 1)
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem24, 0, 7, 1, 1)
        self.logoutButton = QtGui.QPushButton(self.centralwidget)
        self.logoutButton.setObjectName(_fromUtf8("logoutButton"))
        self.gridLayout.addWidget(self.logoutButton, 8, 7, 1, 1)
        self.supportButton = QtGui.QPushButton(self.centralwidget)
        self.supportButton.setObjectName(_fromUtf8("supportButton"))
        self.gridLayout.addWidget(self.supportButton, 8, 1, 1, 1)
        self.billingLabel = QtGui.QLabel(self.centralwidget)
        self.billingLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.billingLabel.setObjectName(_fromUtf8("billingLabel"))
        self.gridLayout.addWidget(self.billingLabel, 6, 4, 1, 1)
        self.pricingButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.pricingButton.setStyleSheet(_fromUtf8("background-image: url(:/Homepage/Homepage/Pricing.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
""))
        self.pricingButton.setText(_fromUtf8(""))
        self.pricingButton.setIcon(icon)
        self.pricingButton.setObjectName(_fromUtf8("pricingButton"))
        self.gridLayout.addWidget(self.pricingButton, 3, 2, 1, 1)
        self.ordersLabel = QtGui.QLabel(self.centralwidget)
        self.ordersLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ordersLabel.setObjectName(_fromUtf8("ordersLabel"))
        self.gridLayout.addWidget(self.ordersLabel, 2, 6, 1, 1)
        self.suppliersButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.suppliersButton.setStyleSheet(_fromUtf8("background-image: url(:/Homepage/Homepage/Supplier.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
""))
        self.suppliersButton.setText(_fromUtf8(""))
        self.suppliersButton.setIcon(icon)
        self.suppliersButton.setObjectName(_fromUtf8("suppliersButton"))
        self.gridLayout.addWidget(self.suppliersButton, 1, 4, 1, 1)
        self.pricingLabel = QtGui.QLabel(self.centralwidget)
        self.pricingLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pricingLabel.setObjectName(_fromUtf8("pricingLabel"))
        self.gridLayout.addWidget(self.pricingLabel, 6, 2, 1, 1)
        self.stocksLabel = QtGui.QLabel(self.centralwidget)
        self.stocksLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.stocksLabel.setObjectName(_fromUtf8("stocksLabel"))
        self.gridLayout.addWidget(self.stocksLabel, 6, 6, 1, 1)
        self.stocksButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.stocksButton.setStyleSheet(_fromUtf8("background-image: url(:/Homepage/Homepage/Stock.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
""))
        self.stocksButton.setText(_fromUtf8(""))
        self.stocksButton.setIcon(icon)
        self.stocksButton.setObjectName(_fromUtf8("stocksButton"))
        self.gridLayout.addWidget(self.stocksButton, 3, 6, 1, 1)
        self.suppliersLabel = QtGui.QLabel(self.centralwidget)
        self.suppliersLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.suppliersLabel.setObjectName(_fromUtf8("suppliersLabel"))
        self.gridLayout.addWidget(self.suppliersLabel, 2, 4, 1, 1)
        self.customerButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.customerButton.setStyleSheet(_fromUtf8("background-image: url(:/Homepage/Homepage/Customer.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
""))
        self.customerButton.setText(_fromUtf8(""))
        self.customerButton.setIcon(icon)
        self.customerButton.setObjectName(_fromUtf8("customerButton"))
        self.gridLayout.addWidget(self.customerButton, 1, 2, 1, 1)
        spacerItem25 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem25, 1, 5, 1, 1)
        spacerItem26 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem26, 3, 3, 1, 1)
        spacerItem27 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem27, 1, 3, 1, 1)
        spacerItem28 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem28, 3, 5, 1, 1)
        spacerItem29 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem29, 2, 1, 1, 1)
        Homepage.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Homepage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 895, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Homepage.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Homepage)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Homepage.setStatusBar(self.statusbar)

        self.retranslateUi(Homepage)
        QtCore.QMetaObject.connectSlotsByName(Homepage)
        Homepage.setTabOrder(self.customerButton, self.suppliersButton)
        Homepage.setTabOrder(self.suppliersButton, self.ordersButton)
        Homepage.setTabOrder(self.ordersButton, self.pricingButton)
        Homepage.setTabOrder(self.pricingButton, self.billingButton)
        Homepage.setTabOrder(self.billingButton, self.stocksButton)
        Homepage.setTabOrder(self.stocksButton, self.supportButton)
        Homepage.setTabOrder(self.supportButton, self.logoutButton)

    def retranslateUi(self, Homepage):
        Homepage.setWindowTitle(_translate("Homepage", "Homepage", None))
        self.customerLabel.setText(_translate("Homepage", "Customer", None))
        self.userNameLabel.setText(_translate("Homepage", "User Name", None))
        self.varunEnterprisesLabel.setText(_translate("Homepage", "Varun Enterprises", None))
        self.logoutButton.setText(_translate("Homepage", "Logout", None))
        self.supportButton.setText(_translate("Homepage", "Support", None))
        self.billingLabel.setText(_translate("Homepage", "Billing", None))
        self.ordersLabel.setText(_translate("Homepage", "Orders", None))
        self.pricingLabel.setText(_translate("Homepage", "Pricing", None))
        self.stocksLabel.setText(_translate("Homepage", "Stocks", None))
        self.suppliersLabel.setText(_translate("Homepage", "Suppliers", None))

import rec_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Homepage = QtGui.QMainWindow()
    ui = Ui_Homepage()
    ui.setupUi(Homepage)
    Homepage.show()
    sys.exit(app.exec_())

