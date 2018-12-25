# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Homepage(object):
    def setupUi(self, Homepage):
        Homepage.setObjectName("Homepage")
        Homepage.resize(895, 511)
        Homepage.setStyleSheet("QMainWindow{\n"
"background-color: rgb(191, 191, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"font-size:28px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(Homepage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.billingButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.billingButton.setStyleSheet("background-image: url(:/Homepage/Homepage/Billing.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
"")
        self.billingButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Homepage/background.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.billingButton.setIcon(icon)
        self.billingButton.setObjectName("billingButton")
        self.gridLayout.addWidget(self.billingButton, 3, 4, 1, 1)
        self.customerLabel = QtWidgets.QLabel(self.centralwidget)
        self.customerLabel.setStyleSheet("font-size: 28px;")
        self.customerLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.customerLabel.setObjectName("customerLabel")
        self.gridLayout.addWidget(self.customerLabel, 2, 2, 1, 1)
        self.ordersButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ordersButton.setStyleSheet("background-image: url(:/Homepage/Homepage/Orders.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
"")
        self.ordersButton.setText("")
        self.ordersButton.setIcon(icon)
        self.ordersButton.setDescription("")
        self.ordersButton.setObjectName("ordersButton")
        self.gridLayout.addWidget(self.ordersButton, 1, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 8, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 8, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 8, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 7, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 7, 1, 1)
        self.userNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.userNameLabel.setStyleSheet("font-size:20px;")
        self.userNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userNameLabel.setObjectName("userNameLabel")
        self.gridLayout.addWidget(self.userNameLabel, 0, 8, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 6, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 8, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 6, 7, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 6, 8, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 6, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 3, 7, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 2, 0, 1, 1)
        self.varunEnterprisesLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.varunEnterprisesLabel.setFont(font)
        self.varunEnterprisesLabel.setStyleSheet("font-size:35px;")
        self.varunEnterprisesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.varunEnterprisesLabel.setObjectName("varunEnterprisesLabel")
        self.gridLayout.addWidget(self.varunEnterprisesLabel, 0, 2, 1, 5)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 8, 8, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 2, 5, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 6, 5, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 6, 3, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 0, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 8, 2, 1, 5)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem22, 2, 3, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem23, 0, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem24, 0, 7, 1, 1)
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setObjectName("logoutButton")
        self.gridLayout.addWidget(self.logoutButton, 8, 7, 1, 1)
        self.supportButton = QtWidgets.QPushButton(self.centralwidget)
        self.supportButton.setObjectName("supportButton")
        self.gridLayout.addWidget(self.supportButton, 8, 1, 1, 1)
        self.billingLabel = QtWidgets.QLabel(self.centralwidget)
        self.billingLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.billingLabel.setObjectName("billingLabel")
        self.gridLayout.addWidget(self.billingLabel, 6, 4, 1, 1)
        self.pricingButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.pricingButton.setStyleSheet("background-image: url(:/Homepage/Homepage/Pricing.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
"")
        self.pricingButton.setText("")
        self.pricingButton.setIcon(icon)
        self.pricingButton.setObjectName("pricingButton")
        self.gridLayout.addWidget(self.pricingButton, 3, 2, 1, 1)
        self.ordersLabel = QtWidgets.QLabel(self.centralwidget)
        self.ordersLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ordersLabel.setObjectName("ordersLabel")
        self.gridLayout.addWidget(self.ordersLabel, 2, 6, 1, 1)
        self.suppliersButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.suppliersButton.setStyleSheet("background-image: url(:/Homepage/Homepage/Supplier.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
"")
        self.suppliersButton.setText("")
        self.suppliersButton.setIcon(icon)
        self.suppliersButton.setObjectName("suppliersButton")
        self.gridLayout.addWidget(self.suppliersButton, 1, 4, 1, 1)
        self.pricingLabel = QtWidgets.QLabel(self.centralwidget)
        self.pricingLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pricingLabel.setObjectName("pricingLabel")
        self.gridLayout.addWidget(self.pricingLabel, 6, 2, 1, 1)
        self.stocksLabel = QtWidgets.QLabel(self.centralwidget)
        self.stocksLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.stocksLabel.setObjectName("stocksLabel")
        self.gridLayout.addWidget(self.stocksLabel, 6, 6, 1, 1)
        self.stocksButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.stocksButton.setStyleSheet("background-image: url(:/Homepage/Homepage/Stock.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
"")
        self.stocksButton.setText("")
        self.stocksButton.setIcon(icon)
        self.stocksButton.setObjectName("stocksButton")
        self.gridLayout.addWidget(self.stocksButton, 3, 6, 1, 1)
        self.suppliersLabel = QtWidgets.QLabel(self.centralwidget)
        self.suppliersLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.suppliersLabel.setObjectName("suppliersLabel")
        self.gridLayout.addWidget(self.suppliersLabel, 2, 4, 1, 1)
        self.customerButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.customerButton.setStyleSheet("background-image: url(:/Homepage/Homepage/Customer.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment:fixed;\n"
"background-size:10px 10px;\n"
"background-position:center;\n"
"background-color: rgb(191, 191, 255);\n"
"")
        self.customerButton.setText("")
        self.customerButton.setIcon(icon)
        self.customerButton.setObjectName("customerButton")
        self.gridLayout.addWidget(self.customerButton, 1, 2, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem25, 1, 5, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem26, 3, 3, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem27, 1, 3, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem28, 3, 5, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem29, 2, 1, 1, 1)
        Homepage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Homepage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 895, 21))
        self.menubar.setObjectName("menubar")
        Homepage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Homepage)
        self.statusbar.setObjectName("statusbar")
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
        _translate = QtCore.QCoreApplication.translate
        Homepage.setWindowTitle(_translate("Homepage", "Homepage"))
        self.customerLabel.setText(_translate("Homepage", "Customer"))
        self.userNameLabel.setText(_translate("Homepage", "User Name"))
        self.varunEnterprisesLabel.setText(_translate("Homepage", "Varun Enterprises"))
        self.logoutButton.setText(_translate("Homepage", "Logout"))
        self.supportButton.setText(_translate("Homepage", "Support"))
        self.billingLabel.setText(_translate("Homepage", "Billing"))
        self.ordersLabel.setText(_translate("Homepage", "Orders"))
        self.pricingLabel.setText(_translate("Homepage", "Pricing"))
        self.stocksLabel.setText(_translate("Homepage", "Stocks"))
        self.suppliersLabel.setText(_translate("Homepage", "Suppliers"))

import rec_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Homepage = QtWidgets.QMainWindow()
    ui = Ui_Homepage()
    ui.setupUi(Homepage)
    Homepage.show()
    sys.exit(app.exec_())

