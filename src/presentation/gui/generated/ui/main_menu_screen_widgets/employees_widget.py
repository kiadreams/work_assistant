# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employees_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_EmployeesWidget(object):
    def setupUi(self, EmployeesWidget):
        if not EmployeesWidget.objectName():
            EmployeesWidget.setObjectName(u"EmployeesWidget")
        EmployeesWidget.resize(1005, 932)
        self.verticalLayout_2 = QVBoxLayout(EmployeesWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_to_main_menu = QPushButton(EmployeesWidget)
        self.pushButton_to_main_menu.setObjectName(u"pushButton_to_main_menu")

        self.horizontalLayout_4.addWidget(self.pushButton_to_main_menu)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_employees_data_table = QTableWidget(EmployeesWidget)
        self.tableWidget_employees_data_table.setObjectName(u"tableWidget_employees_data_table")

        self.gridLayout.addWidget(self.tableWidget_employees_data_table, 2, 2, 4, 1)

        self.label = QLabel(EmployeesWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 3, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 2, 1)

        self.pushButton_add_employee = QPushButton(EmployeesWidget)
        self.pushButton_add_employee.setObjectName(u"pushButton_add_employee")

        self.gridLayout.addWidget(self.pushButton_add_employee, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_division_list_title = QLabel(EmployeesWidget)
        self.label_division_list_title.setObjectName(u"label_division_list_title")

        self.horizontalLayout_2.addWidget(self.label_division_list_title)

        self.comboBox_division_list_2 = QComboBox(EmployeesWidget)
        self.comboBox_division_list_2.setObjectName(u"comboBox_division_list_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_division_list_2.sizePolicy().hasHeightForWidth())
        self.comboBox_division_list_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.comboBox_division_list_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.label_department_list_title = QLabel(EmployeesWidget)
        self.label_department_list_title.setObjectName(u"label_department_list_title")

        self.horizontalLayout_2.addWidget(self.label_department_list_title)

        self.comboBox_department_list = QComboBox(EmployeesWidget)
        self.comboBox_department_list.setObjectName(u"comboBox_department_list")
        sizePolicy.setHeightForWidth(self.comboBox_department_list.sizePolicy().hasHeightForWidth())
        self.comboBox_department_list.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.comboBox_department_list)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 4)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)

        self.pushButton_delete_employee = QPushButton(EmployeesWidget)
        self.pushButton_delete_employee.setObjectName(u"pushButton_delete_employee")

        self.gridLayout.addWidget(self.pushButton_delete_employee, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_2.setStretch(2, 1)

        self.retranslateUi(EmployeesWidget)

        QMetaObject.connectSlotsByName(EmployeesWidget)
    # setupUi

    def retranslateUi(self, EmployeesWidget):
        EmployeesWidget.setWindowTitle(QCoreApplication.translate("EmployeesWidget", u"Form", None))
        self.pushButton_to_main_menu.setText(QCoreApplication.translate("EmployeesWidget", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label.setText(QCoreApplication.translate("EmployeesWidget", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u043a\u0440\u0441\u043e\u043d\u0430\u043b\u0430:", None))
        self.pushButton_add_employee.setText(QCoreApplication.translate("EmployeesWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_division_list_title.setText(QCoreApplication.translate("EmployeesWidget", u" \u0421\u043b\u0443\u0436\u0431\u0430", None))
        self.label_department_list_title.setText(QCoreApplication.translate("EmployeesWidget", u"\u0413\u0440\u0443\u043f\u043f\u0430 / \u0443\u0447\u0430\u0441\u0442\u043e\u043a", None))
        self.pushButton_delete_employee.setText(QCoreApplication.translate("EmployeesWidget", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
    # retranslateUi

