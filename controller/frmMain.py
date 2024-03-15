from PySide6 import QtCore, QtGui, QtWidgets, QtMultimedia
from ui.frmMain import Ui_frmMain
from controller.frmAbout import frmAbout
from controller.frmModelSetsList import frmModelSetsList
from controller import config
import os
import soundfile
from datetime import datetime
import shutil


FullPathRole = QtCore.Qt.ItemDataRole.UserRole + 1

dict_language = {
    "中文": "all_zh",  # 全部按中文识别
    "英文": "en",  # 全部按英文识别#######不变
    "日文": "all_ja",  # 全部按日文识别
    "中英混合": "zh",  # 按中英混合识别####不变
    "日英混合": "ja",  # 按日英混合识别####不变
    "多语种混合": "auto",  # 多语种启动切分识别语种
}
dict_how_to_cut = {
    "不切": 0,
    "凑四句一切": 1,
    "凑50字一切": 2,
    "按中文句号。切": 3,
    "按英文句号.切": 4,
    "按标点符号切": 5
}


Tmp_root = "tmp"
os.makedirs(Tmp_root, exist_ok=True)


class AudioListWidget(QtWidgets.QListWidget):
    def __init__(self):
        super().__init__()
        self.setDragEnabled(True)
        self.setDragDropMode(self.DragDropMode.DragDrop)

    def startDrag(self, actions):
        drag = QtGui.QDrag(self)
        indexes = self.selectedIndexes()
        mime = self.model().mimeData(indexes)
        urlList = []
        for index in indexes:
            urlList.append(QtCore.QUrl.fromLocalFile(index.data(FullPathRole)))
        mime.setUrls(urlList)
        drag.setMimeData(mime)
        drag.exec_(actions)


class NoAutoAdjustComboBox(QtWidgets.QComboBox):
    def __init__(self, size_hint_width):
        super().__init__()
        self.size_hint_width = size_hint_width

    def sizeHint(self):
        return self.minimumSizeHint()

    def minimumSizeHint(self):
        return QtCore.QSize(self.size_hint_width, 20)

    def showEvent(self, e):
        pass


class frmMain(QtWidgets.QMainWindow, Ui_frmMain):
    def __init__(self, parent=None):
        # 构建UI
        super(frmMain, self).__init__(parent)

        splash = QtWidgets.QSplashScreen(QtGui.QPixmap(":res/image/splash.png"))
        splash.show()
        splash.showMessage(f'Loading ...', QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignBottom, QtCore.Qt.GlobalColor.white)

        self.setupUi(self)
        self.lvAudio = AudioListWidget()
        self.lvAudio.setObjectName("lvAudio")
        self.vlayAudioList.insertWidget(0, self.lvAudio)

        self.comboboxModelSet = NoAutoAdjustComboBox(94)
        self.comboboxModelSet.setObjectName("comboboxModelSet")
        self.comboboxModelSet.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayModelSelect.insertWidget(1, self.comboboxModelSet)

        self.comboboxRefAudio = NoAutoAdjustComboBox(94)
        self.comboboxRefAudio.setObjectName("comboboxRefAudio")
        self.comboboxRefAudio.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayModelSelect.insertWidget(2, self.comboboxRefAudio)

        self.comboboxTextLang.addItems(dict_language.keys())
        self.comboboxHowToCut.addItems(dict_how_to_cut.keys())

        # 加载推理核心
        try:
            pass
            self.inference_core = self.__class__.inference_core()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "错误", f"推理核心加载失败！\n错误信息：{str(e)}", QtWidgets.QMessageBox.StandardButton.Ok)
            os._exit(1)

        # 连接事件
        self.btnSynthesize.clicked.connect(self.btnSynthesize_Clicked)  # 合成按钮
        self.comboboxModelSet.currentIndexChanged.connect(self.comboboxModelSet_currentIndexChanged)  # 切换模型组
        self.btnManageModelSets.clicked.connect(self.btnManageModelSets_CLicked)  # 管理模型组
        self.btnSave.clicked.connect(self.btnSave_Clicked)  # 保存至项目按钮
        self.btnPickProjectPath.clicked.connect(self.btnPickProjectPath_Clicked)  # 挑选项目路径
        self.lvAudio.itemDoubleClicked.connect(self.lvAudio_itemDoubleClicked)
        self.chkboxAlwaysTop.stateChanged.connect(self.chkboxAlwaysTop_stateChanged)  # 总在最前切换开关
        self.installEventFilter(self)  # 自动透明功能
        self.labelAbout.mousePressEvent = self.labelAbout_Clicked  # 关于

        # 试听用播放器
        self.media_player = QtMultimedia.QMediaPlayer()
        self.audioOutput = QtMultimedia.QAudioOutput()
        self.media_player.setAudioOutput(self.audioOutput)
        self.btnPlayPause.clicked.connect(self.player_play_pause)
        self.media_player.positionChanged.connect(self.player_update_position)
        self.media_player.durationChanged.connect(self.player_update_duration)
        self.sliderPlayback.sliderReleased.connect(self.player_set_position)

        # 全局变量
        self.current_tmp_wav_path = ""
        self.current_text = ""

        # 加载设置
        config.init()
        self.model_sets_list = config.get_config("ModelSets")
        if not self.model_sets_list:  # 如果不存在任何模型组，则要求设置
            QtWidgets.QMessageBox.information(self, "提示", f"未找到任何模型组！\n首次使用请先配置模型", QtWidgets.QMessageBox.StandardButton.Ok)
            new_model_set_list, ok = frmModelSetsList.getModelSetList()
            if ok:
                self.model_sets_list = new_model_set_list
            else:
                QtWidgets.QMessageBox.warning(self, "错误", "未设置任何模型组，即将退出！", QtWidgets.QMessageBox.StandardButton.Ok)
                os._exit(1)

        self.refresh_model_set_list()

        if self.comboboxModelSet.findText(config.get_config("CurrentModelSet")) != -1:
            self.comboboxModelSet.setCurrentText(config.get_config("CurrentModelSet"))
        else:
            self.comboboxModelSet.setCurrentIndex(0)

        self.comboboxModelSet_currentIndexChanged()  # 强制触发一次切换当前模型

        if self.comboboxRefAudio.findText(config.get_config("CurrentRefAudio")) != -1:
            self.comboboxRefAudio.setCurrentText(config.get_config("CurrentRefAudio"))
        else:
            self.comboboxRefAudio.setCurrentIndex(0)

        self.set_always_top(self.chkboxAlwaysTop.isChecked())

        self.spinboxTopK.setValue(config.get_config("TopK"))
        self.spinboxTopP.setValue(config.get_config("TopP"))
        self.spinboxTemp.setValue(config.get_config("Temp"))
        self.comboboxTextLang.setCurrentText(config.get_config("Lang"))
        self.comboboxHowToCut.setCurrentText(config.get_config("HowToCut"))
        self.chkboxAlwaysTop.setChecked(config.get_config("AlwaysTop"))
        self.chkboxAutoTrans.setChecked(config.get_config("AutoTrans"))
        self.lneditProjectPath.setText(config.get_config("SavePath"))

        self.set_playback_control_enabled(False)

        # 合成语音线程
        self.synthesize_thread = SynthesizeThread(self)
        self.synthesize_thread.finished_signal.connect(self.on_synthesize_thread_finished)

        splash.finish(self)

    @classmethod
    def inference_core(cls):
        import inference_core
        return inference_core

    def closeEvent(self, a0):
        del self.media_player

        # 保存设置
        config.set_config("ModelSets", self.model_sets_list)
        config.set_config("CurrentModelSet", self.comboboxModelSet.currentText())
        config.set_config("CurrentRefAudio", self.comboboxRefAudio.currentText())
        config.set_config("TopK", self.spinboxTopK.value())
        config.set_config("TopP", self.spinboxTopP.value())
        config.set_config("Temp", self.spinboxTemp.value())
        config.set_config("Lang", self.comboboxTextLang.currentText())
        config.set_config("HowToCut", self.comboboxHowToCut.currentText())
        config.set_config("AlwaysTop", self.chkboxAlwaysTop.isChecked())
        config.set_config("AutoTrans", self.chkboxAutoTrans.isChecked())
        config.set_config("SavePath", self.lneditProjectPath.text())

        config.save_config()

        # 清理临时文件
        for f in os.listdir("./tmp"):
            try:
                os.remove(os.path.join("./tmp", f))
            except:
                pass

        a0.accept()

    def eventFilter(self, obj, event):  # 失去焦点自动透明
        if self.chkboxAutoTrans.isChecked():
            if event.type() == QtCore.QEvent.Type.WindowActivate:
                self.setWindowOpacity(1.0)
            elif event.type() == QtCore.QEvent.Type.WindowDeactivate:
                self.setWindowOpacity(0.8)

        return super().eventFilter(obj, event)

    def refresh_model_set_list(self):
        self.comboboxModelSet.blockSignals(True)

        self.comboboxModelSet.clear()
        for m in self.model_sets_list:
            self.comboboxModelSet.addItem(m["Name"])
        self.comboboxModelSet.setCurrentIndex(0)

        self.refresh_ref_audio_list()

        self.comboboxModelSet.blockSignals(False)

    def refresh_ref_audio_list(self):
        self.comboboxRefAudio.clear()

        index = self.comboboxModelSet.currentIndex()

        for r in self.model_sets_list[index]["RefAudio"]:
            self.comboboxRefAudio.addItem(r["Nickname"])
        self.comboboxRefAudio.setCurrentIndex(0)

    def chkboxAlwaysTop_stateChanged(self):
        self.set_always_top(self.chkboxAlwaysTop.isChecked())

    def set_always_top(self, value):
        if value:
            self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint | self.windowFlags())
            self.show()
        else:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowType.WindowStaysOnTopHint)
            self.show()

    def comboboxModelSet_currentIndexChanged(self):  # 切换模型
        index = self.comboboxModelSet.currentIndex()
        self.btnSynthesize.setEnabled(False)  # 不知道切换是否成功，先禁用合成按钮

        self.inference_core.change_gpt_weights(self.model_sets_list[index]["GPT"])
        self.inference_core.change_sovits_weights(self.model_sets_list[index]["SoVITS"])
        self.refresh_ref_audio_list()
        self.btnSynthesize.setEnabled(True)
        try:
            pass
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "错误",
                                          f"加载模型组出错！\n错误信息{e}",
                                          QtWidgets.QMessageBox.StandardButton.Ok)
            self.comboboxModelSet.setCurrentIndex(-1)

    def btnManageModelSets_CLicked(self):
        self.set_always_top(False)

        new_model_set_list, ok = frmModelSetsList.getModelSetList(self.model_sets_list)
        if ok:
            self.model_sets_list = new_model_set_list
            self.refresh_model_set_list()
            self.comboboxModelSet_currentIndexChanged()  # 强制执行一次切换模型

        self.set_always_top(self.chkboxAlwaysTop.isChecked())

    def btnSynthesize_Clicked(self):
        self.set_playback_control_enabled(False)
        self.btnSynthesize.setText("合成中 ...")
        self.btnSynthesize.setEnabled(False)
        self.synthesize_thread.start()

    def on_synthesize_thread_finished(self, error, path, text):
        if not error:
            self.current_tmp_wav_path = path
            self.current_text = text
            self.media_player.setSource(QtCore.QUrl.fromLocalFile(self.current_tmp_wav_path))
            self.set_playback_control_enabled(True)
        else:
            QtWidgets.QMessageBox.warning(self, "错误", f"合成出错！\n错误信息{error}", QtWidgets.QMessageBox.StandardButton.Ok)
        self.btnSynthesize.setText("合成")
        self.btnSynthesize.setEnabled(True)

    def btnPickProjectPath_Clicked(self):
        self.lneditProjectPath.setText(QtWidgets.QFileDialog.getExistingDirectory(self, "项目路径", os.getcwd()))

    def btnSave_Clicked(self):
        if self.lneditProjectPath.text() == "":
            QtWidgets.QMessageBox.information(self, "提示", f"请先指定合成语音的保存路径！", QtWidgets.QMessageBox.StandardButton.Ok)
            return

        audio_path = os.path.join(self.lneditProjectPath.text(), os.path.basename(self.current_tmp_wav_path))

        try:
            shutil.copy2(self.current_tmp_wav_path, audio_path)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "错误", f"保存出错！\n错误信息{str(e)}", QtWidgets.QMessageBox.StandardButton.Ok)
            return

        item = QtWidgets.QListWidgetItem(self.current_text)
        item.setData(FullPathRole, audio_path)
        self.lvAudio.addItem(item)
        self.txteditText.clear()
        self.current_text = ""
        self.current_tmp_wav_path = ""
        self.set_playback_control_enabled(False)

    def lvAudio_itemDoubleClicked(self, item):
        clipboard = QtWidgets.QApplication.clipboard()
        text = item.text()
        clipboard.setText(text, mode=QtGui.QClipboard.Mode.Clipboard)

    def set_playback_control_enabled(self, is_enabled):
        if is_enabled:
            self.media_player.play()
        else:
            self.media_player.stop()
        self.btnPlayPause.setEnabled(is_enabled)
        self.btnSave.setEnabled(is_enabled)
        self.sliderPlayback.setEnabled(is_enabled)

    def player_play_pause(self):
        if self.media_player.playbackState() == QtMultimedia.QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def player_set_position(self):
        self.media_player.setPosition(self.sliderPlayback.value())

    def player_update_position(self, position):
        self.sliderPlayback.setValue(position)

        current_time = position // 1000
        total_time = self.media_player.duration() // 1000
        self.labelPlaybackTime.setText(f"{current_time // 60:02}:{current_time % 60:02}/{total_time // 60:02}:{total_time % 60:02}")

    def player_update_duration(self, duration):
        self.sliderPlayback.setRange(0, duration)

    def labelAbout_Clicked(self, e):
        self.frmAbout_ = frmAbout()
        self.frmAbout_.show()


class SynthesizeThread(QtCore.QThread):
    finished_signal = QtCore.Signal(str, str, str)

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        try:
            ref_audio = self.parent.model_sets_list[self.parent.comboboxModelSet.currentIndex()]["RefAudio"][
                self.parent.comboboxRefAudio.currentIndex()]

            r_audio = ref_audio["Path"]
            r_text = ref_audio["Text"]
            r_lang = dict_language[ref_audio["Lang"]]
            text = self.parent.txteditText.toPlainText()
            t_lang = dict_language[self.parent.comboboxTextLang.currentText()]
            how_to_cut = dict_how_to_cut[self.parent.comboboxHowToCut.currentText()]
            top_k = self.parent.spinboxTopK.value()
            top_p = self.parent.spinboxTopP.value()
            temp = self.parent.spinboxTemp.value()

            gen_audio = self.parent.inference_core.get_tts_wav(r_audio, r_text, r_lang, text, t_lang, how_to_cut, top_k, top_p, temp)
            sample_rate, audio_array = next(gen_audio)

            current_tmp_wav = os.path.join(Tmp_root, datetime.now().strftime('%Y%m%d-%H%M%S') + ".wav")
            current_text = text

            soundfile.write(current_tmp_wav, audio_array, sample_rate, format="wav")

            self.finished_signal.emit("", current_tmp_wav, current_text)
        except Exception as e:
            self.finished_signal.emit(str(e), "", "")
