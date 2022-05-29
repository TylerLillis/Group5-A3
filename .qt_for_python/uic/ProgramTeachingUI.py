# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgramTeachingUI.ui'
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
        MainWindow.resize(967, 598)
        MainWindow.setMinimumSize(QSize(967, 598))
        MainWindow.setMaximumSize(QSize(967, 976))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblOutput = QLabel(self.centralwidget)
        self.lblOutput.setObjectName(u"lblOutput")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblOutput.setFont(font)

        self.verticalLayout_2.addWidget(self.lblOutput)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 948, 956))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnHome = QPushButton(self.scrollAreaWidgetContents)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMinimumSize(QSize(0, 70))

        self.horizontalLayout_2.addWidget(self.btnHome)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(750, 800))
        self.frame.setStyleSheet(u"border-radius: 35px;\n"
"background-color: rgb(3, 32, 74);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 301, 91))
        font1 = QFont()
        font1.setPointSize(40)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 120, 601, 671))
        font2 = QFont()
        font2.setPointSize(15)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(540, 30, 151, 31))
        font3 = QFont()
        font3.setPointSize(20)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.btnBack = QPushButton(self.scrollAreaWidgetContents)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setPointSize(14)
        self.btnBack.setFont(font4)
        self.btnBack.setStyleSheet(u"background-color: rgb(119, 136, 153);\n"
"color: rgb(250, 250, 210);")

        self.horizontalLayout_4.addWidget(self.btnBack)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btnProceed = QPushButton(self.scrollAreaWidgetContents)
        self.btnProceed.setObjectName(u"btnProceed")
        self.btnProceed.setMinimumSize(QSize(0, 50))
        self.btnProceed.setFont(font4)
        self.btnProceed.setStyleSheet(u"background-color: rgb(119, 136, 153);\n"
"color: rgb(250, 250, 210);")

        self.horizontalLayout_4.addWidget(self.btnProceed)

        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 967, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Teaching Section", None))
        self.lblOutput.setText(QCoreApplication.translate("MainWindow", u"Output: None currently", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sub Section", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget velit aliquet sagittis id consectetur purus ut faucibus. Ornare arcu dui vivamus arcu felis bibendum. Vulputate odio ut enim blandit volutpat maecenas. Amet nulla facilisi morbi tempus. Hac habitasse platea dictumst quisque sagittis purus sit amet. Aliquet sagittis id consectetur purus ut faucibus pulvinar elementum integer. Felis eget nunc lobortis mattis aliquam. Netus et malesuada fames ac turpis egestas sed. Faucibus purus in massa tempor nec feugiat nisl. Nullam vehicula ipsum a arcu cursus. Venenatis lectus magna fringilla urna porttitor.\n"
"\n"
"Egestas egestas fringilla phasellus faucibus scelerisque. Diam donec adipiscing tristique risus. Eget nunc lobortis mattis aliquam faucibus. Ultrices sagittis orci a scelerisque purus semper. Aliquet risus feugiat in ante metus dictum at. Ac tincidunt vitae semper quis lectus. Aliquam ultrices sagittis orci a scelerisque purus semper "
                        "eget. Maecenas volutpat blandit aliquam etiam erat velit scelerisque. Tristique senectus et netus et malesuada fames ac turpis. Feugiat scelerisque varius morbi enim nunc faucibus. Quis viverra nibh cras pulvinar mattis nunc sed blandit. Sed vulputate mi sit amet. Senectus et netus et malesuada fames ac turpis egestas sed. Suspendisse sed nisi lacus sed viverra. Nec feugiat nisl pretium fusce. Fermentum iaculis eu non diam phasellus vestibulum lorem sed risus. Aliquam nulla facilisi cras fermentum odio eu feugiat. Egestas congue quisque egestas diam.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Scroll down", None))
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.btnProceed.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
    # retranslateUi

