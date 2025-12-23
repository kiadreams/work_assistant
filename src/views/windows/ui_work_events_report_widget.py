# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_work_events_report_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_WorkEventReportsWidget(object):
    def setupUi(self, WorkEventReportsWidget):
        if not WorkEventReportsWidget.objectName():
            WorkEventReportsWidget.setObjectName(u"WorkEventReportsWidget")
        WorkEventReportsWidget.resize(1118, 1024)
        self.verticalLayout_5 = QVBoxLayout(WorkEventReportsWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_period_name = QLabel(WorkEventReportsWidget)
        self.label_period_name.setObjectName(u"label_period_name")

        self.verticalLayout_2.addWidget(self.label_period_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_prefix_of_start_period = QLabel(WorkEventReportsWidget)
        self.label_prefix_of_start_period.setObjectName(u"label_prefix_of_start_period")

        self.horizontalLayout.addWidget(self.label_prefix_of_start_period)

        self.dateEdit_start_period = QDateEdit(WorkEventReportsWidget)
        self.dateEdit_start_period.setObjectName(u"dateEdit_start_period")
        self.dateEdit_start_period.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit_start_period)

        self.label_prefix_of_end_period = QLabel(WorkEventReportsWidget)
        self.label_prefix_of_end_period.setObjectName(u"label_prefix_of_end_period")

        self.horizontalLayout.addWidget(self.label_prefix_of_end_period)

        self.dateEdit_end_period = QDateEdit(WorkEventReportsWidget)
        self.dateEdit_end_period.setObjectName(u"dateEdit_end_period")
        self.dateEdit_end_period.setKeyboardTracking(True)
        self.dateEdit_end_period.setProperty(u"showGroupSeparator", False)
        self.dateEdit_end_period.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit_end_period)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_service_name = QLabel(WorkEventReportsWidget)
        self.label_service_name.setObjectName(u"label_service_name")
        self.label_service_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_service_name)

        self.comboBox_service_list = QComboBox(WorkEventReportsWidget)
        self.comboBox_service_list.setObjectName(u"comboBox_service_list")

        self.horizontalLayout_3.addWidget(self.comboBox_service_list)

        self.label_group_name = QLabel(WorkEventReportsWidget)
        self.label_group_name.setObjectName(u"label_group_name")
        self.label_group_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_group_name)

        self.comboBox_group_list = QComboBox(WorkEventReportsWidget)
        self.comboBox_group_list.setObjectName(u"comboBox_group_list")

        self.horizontalLayout_3.addWidget(self.comboBox_group_list)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_staff_list = QLabel(WorkEventReportsWidget)
        self.label_staff_list.setObjectName(u"label_staff_list")
        self.label_staff_list.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_staff_list.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_staff_list)

        self.comboBox_staff_list = QComboBox(WorkEventReportsWidget)
        self.comboBox_staff_list.setObjectName(u"comboBox_staff_list")

        self.horizontalLayout_4.addWidget(self.comboBox_staff_list)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.line = QFrame(WorkEventReportsWidget)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.comboBox_work_event_list = QComboBox(WorkEventReportsWidget)
        self.comboBox_work_event_list.setObjectName(u"comboBox_work_event_list")

        self.verticalLayout_3.addWidget(self.comboBox_work_event_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_edit_event = QPushButton(WorkEventReportsWidget)
        self.pushButton_edit_event.setObjectName(u"pushButton_edit_event")

        self.horizontalLayout_2.addWidget(self.pushButton_edit_event)

        self.pushButton_add_event = QPushButton(WorkEventReportsWidget)
        self.pushButton_add_event.setObjectName(u"pushButton_add_event")

        self.horizontalLayout_2.addWidget(self.pushButton_add_event)

        self.pushButton_delete_event = QPushButton(WorkEventReportsWidget)
        self.pushButton_delete_event.setObjectName(u"pushButton_delete_event")

        self.horizontalLayout_2.addWidget(self.pushButton_delete_event)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.pushButton_show_event_details = QPushButton(WorkEventReportsWidget)
        self.pushButton_show_event_details.setObjectName(u"pushButton_show_event_details")

        self.verticalLayout_3.addWidget(self.pushButton_show_event_details)

        self.pushButton_show_all_events = QPushButton(WorkEventReportsWidget)
        self.pushButton_show_all_events.setObjectName(u"pushButton_show_all_events")

        self.verticalLayout_3.addWidget(self.pushButton_show_all_events)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.tableWidget_work_event_data_table = QTableWidget(WorkEventReportsWidget)
        self.tableWidget_work_event_data_table.setObjectName(u"tableWidget_work_event_data_table")

        self.verticalLayout_4.addWidget(self.tableWidget_work_event_data_table)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.retranslateUi(WorkEventReportsWidget)

        QMetaObject.connectSlotsByName(WorkEventReportsWidget)
    # setupUi

    def retranslateUi(self, WorkEventReportsWidget):
        WorkEventReportsWidget.setWindowTitle(QCoreApplication.translate("WorkEventReportsWidget", u"Form", None))
        self.label_period_name.setText(QCoreApplication.translate("WorkEventReportsWidget", u"\u0421\u043e\u0431\u044b\u0442\u0438\u044f \u0437\u0430 \u043f\u0435\u0440\u0438\u043e\u0434:", None))
        self.label_prefix_of_start_period.setText(QCoreApplication.translate("WorkEventReportsWidget", u"\u0441:", None))
        self.label_prefix_of_end_period.setText(QCoreApplication.translate("WorkEventReportsWidget", u"\u043f\u043e:", None))
        self.label_service_name.setText(QCoreApplication.translate("WorkEventReportsWidget", u"\u0421\u043b\u0443\u0436\u0431\u0430:", None))
        self.label_group_name.setText(QCoreApplication.translate("WorkEventReportsWidget", u"\u0413\u0440\u0443\u043f\u043f\u0430:", None))
        self.label_staff_list.setText(QCoreApplication.translate("WorkEventReportsWidget", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a:", None))
        self.pushButton_edit_event.setText(QCoreApplication.translate("WorkEventReportsWidget", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_add_event.setText(QCoreApplication.translate("WorkEventReportsWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_delete_event.setText(QCoreApplication.translate("WorkEventReportsWidget", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.pushButton_show_event_details.setText(QCoreApplication.translate("WorkEventReportsWidget", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043f\u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u043c\u0443 \u0437\u0430\u043a\u0430\u0437\u0443", None))
        self.pushButton_show_all_events.setText(QCoreApplication.translate("WorkEventReportsWidget", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0437\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430", None))
    # retranslateUi

