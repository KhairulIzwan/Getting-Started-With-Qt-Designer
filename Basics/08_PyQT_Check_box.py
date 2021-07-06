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
		self.setWindowIcon(QtGui.QIcon('../ui/resources/help-content.png'))
		
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
		btn.move(0,100)
		
		extractAction = QtGui.QAction(QtGui.QIcon('../ui/resources/help-content.png'), 'Flee the Scene', self)
		extractAction.triggered.connect(self.close_application)

		self.toolBar = self.addToolBar("Extraction")
		self.toolBar.addAction(extractAction)
		
		checkBox = QtGui.QCheckBox('Enlarge Window', self)
		checkBox.move(100, 25)
		checkBox.stateChanged.connect(self.enlarge_window)
		# depending on what you want the default to be.
		#checkBox.toggle()

	def enlarge_window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50,50, 1000, 600)
		else:
			self.setGeometry(50, 50, 500, 300)
            
	def close_application(self):
		choice = QtGui.QMessageBox.question(
				self, 'Extract!',
				"Get into the chopper?",
				QtGui.QMessageBox.Yes |QtGui.QMessageBox.No)
				
		if choice == QtGui.QMessageBox.Yes:
			print("Extracting Naaaaaaoooww!!!!")
			sys.exit()
		else:
			pass
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	GUI.show()
	sys.exit(app.exec_())
