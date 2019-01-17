import os
from PyQt5 import QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import rec_rc
import pymysql

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "addCustomer.ui"))


class addCustomerDialog(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.CancelButton.clicked.connect(self.close)
        self.OkButton.clicked.connect(self.insertData)
        
    def insertData(self):
        name = self.nameInput.text()
        phoneNum = self.phoneNumber1Input.text()
        addr = self.AdressInput.toPlainText()
        try:
            phoneNum = int(phoneNum)
        except:
            QMessageBox.about(self,'Alert!','Enter numberic contact number only')
        
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
       
        try:
            cursor.execute( "INSERT INTO CUSTOMER_INFO(C_NAME,C_CONTACT,C_ADDRESS) VALUES (%s,%s,%s)",(name,phoneNum,addr))
            db.commit()
            QMessageBox.about(self,'Entry','data inserted successfully')     
        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)
            db.rollback()
        db.close()
        self.close()
        
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    w = addCustomerDialog()
    w.show()
    sys.exit(app.exec_())

