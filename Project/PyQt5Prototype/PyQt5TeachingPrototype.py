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
        uic.loadUi(os.path.join(sys.path[0], "ProgramTeachingUI.ui"), self)
        self.show()
        
        #Connect elements to functions
        self.btnHome.clicked.connect(self.HomeClicked)
        self.btnBack.clicked.connect(self.BackClicked)
        self.btnProceed.clicked.connect(self.ProceedClicked)

    #Functions behind UI elements
    def HomeClicked(self):
        self.lblOutput.setText('Output: Home was clicked')

    def BackClicked(self):
        self.lblOutput.setText('Output: Back was clicked')

    def ProceedClicked(self):
        self.lblOutput.setText('Output: Proceed was clicked')



#Creates an instance of the app and window and then executes the program.
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()