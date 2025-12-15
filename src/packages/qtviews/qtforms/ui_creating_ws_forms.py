# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_creating_ws_forms.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
    QKeySequenceEdit, QLabel, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1196, 807)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(530, 10, 101, 26))
        self.qtw_data = QTabWidget(Form)
        self.qtw_data.setObjectName(u"qtw_data")
        self.qtw_data.setGeometry(QRect(10, 50, 361, 211))
        self.qw_personal = QWidget()
        self.qw_personal.setObjectName(u"qw_personal")
        self.qtw_data.addTab(self.qw_personal, "")
        self.qw_groups = QWidget()
        self.qw_groups.setObjectName(u"qw_groups")
        self.qtw_data.addTab(self.qw_groups, "")
        self.keySequenceEdit = QKeySequenceEdit(Form)
        self.keySequenceEdit.setObjectName(u"keySequenceEdit")
        self.keySequenceEdit.setGeometry(QRect(30, 440, 113, 21))
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(519, 300, 256, 192))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 550, 213, 29))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout.addWidget(self.dateEdit)


        self.retranslateUi(Form)

        self.qtw_data.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.qtw_data.setTabText(self.qtw_data.indexOf(self.qw_personal), QCoreApplication.translate("Form", u"Tab 1", None))
        self.qtw_data.setTabText(self.qtw_data.indexOf(self.qw_groups), QCoreApplication.translate("Form", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel1112", None))
    # retranslateUi

