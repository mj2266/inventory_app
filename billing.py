# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 09:56:16 2018

@author: NIHARIKA CHATURVEDI
"""

import os
from PyQt5 import QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QInputDialog
from functools import partial
import rec_rc

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "UI FILES/billing.ui"))

class billingWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.addContact.clicked.connect(self.createInputDialog)
        
        
    def createInputDialog(self):
          text,ok = QInputDialog.getText(self,"input dialog","Enter New Customer" )
          if ok:
              self.display.setText(str(text))
        
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
        
    w = billingWindow()
    w.show()
    sys.exit(app.exec_())