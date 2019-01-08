import os
from PyQt5 import QtGui, uic, QtWidgets
from functools import partial
import rec_rc

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "UI FILES/addCustomer.ui"))

class addCustomerDialog(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        
        self.okButton.clicked.connect(self.close)
        
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
        
    w = addCustomerDialog()
    w.show()
    sys.exit(app.exec_())

