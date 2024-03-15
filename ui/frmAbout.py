# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmAbout.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_frmAbout(object):
    def setupUi(self, frmAbout):
        if not frmAbout.objectName():
            frmAbout.setObjectName(u"frmAbout")
        frmAbout.resize(446, 136)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmAbout.sizePolicy().hasHeightForWidth())
        frmAbout.setSizePolicy(sizePolicy)
        frmAbout.setMinimumSize(QSize(446, 136))
        frmAbout.setMaximumSize(QSize(446, 136))
        self.labelLogo = QLabel(frmAbout)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setGeometry(QRect(13, 16, 64, 64))
        sizePolicy.setHeightForWidth(self.labelLogo.sizePolicy().hasHeightForWidth())
        self.labelLogo.setSizePolicy(sizePolicy)
        self.labelLogo.setMinimumSize(QSize(64, 64))
        self.labelLogo.setMaximumSize(QSize(64, 64))
        self.labelLogo.setScaledContents(True)
        self.labelInfo = QLabel(frmAbout)
        self.labelInfo.setObjectName(u"labelInfo")
        self.labelInfo.setGeometry(QRect(90, 15, 351, 81))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.labelInfo.setFont(font)
        self.btnClose = QPushButton(frmAbout)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(360, 100, 75, 23))
        self.labelQtLogo = QLabel(frmAbout)
        self.labelQtLogo.setObjectName(u"labelQtLogo")
        self.labelQtLogo.setGeometry(QRect(335, 15, 96, 23))
        sizePolicy.setHeightForWidth(self.labelQtLogo.sizePolicy().hasHeightForWidth())
        self.labelQtLogo.setSizePolicy(sizePolicy)
        self.labelQtLogo.setMaximumSize(QSize(96, 23))
        self.labelQtLogo.setScaledContents(True)
        self.horizontalLayoutWidget = QWidget(frmAbout)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(90, 100, 261, 22))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelGithub = QLabel(self.horizontalLayoutWidget)
        self.labelGithub.setObjectName(u"labelGithub")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelGithub.sizePolicy().hasHeightForWidth())
        self.labelGithub.setSizePolicy(sizePolicy1)
        self.labelGithub.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.labelGithub)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.labelHuggingFace = QLabel(self.horizontalLayoutWidget)
        self.labelHuggingFace.setObjectName(u"labelHuggingFace")
        sizePolicy1.setHeightForWidth(self.labelHuggingFace.sizePolicy().hasHeightForWidth())
        self.labelHuggingFace.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.labelHuggingFace)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.labelBilibili = QLabel(self.horizontalLayoutWidget)
        self.labelBilibili.setObjectName(u"labelBilibili")
        sizePolicy1.setHeightForWidth(self.labelBilibili.sizePolicy().hasHeightForWidth())
        self.labelBilibili.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.labelBilibili)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.retranslateUi(frmAbout)
        self.btnClose.clicked.connect(frmAbout.close)

        QMetaObject.connectSlotsByName(frmAbout)
    # setupUi

    def retranslateUi(self, frmAbout):
        frmAbout.setWindowTitle(QCoreApplication.translate("frmAbout", u"\u5173\u4e8e", None))
        self.labelLogo.setText("")
        self.labelInfo.setText(QCoreApplication.translate("frmAbout", u"Dub Genius\n"
"Version 1.0.0\n"
"Developed by 2DIPW\n"
"Licensed under GNU General Public License v3\n"
"Open source leads the world to a brighter future!", None))
        self.btnClose.setText(QCoreApplication.translate("frmAbout", u"\u5173\u95ed", None))
        self.labelQtLogo.setText("")
        self.labelGithub.setText(QCoreApplication.translate("frmAbout", u"<html><head/><body><p><a href=\"https://github.com/2DIPW\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a></p></body></html>", None))
        self.labelHuggingFace.setText(QCoreApplication.translate("frmAbout", u"<html><head/><body><p><a href=\"https://huggingface.co/2DIPW\"><span style=\" text-decoration: underline; color:#0000ff;\">HuggingFace</span></a></p></body></html>", None))
        self.labelBilibili.setText(QCoreApplication.translate("frmAbout", u"<html><head/><body><p><a href=\"https://space.bilibili.com/1823254607\"><span style=\" text-decoration: underline; color:#0000ff;\">Bilibili</span></a></p></body></html>", None))
    # retranslateUi

