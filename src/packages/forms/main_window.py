# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(743, 521)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0.128, y1:0.514, x2:0.530911, y2:0.644, stop:0 rgba(62, 220, 250, 255), stop:0.731884 rgba(153, 193, 197, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(673, 0))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_title_of_version = QLabel(self.centralwidget)
        self.label_title_of_version.setObjectName(u"label_title_of_version")
        font = QFont()
        font.setPointSize(9)
        self.label_title_of_version.setFont(font)
        self.label_title_of_version.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label_title_of_version)

        self.label_of_version = QLabel(self.centralwidget)
        self.label_of_version.setObjectName(u"label_of_version")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label_of_version.sizePolicy().hasHeightForWidth())
        self.label_of_version.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        self.label_of_version.setFont(font1)
        self.label_of_version.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label_of_version)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_create_sheets = QPushButton(self.centralwidget)
        self.pushButton_create_sheets.setObjectName(u"pushButton_create_sheets")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(15)
        sizePolicy1.setHeightForWidth(self.pushButton_create_sheets.sizePolicy().hasHeightForWidth())
        self.pushButton_create_sheets.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setWeight(QFont.DemiBold)
        font2.setItalic(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.pushButton_create_sheets.setFont(font2)
        self.pushButton_create_sheets.setStyleSheet(u"border-color: rgb(119, 118, 123);\n"
"background-color: rgb(32, 111, 208);\n"
"background-color: rgb(32, 155, 208);")

        self.verticalLayout.addWidget(self.pushButton_create_sheets)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_exit = QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setWeight(QFont.DemiBold)
        self.pushButton_exit.setFont(font3)
        self.pushButton_exit.setStyleSheet(u"border-color: rgb(119, 118, 123);\n"
"background-color: rgb(32, 111, 208);\n"
"background-color: rgb(32, 155, 208);")

        self.verticalLayout.addWidget(self.pushButton_exit)


        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.label_title_app = QLabel(self.centralwidget)
        self.label_title_app.setObjectName(u"label_title_app")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setUnderline(True)
        font4.setStrikeOut(False)
        self.label_title_app.setFont(font4)
        self.label_title_app.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title_app.setIndent(-1)

        self.gridLayout.addWidget(self.label_title_app, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_exit.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title_of_version.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f:", None))
        self.label_of_version.setText("")
        self.pushButton_create_sheets.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0417\u0414\u0410\u0422\u042c \u0412\u0415\u0414\u041e\u041c\u041e\u0421\u0422\u042c \u0420\u0410\u0411\u041e\u0422", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u042b\u0419\u0422\u0418 \u0418\u0417 \u041f\u0420\u0418\u041b\u041e\u0416\u0415\u041d\u0418\u042f", None))
        self.label_title_app.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#3584e4;\">\u0420\u0410\u0411\u041e\u0427\u0418\u0419 \u0410\u0421\u0421\u0418\u0421\u0422\u0415\u041d\u0422</span></p></body></html>", None))
    # retranslateUi

