from PySide6 import QtCore, QtWidgets
from ui.frmModelSetsList import Ui_frmModelSetsList
from controller.frmEditModelSet import frmEditModelSet

RefListRole = QtCore.Qt.ItemDataRole.UserRole + 1


class frmModelSetsList(QtWidgets.QDialog, Ui_frmModelSetsList):
    def __init__(self, model_set_list):
        super(frmModelSetsList, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowType.WindowMaximizeButtonHint)

        # 定义表头
        self.tableModelSetsList.setHorizontalHeaderLabels(["模型组名", "GPT模型", "SoVITS模型", "参考音频组"])
        self.tableModelSetsList.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableModelSetsList.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableModelSetsList.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableModelSetsList.setColumnWidth(3, 70)

        # 填入信息
        if model_set_list:
            for r in model_set_list:
                self.add_new_row_to_modellist(r)

        # 连接事件
        self.btnAddModelSet.clicked.connect(self.btnAddModelSet_Clicked)
        self.btnEditModelSet.clicked.connect(self.btnEditModelSet_Clicked)
        self.btnCopyModelSet.clicked.connect(self.btnCopyModelSet_Clicked)
        self.btnDeleteModelSet.clicked.connect(self.btnDeleteModelSet_Clicked)
        self.tableModelSetsList.itemDoubleClicked.connect(self.btnEditModelSet_Clicked)
        self.btnSave.clicked.connect(self.btnSave_Clicked)
        self.btnCancel.clicked.connect(self.reject)

        self.model_set_list = None

    def btnAddModelSet_Clicked(self):
        model_set_info, ok = frmEditModelSet.getEditedModelSetInfo()
        if ok:
            self.add_new_row_to_modellist(model_set_info)

    def btnCopyModelSet_Clicked(self):
        if self.tableModelSetsList.selectedIndexes():
            index = self.tableModelSetsList.selectedIndexes()[0].row()
            model_set_info, ok = frmEditModelSet.getEditedModelSetInfo(self.get_modellist_row(index))
            if ok:
                self.add_new_row_to_modellist(model_set_info)

    def btnDeleteModelSet_Clicked(self):
        response = QtWidgets.QMessageBox.question(self, "确认删除",
                                                  "确实要删除选中的模型组吗？\n此操作无法撤销！",
                                                  QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                                                  QtWidgets.QMessageBox.StandardButton.No)
        if response == QtWidgets.QMessageBox.StandardButton.Yes:
            rows = self.tableModelSetsList.selectedIndexes()
            rows_to_delete = [row.row() for row in rows]
            if len(rows_to_delete) > 0:
                for row in sorted(set(rows_to_delete), reverse=True):
                    self.tableModelSetsList.removeRow(row)

    def btnEditModelSet_Clicked(self, *args):
        if self.tableModelSetsList.selectedIndexes():
            index = self.tableModelSetsList.selectedIndexes()[0].row()
            new_model_set_info, ok = frmEditModelSet.getEditedModelSetInfo(self.get_modellist_row(index))
            if ok:
                self.edit_modellist_row(index, new_model_set_info)
        else:
            QtWidgets.QMessageBox.warning(self, "错误",
                                          f"请选中要编辑的模型组！",
                                          QtWidgets.QMessageBox.StandardButton.Ok)

    def add_new_row_to_modellist(self, info):
        self.tableModelSetsList.insertRow(self.tableModelSetsList.rowCount())  # 添加新的一行
        index = self.tableModelSetsList.rowCount() - 1
        self.edit_modellist_row(index, info)

    def get_modellist_row(self, index):
        name = self.tableModelSetsList.item(index, 0).text()
        gpt = self.tableModelSetsList.item(index, 1).text()
        sovits = self.tableModelSetsList.item(index, 2).text()
        ref = self.tableModelSetsList.item(index, 3).data(RefListRole)
        return {"Name": name, "GPT": gpt, "SoVITS": sovits, "RefAudio": ref}

    def edit_modellist_row(self, index, info):
        self.tableModelSetsList.setItem(index, 0, QtWidgets.QTableWidgetItem(info["Name"]))
        self.tableModelSetsList.setItem(index, 1, QtWidgets.QTableWidgetItem(info["GPT"]))
        self.tableModelSetsList.setItem(index, 2, QtWidgets.QTableWidgetItem(info["SoVITS"]))
        ref_list_item = QtWidgets.QTableWidgetItem(str(len(info["RefAudio"])) + "条")
        ref_list_item.setData(RefListRole, info["RefAudio"])
        self.tableModelSetsList.setItem(index, 3, ref_list_item)

    def dump_model_set_list(self):
        model_set_list = [self.get_modellist_row(i) for i in range(self.tableModelSetsList.rowCount())]
        return model_set_list

    def btnSave_Clicked(self):
        self.model_set_list = self.dump_model_set_list()
        if self.model_set_list:
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "错误",
                                          f"请至少添加一个模型组！",
                                          QtWidgets.QMessageBox.StandardButton.Ok)

    @staticmethod
    def getModelSetList(model_set_list=None):
        dialog = frmModelSetsList(model_set_list)
        ok = dialog.exec_()
        return dialog.model_set_list, ok == QtWidgets.QDialog.DialogCode.Accepted
