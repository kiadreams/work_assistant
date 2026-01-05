# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_edit_data_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    Qt,
)
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QVBoxLayout,
)


class Ui_DialogEditData(object):
    def setupUi(self, DialogEditData):
        if not DialogEditData.objectName():
            DialogEditData.setObjectName("DialogEditData")
        DialogEditData.resize(986, 307)
        self.verticalLayout_2 = QVBoxLayout(DialogEditData)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_table_name = QLabel(DialogEditData)
        self.label_table_name.setObjectName("label_table_name")

        self.verticalLayout.addWidget(self.label_table_name)

        self.tableWidget_data = QTableWidget(DialogEditData)
        self.tableWidget_data.setObjectName("tableWidget_data")

        self.verticalLayout.addWidget(self.tableWidget_data)

        self.buttonBox_exit = QDialogButtonBox(DialogEditData)
        self.buttonBox_exit.setObjectName("buttonBox_exit")
        self.buttonBox_exit.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox_exit.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )

        self.verticalLayout.addWidget(self.buttonBox_exit)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DialogEditData)
        self.buttonBox_exit.accepted.connect(DialogEditData.accept)
        self.buttonBox_exit.rejected.connect(DialogEditData.reject)

        QMetaObject.connectSlotsByName(DialogEditData)

    # setupUi

    def retranslateUi(self, DialogEditData):
        DialogEditData.setWindowTitle(QCoreApplication.translate("DialogEditData", "Dialog", None))
        self.label_table_name.setText(
            QCoreApplication.translate("DialogEditData", "TextLabel", None)
        )

    # retranslateUi
