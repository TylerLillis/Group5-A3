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
        uic.loadUi(os.path.join(sys.path[0], "ProgramTestingUI.ui"), self)
        self.show()

        #Connect elements to functions
        self.Option1.clicked.connect(self.Option1Clicked)
        self.Option2.clicked.connect(self.Option2Clicked)
                                     
    def Option1Clicked(self):
        self.answer.setText("Option 1 was clicked")


    def Option2Clicked(self):
        self.answer.setText("Option 2 was clicked")




#Creates an instance of the app and window and then executes the program.
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
