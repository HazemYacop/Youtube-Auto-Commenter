# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserInterface.ui'
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
        MainWindow.resize(1008, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(132, 250, 176, 255), stop:1 rgba(143, 211, 244, 255));\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.MainPage = QWidget()
        self.MainPage.setObjectName(u"MainPage")
        self.gridLayout_4 = QGridLayout(self.MainPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.InputsLayout = QVBoxLayout()
        self.InputsLayout.setSpacing(30)
        self.InputsLayout.setObjectName(u"InputsLayout")
        self.InputsLayout.setContentsMargins(100, -1, 100, 30)
        self.Spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.InputsLayout.addItem(self.Spacer)

        self.SheetLayout = QHBoxLayout()
        self.SheetLayout.setSpacing(0)
        self.SheetLayout.setObjectName(u"SheetLayout")
        self.SheetLabel = QLabel(self.MainPage)
        self.SheetLabel.setObjectName(u"SheetLabel")
        self.SheetLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")

        self.SheetLayout.addWidget(self.SheetLabel)

        self.Sheet = QLineEdit(self.MainPage)
        self.Sheet.setObjectName(u"Sheet")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sheet.sizePolicy().hasHeightForWidth())
        self.Sheet.setSizePolicy(sizePolicy)
        self.Sheet.setMinimumSize(QSize(300, 35))
        self.Sheet.setMaximumSize(QSize(16777215, 16777215))
        self.Sheet.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background: transparent;")
        self.Sheet.setAlignment(Qt.AlignCenter)

        self.SheetLayout.addWidget(self.Sheet)


        self.InputsLayout.addLayout(self.SheetLayout)

        self.WorksheetLayout = QHBoxLayout()
        self.WorksheetLayout.setSpacing(0)
        self.WorksheetLayout.setObjectName(u"WorksheetLayout")
        self.WorksheetLabel = QLabel(self.MainPage)
        self.WorksheetLabel.setObjectName(u"WorksheetLabel")
        self.WorksheetLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")

        self.WorksheetLayout.addWidget(self.WorksheetLabel)

        self.Worksheet = QLineEdit(self.MainPage)
        self.Worksheet.setObjectName(u"Worksheet")
        sizePolicy.setHeightForWidth(self.Worksheet.sizePolicy().hasHeightForWidth())
        self.Worksheet.setSizePolicy(sizePolicy)
        self.Worksheet.setMinimumSize(QSize(300, 35))
        self.Worksheet.setMaximumSize(QSize(16777215, 16777215))
        self.Worksheet.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background: transparent;")
        self.Worksheet.setAlignment(Qt.AlignCenter)

        self.WorksheetLayout.addWidget(self.Worksheet)


        self.InputsLayout.addLayout(self.WorksheetLayout)

        self.StartFromRowLayout = QHBoxLayout()
        self.StartFromRowLayout.setSpacing(0)
        self.StartFromRowLayout.setObjectName(u"StartFromRowLayout")
        self.StartFromRowLabel = QLabel(self.MainPage)
        self.StartFromRowLabel.setObjectName(u"StartFromRowLabel")
        self.StartFromRowLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")

        self.StartFromRowLayout.addWidget(self.StartFromRowLabel)

        self.StartFromRow = QLineEdit(self.MainPage)
        self.StartFromRow.setObjectName(u"StartFromRow")
        sizePolicy.setHeightForWidth(self.StartFromRow.sizePolicy().hasHeightForWidth())
        self.StartFromRow.setSizePolicy(sizePolicy)
        self.StartFromRow.setMinimumSize(QSize(300, 35))
        self.StartFromRow.setMaximumSize(QSize(16777215, 16777215))
        self.StartFromRow.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background: transparent;")
        self.StartFromRow.setAlignment(Qt.AlignCenter)

        self.StartFromRowLayout.addWidget(self.StartFromRow)


        self.InputsLayout.addLayout(self.StartFromRowLayout)

        self.Spacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.InputsLayout.addItem(self.Spacer_2)


        self.gridLayout_4.addLayout(self.InputsLayout, 0, 0, 1, 1)

        self.NextToChromeProfilesLayout = QHBoxLayout()
        self.NextToChromeProfilesLayout.setObjectName(u"NextToChromeProfilesLayout")
        self.NextToChromeProfilesLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.NextToChromeProfilesLayout.addItem(self.Spacer_3)

        self.NextToChromeProfilesButtonLayout = QVBoxLayout()
        self.NextToChromeProfilesButtonLayout.setObjectName(u"NextToChromeProfilesButtonLayout")
        self.HowDoesItWorkButton = QPushButton(self.MainPage)
        self.HowDoesItWorkButton.setObjectName(u"HowDoesItWorkButton")
        self.HowDoesItWorkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.HowDoesItWorkButton.setStyleSheet(u"color:rgb(0, 0, 255);\n"
"font: 9pt \"MS Sans Serif\";\n"
"text-decoration: underline;")

        self.NextToChromeProfilesButtonLayout.addWidget(self.HowDoesItWorkButton)

        self.NextToChromeProfilesPageButton = QPushButton(self.MainPage)
        self.NextToChromeProfilesPageButton.setObjectName(u"NextToChromeProfilesPageButton")
        self.NextToChromeProfilesPageButton.setMinimumSize(QSize(300, 40))
        self.NextToChromeProfilesPageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.NextToChromeProfilesPageButton.setStyleSheet(u"QPushButton#NextToChromeProfilesPageButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#NextToChromeProfilesPageButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.NextToChromeProfilesButtonLayout.addWidget(self.NextToChromeProfilesPageButton)


        self.NextToChromeProfilesLayout.addLayout(self.NextToChromeProfilesButtonLayout)

        self.Spacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.NextToChromeProfilesLayout.addItem(self.Spacer_4)


        self.gridLayout_4.addLayout(self.NextToChromeProfilesLayout, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.MainPage)
        self.ChromeProfilesPage = QWidget()
        self.ChromeProfilesPage.setObjectName(u"ChromeProfilesPage")
        self.gridLayout_5 = QGridLayout(self.ChromeProfilesPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Spacer_15 = QSpacerItem(20, 22, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.Spacer_15, 0, 0, 1, 1)

        self.ChromeProfileLayout = QVBoxLayout()
        self.ChromeProfileLayout.setSpacing(50)
        self.ChromeProfileLayout.setObjectName(u"ChromeProfileLayout")
        self.ChromeProfileLayout.setContentsMargins(-1, 20, -1, 20)
        self.ChromeProfileLabel = QLabel(self.ChromeProfilesPage)
        self.ChromeProfileLabel.setObjectName(u"ChromeProfileLabel")
        self.ChromeProfileLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.ChromeProfileLabel.setAlignment(Qt.AlignCenter)

        self.ChromeProfileLayout.addWidget(self.ChromeProfileLabel)

        self.ChromeProfile = QLineEdit(self.ChromeProfilesPage)
        self.ChromeProfile.setObjectName(u"ChromeProfile")
        sizePolicy.setHeightForWidth(self.ChromeProfile.sizePolicy().hasHeightForWidth())
        self.ChromeProfile.setSizePolicy(sizePolicy)
        self.ChromeProfile.setMinimumSize(QSize(300, 35))
        self.ChromeProfile.setMaximumSize(QSize(16777215, 16777215))
        self.ChromeProfile.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background: transparent;")
        self.ChromeProfile.setAlignment(Qt.AlignCenter)

        self.ChromeProfileLayout.addWidget(self.ChromeProfile)

        self.OpenChromeProfileButtonLayout = QHBoxLayout()
        self.OpenChromeProfileButtonLayout.setObjectName(u"OpenChromeProfileButtonLayout")
        self.Spacer_17 = QSpacerItem(138, 34, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.OpenChromeProfileButtonLayout.addItem(self.Spacer_17)

        self.OpenChromeProfileButton = QPushButton(self.ChromeProfilesPage)
        self.OpenChromeProfileButton.setObjectName(u"OpenChromeProfileButton")
        self.OpenChromeProfileButton.setMinimumSize(QSize(300, 40))
        self.OpenChromeProfileButton.setMaximumSize(QSize(16777215, 16777215))
        self.OpenChromeProfileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.OpenChromeProfileButton.setStyleSheet(u"QPushButton#OpenChromeProfileButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#OpenChromeProfileButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.OpenChromeProfileButtonLayout.addWidget(self.OpenChromeProfileButton)

        self.Spacer_18 = QSpacerItem(138, 34, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.OpenChromeProfileButtonLayout.addItem(self.Spacer_18)


        self.ChromeProfileLayout.addLayout(self.OpenChromeProfileButtonLayout)


        self.gridLayout_5.addLayout(self.ChromeProfileLayout, 1, 0, 1, 1)

        self.Spacer_16 = QSpacerItem(20, 254, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.Spacer_16, 2, 0, 1, 1)

        self.NextToShareLayout = QHBoxLayout()
        self.NextToShareLayout.setObjectName(u"NextToShareLayout")
        self.NextToShareLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.NextToShareLayout.addItem(self.Spacer_5)

        self.BackToMainPageButton = QPushButton(self.ChromeProfilesPage)
        self.BackToMainPageButton.setObjectName(u"BackToMainPageButton")
        self.BackToMainPageButton.setMinimumSize(QSize(300, 40))
        self.BackToMainPageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackToMainPageButton.setStyleSheet(u"QPushButton#BackToMainPageButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#BackToMainPageButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.NextToShareLayout.addWidget(self.BackToMainPageButton)

        self.NextToSharePageButton = QPushButton(self.ChromeProfilesPage)
        self.NextToSharePageButton.setObjectName(u"NextToSharePageButton")
        self.NextToSharePageButton.setMinimumSize(QSize(300, 40))
        self.NextToSharePageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.NextToSharePageButton.setStyleSheet(u"QPushButton#NextToSharePageButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#NextToSharePageButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.NextToShareLayout.addWidget(self.NextToSharePageButton)

        self.Spacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.NextToShareLayout.addItem(self.Spacer_6)


        self.gridLayout_5.addLayout(self.NextToShareLayout, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.ChromeProfilesPage)
        self.ShareEmailPage = QWidget()
        self.ShareEmailPage.setObjectName(u"ShareEmailPage")
        self.gridLayout_3 = QGridLayout(self.ShareEmailPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Spacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.Spacer_8, 0, 0, 1, 1)

        self.ShareEmailLayout = QVBoxLayout()
        self.ShareEmailLayout.setSpacing(60)
        self.ShareEmailLayout.setObjectName(u"ShareEmailLayout")
        self.ShareEmailLabel = QLabel(self.ShareEmailPage)
        self.ShareEmailLabel.setObjectName(u"ShareEmailLabel")
        self.ShareEmailLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.ShareEmailLabel.setAlignment(Qt.AlignCenter)

        self.ShareEmailLayout.addWidget(self.ShareEmailLabel)

        self.CopyEmailButtonLayout = QHBoxLayout()
        self.CopyEmailButtonLayout.setObjectName(u"CopyEmailButtonLayout")
        self.Spacer_19 = QSpacerItem(37, 37, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.CopyEmailButtonLayout.addItem(self.Spacer_19)

        self.EmailCopiedSuccessfullyLayout = QVBoxLayout()
        self.EmailCopiedSuccessfullyLayout.setSpacing(15)
        self.EmailCopiedSuccessfullyLayout.setObjectName(u"EmailCopiedSuccessfullyLayout")
        self.CopyEmailButton = QPushButton(self.ShareEmailPage)
        self.CopyEmailButton.setObjectName(u"CopyEmailButton")
        self.CopyEmailButton.setMinimumSize(QSize(300, 40))
        self.CopyEmailButton.setMaximumSize(QSize(16777215, 16777215))
        self.CopyEmailButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.CopyEmailButton.setStyleSheet(u"QPushButton#CopyEmailButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#CopyEmailButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.EmailCopiedSuccessfullyLayout.addWidget(self.CopyEmailButton)

        self.EmailCopiedSuccessfullyLabel = QLabel(self.ShareEmailPage)
        self.EmailCopiedSuccessfullyLabel.setObjectName(u"EmailCopiedSuccessfullyLabel")
        self.EmailCopiedSuccessfullyLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 11pt \"Segoe UI Black\";")
        self.EmailCopiedSuccessfullyLabel.setAlignment(Qt.AlignCenter)

        self.EmailCopiedSuccessfullyLayout.addWidget(self.EmailCopiedSuccessfullyLabel)


        self.CopyEmailButtonLayout.addLayout(self.EmailCopiedSuccessfullyLayout)

        self.Spacer_20 = QSpacerItem(37, 37, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.CopyEmailButtonLayout.addItem(self.Spacer_20)


        self.ShareEmailLayout.addLayout(self.CopyEmailButtonLayout)


        self.gridLayout_3.addLayout(self.ShareEmailLayout, 1, 0, 1, 1)

        self.Spacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.Spacer_7, 2, 0, 1, 1)

        self.StartLayout = QHBoxLayout()
        self.StartLayout.setObjectName(u"StartLayout")
        self.StartLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StartLayout.addItem(self.Spacer_10)

        self.BackToMesaagePageButton = QPushButton(self.ShareEmailPage)
        self.BackToMesaagePageButton.setObjectName(u"BackToMesaagePageButton")
        self.BackToMesaagePageButton.setMinimumSize(QSize(300, 40))
        self.BackToMesaagePageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackToMesaagePageButton.setStyleSheet(u"QPushButton#BackToMesaagePageButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#BackToMesaagePageButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.StartLayout.addWidget(self.BackToMesaagePageButton)

        self.StartButton = QPushButton(self.ShareEmailPage)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setMinimumSize(QSize(300, 40))
        self.StartButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.StartButton.setStyleSheet(u"QPushButton#StartButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#StartButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.StartLayout.addWidget(self.StartButton)

        self.Spacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StartLayout.addItem(self.Spacer_9)


        self.gridLayout_3.addLayout(self.StartLayout, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.ShareEmailPage)
        self.StatusPage = QWidget()
        self.StatusPage.setObjectName(u"StatusPage")
        self.gridLayout_2 = QGridLayout(self.StatusPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.BackButtonLayout = QHBoxLayout()
        self.BackButtonLayout.setObjectName(u"BackButtonLayout")
        self.BackButtonLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BackButtonLayout.addItem(self.Spacer_11)

        self.BackButton = QPushButton(self.StatusPage)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setMinimumSize(QSize(300, 40))
        self.BackButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackButton.setStyleSheet(u"QPushButton#BackButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#BackButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.BackButtonLayout.addWidget(self.BackButton)

        self.Spacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BackButtonLayout.addItem(self.Spacer_12)


        self.gridLayout_2.addLayout(self.BackButtonLayout, 4, 0, 1, 1)

        self.Spacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.Spacer_13, 0, 0, 1, 1)

        self.StatusLayout = QVBoxLayout()
        self.StatusLayout.setSpacing(30)
        self.StatusLayout.setObjectName(u"StatusLayout")
        self.WorkingLabel = QLabel(self.StatusPage)
        self.WorkingLabel.setObjectName(u"WorkingLabel")
        self.WorkingLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.WorkingLabel.setAlignment(Qt.AlignCenter)

        self.StatusLayout.addWidget(self.WorkingLabel)

        self.SheetStatusLabel = QLabel(self.StatusPage)
        self.SheetStatusLabel.setObjectName(u"SheetStatusLabel")
        self.SheetStatusLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.SheetStatusLabel.setAlignment(Qt.AlignCenter)

        self.StatusLayout.addWidget(self.SheetStatusLabel)

        self.WorksheetStatusLabel = QLabel(self.StatusPage)
        self.WorksheetStatusLabel.setObjectName(u"WorksheetStatusLabel")
        self.WorksheetStatusLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.WorksheetStatusLabel.setAlignment(Qt.AlignCenter)

        self.StatusLayout.addWidget(self.WorksheetStatusLabel)

        self.StartFromRowStatusLabel = QLabel(self.StatusPage)
        self.StartFromRowStatusLabel.setObjectName(u"StartFromRowStatusLabel")
        self.StartFromRowStatusLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.StartFromRowStatusLabel.setAlignment(Qt.AlignCenter)

        self.StatusLayout.addWidget(self.StartFromRowStatusLabel)

        self.VideosFinishedStatusLabel = QLabel(self.StatusPage)
        self.VideosFinishedStatusLabel.setObjectName(u"VideosFinishedStatusLabel")
        self.VideosFinishedStatusLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.VideosFinishedStatusLabel.setAlignment(Qt.AlignCenter)

        self.StatusLayout.addWidget(self.VideosFinishedStatusLabel)


        self.gridLayout_2.addLayout(self.StatusLayout, 1, 0, 1, 1)

        self.Spacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.Spacer_14, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.StatusPage)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SheetLabel.setText(QCoreApplication.translate("MainWindow", u"Sheet :", None))
        self.Sheet.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.WorksheetLabel.setText(QCoreApplication.translate("MainWindow", u"Worksheet :", None))
        self.Worksheet.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.StartFromRowLabel.setText(QCoreApplication.translate("MainWindow", u"Start From Row :", None))
        self.StartFromRow.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.HowDoesItWorkButton.setText(QCoreApplication.translate("MainWindow", u"How does it work ?", None))
        self.NextToChromeProfilesPageButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.ChromeProfileLabel.setText(QCoreApplication.translate("MainWindow", u"Chrome Profile :", None))
        self.ChromeProfile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.OpenChromeProfileButton.setText(QCoreApplication.translate("MainWindow", u"Open Chrome Profile", None))
        self.BackToMainPageButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.NextToSharePageButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.ShareEmailLabel.setText(QCoreApplication.translate("MainWindow", u"Please Share The Program's Email to the sheet :", None))
        self.CopyEmailButton.setText(QCoreApplication.translate("MainWindow", u"Copy Email", None))
        self.EmailCopiedSuccessfullyLabel.setText("")
        self.BackToMesaagePageButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.BackButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.WorkingLabel.setText(QCoreApplication.translate("MainWindow", u"Working ...", None))
        self.SheetStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Sheet :", None))
        self.WorksheetStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Worksheet :", None))
        self.StartFromRowStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Start From Row :", None))
        self.VideosFinishedStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Videos Finished :", None))
    # retranslateUi

