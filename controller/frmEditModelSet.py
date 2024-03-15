import os
from PySide6 import QtCore, QtGui, QtWidgets
from ui.frmEditModelSet import Ui_frmEditModelSet

lang_list = ["中文", "英文", "日文"]


class frmEditModelSet(QtWidgets.QDialog, Ui_frmEditModelSet):
    def __init__(self, model_set_info):
        super(frmEditModelSet, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowType.WindowMaximizeButtonHint)

        # 定义表头
        self.tableRefAudioList.setHorizontalHeaderLabels(["别名", "文件路径", "语言", "参考文本"])
        self.tableRefAudioList.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableRefAudioList.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableRefAudioList.setColumnWidth(2, 50)
        self.tableRefAudioList.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)

        # 定义批量修改语言菜单
        menuSetLangTo = QtWidgets.QMenu(self)
        for l in lang_list:
            actionSetLangTo = QtGui.QAction(l, self)
            actionSetLangTo.triggered.connect(lambda _=True, lang=l: self.set_selected_rows_lang_to(lang))
            menuSetLangTo.addAction(actionSetLangTo)
        self.btnSetLangTo.setMenu(menuSetLangTo)

        # 填入信息
        if model_set_info:
            self.lneditModelSetName.setText(model_set_info["Name"])
            self.lneditGPTModelName.setText(model_set_info["GPT"])
            self.lneditSoVITSModelName.setText(model_set_info["SoVITS"])
            for r in model_set_info["RefAudio"]:
                self.add_new_row_to_ref_list(r)

        # 连接事件
        self.btnAddRefAudio.clicked.connect(self.btnAddRefAudio_Clicked)
        self.btnDeleteRefAudio.clicked.connect(self.btnDeleteRefAudio_Clicked)
        self.btnPickGPTModel.clicked.connect(self.btnPickGPTModel_Clicked)
        self.btnPickSoVITSModel.clicked.connect(self.btnPickSoVITSModel_Clicked)
        self.btnSave.clicked.connect(self.btnSave_Clicked)
        self.btnCancel.clicked.connect(self.reject)

        self.info = None

        self.last_dir = os.getcwd()

    def btnAddRefAudio_Clicked(self):  # 添加参考音频
        dialog = QtWidgets.QFileDialog()
        file_paths, _ = dialog.getOpenFileNames(parent=self, caption="选择文件", dir=self.last_dir, filter="音频文件 (*.wav *.mp3)")

        if file_paths:
            self.last_dir = os.path.dirname(file_paths[0])
            for f in file_paths:
                basename = os.path.splitext(os.path.basename(f))[0]
                self.add_new_row_to_ref_list({"Nickname": basename, "Path": f, "Lang": lang_list[0], "Text": basename})

    def btnDeleteRefAudio_Clicked(self):  # 删除所选列的参考音频
        response = QtWidgets.QMessageBox.question(self, "确认删除",
                                                  "确实要删除选中的参考音频吗？\n此操作无法撤销！",
                                                  QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                                                  QtWidgets.QMessageBox.StandardButton.No)
        if response == QtWidgets.QMessageBox.StandardButton.Yes:
            rows = self.tableRefAudioList.selectedIndexes()
            rows_to_delete = [row.row() for row in rows]
            if len(rows_to_delete) > 0:
                for row in sorted(set(rows_to_delete), reverse=True):
                    self.tableRefAudioList.removeRow(row)

    def set_selected_rows_lang_to(self, lang):  # 将所选列的语言设置为
        rows = self.tableRefAudioList.selectedIndexes()
        for row in rows:
            self.tableRefAudioList.cellWidget(row.row(), 2).setCurrentText(lang)

    def add_new_row_to_ref_list(self, r):
        self.tableRefAudioList.insertRow(self.tableRefAudioList.rowCount())  # 添加新的一行
        row_id = self.tableRefAudioList.rowCount() - 1

        # 别名
        #nickname = QtWidgets.QLineEdit()
        nickname = QtWidgets.QTableWidgetItem(r["Nickname"])
        #nickname.setText(r["Nickname"])
        #nickname.setStyleSheet("QLineEdit { border: none; }")
        #self.tableRefAudioList.setCellWidget(row_id, 0, nickname)
        self.tableRefAudioList.setItem(row_id, 0, nickname)

        # 路径
        path = QtWidgets.QLineEdit()
        path.setText(r["Path"])
        path.setReadOnly(True)
        path.mouseReleaseEvent = lambda _, widget=path: self.set_ref_path(widget)
        path.setStyleSheet("QLineEdit { border: none; }")
        self.tableRefAudioList.setCellWidget(row_id, 1, path)

        # 语言
        lang = QtWidgets.QComboBox()
        lang.addItems(lang_list)
        lang.setCurrentText(r["Lang"])
        self.tableRefAudioList.setCellWidget(row_id, 2, lang)

        # 文本
        # text = QtWidgets.QLineEdit()
        # text.setText(r["Text"])
        # text.setStyleSheet("QLineEdit { border: none; }")
        # self.tableRefAudioList.setCellWidget(row_id, 3, text)
        # nickname = QtWidgets.QLineEdit()
        text = QtWidgets.QTableWidgetItem(r["Text"])
        # nickname.setText(r["Nickname"])
        # nickname.setStyleSheet("QLineEdit { border: none; }")
        # self.tableRefAudioList.setCellWidget(row_id, 0, nickname)
        self.tableRefAudioList.setItem(row_id, 3, text)

    def set_ref_path(self, widget):
        dialog = QtWidgets.QFileDialog()
        last_dir = os.path.dirname(widget.text())
        file_path, _ = dialog.getOpenFileName(parent=self, caption="选择文件", dir=last_dir, filter="音频文件 (*.wav *.mp3)")
        if file_path:
            widget.setText(file_path)

    def btnPickGPTModel_Clicked(self):
        dialog = QtWidgets.QFileDialog()
        if self.lneditGPTModelName.text():
            last_dir = os.path.dirname(self.lneditGPTModelName.text())
        else:
            last_dir = os.getcwd()
        file_path, _ = dialog.getOpenFileName(parent=self, caption="选择文件", dir=last_dir, filter="GPT模型 (*.ckpt)")
        if file_path:
            self.lneditGPTModelName.setText(file_path)

    def btnPickSoVITSModel_Clicked(self):
        dialog = QtWidgets.QFileDialog()
        if self.lneditSoVITSModelName.text():
            last_dir = os.path.dirname(self.lneditSoVITSModelName.text())
        else:
            last_dir = os.getcwd()
        file_path, _ = dialog.getOpenFileName(parent=self, caption="选择文件", dir=last_dir, filter="SoVITS模型 (*.pth)")
        if file_path:
            self.lneditSoVITSModelName.setText(file_path)

    def dump_model_set_info(self):
        ref_list = []
        for i in range(self.tableRefAudioList.rowCount()):
            #nickname = self.tableRefAudioList.cellWidget(i, 0).text()
            nickname = self.tableRefAudioList.item(i, 0).text()
            path = self.tableRefAudioList.cellWidget(i, 1).text()
            lang = self.tableRefAudioList.cellWidget(i, 2).currentText()
            #text = self.tableRefAudioList.cellWidget(i, 3).text()
            text = self.tableRefAudioList.item(i, 3).text()
            if "" in [nickname, path, lang, text]:
                QtWidgets.QMessageBox.warning(self, "错误",
                                              f"参考音频组存在未填写的项！\n请确保每个字段均已正确填写",
                                              QtWidgets.QMessageBox.StandardButton.Ok)
                return None
            else:
                ref_list.append({"Nickname": nickname, "Path": path, "Lang": lang, "Text": text})

        name = self.lneditModelSetName.text()
        gpt = self.lneditGPTModelName.text()
        sovits = self.lneditSoVITSModelName.text()

        if "" in [name, gpt, sovits] or ref_list == []:
            QtWidgets.QMessageBox.warning(self, "错误",
                                          f"模型组存在未填写的项！\n请确保每个字段均已正确填写",
                                          QtWidgets.QMessageBox.StandardButton.Ok)
            return None
        else:
            info = {"Name": name, "GPT": gpt, "SoVITS": sovits, "RefAudio": ref_list}
            return info

    def btnSave_Clicked(self):
        self.info = self.dump_model_set_info()
        if self.info:
            self.accept()

    @staticmethod
    def getEditedModelSetInfo(model_set_info=None):
        dialog = frmEditModelSet(model_set_info)
        ok = dialog.exec()
        return dialog.info, ok == QtWidgets.QDialog.DialogCode.Accepted
