import sys
from PySide6 import QtWidgets
from controller.frmMain import frmMain

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    frmMain_ = frmMain()
    frmMain_.show()
    sys.exit(app.exec())
