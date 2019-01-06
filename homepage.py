import os
from PyQt5 import QtGui, uic, QtWidgets
from functools import partial
import rec_rc

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "UI FILES/homepage.ui"))

class homepageWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = homepageWindow()
    w.show()
    sys.exit(app.exec_())
    