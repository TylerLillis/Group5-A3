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
        self.btnAchievement1.clicked.connect(self.Achievement1Clicked)
        self.btnAchievement2.clicked.connect(self.Achievement2Clicked)
        self.btnAchievement3.clicked.connect(self.Achievement3Clicked)
        self.btnAchievement4.clicked.connect(self.Achievement4Clicked)
        self.btnAchievement5.clicked.connect(self.Achievement5Clicked)
        self.btnAchievement6.clicked.connect(self.Achievement6Clicked)

    #Functions behind UI elements
    global messagebox
    def messagebox():
        msg = QMessageBox()
        msg.setText('Unlocked **Achievement name**')
        msg.setWindowTitle('Achievement')
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def Achievement1Clicked(self):
        self.frmAchievement1.setStyleSheet("border-radius: 15px; border-width: 4px; border-style: solid; border-color: rgb(103, 183, 72); background-color: rgb(103, 183, 72);")
        messagebox()
    def Achievement2Clicked(self):
        self.frmAchievement2.setStyleSheet("border-radius: 15px; border-width: 4px; border-style: solid; border-color: rgb(103, 183, 72); background-color: rgb(103, 183, 72);")
        messagebox()
    def Achievement3Clicked(self):
        self.frmAchievement3.setStyleSheet("border-radius: 15px; border-width: 4px; border-style: solid; border-color: rgb(103, 183, 72); background-color: rgb(103, 183, 72);")
        messagebox()
    def Achievement4Clicked(self):
        self.frmAchievement4.setStyleSheet("border-radius: 15px; border-width: 4px; border-style: solid; border-color: rgb(103, 183, 72); background-color: rgb(103, 183, 72);")
        messagebox()
    def Achievement5Clicked(self):
        self.frmAchievement5.setStyleSheet("border-radius: 15px; border-width: 4px; border-style: solid; border-color: rgb(103, 183, 72); background-color: rgb(103, 183, 72);")
        messagebox()
    def Achievement6Clicked(self):
        self.frmAchievement6.setStyleSheet("border-radius: 15px; border-width: 4px; border-style: solid; border-color: rgb(103, 183, 72); background-color: rgb(103, 183, 72);")
        messagebox()
#Creates an instance of the app and window and then executes the program.
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()