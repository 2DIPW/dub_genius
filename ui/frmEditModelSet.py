# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmEditModelSet.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import ui.resource_rc

class Ui_frmEditModelSet(object):
    def setupUi(self, frmEditModelSet):
        if not frmEditModelSet.objectName():
            frmEditModelSet.setObjectName(u"frmEditModelSet")
        frmEditModelSet.resize(532, 447)
        icon = QIcon()
        icon.addFile(u":/res/image/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        frmEditModelSet.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(frmEditModelSet)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(frmEditModelSet)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(69, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lneditModelSetName = QLineEdit(self.groupBox)
        self.lneditModelSetName.setObjectName(u"lneditModelSetName")

        self.horizontalLayout_3.addWidget(self.lneditModelSetName)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(69, 0))

        self.horizontalLayout.addWidget(self.label)

        self.lneditGPTModelName = QLineEdit(self.groupBox)
        self.lneditGPTModelName.setObjectName(u"lneditGPTModelName")
        self.lneditGPTModelName.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lneditGPTModelName)

        self.btnPickGPTModel = QPushButton(self.groupBox)
        self.btnPickGPTModel.setObjectName(u"btnPickGPTModel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnPickGPTModel.sizePolicy().hasHeightForWidth())
        self.btnPickGPTModel.setSizePolicy(sizePolicy1)
        self.btnPickGPTModel.setMaximumSize(QSize(35, 20))

        self.horizontalLayout.addWidget(self.btnPickGPTModel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lneditSoVITSModelName = QLineEdit(self.groupBox)
        self.lneditSoVITSModelName.setObjectName(u"lneditSoVITSModelName")
        self.lneditSoVITSModelName.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lneditSoVITSModelName)

        self.btnPickSoVITSModel = QPushButton(self.groupBox)
        self.btnPickSoVITSModel.setObjectName(u"btnPickSoVITSModel")
        sizePolicy1.setHeightForWidth(self.btnPickSoVITSModel.sizePolicy().hasHeightForWidth())
        self.btnPickSoVITSModel.setSizePolicy(sizePolicy1)
        self.btnPickSoVITSModel.setMaximumSize(QSize(35, 20))

        self.horizontalLayout_2.addWidget(self.btnPickSoVITSModel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(frmEditModelSet)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableRefAudioList = QTableWidget(self.groupBox_2)
        if (self.tableRefAudioList.columnCount() < 4):
            self.tableRefAudioList.setColumnCount(4)
        self.tableRefAudioList.setObjectName(u"tableRefAudioList")
        self.tableRefAudioList.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        self.tableRefAudioList.setProperty("showDropIndicator", False)
        self.tableRefAudioList.setSortingEnabled(True)
        self.tableRefAudioList.setColumnCount(4)
        self.tableRefAudioList.horizontalHeader().setHighlightSections(False)
        self.tableRefAudioList.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableRefAudioList)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnAddRefAudio = QPushButton(self.groupBox_2)
        self.btnAddRefAudio.setObjectName(u"btnAddRefAudio")

        self.horizontalLayout_4.addWidget(self.btnAddRefAudio)

        self.btnDeleteRefAudio = QPushButton(self.groupBox_2)
        self.btnDeleteRefAudio.setObjectName(u"btnDeleteRefAudio")

        self.horizontalLayout_4.addWidget(self.btnDeleteRefAudio)

        self.btnSetLangTo = QPushButton(self.groupBox_2)
        self.btnSetLangTo.setObjectName(u"btnSetLangTo")

        self.horizontalLayout_4.addWidget(self.btnSetLangTo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(frmEditModelSet)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_5.addWidget(self.btnSave)

        self.btnCancel = QPushButton(frmEditModelSet)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_5.addWidget(self.btnCancel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.retranslateUi(frmEditModelSet)

        QMetaObject.connectSlotsByName(frmEditModelSet)
    # setupUi

    def retranslateUi(self, frmEditModelSet):
        frmEditModelSet.setWindowTitle(QCoreApplication.translate("frmEditModelSet", u"\u7f16\u8f91\u6a21\u578b\u7ec4", None))
        self.groupBox.setTitle(QCoreApplication.translate("frmEditModelSet", u"\u6a21\u578b\u7ec4", None))
        self.label_3.setText(QCoreApplication.translate("frmEditModelSet", u"\u6a21\u578b\u7ec4\u540d", None))
        self.label.setText(QCoreApplication.translate("frmEditModelSet", u"GPT \u6a21\u578b", None))
        self.btnPickGPTModel.setText(QCoreApplication.translate("frmEditModelSet", u"...", None))
        self.label_2.setText(QCoreApplication.translate("frmEditModelSet", u"SoVITS \u6a21\u578b", None))
        self.btnPickSoVITSModel.setText(QCoreApplication.translate("frmEditModelSet", u"...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("frmEditModelSet", u"\u53c2\u8003\u97f3\u9891\u7ec4", None))
        self.btnAddRefAudio.setText(QCoreApplication.translate("frmEditModelSet", u"\u6dfb\u52a0", None))
        self.btnDeleteRefAudio.setText(QCoreApplication.translate("frmEditModelSet", u"\u5220\u9664", None))
        self.btnSetLangTo.setText(QCoreApplication.translate("frmEditModelSet", u"\u6279\u91cf\u8bbe\u7f6e\u8bed\u8a00\u4e3a", None))
        self.btnSave.setText(QCoreApplication.translate("frmEditModelSet", u"\u4fdd\u5b58", None))
        self.btnCancel.setText(QCoreApplication.translate("frmEditModelSet", u"\u53d6\u6d88", None))
    # retranslateUi

