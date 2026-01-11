# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_work_events_report_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
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


class Ui_WorkEventReportWidget(object):
    def setupUi(self, WorkEventReportWidget):
        if not WorkEventReportWidget.objectName():
            WorkEventReportWidget.setObjectName("WorkEventReportWidget")
        WorkEventReportWidget.resize(1118, 1024)
        self.verticalLayout_5 = QVBoxLayout(WorkEventReportWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(
            48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_period_name = QLabel(WorkEventReportWidget)
        self.label_period_name.setObjectName("label_period_name")

        self.verticalLayout_2.addWidget(self.label_period_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_prefix_of_start_period = QLabel(WorkEventReportWidget)
        self.label_prefix_of_start_period.setObjectName("label_prefix_of_start_period")

        self.horizontalLayout.addWidget(self.label_prefix_of_start_period)

        self.dateEdit_start_period = QDateEdit(WorkEventReportWidget)
        self.dateEdit_start_period.setObjectName("dateEdit_start_period")
        self.dateEdit_start_period.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit_start_period)

        self.label_prefix_of_end_period = QLabel(WorkEventReportWidget)
        self.label_prefix_of_end_period.setObjectName("label_prefix_of_end_period")

        self.horizontalLayout.addWidget(self.label_prefix_of_end_period)

        self.dateEdit_end_period = QDateEdit(WorkEventReportWidget)
        self.dateEdit_end_period.setObjectName("dateEdit_end_period")
        self.dateEdit_end_period.setKeyboardTracking(True)
        self.dateEdit_end_period.setProperty("showGroupSeparator", False)
        self.dateEdit_end_period.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit_end_period)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_division_name = QLabel(WorkEventReportWidget)
        self.label_division_name.setObjectName("label_division_name")
        self.label_division_name.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.horizontalLayout_3.addWidget(self.label_division_name)

        self.comboBox_division_list = QComboBox(WorkEventReportWidget)
        self.comboBox_division_list.setObjectName("comboBox_division_list")

        self.horizontalLayout_3.addWidget(self.comboBox_division_list)

        self.label_department_name = QLabel(WorkEventReportWidget)
        self.label_department_name.setObjectName("label_department_name")
        self.label_department_name.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.horizontalLayout_3.addWidget(self.label_department_name)

        self.comboBox_department_list = QComboBox(WorkEventReportWidget)
        self.comboBox_department_list.setObjectName("comboBox_department_list")

        self.horizontalLayout_3.addWidget(self.comboBox_department_list)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_staff_list = QLabel(WorkEventReportWidget)
        self.label_staff_list.setObjectName("label_staff_list")
        self.label_staff_list.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_staff_list.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.horizontalLayout_4.addWidget(self.label_staff_list)

        self.comboBox_staff_list = QComboBox(WorkEventReportWidget)
        self.comboBox_staff_list.setObjectName("comboBox_staff_list")

        self.horizontalLayout_4.addWidget(self.comboBox_staff_list)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.line = QFrame(WorkEventReportWidget)
        self.line.setObjectName("line")
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.comboBox_work_event_list = QComboBox(WorkEventReportWidget)
        self.comboBox_work_event_list.setObjectName("comboBox_work_event_list")

        self.verticalLayout_3.addWidget(self.comboBox_work_event_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_edit_event = QPushButton(WorkEventReportWidget)
        self.pushButton_edit_event.setObjectName("pushButton_edit_event")

        self.horizontalLayout_2.addWidget(self.pushButton_edit_event)

        self.pushButton_add_event = QPushButton(WorkEventReportWidget)
        self.pushButton_add_event.setObjectName("pushButton_add_event")

        self.horizontalLayout_2.addWidget(self.pushButton_add_event)

        self.pushButton_delete_event = QPushButton(WorkEventReportWidget)
        self.pushButton_delete_event.setObjectName("pushButton_delete_event")

        self.horizontalLayout_2.addWidget(self.pushButton_delete_event)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.pushButton_show_event_details = QPushButton(WorkEventReportWidget)
        self.pushButton_show_event_details.setObjectName("pushButton_show_event_details")

        self.verticalLayout_3.addWidget(self.pushButton_show_event_details)

        self.pushButton_show_all_events = QPushButton(WorkEventReportWidget)
        self.pushButton_show_all_events.setObjectName("pushButton_show_all_events")

        self.verticalLayout_3.addWidget(self.pushButton_show_all_events)

        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.tableWidget_work_event_data_table = QTableWidget(WorkEventReportWidget)
        self.tableWidget_work_event_data_table.setObjectName("tableWidget_work_event_data_table")

        self.verticalLayout_4.addWidget(self.tableWidget_work_event_data_table)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(WorkEventReportWidget)

        QMetaObject.connectSlotsByName(WorkEventReportWidget)

    # setupUi

    def retranslateUi(self, WorkEventReportWidget):
        WorkEventReportWidget.setWindowTitle(
            QCoreApplication.translate("WorkEventReportWidget", "Form", None)
        )
        self.label_period_name.setText(
            QCoreApplication.translate(
                "WorkEventReportWidget",
                "\u0421\u043e\u0431\u044b\u0442\u0438\u044f \u0437\u0430 \u043f\u0435\u0440\u0438\u043e\u0434:",
                None,
            )
        )
        self.label_prefix_of_start_period.setText(
            QCoreApplication.translate("WorkEventReportWidget", "\u0441:", None)
        )
        self.label_prefix_of_end_period.setText(
            QCoreApplication.translate("WorkEventReportWidget", "\u043f\u043e:", None)
        )
        self.label_division_name.setText(
            QCoreApplication.translate(
                "WorkEventReportWidget", "\u0421\u043b\u0443\u0436\u0431\u0430:", None
            )
        )
        self.label_department_name.setText(
            QCoreApplication.translate(
                "WorkEventReportWidget", "\u0413\u0440\u0443\u043f\u043f\u0430:", None
            )
        )
        self.label_staff_list.setText(
            QCoreApplication.translate(
                "WorkEventReportWidget", "\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a:", None
            )
        )
        self.pushButton_edit_event.setText(
            QCoreApplication.translate(
                "WorkEventReportWidget",
                "\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                None,
            )
        )
        self.pushButton_add_event.setText(
            QCoreApplication.translate(
                "WorkEventReportWidget", "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None
            )
        )
        self.pushButton_delete_event.setText(
            QCoreApplication.translate(
                "WorkEventReportWidget", "\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None
            )
        )
        self.pushButton_show_event_details.setText(
            QCoreApplication.translate(
                "WorkEventReportWidget",
                "\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043f\u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u043c\u0443 \u0437\u0430\u043a\u0430\u0437\u0443",
                None,
            )
        )
        self.pushButton_show_all_events.setText(
            QCoreApplication.translate(
                "WorkEventReportWidget",
                "\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0437\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430",
                None,
            )
        )

    # retranslateUi
