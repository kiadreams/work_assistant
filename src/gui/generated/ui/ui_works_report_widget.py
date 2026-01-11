# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_works_report_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QVBoxLayout,
)


class Ui_WorkReportWidget(object):
    def setupUi(self, WorkReportWidget):
        if not WorkReportWidget.objectName():
            WorkReportWidget.setObjectName("WorkReportWidget")
        WorkReportWidget.resize(1037, 1077)
        self.verticalLayout_3 = QVBoxLayout(WorkReportWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_period_name = QLabel(WorkReportWidget)
        self.label_period_name.setObjectName("label_period_name")

        self.verticalLayout.addWidget(self.label_period_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_prefix_start_period = QLabel(WorkReportWidget)
        self.label_prefix_start_period.setObjectName("label_prefix_start_period")

        self.horizontalLayout.addWidget(self.label_prefix_start_period)

        self.dateEdit_start_period = QDateEdit(WorkReportWidget)
        self.dateEdit_start_period.setObjectName("dateEdit_start_period")
        self.dateEdit_start_period.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit_start_period)

        self.label_prefix_end_period = QLabel(WorkReportWidget)
        self.label_prefix_end_period.setObjectName("label_prefix_end_period")

        self.horizontalLayout.addWidget(self.label_prefix_end_period)

        self.dateEdit_end_period = QDateEdit(WorkReportWidget)
        self.dateEdit_end_period.setObjectName("dateEdit_end_period")
        self.dateEdit_end_period.setKeyboardTracking(True)
        self.dateEdit_end_period.setProperty("showGroupSeparator", False)
        self.dateEdit_end_period.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit_end_period)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(WorkReportWidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.comboBox_work_list = QComboBox(WorkReportWidget)
        self.comboBox_work_list.setObjectName("comboBox_work_list")

        self.verticalLayout.addWidget(self.comboBox_work_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_edit_work = QPushButton(WorkReportWidget)
        self.pushButton_edit_work.setObjectName("pushButton_edit_work")

        self.horizontalLayout_2.addWidget(self.pushButton_edit_work)

        self.pushButton_add_work = QPushButton(WorkReportWidget)
        self.pushButton_add_work.setObjectName("pushButton_add_work")

        self.horizontalLayout_2.addWidget(self.pushButton_add_work)

        self.pushButton_delete_work = QPushButton(WorkReportWidget)
        self.pushButton_delete_work.setObjectName("pushButton_delete_work")

        self.horizontalLayout_2.addWidget(self.pushButton_delete_work)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_show_all_works = QPushButton(WorkReportWidget)
        self.pushButton_show_all_works.setObjectName("pushButton_show_all_works")

        self.verticalLayout.addWidget(self.pushButton_show_all_works)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tableWidget_works_data_table = QTableWidget(WorkReportWidget)
        self.tableWidget_works_data_table.setObjectName("tableWidget_works_data_table")

        self.verticalLayout_2.addWidget(self.tableWidget_works_data_table)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(WorkReportWidget)

        QMetaObject.connectSlotsByName(WorkReportWidget)

    # setupUi

    def retranslateUi(self, WorkReportWidget):
        WorkReportWidget.setWindowTitle(
            QCoreApplication.translate("WorkReportWidget", "Form", None)
        )
        self.label_period_name.setText(
            QCoreApplication.translate(
                "WorkReportWidget",
                "\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0440\u0430\u0431\u043e\u0442 \u0437\u0430 \u043f\u0435\u0440\u0438\u043e\u0434:",
                None,
            )
        )
        self.label_prefix_start_period.setText(
            QCoreApplication.translate("WorkReportWidget", "\u0441:", None)
        )
        self.label_prefix_end_period.setText(
            QCoreApplication.translate("WorkReportWidget", "\u043f\u043e:", None)
        )
        self.pushButton_edit_work.setText(
            QCoreApplication.translate(
                "WorkReportWidget",
                "\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                None,
            )
        )
        self.pushButton_add_work.setText(
            QCoreApplication.translate(
                "WorkReportWidget", "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None
            )
        )
        self.pushButton_delete_work.setText(
            QCoreApplication.translate(
                "WorkReportWidget", "\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None
            )
        )
        self.pushButton_show_all_works.setText(
            QCoreApplication.translate(
                "WorkReportWidget",
                "\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u0440\u0430\u0431\u043e\u0442\u044b \u0437\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434",
                None,
            )
        )

    # retranslateUi
