# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_staff_report_widget.ui'
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


class Ui_StaffReportWidget(object):
    def setupUi(self, StaffReportWidget):
        if not StaffReportWidget.objectName():
            StaffReportWidget.setObjectName("StaffReportWidget")
        StaffReportWidget.resize(886, 739)
        self.verticalLayout_2 = QVBoxLayout(StaffReportWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_division_list_title = QLabel(StaffReportWidget)
        self.label_division_list_title.setObjectName("label_division_list_title")

        self.horizontalLayout_2.addWidget(self.label_division_list_title)

        self.comboBox_division_list_2 = QComboBox(StaffReportWidget)
        self.comboBox_division_list_2.setObjectName("comboBox_division_list_2")

        self.horizontalLayout_2.addWidget(self.comboBox_division_list_2)

        self.label_department_list_title = QLabel(StaffReportWidget)
        self.label_department_list_title.setObjectName("label_department_list_title")

        self.horizontalLayout_2.addWidget(self.label_department_list_title)

        self.comboBox_department_list = QComboBox(StaffReportWidget)
        self.comboBox_department_list.setObjectName("comboBox_department_list")

        self.horizontalLayout_2.addWidget(self.comboBox_department_list)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(StaffReportWidget)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.comboBox_division_list = QComboBox(StaffReportWidget)
        self.comboBox_division_list.setObjectName("comboBox_division_list")

        self.verticalLayout.addWidget(self.comboBox_division_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_edit_staff = QPushButton(StaffReportWidget)
        self.pushButton_edit_staff.setObjectName("pushButton_edit_staff")

        self.horizontalLayout.addWidget(self.pushButton_edit_staff)

        self.pushButton_add_staff = QPushButton(StaffReportWidget)
        self.pushButton_add_staff.setObjectName("pushButton_add_staff")

        self.horizontalLayout.addWidget(self.pushButton_add_staff)

        self.pushButton_delete_staff = QPushButton(StaffReportWidget)
        self.pushButton_delete_staff.setObjectName("pushButton_delete_staff")

        self.horizontalLayout.addWidget(self.pushButton_delete_staff)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_show_all_staff = QPushButton(StaffReportWidget)
        self.pushButton_show_all_staff.setObjectName("pushButton_show_all_staff")

        self.verticalLayout.addWidget(self.pushButton_show_all_staff)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tableWidget_staff_data_table = QTableWidget(StaffReportWidget)
        self.tableWidget_staff_data_table.setObjectName("tableWidget_staff_data_table")

        self.verticalLayout_2.addWidget(self.tableWidget_staff_data_table)

        self.retranslateUi(StaffReportWidget)

        QMetaObject.connectSlotsByName(StaffReportWidget)

    # setupUi

    def retranslateUi(self, StaffReportWidget):
        StaffReportWidget.setWindowTitle(
            QCoreApplication.translate("StaffReportWidget", "Form", None)
        )
        self.label_division_list_title.setText(
            QCoreApplication.translate(
                "StaffReportWidget", " \u0421\u043b\u0443\u0436\u0431\u0430", None
            )
        )
        self.label_department_list_title.setText(
            QCoreApplication.translate(
                "StaffReportWidget",
                "\u0413\u0440\u0443\u043f\u043f\u0430 / \u0443\u0447\u0430\u0441\u0442\u043e\u043a",
                None,
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "StaffReportWidget", "\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None
            )
        )
        self.pushButton_edit_staff.setText(
            QCoreApplication.translate(
                "StaffReportWidget",
                "\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                None,
            )
        )
        self.pushButton_add_staff.setText(
            QCoreApplication.translate(
                "StaffReportWidget", "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None
            )
        )
        self.pushButton_delete_staff.setText(
            QCoreApplication.translate(
                "StaffReportWidget", "\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None
            )
        )
        self.pushButton_show_all_staff.setText(
            QCoreApplication.translate(
                "StaffReportWidget",
                "\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0435\u0441\u044c \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b",
                None,
            )
        )

    # retranslateUi
