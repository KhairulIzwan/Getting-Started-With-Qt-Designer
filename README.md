# Getting-Started-With-Qt-Designer

## Reference
1. [Qt Designer and Python: Build Your GUI Applications Faster](https://realpython.com/qt-designer-python/#connecting-signals-and-slots)
2. [PyQT Basic Tutorial](https://pythonprogramming.net/basic-gui-pyqt-tutorial/)

## Notes

### 1. Installing and Running Qt Designer
1. PyQt4:
	1. sudo apt-get install python-pyqt4
	2. sudo apt-get install qttools-dev-tools
	3. sudo apt-get install qttools-dev
	
2. PyQt5:
	1. sudo apt-get install python3-pyqt5
	2. sudo apt-get install qttools5-dev-tools
	3. sudo apt-get install qttools5-dev
	
### 2. Exporting Design from UI to python file
1. PyQt4:
	1. pyuic4 /home/linux/helloworld.ui -o helloworld.py
	
	**or**
	
	2. pyuic4 -x /home/linux/helloworld.ui -o helloworld.py

2. PyQt5:
	1. pyuic5 /home/linux/helloworld.ui -o helloworld.py

	**or**
	
	2. pyuic5 -x /home/linux/helloworld.ui -o helloworld.py
