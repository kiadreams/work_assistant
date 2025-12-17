# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stcWdgt_windows = QStackedWidget(self.centralwidget)
        self.stcWdgt_windows.setObjectName(u"stcWdgt_windows")
        self.page_1_main_menu = QWidget()
        self.page_1_main_menu.setObjectName(u"page_1_main_menu")
        self.verticalLayout = QVBoxLayout(self.page_1_main_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_app_title = QLabel(self.page_1_main_menu)
        self.lbl_app_title.setObjectName(u"lbl_app_title")

        self.verticalLayout_2.addWidget(self.lbl_app_title)

        self.lbl_app_version = QLabel(self.page_1_main_menu)
        self.lbl_app_version.setObjectName(u"lbl_app_version")

        self.verticalLayout_2.addWidget(self.lbl_app_version)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.psb_create_sheets = QPushButton(self.page_1_main_menu)
        self.psb_create_sheets.setObjectName(u"psb_create_sheets")

        self.gridLayout.addWidget(self.psb_create_sheets, 0, 1, 1, 1)

        self.psb_exit = QPushButton(self.page_1_main_menu)
        self.psb_exit.setObjectName(u"psb_exit")

        self.gridLayout.addWidget(self.psb_exit, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.psb_create_protocols = QPushButton(self.page_1_main_menu)
        self.psb_create_protocols.setObjectName(u"psb_create_protocols")

        self.gridLayout.addWidget(self.psb_create_protocols, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pte_logs = QPlainTextEdit(self.page_1_main_menu)
        self.pte_logs.setObjectName(u"pte_logs")
        self.pte_logs.setUndoRedoEnabled(False)
        self.pte_logs.setReadOnly(True)

        self.verticalLayout.addWidget(self.pte_logs)

        self.stcWdgt_windows.addWidget(self.page_1_main_menu)
        self.page_2_creating_ws = QWidget()
        self.page_2_creating_ws.setObjectName(u"page_2_creating_ws")
        self.verticalLayout_5 = QVBoxLayout(self.page_2_creating_ws)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_7 = QPushButton(self.page_2_creating_ws)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout.addWidget(self.pushButton_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.psb_groups = QPushButton(self.page_2_creating_ws)
        self.buttonGroup_creating_ws = QButtonGroup(MainWindow)
        self.buttonGroup_creating_ws.setObjectName(u"buttonGroup_creating_ws")
        self.buttonGroup_creating_ws.addButton(self.psb_groups)
        self.psb_groups.setObjectName(u"psb_groups")
        self.psb_groups.setCheckable(True)

        self.verticalLayout_4.addWidget(self.psb_groups)

        self.pushButton_2 = QPushButton(self.page_2_creating_ws)
        self.buttonGroup_creating_ws.addButton(self.pushButton_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.page_2_creating_ws)
        self.buttonGroup_creating_ws.addButton(self.pushButton_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.page_2_creating_ws)
        self.buttonGroup_creating_ws.addButton(self.pushButton_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.page_2_creating_ws)
        self.buttonGroup_creating_ws.addButton(self.pushButton_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.page_2_creating_ws)
        self.buttonGroup_creating_ws.addButton(self.pushButton_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.stackedWidget_2 = QStackedWidget(self.page_2_creating_ws)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 300, 181, 18))
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_2 = QLabel(self.page_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 260, 161, 18))
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_3 = QLabel(self.page_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 320, 161, 18))
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_4 = QLabel(self.page_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 260, 161, 18))
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_5 = QLabel(self.page_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 300, 161, 18))
        self.stackedWidget_2.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_6 = QLabel(self.page_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 270, 161, 18))
        self.stackedWidget_2.addWidget(self.page_8)

        self.horizontalLayout_2.addWidget(self.stackedWidget_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.stcWdgt_windows.addWidget(self.page_2_creating_ws)

        self.verticalLayout_3.addWidget(self.stcWdgt_windows)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.psb_create_sheets, self.psb_create_protocols)
        QWidget.setTabOrder(self.psb_create_protocols, self.psb_exit)
        QWidget.setTabOrder(self.psb_exit, self.pte_logs)

        self.retranslateUi(MainWindow)

        self.stcWdgt_windows.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_app_title.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0431\u043e\u0447\u0438\u0439 \u0430\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442", None))
        self.lbl_app_version.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0435\u0440\u0441\u0438\u044f \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f: 1.1.1", None))
        self.psb_create_sheets.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0432\u0435\u0434\u043e\u043c\u043e\u0441\u0442\u0435\u0439 \u0440\u0430\u0431\u043e\u0442", None))
        self.psb_exit.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0439\u0442\u0438 \u0438\u0437 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.psb_create_protocols.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b\u043e\u0432", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.psb_groups.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0438\u0434\u044b \u0440\u0430\u0431\u043e\u0442", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0430\u043a\u0430\u0437\u044b", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0431\u043e\u0447\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0438\u0434\u044b \u0440\u0430\u0431\u043e\u0442", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0430\u043a\u0430\u0437\u044b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0431\u043e\u0447\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
    # retranslateUi

