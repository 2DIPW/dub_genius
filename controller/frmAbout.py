from PySide6 import QtCore, QtGui, QtWidgets
from ui.frmAbout import Ui_frmAbout
import ui.resource_rc


class frmAbout(QtWidgets.QDialog, Ui_frmAbout):
    def __init__(self, parent=None):
        super(frmAbout, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowType.WindowContextHelpButtonHint)
        self.labelLogo.setPixmap(QtGui.QPixmap(":res/image/logo_128.png"))
        self.labelQtLogo.setPixmap(QtGui.QPixmap(":res/image/qt_logo.png"))
        self.setWindowIcon(QtGui.QIcon(":res/image/icon.ico"))

