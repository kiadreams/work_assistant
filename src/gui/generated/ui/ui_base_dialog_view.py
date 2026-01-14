# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_base_dialog_view.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_BaseDialogView(object):
    def setupUi(self, BaseDialogView):
        if not BaseDialogView.objectName():
            BaseDialogView.setObjectName(u"BaseDialogView")
        BaseDialogView.resize(986, 307)
        self.verticalLayout_2 = QVBoxLayout(BaseDialogView)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.labelTitleDialog = QLabel(BaseDialogView)
        self.labelTitleDialog.setObjectName(u"labelTitleDialog")

        self.verticalLayout.addWidget(self.labelTitleDialog)

        self.buttonBox_exit = QDialogButtonBox(BaseDialogView)
        self.buttonBox_exit.setObjectName(u"buttonBox_exit")
        self.buttonBox_exit.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox_exit.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox_exit)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(BaseDialogView)
        self.buttonBox_exit.accepted.connect(BaseDialogView.accept)
        self.buttonBox_exit.rejected.connect(BaseDialogView.reject)

        QMetaObject.connectSlotsByName(BaseDialogView)
    # setupUi

    def retranslateUi(self, BaseDialogView):
        BaseDialogView.setWindowTitle(QCoreApplication.translate("BaseDialogView", u"Dialog", None))
        self.labelTitleDialog.setText(QCoreApplication.translate("BaseDialogView", u"TextLabel", None))
    # retranslateUi

