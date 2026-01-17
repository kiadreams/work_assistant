# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_menu_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
)
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)


class Ui_MainMenuWidget(object):
    def setupUi(self, MainMenuWidget):
        if not MainMenuWidget.objectName():
            MainMenuWidget.setObjectName("MainMenuWidget")
        MainMenuWidget.resize(1206, 819)
        self.gridLayout = QGridLayout(MainMenuWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_app_title = QLabel(MainMenuWidget)
        self.label_app_title.setObjectName("label_app_title")

        self.verticalLayout.addWidget(self.label_app_title)

        self.label_app_version = QLabel(MainMenuWidget)
        self.label_app_version.setObjectName("label_app_version")

        self.verticalLayout.addWidget(self.label_app_version)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_create_sheets = QPushButton(MainMenuWidget)
        self.pushButton_create_sheets.setObjectName("pushButton_create_sheets")

        self.verticalLayout_2.addWidget(self.pushButton_create_sheets)

        self.pushButton_create_protocols = QPushButton(MainMenuWidget)
        self.pushButton_create_protocols.setObjectName("pushButton_create_protocols")

        self.verticalLayout_2.addWidget(self.pushButton_create_protocols)

        self.pushButton_exit = QPushButton(MainMenuWidget)
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.verticalLayout_2.addWidget(self.pushButton_exit)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.plainTextEdit_logs = QPlainTextEdit(MainMenuWidget)
        self.plainTextEdit_logs.setObjectName("plainTextEdit_logs")
        self.plainTextEdit_logs.setMinimumSize(QSize(0, 20))
        self.plainTextEdit_logs.setUndoRedoEnabled(False)
        self.plainTextEdit_logs.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.plainTextEdit_logs)

        self.verticalLayout_3.setStretch(1, 5)
        self.verticalLayout_3.setStretch(3, 5)
        self.verticalLayout_3.setStretch(4, 2)

        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(MainMenuWidget)

        QMetaObject.connectSlotsByName(MainMenuWidget)

    # setupUi

    def retranslateUi(self, MainMenuWidget):
        MainMenuWidget.setWindowTitle(QCoreApplication.translate("MainMenuWidget", "Form", None))
        self.label_app_title.setText(
            QCoreApplication.translate(
                "MainMenuWidget",
                "\u0440\u0430\u0431\u043e\u0447\u0438\u0439 \u0430\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442",
                None,
            )
        )
        self.label_app_version.setText(
            QCoreApplication.translate(
                "MainMenuWidget",
                "\u0432\u0435\u0440\u0441\u0438\u044f \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f: 1.1.1",
                None,
            )
        )
        self.pushButton_create_sheets.setText(
            QCoreApplication.translate(
                "MainMenuWidget",
                "\u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0432\u0435\u0434\u043e\u043c\u043e\u0441\u0442\u0435\u0439 \u0440\u0430\u0431\u043e\u0442",
                None,
            )
        )
        self.pushButton_create_protocols.setText(
            QCoreApplication.translate(
                "MainMenuWidget",
                "\u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b\u043e\u0432",
                None,
            )
        )
        self.pushButton_exit.setText(
            QCoreApplication.translate(
                "MainMenuWidget",
                "\u0432\u044b\u0439\u0442\u0438 \u0438\u0437 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f",
                None,
            )
        )

    # retranslateUi
