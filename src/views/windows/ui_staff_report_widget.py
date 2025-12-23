# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_staff_report_widget.ui'
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

class Ui_StaffReportsWidget(object):
    def setupUi(self, StaffReportsWidget):
        if not StaffReportsWidget.objectName():
            StaffReportsWidget.setObjectName(u"StaffReportsWidget")
        StaffReportsWidget.resize(886, 739)
        self.verticalLayout_2 = QVBoxLayout(StaffReportsWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_sirvice_list_title = QLabel(StaffReportsWidget)
        self.label_sirvice_list_title.setObjectName(u"label_sirvice_list_title")

        self.horizontalLayout_2.addWidget(self.label_sirvice_list_title)

        self.comboBox_service_list = QComboBox(StaffReportsWidget)
        self.comboBox_service_list.setObjectName(u"comboBox_service_list")

        self.horizontalLayout_2.addWidget(self.comboBox_service_list)

        self.label_group_list_title = QLabel(StaffReportsWidget)
        self.label_group_list_title.setObjectName(u"label_group_list_title")

        self.horizontalLayout_2.addWidget(self.label_group_list_title)

        self.comboBox_group_list = QComboBox(StaffReportsWidget)
        self.comboBox_group_list.setObjectName(u"comboBox_group_list")

        self.horizontalLayout_2.addWidget(self.comboBox_group_list)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(StaffReportsWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBox_service_list_2 = QComboBox(StaffReportsWidget)
        self.comboBox_service_list_2.setObjectName(u"comboBox_service_list_2")

        self.verticalLayout.addWidget(self.comboBox_service_list_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(StaffReportsWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(StaffReportsWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(StaffReportsWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_4 = QPushButton(StaffReportsWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tableWidget_service_data_table = QTableWidget(StaffReportsWidget)
        self.tableWidget_service_data_table.setObjectName(u"tableWidget_service_data_table")

        self.verticalLayout_2.addWidget(self.tableWidget_service_data_table)


        self.retranslateUi(StaffReportsWidget)

        QMetaObject.connectSlotsByName(StaffReportsWidget)
    # setupUi

    def retranslateUi(self, StaffReportsWidget):
        StaffReportsWidget.setWindowTitle(QCoreApplication.translate("StaffReportsWidget", u"Form", None))
        self.label_sirvice_list_title.setText(QCoreApplication.translate("StaffReportsWidget", u" \u0421\u043b\u0443\u0436\u0431\u0430", None))
        self.label_group_list_title.setText(QCoreApplication.translate("StaffReportsWidget", u"\u0413\u0440\u0443\u043f\u043f\u0430 / \u0443\u0447\u0430\u0441\u0442\u043e\u043a", None))
        self.label.setText(QCoreApplication.translate("StaffReportsWidget", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.pushButton.setText(QCoreApplication.translate("StaffReportsWidget", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("StaffReportsWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("StaffReportsWidget", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.pushButton_4.setText(QCoreApplication.translate("StaffReportsWidget", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0435\u0441\u044c \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
    # retranslateUi

