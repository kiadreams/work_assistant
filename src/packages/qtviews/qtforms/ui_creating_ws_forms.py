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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QCommandLinkButton,
    QDateEdit, QDial, QDialogButtonBox, QKeySequenceEdit,
    QLabel, QLayout, QPushButton, QRadioButton,
    QScrollBar, QSizePolicy, QSlider, QTabWidget,
    QToolBox, QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(693, 510)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(530, 10, 101, 26))
        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(190, 290, 112, 23))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 380, 81, 26))
        self.qtw_data = QTabWidget(Form)
        self.qtw_data.setObjectName(u"qtw_data")
        self.qtw_data.setGeometry(QRect(10, 50, 361, 211))
        self.qw_personal = QWidget()
        self.qw_personal.setObjectName(u"qw_personal")
        self.qtw_data.addTab(self.qw_personal, "")
        self.qw_groups = QWidget()
        self.qw_groups.setObjectName(u"qw_groups")
        self.qtw_data.addTab(self.qw_groups, "")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 310, 49, 16))
        self.toolBox = QToolBox(Form)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(390, 120, 271, 114))
        self.toolBox.setMinimumSize(QSize(271, 0))
        self.toolBox.setMaximumSize(QSize(16777215, 114))
        self.toolBoxPage1 = QWidget()
        self.toolBoxPage1.setObjectName(u"toolBoxPage1")
        self.toolBox.addItem(self.toolBoxPage1, u"")
        self.toolBoxPage2 = QWidget()
        self.toolBoxPage2.setObjectName(u"toolBoxPage2")
        self.toolBox.addItem(self.toolBoxPage2, u"")
        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(180, 370, 160, 16))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.verticalSlider = QSlider(Form)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(420, 300, 16, 160))
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.verticalScrollBar = QScrollBar(Form)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(510, 260, 16, 160))
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)
        self.horizontalScrollBar = QScrollBar(Form)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(150, 410, 160, 16))
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)
        self.keySequenceEdit = QKeySequenceEdit(Form)
        self.keySequenceEdit.setObjectName(u"keySequenceEdit")
        self.keySequenceEdit.setGeometry(QRect(30, 440, 113, 21))
        self.dial = QDial(Form)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(250, 400, 50, 64))
        self.toolButton = QToolButton(Form)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(470, 340, 21, 22))
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(470, 380, 98, 24))
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(470, 420, 84, 24))
        self.commandLinkButton = QCommandLinkButton(Form)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(470, 300, 172, 41))
        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(170, 460, 168, 26))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.retranslateUi(Form)

        self.qtw_data.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.qtw_data.setTabText(self.qtw_data.indexOf(self.qw_personal), QCoreApplication.translate("Form", u"Tab 1", None))
        self.qtw_data.setTabText(self.qtw_data.indexOf(self.qw_groups), QCoreApplication.translate("Form", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1), "")
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2), "")
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Form", u"CommandLinkButton", None))
    # retranslateUi

