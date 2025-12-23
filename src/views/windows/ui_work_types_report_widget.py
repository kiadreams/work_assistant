# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_work_types_report_widget.ui'
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

class Ui_WorkTypeReportsWidget(object):
    def setupUi(self, WorkTypeReportsWidget):
        if not WorkTypeReportsWidget.objectName():
            WorkTypeReportsWidget.setObjectName(u"WorkTypeReportsWidget")
        WorkTypeReportsWidget.resize(886, 739)
        self.verticalLayout_2 = QVBoxLayout(WorkTypeReportsWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(WorkTypeReportsWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBox_service_list_2 = QComboBox(WorkTypeReportsWidget)
        self.comboBox_service_list_2.setObjectName(u"comboBox_service_list_2")

        self.verticalLayout.addWidget(self.comboBox_service_list_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(WorkTypeReportsWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(WorkTypeReportsWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(WorkTypeReportsWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_4 = QPushButton(WorkTypeReportsWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tableWidget_service_data_table = QTableWidget(WorkTypeReportsWidget)
        self.tableWidget_service_data_table.setObjectName(u"tableWidget_service_data_table")

        self.verticalLayout_2.addWidget(self.tableWidget_service_data_table)


        self.retranslateUi(WorkTypeReportsWidget)

        QMetaObject.connectSlotsByName(WorkTypeReportsWidget)
    # setupUi

    def retranslateUi(self, WorkTypeReportsWidget):
        WorkTypeReportsWidget.setWindowTitle(QCoreApplication.translate("WorkTypeReportsWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("WorkTypeReportsWidget", u"\u0412\u0438\u0434\u044b \u0440\u0430\u0431\u043e\u0442:", None))
        self.pushButton.setText(QCoreApplication.translate("WorkTypeReportsWidget", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("WorkTypeReportsWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("WorkTypeReportsWidget", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.pushButton_4.setText(QCoreApplication.translate("WorkTypeReportsWidget", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u0442\u0438\u043f\u044b \u0440\u0430\u0431\u043e\u0442", None))
    # retranslateUi

