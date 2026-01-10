# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_reports_window_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
)


class Ui_ReportsWindowWidget(object):
    def setupUi(self, ReportsWindowWidget):
        if not ReportsWindowWidget.objectName():
            ReportsWindowWidget.setObjectName(u"ReportsWindowWidget")
        ReportsWindowWidget.resize(1250, 849)
        self.verticalLayout_3 = QVBoxLayout(ReportsWindowWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_go_to_main_menu = QPushButton(ReportsWindowWidget)
        self.pushButton_go_to_main_menu.setObjectName(u"pushButton_go_to_main_menu")

        self.horizontalLayout.addWidget(self.pushButton_go_to_main_menu)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_prefix_company = QLabel(ReportsWindowWidget)
        self.label_prefix_company.setObjectName(u"label_prefix_company")

        self.horizontalLayout_2.addWidget(self.label_prefix_company)

        self.comboBox_company = QComboBox(ReportsWindowWidget)
        self.comboBox_company.setObjectName(u"comboBox_company")
        self.comboBox_company.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.comboBox_company)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_divisions = QPushButton(ReportsWindowWidget)
        self.pushButton_divisions.setObjectName(u"pushButton_divisions")
        self.pushButton_divisions.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_divisions)

        self.pushButton_staff = QPushButton(ReportsWindowWidget)
        self.pushButton_staff.setObjectName(u"pushButton_staff")
        self.pushButton_staff.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_staff)

        self.pushButton_work_types = QPushButton(ReportsWindowWidget)
        self.pushButton_work_types.setObjectName(u"pushButton_work_types")
        self.pushButton_work_types.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_work_types)

        self.pushButton_works = QPushButton(ReportsWindowWidget)
        self.pushButton_works.setObjectName(u"pushButton_works")
        self.pushButton_works.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_works)

        self.pushButton_orders = QPushButton(ReportsWindowWidget)
        self.pushButton_orders.setObjectName(u"pushButton_orders")
        self.pushButton_orders.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_orders)

        self.pushButton_work_events = QPushButton(ReportsWindowWidget)
        self.pushButton_work_events.setObjectName(u"pushButton_work_events")
        self.pushButton_work_events.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_work_events)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.stackedWidget_report_types = QStackedWidget(ReportsWindowWidget)
        self.stackedWidget_report_types.setObjectName(u"stackedWidget_report_types")

        self.horizontalLayout_3.addWidget(self.stackedWidget_report_types)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(ReportsWindowWidget)

        self.stackedWidget_report_types.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(ReportsWindowWidget)
    # setupUi

    def retranslateUi(self, ReportsWindowWidget):
        ReportsWindowWidget.setWindowTitle(QCoreApplication.translate("ReportsWindowWidget", u"Form", None))
        self.pushButton_go_to_main_menu.setText(QCoreApplication.translate("ReportsWindowWidget", u"\u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label_prefix_company.setText(QCoreApplication.translate("ReportsWindowWidget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0435:", None))
        self.pushButton_divisions.setText(QCoreApplication.translate("ReportsWindowWidget", u"\u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton_staff.setText(QCoreApplication.translate("ReportsWindowWidget", u"\u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.pushButton_work_types.setText(QCoreApplication.translate("ReportsWindowWidget", u"\u0432\u0438\u0434\u044b \u0440\u0430\u0431\u043e\u0442", None))
        self.pushButton_works.setText(QCoreApplication.translate("ReportsWindowWidget", u"\u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.pushButton_orders.setText(QCoreApplication.translate("ReportsWindowWidget", u"\u0437\u0430\u043a\u0430\u0437\u044b", None))
        self.pushButton_work_events.setText(QCoreApplication.translate("ReportsWindowWidget", u"\u0440\u0430\u0431\u043e\u0447\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
    # retranslateUi

