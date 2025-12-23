# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_report_generation_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_ReportGenerationWidget(object):
    def setupUi(self, ReportGenerationWidget):
        if not ReportGenerationWidget.objectName():
            ReportGenerationWidget.setObjectName(u"ReportGenerationWidget")
        ReportGenerationWidget.resize(1250, 849)
        self.verticalLayout_3 = QVBoxLayout(ReportGenerationWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_go_to_main_menu = QPushButton(ReportGenerationWidget)
        self.pushButton_go_to_main_menu.setObjectName(u"pushButton_go_to_main_menu")

        self.horizontalLayout.addWidget(self.pushButton_go_to_main_menu)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_prefix_company = QLabel(ReportGenerationWidget)
        self.label_prefix_company.setObjectName(u"label_prefix_company")

        self.horizontalLayout_2.addWidget(self.label_prefix_company)

        self.comboBox_company = QComboBox(ReportGenerationWidget)
        self.comboBox_company.setObjectName(u"comboBox_company")
        self.comboBox_company.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.comboBox_company)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_services = QPushButton(ReportGenerationWidget)
        self.pushButton_services.setObjectName(u"pushButton_services")
        self.pushButton_services.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_services)

        self.pushButton_staff = QPushButton(ReportGenerationWidget)
        self.pushButton_staff.setObjectName(u"pushButton_staff")
        self.pushButton_staff.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_staff)

        self.pushButton_work_types = QPushButton(ReportGenerationWidget)
        self.pushButton_work_types.setObjectName(u"pushButton_work_types")
        self.pushButton_work_types.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_work_types)

        self.pushButton_works = QPushButton(ReportGenerationWidget)
        self.pushButton_works.setObjectName(u"pushButton_works")
        self.pushButton_works.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_works)

        self.pushButton_orders = QPushButton(ReportGenerationWidget)
        self.pushButton_orders.setObjectName(u"pushButton_orders")
        self.pushButton_orders.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_orders)

        self.pushButton_work_events = QPushButton(ReportGenerationWidget)
        self.pushButton_work_events.setObjectName(u"pushButton_work_events")
        self.pushButton_work_events.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_work_events)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.stackedWidget_types_of_reports = QStackedWidget(ReportGenerationWidget)
        self.stackedWidget_types_of_reports.setObjectName(u"stackedWidget_types_of_reports")
        self.page_0_services_and_goups = QWidget()
        self.page_0_services_and_goups.setObjectName(u"page_0_services_and_goups")
        self.stackedWidget_types_of_reports.addWidget(self.page_0_services_and_goups)
        self.page_1_staff = QWidget()
        self.page_1_staff.setObjectName(u"page_1_staff")
        self.stackedWidget_types_of_reports.addWidget(self.page_1_staff)
        self.page_2_types_of_work = QWidget()
        self.page_2_types_of_work.setObjectName(u"page_2_types_of_work")
        self.stackedWidget_types_of_reports.addWidget(self.page_2_types_of_work)
        self.page_3_works = QWidget()
        self.page_3_works.setObjectName(u"page_3_works")
        self.stackedWidget_types_of_reports.addWidget(self.page_3_works)
        self.page_4_orders = QWidget()
        self.page_4_orders.setObjectName(u"page_4_orders")
        self.stackedWidget_types_of_reports.addWidget(self.page_4_orders)
        self.page_5_work_events = QWidget()
        self.page_5_work_events.setObjectName(u"page_5_work_events")
        self.stackedWidget_types_of_reports.addWidget(self.page_5_work_events)

        self.horizontalLayout_3.addWidget(self.stackedWidget_types_of_reports)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(ReportGenerationWidget)

        self.stackedWidget_types_of_reports.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(ReportGenerationWidget)
    # setupUi

    def retranslateUi(self, ReportGenerationWidget):
        ReportGenerationWidget.setWindowTitle(QCoreApplication.translate("ReportGenerationWidget", u"Form", None))
        self.pushButton_go_to_main_menu.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label_prefix_company.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0435:", None))
        self.pushButton_services.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton_staff.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.pushButton_work_types.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0432\u0438\u0434\u044b \u0440\u0430\u0431\u043e\u0442", None))
        self.pushButton_works.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.pushButton_orders.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0437\u0430\u043a\u0430\u0437\u044b", None))
        self.pushButton_work_events.setText(QCoreApplication.translate("ReportGenerationWidget", u"\u0440\u0430\u0431\u043e\u0447\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
    # retranslateUi

