import os
from PyQt5 import QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QInputDialog
import rec_rc
from addCustomer import addCustomerDialog
import pymysql
current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "billing.ui"))


class billingWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.Search.clicked.connect(self.searchCust)
        self.addContact.clicked.connect(self.addCustomer)
        #self.addItem.clicked.connect(self.addItem)

        self.populateCombo1()
        self.populateCombo2()
        self.cbox1.currentIndexChanged.connect(self.populateCombo2)

    def addCustomer(self):
        self.addCust = addCustomerDialog()
        self.addCust.exec_()
        self.display = self.addCust.AdressInput.text()

    def populateCombo1(self):
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        query = "SELECT category_name from category"

        try:
            cursor.execute(query)
            comboBox1Content = cursor.fetchall()
            self.cbox1.clear()
            for i in range(len(comboBox1Content)):
                self.cbox1.addItem("")
                self.cbox1.setItemText(i, comboBox1Content[i][0])

        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)

        db.close()

    def populateCombo2(self):
        cbox1Text = self.cbox1.currentText()
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        query ='''
        select item_name 
        from items, category 
        where item_category_id = category_id and category_name = "%s"
        '''%cbox1Text
        try:
            cursor.execute(query)
            comboBox2Content = cursor.fetchall()
            self.cbox2.clear()
            for i in range(len(comboBox2Content)):
                self.cbox2.addItem("")
                self.cbox2.setItemText(i, comboBox2Content[i][0])

        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)
        db.close()
        
    def searchCust(self):
        contact = self.contact.text()
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
       
        try:
            cursor.execute("select C_address from Customer_info where C_contact = %s",contact)
            data = cursor.fetchall()
            self.display.setPlainText(data[0][0])
        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)
        db.close()
        
""" def addItem(self):
        cbox2Text = self.cbox2.currentText()
        db = pymysql.connect("localhost", "root", "", "ims")
        curso r= db.cursor()
        
        try:
            cursor.execute("select item_name, item_price from items ")"""
        
        
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = billingWindow()
    w.show()
    sys.exit(app.exec_())
