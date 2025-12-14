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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

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
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pte_logs = QPlainTextEdit(self.centralwidget)
        self.pte_logs.setObjectName(u"pte_logs")
        self.pte_logs.setUndoRedoEnabled(False)
        self.pte_logs.setReadOnly(True)

        self.gridLayout_2.addWidget(self.pte_logs, 4, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.psb_create_sheets = QPushButton(self.centralwidget)
        self.psb_create_sheets.setObjectName(u"psb_create_sheets")

        self.gridLayout.addWidget(self.psb_create_sheets, 0, 1, 1, 1)

        self.psb_exit = QPushButton(self.centralwidget)
        self.psb_exit.setObjectName(u"psb_exit")

        self.gridLayout.addWidget(self.psb_exit, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.psb_create_protocols = QPushButton(self.centralwidget)
        self.psb_create_protocols.setObjectName(u"psb_create_protocols")

        self.gridLayout.addWidget(self.psb_create_protocols, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_app_title = QLabel(self.centralwidget)
        self.lbl_app_title.setObjectName(u"lbl_app_title")

        self.verticalLayout_2.addWidget(self.lbl_app_title)

        self.lbl_app_version = QLabel(self.centralwidget)
        self.lbl_app_version.setObjectName(u"lbl_app_version")

        self.verticalLayout_2.addWidget(self.lbl_app_version)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 2)

        self.gridLayout_2.setRowStretch(1, 3)
        self.gridLayout_2.setRowStretch(2, 3)
        self.gridLayout_2.setRowStretch(3, 3)
        self.gridLayout_2.setRowStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.psb_create_sheets, self.psb_create_protocols)
        QWidget.setTabOrder(self.psb_create_protocols, self.psb_exit)
        QWidget.setTabOrder(self.psb_exit, self.pte_logs)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.psb_create_sheets.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0432\u0435\u0434\u043e\u043c\u043e\u0441\u0442\u0435\u0439 \u0440\u0430\u0431\u043e\u0442", None))
        self.psb_exit.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0439\u0442\u0438 \u0438\u0437 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.psb_create_protocols.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b\u043e\u0432", None))
        self.lbl_app_title.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0431\u043e\u0447\u0438\u0439 \u0430\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442", None))
        self.lbl_app_version.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0435\u0440\u0441\u0438\u044f \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f: 1.1.1", None))
    # retranslateUi

