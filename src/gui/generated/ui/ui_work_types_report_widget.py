# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_work_types_report_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QVBoxLayout,
)


class Ui_WorkTypeReportWidget(object):
    def setupUi(self, WorkTypeReportWidget):
        if not WorkTypeReportWidget.objectName():
            WorkTypeReportWidget.setObjectName(u"WorkTypeReportWidget")
        WorkTypeReportWidget.resize(886, 739)
        self.verticalLayout_2 = QVBoxLayout(WorkTypeReportWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(WorkTypeReportWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBox_work_type_list = QComboBox(WorkTypeReportWidget)
        self.comboBox_work_type_list.setObjectName(u"comboBox_work_type_list")

        self.verticalLayout.addWidget(self.comboBox_work_type_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_edit_work_type = QPushButton(WorkTypeReportWidget)
        self.pushButton_edit_work_type.setObjectName(u"pushButton_edit_work_type")

        self.horizontalLayout.addWidget(self.pushButton_edit_work_type)

        self.pushButton_add_work_type = QPushButton(WorkTypeReportWidget)
        self.pushButton_add_work_type.setObjectName(u"pushButton_add_work_type")

        self.horizontalLayout.addWidget(self.pushButton_add_work_type)

        self.pushButton_delete_work_type = QPushButton(WorkTypeReportWidget)
        self.pushButton_delete_work_type.setObjectName(u"pushButton_delete_work_type")

        self.horizontalLayout.addWidget(self.pushButton_delete_work_type)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_show_all_work_types = QPushButton(WorkTypeReportWidget)
        self.pushButton_show_all_work_types.setObjectName(u"pushButton_show_all_work_types")

        self.verticalLayout.addWidget(self.pushButton_show_all_work_types)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tableWidget_work_type_data_table = QTableWidget(WorkTypeReportWidget)
        self.tableWidget_work_type_data_table.setObjectName(u"tableWidget_work_type_data_table")

        self.verticalLayout_2.addWidget(self.tableWidget_work_type_data_table)


        self.retranslateUi(WorkTypeReportWidget)

        QMetaObject.connectSlotsByName(WorkTypeReportWidget)
    # setupUi

    def retranslateUi(self, WorkTypeReportWidget):
        WorkTypeReportWidget.setWindowTitle(QCoreApplication.translate("WorkTypeReportWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("WorkTypeReportWidget", u"\u0412\u0438\u0434\u044b \u0440\u0430\u0431\u043e\u0442:", None))
        self.pushButton_edit_work_type.setText(QCoreApplication.translate("WorkTypeReportWidget", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_add_work_type.setText(QCoreApplication.translate("WorkTypeReportWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_delete_work_type.setText(QCoreApplication.translate("WorkTypeReportWidget", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.pushButton_show_all_work_types.setText(QCoreApplication.translate("WorkTypeReportWidget", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u0442\u0438\u043f\u044b \u0440\u0430\u0431\u043e\u0442", None))
    # retranslateUi

