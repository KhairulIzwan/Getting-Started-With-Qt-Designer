#!/usr/bin/env python

# import the necessary packages
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(0, 0, 500, 300)
window.setWindowTitle("PyQT Tuts!")
window.show()

sys.exit(app.exec_())
