# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_orders_report_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDate, QMetaObject, Qt
from PySide6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QVBoxLayout,
)


class Ui_OrderReportWidget(object):
    def setupUi(self, OrderReportWidget):
        if not OrderReportWidget.objectName():
            OrderReportWidget.setObjectName(u"OrderReportWidget")
        OrderReportWidget.resize(1036, 1077)
        self.verticalLayout_3 = QVBoxLayout(OrderReportWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_company_name = QLabel(OrderReportWidget)
        self.label_company_name.setObjectName(u"label_company_name")

        self.verticalLayout.addWidget(self.label_company_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_prefix_start_period = QLabel(OrderReportWidget)
        self.label_prefix_start_period.setObjectName(u"label_prefix_start_period")
        self.label_prefix_start_period.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_prefix_start_period)

        self.dateEdit_start_period = QDateEdit(OrderReportWidget)
        self.dateEdit_start_period.setObjectName(u"dateEdit_start_period")
        self.dateEdit_start_period.setFrame(True)
        self.dateEdit_start_period.setAccelerated(False)
        self.dateEdit_start_period.setKeyboardTracking(True)
        self.dateEdit_start_period.setProperty(u"showGroupSeparator", True)
        self.dateEdit_start_period.setCurrentSection(QDateTimeEdit.Section.MonthSection)
        self.dateEdit_start_period.setCalendarPopup(False)
        self.dateEdit_start_period.setCurrentSectionIndex(0)
        self.dateEdit_start_period.setDate(QDate(2025, 1, 1))

        self.horizontalLayout.addWidget(self.dateEdit_start_period)

        self.label_prefix_end_period = QLabel(OrderReportWidget)
        self.label_prefix_end_period.setObjectName(u"label_prefix_end_period")
        self.label_prefix_end_period.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_prefix_end_period)

        self.dateEdit_end_period = QDateEdit(OrderReportWidget)
        self.dateEdit_end_period.setObjectName(u"dateEdit_end_period")
        self.dateEdit_end_period.setKeyboardTracking(True)
        self.dateEdit_end_period.setProperty(u"showGroupSeparator", True)
        self.dateEdit_end_period.setCurrentSection(QDateTimeEdit.Section.MonthSection)
        self.dateEdit_end_period.setCalendarPopup(True)
        self.dateEdit_end_period.setDate(QDate(2025, 12, 1))

        self.horizontalLayout.addWidget(self.dateEdit_end_period)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(OrderReportWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.comboBox_order_list = QComboBox(OrderReportWidget)
        self.comboBox_order_list.setObjectName(u"comboBox_order_list")

        self.verticalLayout.addWidget(self.comboBox_order_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_edit_order = QPushButton(OrderReportWidget)
        self.pushButton_edit_order.setObjectName(u"pushButton_edit_order")

        self.horizontalLayout_2.addWidget(self.pushButton_edit_order)

        self.pushButton_add_order = QPushButton(OrderReportWidget)
        self.pushButton_add_order.setObjectName(u"pushButton_add_order")

        self.horizontalLayout_2.addWidget(self.pushButton_add_order)

        self.pushButton_delete_order = QPushButton(OrderReportWidget)
        self.pushButton_delete_order.setObjectName(u"pushButton_delete_order")

        self.horizontalLayout_2.addWidget(self.pushButton_delete_order)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_show_all_orders = QPushButton(OrderReportWidget)
        self.pushButton_show_all_orders.setObjectName(u"pushButton_show_all_orders")

        self.verticalLayout.addWidget(self.pushButton_show_all_orders)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tableWidget_order_data_table = QTableWidget(OrderReportWidget)
        self.tableWidget_order_data_table.setObjectName(u"tableWidget_order_data_table")

        self.verticalLayout_2.addWidget(self.tableWidget_order_data_table)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(OrderReportWidget)

        QMetaObject.connectSlotsByName(OrderReportWidget)
    # setupUi

    def retranslateUi(self, OrderReportWidget):
        OrderReportWidget.setWindowTitle(QCoreApplication.translate("OrderReportWidget", u"Form", None))
        self.label_company_name.setText(QCoreApplication.translate("OrderReportWidget", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0437\u0430\u043a\u0430\u0437\u043e\u0432 \u0437\u0430 \u043f\u0435\u0440\u0438\u043e\u0434:", None))
        self.label_prefix_start_period.setText(QCoreApplication.translate("OrderReportWidget", u"\u0441:", None))
        self.dateEdit_start_period.setDisplayFormat(QCoreApplication.translate("OrderReportWidget", u"MM.yyyy", None))
        self.label_prefix_end_period.setText(QCoreApplication.translate("OrderReportWidget", u"\u043f\u043e:", None))
        self.dateEdit_end_period.setDisplayFormat(QCoreApplication.translate("OrderReportWidget", u"MM.yyyy", None))
        self.pushButton_edit_order.setText(QCoreApplication.translate("OrderReportWidget", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_add_order.setText(QCoreApplication.translate("OrderReportWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_delete_order.setText(QCoreApplication.translate("OrderReportWidget", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.pushButton_show_all_orders.setText(QCoreApplication.translate("OrderReportWidget", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u0437\u0430\u043a\u0430\u0437\u044b \u0437\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
    # retranslateUi

