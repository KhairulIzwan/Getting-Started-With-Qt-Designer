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
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("PyQT tuts!")
		self.setWindowIcon(QtGui.QIcon('../ui/resources/help-content.png'))
		
		extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Leave The App')
		extractAction.triggered.connect(self.close_application)

		openEditor = QtGui.QAction("&Editor", self)
		openEditor.setShortcut("Ctrl+E")
		openEditor.setStatusTip('Open Editor')
		openEditor.triggered.connect(self.editor)
        
		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		
		editorMenu = mainMenu.addMenu("&Editor")
		editorMenu.addAction(openEditor)
        
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
		
		fontChoice = QtGui.QAction(
			QtGui.QIcon('../ui/resources/help-content.png'), 
			'Font', 
			self)
		fontChoice.triggered.connect(self.font_choice)
		
		#self.toolBar = self.addToolBar("Font")
		self.toolBar.addAction(fontChoice)
		
		color = QtGui.QColor(25, 255, 0)
		
		fontColor = QtGui.QAction('Font bg Color', self)
		fontColor.triggered.connect(self.color_picker)

		self.toolBar.addAction(fontColor)
		
		self.checkBox = QtGui.QCheckBox('Enlarge Window', self)
		self.checkBox.move(100, 25)
		self.checkBox.stateChanged.connect(self.enlarge_window)
		# depending on what you want the default to be.
		#self.checkBox.toggle()

		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(200, 80, 250, 20)

		self.btn = QtGui.QPushButton("Download",self)
		self.btn.move(200,120)
		self.btn.clicked.connect(self.download)
		
		print(self.style().objectName())
		self.styleChoice = QtGui.QLabel("Windows Vista", self)

		comboBox = QtGui.QComboBox(self)
		comboBox.addItem("motif")
		comboBox.addItem("Windows")
		comboBox.addItem("cde")
		comboBox.addItem("Plastique")
		comboBox.addItem("Cleanlooks")
		comboBox.addItem("windowsvista")
		comboBox.move(50, 250)

		self.styleChoice.move(50,150)
		comboBox.activated[str].connect(self.style_choice)
		
		cal = QtGui.QCalendarWidget(self)
		cal.move(200,200)
		cal.resize(200,200)

	def color_picker(self):
		color = QtGui.QColorDialog.getColor()
		self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())
		
	def editor(self):
		self.textEdit = QtGui.QTextEdit()
		self.setCentralWidget(self.textEdit)
        
	def font_choice(self):
		font, valid = QtGui.QFontDialog.getFont()
		
		if valid:
			self.styleChoice.setFont(font)
			self.checkBox.setFont(font)
            
	def style_choice(self, text):
		self.styleChoice.setText(text)
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))


	def download(self):
		self.completed = 0

		while self.completed < 100:
			self.completed += 0.0001
			self.progress.setValue(self.completed)

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
