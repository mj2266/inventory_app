import os
from PyQt5 import QtGui, uic, QtWidgets
from functools import partial
import rec_rc
import pymysql

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "UI FILES/supp.ui"))

class supplierWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.populate_tree()
        self.searchButton.clicked.connect(self.searchTree)
        self.showAllButton.clicked.connect(self.populate_tree)

        
        
    def populate_tree(self):
        db=pymysql.connect("localhost","root","","ims")
        cursor=db.cursor()
        query = "SELECT * from supplier"
        
        
        try:
            cursor.execute(query)
            data=cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_no =self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_no)
                for column_no,data in enumerate(row_data):
                    self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
            db.commit()
        except:
            db.rollback()
        db.close()
        
        
        
    def searchTree(self):
        searchVal = self.searchInput.text()
        db=pymysql.connect("localhost","root","","ims")
        cursor=db.cursor()
        query = '''SELECT * from supplier
where supp_name like"'''+searchVal+'''%"
or supp_id like"'''+searchVal+'''"
'''
        try:
            cursor.execute(query)
            data=cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_no =self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_no)
                for column_no,data in enumerate(row_data):
                    self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
            db.commit()
        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------",code,msg)

            db.rollback()
        db.close()
        
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
        
    w = supplierWindow()
    w.show()
    sys.exit(app.exec_())