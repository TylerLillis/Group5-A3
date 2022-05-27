#Imports required modules
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import *
import sys
import os

#Creates a class for the UI
class Ui(QtWidgets.QMainWindow):

    #Fixes PyQt5's weird DPI scaling for some laptops
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)    
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) 

    def __init__(self):
        super(Ui, self).__init__()
        #Loads the UI file from filename
        uic.loadUi(os.path.join(sys.path[0], "ProgramUI.ui"), self)
        self.show()
        
        #Connect elements to functions
        self.ExamplePushbutton.clicked.connect(self.ExampleClicked)

    #Functions behind UI elements
    global messagebox
    def messagebox():
        msg = QMessageBox()
        msg.setText('Unlocked **Achievement name**')
        msg.setWindowTitle('Achievement')
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def ExampleClicked(self):
        print('Example button was clicked')
        self.ExampleFrame.setStyleSheet("background-color : yellow")
        self.ExamplePushbutton.setStyleSheet("background-color : yellow")
        messagebox()
        self.ExampleFrame.setStyleSheet("background-color : rgb(0, 255, 0);")
        self.ExamplePushbutton.setStyleSheet("background-color : rgb(0, 255, 0);")
        
        
#Creates an instance of the app and window and then executes the program.
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()