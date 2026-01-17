# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_divisions_report_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
)
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableView,
    QVBoxLayout,
)


class Ui_DivisionReportWidget(object):
    def setupUi(self, DivisionReportWidget):
        if not DivisionReportWidget.objectName():
            DivisionReportWidget.setObjectName("DivisionReportWidget")
        DivisionReportWidget.resize(1058, 660)
        self.verticalLayout_4 = QVBoxLayout(DivisionReportWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_division_list_title = QLabel(DivisionReportWidget)
        self.label_division_list_title.setObjectName("label_division_list_title")

        self.verticalLayout.addWidget(self.label_division_list_title)

        self.comboBox_division_list = QComboBox(DivisionReportWidget)
        self.comboBox_division_list.setObjectName("comboBox_division_list")

        self.verticalLayout.addWidget(self.comboBox_division_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_edit_division = QPushButton(DivisionReportWidget)
        self.pushButton_edit_division.setObjectName("pushButton_edit_division")

        self.horizontalLayout.addWidget(self.pushButton_edit_division)

        self.pushButton_add_division = QPushButton(DivisionReportWidget)
        self.pushButton_add_division.setObjectName("pushButton_add_division")

        self.horizontalLayout.addWidget(self.pushButton_add_division)

        self.pushButton_remove_division = QPushButton(DivisionReportWidget)
        self.pushButton_remove_division.setObjectName("pushButton_remove_division")

        self.horizontalLayout.addWidget(self.pushButton_remove_division)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_show_all_divisions = QPushButton(DivisionReportWidget)
        self.pushButton_show_all_divisions.setObjectName("pushButton_show_all_divisions")

        self.verticalLayout.addWidget(self.pushButton_show_all_divisions)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_department_list_title = QLabel(DivisionReportWidget)
        self.label_department_list_title.setObjectName("label_department_list_title")

        self.verticalLayout_2.addWidget(self.label_department_list_title)

        self.comboBox_department_list = QComboBox(DivisionReportWidget)
        self.comboBox_department_list.setObjectName("comboBox_department_list")

        self.verticalLayout_2.addWidget(self.comboBox_department_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_edit_department = QPushButton(DivisionReportWidget)
        self.pushButton_edit_department.setObjectName("pushButton_edit_department")

        self.horizontalLayout_2.addWidget(self.pushButton_edit_department)

        self.pushButton_add_department = QPushButton(DivisionReportWidget)
        self.pushButton_add_department.setObjectName("pushButton_add_department")

        self.horizontalLayout_2.addWidget(self.pushButton_add_department)

        self.pushButton_remove_department = QPushButton(DivisionReportWidget)
        self.pushButton_remove_department.setObjectName("pushButton_remove_department")

        self.horizontalLayout_2.addWidget(self.pushButton_remove_department)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.pushButton_show_departments_of_division = QPushButton(DivisionReportWidget)
        self.pushButton_show_departments_of_division.setObjectName(
            "pushButton_show_departments_of_division"
        )

        self.verticalLayout_2.addWidget(self.pushButton_show_departments_of_division)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tableView_division_data_table = QTableView(DivisionReportWidget)
        self.tableView_division_data_table.setObjectName("tableView_division_data_table")

        self.verticalLayout_3.addWidget(self.tableView_division_data_table)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(DivisionReportWidget)

        QMetaObject.connectSlotsByName(DivisionReportWidget)

    # setupUi

    def retranslateUi(self, DivisionReportWidget):
        DivisionReportWidget.setWindowTitle(
            QCoreApplication.translate("DivisionReportWidget", "Form", None)
        )
        self.label_division_list_title.setText(
            QCoreApplication.translate(
                "DivisionReportWidget",
                "\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u043b\u0443\u0436\u0431\u044b",
                None,
            )
        )
        self.pushButton_edit_division.setText(
            QCoreApplication.translate(
                "DivisionReportWidget",
                " \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043b\u0443\u0436\u0431\u0443",
                None,
            )
        )
        self.pushButton_add_division.setText(
            QCoreApplication.translate(
                "DivisionReportWidget",
                "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043b\u0443\u0436\u0431\u0443",
                None,
            )
        )
        self.pushButton_remove_division.setText(
            QCoreApplication.translate(
                "DivisionReportWidget",
                "\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043b\u0443\u0436\u0431\u0443",
                None,
            )
        )
        self.pushButton_show_all_divisions.setText(
            QCoreApplication.translate(
                "DivisionReportWidget",
                "\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0432\u0441\u0435\u0445 \u0441\u043b\u0443\u0436\u0431",
                None,
            )
        )
        self.label_department_list_title.setText(
            QCoreApplication.translate(
                "DivisionReportWidget",
                "\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u0440\u0443\u043f\u043f\u044b",
                None,
            )
        )
        self.pushButton_edit_department.setText(
            QCoreApplication.translate(
                "DivisionReportWidget",
                " \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443",
                None,
            )
        )
        self.pushButton_add_department.setText(
            QCoreApplication.translate(
                "DivisionReportWidget",
                "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443",
                None,
            )
        )
        self.pushButton_remove_department.setText(
            QCoreApplication.translate(
                "DivisionReportWidget",
                "\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443",
                None,
            )
        )
        self.pushButton_show_departments_of_division.setText(
            QCoreApplication.translate(
                "DivisionReportWidget",
                "\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u044b \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u0441\u043b\u0443\u0436\u0431\u044b",
                None,
            )
        )

    # retranslateUi
