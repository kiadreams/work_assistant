# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_divisions_report_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_DivisionReportWidget(object):
    def setupUi(self, DivisionReportWidget):
        if not DivisionReportWidget.objectName():
            DivisionReportWidget.setObjectName(u"DivisionReportWidget")
        DivisionReportWidget.resize(1058, 660)
        self.verticalLayout_4 = QVBoxLayout(DivisionReportWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_division_list_title = QLabel(DivisionReportWidget)
        self.label_division_list_title.setObjectName(u"label_division_list_title")

        self.verticalLayout.addWidget(self.label_division_list_title)

        self.comboBox_division_list = QComboBox(DivisionReportWidget)
        self.comboBox_division_list.setObjectName(u"comboBox_division_list")

        self.verticalLayout.addWidget(self.comboBox_division_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_edit_division = QPushButton(DivisionReportWidget)
        self.pushButton_edit_division.setObjectName(u"pushButton_edit_division")

        self.horizontalLayout.addWidget(self.pushButton_edit_division)

        self.pushButton_add_division = QPushButton(DivisionReportWidget)
        self.pushButton_add_division.setObjectName(u"pushButton_add_division")

        self.horizontalLayout.addWidget(self.pushButton_add_division)

        self.pushButton_remove_division = QPushButton(DivisionReportWidget)
        self.pushButton_remove_division.setObjectName(u"pushButton_remove_division")

        self.horizontalLayout.addWidget(self.pushButton_remove_division)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_show_all_divisions = QPushButton(DivisionReportWidget)
        self.pushButton_show_all_divisions.setObjectName(u"pushButton_show_all_divisions")

        self.verticalLayout.addWidget(self.pushButton_show_all_divisions)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_department_list_title = QLabel(DivisionReportWidget)
        self.label_department_list_title.setObjectName(u"label_department_list_title")

        self.verticalLayout_2.addWidget(self.label_department_list_title)

        self.comboBox_department_list = QComboBox(DivisionReportWidget)
        self.comboBox_department_list.setObjectName(u"comboBox_department_list")

        self.verticalLayout_2.addWidget(self.comboBox_department_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_edit_department = QPushButton(DivisionReportWidget)
        self.pushButton_edit_department.setObjectName(u"pushButton_edit_department")

        self.horizontalLayout_2.addWidget(self.pushButton_edit_department)

        self.pushButton_add_department = QPushButton(DivisionReportWidget)
        self.pushButton_add_department.setObjectName(u"pushButton_add_department")

        self.horizontalLayout_2.addWidget(self.pushButton_add_department)

        self.pushButton_remove_department = QPushButton(DivisionReportWidget)
        self.pushButton_remove_department.setObjectName(u"pushButton_remove_department")

        self.horizontalLayout_2.addWidget(self.pushButton_remove_department)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.pushButton_show_all_department = QPushButton(DivisionReportWidget)
        self.pushButton_show_all_department.setObjectName(u"pushButton_show_all_department")

        self.verticalLayout_2.addWidget(self.pushButton_show_all_department)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tableWidget_division_data_table = QTableWidget(DivisionReportWidget)
        self.tableWidget_division_data_table.setObjectName(u"tableWidget_division_data_table")

        self.verticalLayout_3.addWidget(self.tableWidget_division_data_table)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(DivisionReportWidget)

        QMetaObject.connectSlotsByName(DivisionReportWidget)
    # setupUi

    def retranslateUi(self, DivisionReportWidget):
        DivisionReportWidget.setWindowTitle(QCoreApplication.translate("DivisionReportWidget", u"Form", None))
        self.label_division_list_title.setText(QCoreApplication.translate("DivisionReportWidget", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u043b\u0443\u0436\u0431\u044b", None))
        self.pushButton_edit_division.setText(QCoreApplication.translate("DivisionReportWidget", u" \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043b\u0443\u0436\u0431\u0443", None))
        self.pushButton_add_division.setText(QCoreApplication.translate("DivisionReportWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043b\u0443\u0436\u0431\u0443", None))
        self.pushButton_remove_division.setText(QCoreApplication.translate("DivisionReportWidget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043b\u0443\u0436\u0431\u0443", None))
        self.pushButton_show_all_divisions.setText(QCoreApplication.translate("DivisionReportWidget", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0432\u0441\u0435\u0445 \u0441\u043b\u0443\u0436\u0431", None))
        self.label_department_list_title.setText(QCoreApplication.translate("DivisionReportWidget", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.pushButton_edit_department.setText(QCoreApplication.translate("DivisionReportWidget", u" \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.pushButton_add_department.setText(QCoreApplication.translate("DivisionReportWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.pushButton_remove_department.setText(QCoreApplication.translate("DivisionReportWidget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.pushButton_show_all_department.setText(QCoreApplication.translate("DivisionReportWidget", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u044b \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u0441\u043b\u0443\u0436\u0431\u044b", None))
    # retranslateUi

