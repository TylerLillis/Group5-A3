# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgramTestingUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(809, 599)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Option1 = QPushButton(self.centralwidget)
        self.Option1.setObjectName(u"Option1")
        self.Option1.setGeometry(QRect(72, 340, 641, 51))
        self.Option2 = QPushButton(self.centralwidget)
        self.Option2.setObjectName(u"Option2")
        self.Option2.setGeometry(QRect(72, 427, 641, 51))
        self.answer = QLabel(self.centralwidget)
        self.answer.setObjectName(u"answer")
        self.answer.setGeometry(QRect(320, 220, 321, 111))
        self.Question = QLabel(self.centralwidget)
        self.Question.setObjectName(u"Question")
        self.Question.setGeometry(QRect(50, 40, 691, 201))
        self.Question.setScaledContents(False)
        self.Question.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 809, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Option1.setText(QCoreApplication.translate("MainWindow", u"Option 1", None))
        self.Option2.setText(QCoreApplication.translate("MainWindow", u"Option 2", None))
        self.answer.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.Question.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span></p></body></html>", None))
    # retranslateUi

