# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_works_report_widget.ui'
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

class Ui_WorkReportsWidget(object):
    def setupUi(self, WorkReportsWidget):
        if not WorkReportsWidget.objectName():
            WorkReportsWidget.setObjectName(u"WorkReportsWidget")
        WorkReportsWidget.resize(1037, 1077)
        self.verticalLayout_3 = QVBoxLayout(WorkReportsWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_period_name = QLabel(WorkReportsWidget)
        self.label_period_name.setObjectName(u"label_period_name")

        self.verticalLayout.addWidget(self.label_period_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_prefix_start_period = QLabel(WorkReportsWidget)
        self.label_prefix_start_period.setObjectName(u"label_prefix_start_period")

        self.horizontalLayout.addWidget(self.label_prefix_start_period)

        self.dateEdit_start_period = QDateEdit(WorkReportsWidget)
        self.dateEdit_start_period.setObjectName(u"dateEdit_start_period")
        self.dateEdit_start_period.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit_start_period)

        self.label_prefix_end_period = QLabel(WorkReportsWidget)
        self.label_prefix_end_period.setObjectName(u"label_prefix_end_period")

        self.horizontalLayout.addWidget(self.label_prefix_end_period)

        self.dateEdit_end_period = QDateEdit(WorkReportsWidget)
        self.dateEdit_end_period.setObjectName(u"dateEdit_end_period")
        self.dateEdit_end_period.setKeyboardTracking(True)
        self.dateEdit_end_period.setProperty(u"showGroupSeparator", False)
        self.dateEdit_end_period.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit_end_period)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(WorkReportsWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.comboBox_work_list = QComboBox(WorkReportsWidget)
        self.comboBox_work_list.setObjectName(u"comboBox_work_list")

        self.verticalLayout.addWidget(self.comboBox_work_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_edit_work = QPushButton(WorkReportsWidget)
        self.pushButton_edit_work.setObjectName(u"pushButton_edit_work")

        self.horizontalLayout_2.addWidget(self.pushButton_edit_work)

        self.pushButton_add_work = QPushButton(WorkReportsWidget)
        self.pushButton_add_work.setObjectName(u"pushButton_add_work")

        self.horizontalLayout_2.addWidget(self.pushButton_add_work)

        self.pushButton_delete_work = QPushButton(WorkReportsWidget)
        self.pushButton_delete_work.setObjectName(u"pushButton_delete_work")

        self.horizontalLayout_2.addWidget(self.pushButton_delete_work)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_show_all_works = QPushButton(WorkReportsWidget)
        self.pushButton_show_all_works.setObjectName(u"pushButton_show_all_works")

        self.verticalLayout.addWidget(self.pushButton_show_all_works)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tableWidget_works_data_table = QTableWidget(WorkReportsWidget)
        self.tableWidget_works_data_table.setObjectName(u"tableWidget_works_data_table")

        self.verticalLayout_2.addWidget(self.tableWidget_works_data_table)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(WorkReportsWidget)

        QMetaObject.connectSlotsByName(WorkReportsWidget)
    # setupUi

    def retranslateUi(self, WorkReportsWidget):
        WorkReportsWidget.setWindowTitle(QCoreApplication.translate("WorkReportsWidget", u"Form", None))
        self.label_period_name.setText(QCoreApplication.translate("WorkReportsWidget", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0440\u0430\u0431\u043e\u0442 \u0437\u0430 \u043f\u0435\u0440\u0438\u043e\u0434:", None))
        self.label_prefix_start_period.setText(QCoreApplication.translate("WorkReportsWidget", u"\u0441:", None))
        self.label_prefix_end_period.setText(QCoreApplication.translate("WorkReportsWidget", u"\u043f\u043e:", None))
        self.pushButton_edit_work.setText(QCoreApplication.translate("WorkReportsWidget", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_add_work.setText(QCoreApplication.translate("WorkReportsWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_delete_work.setText(QCoreApplication.translate("WorkReportsWidget", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.pushButton_show_all_works.setText(QCoreApplication.translate("WorkReportsWidget", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u0440\u0430\u0431\u043e\u0442\u044b \u0437\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
    # retranslateUi

