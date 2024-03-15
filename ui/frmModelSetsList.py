# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmModelSetsList.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import ui.resource_rc

class Ui_frmModelSetsList(object):
    def setupUi(self, frmModelSetsList):
        if not frmModelSetsList.objectName():
            frmModelSetsList.setObjectName(u"frmModelSetsList")
        frmModelSetsList.resize(592, 358)
        icon = QIcon()
        icon.addFile(u":/res/image/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        frmModelSetsList.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(frmModelSetsList)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableModelSetsList = QTableWidget(frmModelSetsList)
        if (self.tableModelSetsList.columnCount() < 4):
            self.tableModelSetsList.setColumnCount(4)
        self.tableModelSetsList.setObjectName(u"tableModelSetsList")
        self.tableModelSetsList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableModelSetsList.setProperty("showDropIndicator", False)
        self.tableModelSetsList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableModelSetsList.setColumnCount(4)
        self.tableModelSetsList.horizontalHeader().setHighlightSections(False)

        self.horizontalLayout.addWidget(self.tableModelSetsList)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnAddModelSet = QPushButton(frmModelSetsList)
        self.btnAddModelSet.setObjectName(u"btnAddModelSet")

        self.verticalLayout.addWidget(self.btnAddModelSet)

        self.btnEditModelSet = QPushButton(frmModelSetsList)
        self.btnEditModelSet.setObjectName(u"btnEditModelSet")

        self.verticalLayout.addWidget(self.btnEditModelSet)

        self.btnCopyModelSet = QPushButton(frmModelSetsList)
        self.btnCopyModelSet.setObjectName(u"btnCopyModelSet")

        self.verticalLayout.addWidget(self.btnCopyModelSet)

        self.btnDeleteModelSet = QPushButton(frmModelSetsList)
        self.btnDeleteModelSet.setObjectName(u"btnDeleteModelSet")

        self.verticalLayout.addWidget(self.btnDeleteModelSet)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnSave = QPushButton(frmModelSetsList)
        self.btnSave.setObjectName(u"btnSave")

        self.verticalLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(frmModelSetsList)
        self.btnCancel.setObjectName(u"btnCancel")

        self.verticalLayout.addWidget(self.btnCancel)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(frmModelSetsList)

        QMetaObject.connectSlotsByName(frmModelSetsList)
    # setupUi

    def retranslateUi(self, frmModelSetsList):
        frmModelSetsList.setWindowTitle(QCoreApplication.translate("frmModelSetsList", u"\u6a21\u578b\u7ec4\u5217\u8868", None))
        self.btnAddModelSet.setText(QCoreApplication.translate("frmModelSetsList", u"\u6dfb\u52a0", None))
        self.btnEditModelSet.setText(QCoreApplication.translate("frmModelSetsList", u"\u7f16\u8f91", None))
        self.btnCopyModelSet.setText(QCoreApplication.translate("frmModelSetsList", u"\u590d\u5236", None))
        self.btnDeleteModelSet.setText(QCoreApplication.translate("frmModelSetsList", u"\u5220\u9664", None))
        self.btnSave.setText(QCoreApplication.translate("frmModelSetsList", u"\u4fdd\u5b58", None))
        self.btnCancel.setText(QCoreApplication.translate("frmModelSetsList", u"\u53d6\u6d88", None))
    # retranslateUi

