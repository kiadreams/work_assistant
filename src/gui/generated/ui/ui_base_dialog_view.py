# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_base_dialog_view.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
)
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QVBoxLayout,
)


class Ui_BaseDialogView(object):
    def setupUi(self, BaseDialogView):
        if not BaseDialogView.objectName():
            BaseDialogView.setObjectName("BaseDialogView")
        BaseDialogView.resize(986, 307)
        self.verticalLayout = QVBoxLayout(BaseDialogView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonBox_exit = QDialogButtonBox(BaseDialogView)
        self.buttonBox_exit.setObjectName("buttonBox_exit")
        self.buttonBox_exit.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )

        self.verticalLayout.addWidget(self.buttonBox_exit)

        self.retranslateUi(BaseDialogView)

        QMetaObject.connectSlotsByName(BaseDialogView)

    # setupUi

    def retranslateUi(self, BaseDialogView):
        BaseDialogView.setWindowTitle(QCoreApplication.translate("BaseDialogView", "Dialog", None))

    # retranslateUi
