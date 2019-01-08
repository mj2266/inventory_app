import os
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import QEvent
import re
import pymysql
current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(
        os.path.join(current_dir, "addSupplier.ui")
        )


class addSupplierDialog(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.nameInput.setFocus()
        self.cancelButton.clicked.connect(self.close)
        self.okButton.clicked.connect(self.fieldCheck)
        self.emailInput.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusOut:
            email = self.emailInput.text()
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
            if match is None:
                print("BAD SYNTAX")
        return super(addSupplierDialog, self).eventFilter(obj, event)
    
    def emailCheck(self,email):
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if match is None:
            return False
        return True
            
    def fieldCheck(self):
        name = self.nameInput.text()
        address = self.addressInput.text()
        phone1 = self.phoneNumber1Input.text()
        phone2 = self.phoneNumber2Input.text()
        email = self.emailInput.text()
        if(not self.emailCheck(email)):
            self.errorMsg("Warning","Email address is not valid")
            return
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        query = '''
        INSERT INTO supplier 
        (supp_name, supp_address, supp_contact_1, supp_contact_2, supp_email)
        VALUES (%s, %s, %s, %s, %s)'''
        val = (name, address, phone1, phone2, email)
        try:
            cursor.execute(query,val)
            db.commit()
        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)
            db.rollback()
        db.close()
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

    window = addSupplierDialog()
    
    # the below two lines will make window to come to front
    window.setWindowState(window.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
    window.activateWindow()
    # 
    
    window.show()
    sys.exit(app.exec_())
