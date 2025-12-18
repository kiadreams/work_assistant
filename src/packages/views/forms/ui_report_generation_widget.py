# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_report_generation_widget.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_ReportGenerationWidget(object):
    def setupUi(self, ReportGenerationWidget):
        if not ReportGenerationWidget.objectName():
            ReportGenerationWidget.setObjectName(u"ReportGenerationWidget")
        ReportGenerationWidget.resize(1250, 849)
        self.gridLayout = QGridLayout(ReportGenerationWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.psb_go_to_main_menu = QPushButton(ReportGenerationWidget)
        self.psb_go_to_main_menu.setObjectName(u"psb_go_to_main_menu")

        self.horizontalLayout.addWidget(self.psb_go_to_main_menu)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.psb_groups = QPushButton(ReportGenerationWidget)
        self.buttonGroup = QButtonGroup(ReportGenerationWidget)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.setExclusive(True)
        self.buttonGroup.addButton(self.psb_groups)
        self.psb_groups.setObjectName(u"psb_groups")
        self.psb_groups.setCheckable(True)

        self.verticalLayout_4.addWidget(self.psb_groups)

        self.pushButton_2 = QPushButton(ReportGenerationWidget)
        self.buttonGroup.addButton(self.pushButton_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(ReportGenerationWidget)
        self.buttonGroup.addButton(self.pushButton_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(ReportGenerationWidget)
        self.buttonGroup.addButton(self.pushButton_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(ReportGenerationWidget)
        self.buttonGroup.addButton(self.pushButton_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(ReportGenerationWidget)
        self.buttonGroup.addButton(self.pushButton_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.stackedWidget_2 = QStackedWidget(ReportGenerationWidget)
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


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.retranslateUi(ReportGenerationWidget)

        self.stackedWidget_2.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(ReportGenerationWidget)
    # setupUi

    def retranslateUi(self, ReportGenerationWidget):
        ReportGenerationWidget.setWindowTitle(QCoreApplication.translate("ReportGenerationWidget", u"Form", None))
        self.psb_go_to_main_menu.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.psb_groups.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.pushButton_3.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0432\u0438\u0434\u044b \u0440\u0430\u0431\u043e\u0442", None))
        self.pushButton_4.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.pushButton_5.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0437\u0430\u043a\u0430\u0437\u044b", None))
        self.pushButton_6.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0440\u0430\u0431\u043e\u0447\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.label_3.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0432\u0438\u0434\u044b \u0440\u0430\u0431\u043e\u0442", None))
        self.label_4.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.label_5.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0437\u0430\u043a\u0430\u0437\u044b", None))
        self.label_6.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0440\u0430\u0431\u043e\u0447\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
    # retranslateUi

