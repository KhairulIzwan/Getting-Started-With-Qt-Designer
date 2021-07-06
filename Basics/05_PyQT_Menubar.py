#!/usr/bin/env python

# import the necessary packages
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

#QtGui - Deals with the graphical elements.
#QtCore - other non-GUI essentials.
#QtNetwork - Networking, as you may have guessed.
#QtOpenGL - Allows for the incorporation of OpenGL!
#QtSql - Wrapper for SQL handling.
#QtSvg - support for support vector graphics.
#QtXML - for handling XML data

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQT tuts!")
		self.setWindowIcon(QtGui.QIcon('../../ui/resources/help-content.png'))
		
		extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Leave The App')
		extractAction.triggered.connect(self.close_application)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
        
		self.home()

	def home(self):
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(0,0)
		
	def close_application(self):
		print("whooaaaa so custom!!!")
		sys.exit()
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	GUI.show()
	sys.exit(app.exec_())
