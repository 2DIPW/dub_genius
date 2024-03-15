# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmMain.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)
import ui.resource_rc

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        if not frmMain.objectName():
            frmMain.setObjectName(u"frmMain")
        frmMain.resize(290, 420)
        frmMain.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/res/image/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        frmMain.setWindowIcon(icon)
        self.centralwidget = QWidget(frmMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.grpboxSynthesis = QGroupBox(self.centralwidget)
        self.grpboxSynthesis.setObjectName(u"grpboxSynthesis")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpboxSynthesis.sizePolicy().hasHeightForWidth())
        self.grpboxSynthesis.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.grpboxSynthesis)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hlayModelSelect = QHBoxLayout()
        self.hlayModelSelect.setObjectName(u"hlayModelSelect")
        self.label_5 = QLabel(self.grpboxSynthesis)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.hlayModelSelect.addWidget(self.label_5)

        self.btnManageModelSets = QPushButton(self.grpboxSynthesis)
        self.btnManageModelSets.setObjectName(u"btnManageModelSets")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnManageModelSets.sizePolicy().hasHeightForWidth())
        self.btnManageModelSets.setSizePolicy(sizePolicy2)
        self.btnManageModelSets.setMaximumSize(QSize(40, 16777215))

        self.hlayModelSelect.addWidget(self.btnManageModelSets)


        self.verticalLayout.addLayout(self.hlayModelSelect)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.grpboxSynthesis)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.txteditText = QTextEdit(self.grpboxSynthesis)
        self.txteditText.setObjectName(u"txteditText")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txteditText.sizePolicy().hasHeightForWidth())
        self.txteditText.setSizePolicy(sizePolicy3)
        self.txteditText.setMaximumSize(QSize(16777215, 74))
        self.txteditText.setAcceptRichText(False)

        self.horizontalLayout_3.addWidget(self.txteditText)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.grpboxSynthesis)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.spinboxTopK = QSpinBox(self.grpboxSynthesis)
        self.spinboxTopK.setObjectName(u"spinboxTopK")
        sizePolicy2.setHeightForWidth(self.spinboxTopK.sizePolicy().hasHeightForWidth())
        self.spinboxTopK.setSizePolicy(sizePolicy2)
        self.spinboxTopK.setMinimumSize(QSize(46, 0))
        self.spinboxTopK.setMaximumSize(QSize(46, 16777215))
        self.spinboxTopK.setMinimum(1)
        self.spinboxTopK.setMaximum(100)
        self.spinboxTopK.setValue(5)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinboxTopK)

        self.label_7 = QLabel(self.grpboxSynthesis)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.grpboxSynthesis)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.spinboxTopP = QDoubleSpinBox(self.grpboxSynthesis)
        self.spinboxTopP.setObjectName(u"spinboxTopP")
        sizePolicy2.setHeightForWidth(self.spinboxTopP.sizePolicy().hasHeightForWidth())
        self.spinboxTopP.setSizePolicy(sizePolicy2)
        self.spinboxTopP.setMaximum(1.000000000000000)
        self.spinboxTopP.setSingleStep(0.050000000000000)
        self.spinboxTopP.setValue(1.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinboxTopP)

        self.spinboxTemp = QDoubleSpinBox(self.grpboxSynthesis)
        self.spinboxTemp.setObjectName(u"spinboxTemp")
        sizePolicy2.setHeightForWidth(self.spinboxTemp.sizePolicy().hasHeightForWidth())
        self.spinboxTemp.setSizePolicy(sizePolicy2)
        self.spinboxTemp.setMaximum(1.000000000000000)
        self.spinboxTemp.setSingleStep(0.050000000000000)
        self.spinboxTemp.setValue(1.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinboxTemp)


        self.horizontalLayout_3.addLayout(self.formLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.grpboxSynthesis)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(25, 0))

        self.horizontalLayout.addWidget(self.label)

        self.comboboxTextLang = QComboBox(self.grpboxSynthesis)
        self.comboboxTextLang.setObjectName(u"comboboxTextLang")

        self.horizontalLayout.addWidget(self.comboboxTextLang)

        self.label_12 = QLabel(self.grpboxSynthesis)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_12)

        self.comboboxHowToCut = QComboBox(self.grpboxSynthesis)
        self.comboboxHowToCut.setObjectName(u"comboboxHowToCut")

        self.horizontalLayout.addWidget(self.comboboxHowToCut)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sliderPlayback = QSlider(self.grpboxSynthesis)
        self.sliderPlayback.setObjectName(u"sliderPlayback")
        self.sliderPlayback.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.sliderPlayback)

        self.labelPlaybackTime = QLabel(self.grpboxSynthesis)
        self.labelPlaybackTime.setObjectName(u"labelPlaybackTime")

        self.horizontalLayout_12.addWidget(self.labelPlaybackTime)

        self.btnPlayPause = QPushButton(self.grpboxSynthesis)
        self.btnPlayPause.setObjectName(u"btnPlayPause")
        sizePolicy2.setHeightForWidth(self.btnPlayPause.sizePolicy().hasHeightForWidth())
        self.btnPlayPause.setSizePolicy(sizePolicy2)
        self.btnPlayPause.setMinimumSize(QSize(35, 0))
        self.btnPlayPause.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_12.addWidget(self.btnPlayPause)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnSynthesize = QPushButton(self.grpboxSynthesis)
        self.btnSynthesize.setObjectName(u"btnSynthesize")

        self.horizontalLayout_5.addWidget(self.btnSynthesize)

        self.btnSave = QPushButton(self.grpboxSynthesis)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_5.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.grpboxSynthesis)

        self.grpboxResult = QGroupBox(self.centralwidget)
        self.grpboxResult.setObjectName(u"grpboxResult")
        sizePolicy.setHeightForWidth(self.grpboxResult.sizePolicy().hasHeightForWidth())
        self.grpboxResult.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.grpboxResult)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.grpboxResult)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.lneditProjectPath = QLineEdit(self.grpboxResult)
        self.lneditProjectPath.setObjectName(u"lneditProjectPath")
        sizePolicy3.setHeightForWidth(self.lneditProjectPath.sizePolicy().hasHeightForWidth())
        self.lneditProjectPath.setSizePolicy(sizePolicy3)
        self.lneditProjectPath.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_11.addWidget(self.lneditProjectPath)

        self.btnPickProjectPath = QPushButton(self.grpboxResult)
        self.btnPickProjectPath.setObjectName(u"btnPickProjectPath")
        sizePolicy2.setHeightForWidth(self.btnPickProjectPath.sizePolicy().hasHeightForWidth())
        self.btnPickProjectPath.setSizePolicy(sizePolicy2)
        self.btnPickProjectPath.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_11.addWidget(self.btnPickProjectPath)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.vlayAudioList = QVBoxLayout()
        self.vlayAudioList.setObjectName(u"vlayAudioList")

        self.verticalLayout_2.addLayout(self.vlayAudioList)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.chkboxAlwaysTop = QCheckBox(self.grpboxResult)
        self.chkboxAlwaysTop.setObjectName(u"chkboxAlwaysTop")
        self.chkboxAlwaysTop.setChecked(True)

        self.horizontalLayout_13.addWidget(self.chkboxAlwaysTop)

        self.chkboxAutoTrans = QCheckBox(self.grpboxResult)
        self.chkboxAutoTrans.setObjectName(u"chkboxAutoTrans")
        self.chkboxAutoTrans.setChecked(True)

        self.horizontalLayout_13.addWidget(self.chkboxAutoTrans)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.labelAbout = QLabel(self.grpboxResult)
        self.labelAbout.setObjectName(u"labelAbout")
        sizePolicy2.setHeightForWidth(self.labelAbout.sizePolicy().hasHeightForWidth())
        self.labelAbout.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setBold(True)
        font.setItalic(True)
        self.labelAbout.setFont(font)
        self.labelAbout.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.labelAbout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)


        self.verticalLayout_4.addWidget(self.grpboxResult)

        frmMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmMain)

        QMetaObject.connectSlotsByName(frmMain)
    # setupUi

    def retranslateUi(self, frmMain):
        frmMain.setWindowTitle(QCoreApplication.translate("frmMain", u"Dub Genius", None))
        self.grpboxSynthesis.setTitle(QCoreApplication.translate("frmMain", u"\u914d\u97f3\u5408\u6210", None))
        self.label_5.setText(QCoreApplication.translate("frmMain", u"\u6a21\u578b", None))
        self.btnManageModelSets.setText(QCoreApplication.translate("frmMain", u"\u7ba1\u7406", None))
        self.label_9.setText(QCoreApplication.translate("frmMain", u"\u6587\u672c", None))
        self.label_2.setText(QCoreApplication.translate("frmMain", u"top_k", None))
        self.label_7.setText(QCoreApplication.translate("frmMain", u"top_p", None))
        self.label_8.setText(QCoreApplication.translate("frmMain", u"temp", None))
        self.label.setText(QCoreApplication.translate("frmMain", u"\u8bed\u8a00", None))
        self.label_12.setText(QCoreApplication.translate("frmMain", u"\u5207\u5206", None))
        self.labelPlaybackTime.setText(QCoreApplication.translate("frmMain", u"00:00/00:00", None))
        self.btnPlayPause.setText(QCoreApplication.translate("frmMain", u"\u25b6\u2016", None))
        self.btnSynthesize.setText(QCoreApplication.translate("frmMain", u"\u5408\u6210", None))
        self.btnSave.setText(QCoreApplication.translate("frmMain", u"\u4fdd\u5b58", None))
        self.grpboxResult.setTitle(QCoreApplication.translate("frmMain", u"\u5408\u6210\u7ed3\u679c\u5217\u8868", None))
        self.label_6.setText(QCoreApplication.translate("frmMain", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.btnPickProjectPath.setText(QCoreApplication.translate("frmMain", u"...", None))
        self.chkboxAlwaysTop.setText(QCoreApplication.translate("frmMain", u"\u7a97\u53e3\u7f6e\u9876", None))
        self.chkboxAutoTrans.setText(QCoreApplication.translate("frmMain", u"\u81ea\u52a8\u900f\u660e", None))
        self.labelAbout.setText(QCoreApplication.translate("frmMain", u"Dub Genius by 2DIPW", None))
    # retranslateUi

