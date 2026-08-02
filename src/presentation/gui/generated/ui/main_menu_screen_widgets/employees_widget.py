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
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

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

        self.to_main_menu_btn = QPushButton(EmployeesWidget)
        self.to_main_menu_btn.setObjectName(u"to_main_menu_btn")

        self.horizontalLayout_4.addWidget(self.to_main_menu_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.delete_employee_btn = QPushButton(EmployeesWidget)
        self.delete_employee_btn.setObjectName(u"delete_employee_btn")

        self.gridLayout.addWidget(self.delete_employee_btn, 3, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 3, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 2, 1)

        self.employee_data_table_title = QLabel(EmployeesWidget)
        self.employee_data_table_title.setObjectName(u"employee_data_table_title")

        self.gridLayout.addWidget(self.employee_data_table_title, 1, 2, 1, 1)

        self.add_employee_btn = QPushButton(EmployeesWidget)
        self.add_employee_btn.setObjectName(u"add_employee_btn")

        self.gridLayout.addWidget(self.add_employee_btn, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.division_list_title = QLabel(EmployeesWidget)
        self.division_list_title.setObjectName(u"division_list_title")

        self.horizontalLayout_2.addWidget(self.division_list_title)

        self.division_list = QComboBox(EmployeesWidget)
        self.division_list.setObjectName(u"division_list")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.division_list.sizePolicy().hasHeightForWidth())
        self.division_list.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.division_list)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.department_list_title = QLabel(EmployeesWidget)
        self.department_list_title.setObjectName(u"department_list_title")

        self.horizontalLayout_2.addWidget(self.department_list_title)

        self.department_list = QComboBox(EmployeesWidget)
        self.department_list.setObjectName(u"department_list")
        sizePolicy.setHeightForWidth(self.department_list.sizePolicy().hasHeightForWidth())
        self.department_list.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.department_list)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 4)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 2, 1, 1)

        self.employee_data_table = QTableView(EmployeesWidget)
        self.employee_data_table.setObjectName(u"employee_data_table")

        self.gridLayout.addWidget(self.employee_data_table, 2, 2, 3, 1)

        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_2.setStretch(2, 1)

        self.retranslateUi(EmployeesWidget)

        QMetaObject.connectSlotsByName(EmployeesWidget)
    # setupUi

    def retranslateUi(self, EmployeesWidget):
        EmployeesWidget.setWindowTitle(QCoreApplication.translate("EmployeesWidget", u"Form", None))
        self.to_main_menu_btn.setText(QCoreApplication.translate("EmployeesWidget", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.delete_employee_btn.setText(QCoreApplication.translate("EmployeesWidget", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.employee_data_table_title.setText(QCoreApplication.translate("EmployeesWidget", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u043a\u0440\u0441\u043e\u043d\u0430\u043b\u0430:", None))
        self.add_employee_btn.setText(QCoreApplication.translate("EmployeesWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.division_list_title.setText(QCoreApplication.translate("EmployeesWidget", u" \u0421\u043b\u0443\u0436\u0431\u0430", None))
        self.department_list_title.setText(QCoreApplication.translate("EmployeesWidget", u"\u0413\u0440\u0443\u043f\u043f\u0430 / \u0443\u0447\u0430\u0441\u0442\u043e\u043a", None))
    # retranslateUi

