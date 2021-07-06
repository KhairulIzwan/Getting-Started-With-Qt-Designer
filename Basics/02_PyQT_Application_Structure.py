#!/usr/bin/env python

# import the necessary packages
import sys
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQT tuts!")
		self.setWindowIcon(QtGui.QIcon('../../ui/resources/help-content.png'))

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	GUI.show()
	sys.exit(app.exec_())
