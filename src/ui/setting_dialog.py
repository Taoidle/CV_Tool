import json
import util.basic as ub
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QGridLayout, QPushButton, QDesktopWidget, QHBoxLayout, \
    QRadioButton, QLineEdit
from PyQt5.QtCore import Qt


class SettingWindow(QWidget):

    threshold_max_1, threshold_max_2, threshold_max_3, threshold_max_4 = 100, 10, 100, 512
    switch_flag = 1

    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__set_text()
        self.__set_model()

    def __init_ui(self):
        # 读取设置文件
        with open('./settings.json', 'r', encoding='utf-8') as fr:
            json_data = json.load(fr)
            self.default_jpeg_quality = int(json_data["jpg_quality"])
            self.default_png_quality = int(json_data["png_quality"])
            self.default_webp_quality = int(json_data["webp_quality"])
            self.defalut_dct_block = int(json_data['DCT_Block'])
        fr.close()
        # 设置窗口标题
        self.setWindowTitle('设置')
        # 设置窗口只有最小化按钮
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # 屏蔽父窗口
        self.setWindowModality(Qt.ApplicationModal)
        # 设置窗口大小
        self.resize(500, 300)
        # 初始化拖动条
        self.threshold_slider_1 = QSlider(Qt.Horizontal)
        # 设置最大高度
        self.threshold_slider_1.setMaximumHeight(20)
        # 设置最小值
        self.threshold_slider_1.setMinimum(1)
        # 设置最大值
        self.threshold_slider_1.setMaximum(self.threshold_max_1)
        # 设置步进
        self.threshold_slider_1.setSingleStep(1)
        # 设置默认值
        self.threshold_slider_1.setValue(self.default_jpeg_quality)
        # 设置不绘制刻度线
        self.threshold_slider_1.setTickPosition(QSlider.NoTicks)
        # 设置刻度间隔
        self.threshold_slider_1.setTickInterval(5)
        # 链接拖动条动作
        self.threshold_slider_1.valueChanged.connect(self.__return_value)

        self.threshold_slider_2 = QSlider(Qt.Horizontal)
        self.threshold_slider_2.setMaximumHeight(20)
        self.threshold_slider_2.setMinimum(1)
        self.threshold_slider_2.setMaximum(self.threshold_max_2)
        self.threshold_slider_2.setSingleStep(1)
        self.threshold_slider_2.setValue(self.default_png_quality)
        self.threshold_slider_2.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_2.setTickInterval(5)
        self.threshold_slider_2.valueChanged.connect(self.__return_value)

        self.threshold_slider_3 = QSlider(Qt.Horizontal)
        self.threshold_slider_3.setMaximumHeight(20)
        self.threshold_slider_3.setMinimum(0)
        self.threshold_slider_3.setMaximum(self.threshold_max_3)
        self.threshold_slider_3.setSingleStep(1)
        self.threshold_slider_3.setValue(self.default_webp_quality)
        self.threshold_slider_3.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_3.setTickInterval(5)
        self.threshold_slider_3.valueChanged.connect(self.__return_value)

        self.threshold_slider_4 = QSlider(Qt.Horizontal)
        self.threshold_slider_4.setMaximumHeight(20)
        self.threshold_slider_4.setMinimum(1)
        self.threshold_slider_4.setMaximum(self.threshold_max_4)
        self.threshold_slider_4.setSingleStep(1)
        self.threshold_slider_4.setValue(self.defalut_dct_block)
        self.threshold_slider_4.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_4.setTickInterval(5)
        self.threshold_slider_4.valueChanged.connect(self.__return_value)

        self.label_tip_1 = QLabel('jpg质量')
        self.label_tip_1.setMaximumHeight(30)
        self.label_tip_1_value = QLabel(str(self.threshold_slider_1.value()))
        self.label_tip_1_value.setMaximumHeight(30)
        self.label_tip_2 = QLabel('png质量')
        self.label_tip_2.setMaximumHeight(30)
        self.label_tip_2_value = QLabel(str(self.threshold_slider_2.value()))
        self.label_tip_2_value.setMaximumHeight(30)
        self.label_tip_3 = QLabel('webp质量')
        self.label_tip_3.setMaximumHeight(30)
        self.label_tip_3_value = QLabel(str(self.threshold_slider_3.value()))
        self.label_tip_3_value.setMaximumHeight(30)
        self.label_tip_4 = QLabel('DCT块大小')
        self.label_tip_4.setMaximumHeight(30)
        self.label_tip_4_value = QLabel(str(self.threshold_slider_4.value()))
        self.label_tip_4_value.setMaximumHeight(30)

        self.label_tip_5 = QLabel('百度OCR')
        self.label_tip_5.setMaximumHeight(30)
        self.baidu_app_id = QLabel('App ID:')
        self.baidu_app_id.setMaximumHeight(30)
        self.baidu_app_id_text = QLineEdit(self)
        self.baidu_api_key = QLabel('Api Key:')
        self.baidu_api_key.setMaximumHeight(30)
        self.baidu_api_key_text = QLineEdit(self)
        self.baidu_secret_key = QLabel('Secret Key:')
        self.baidu_secret_key.setMaximumHeight(30)
        self.baidu_secret_key_text = QLineEdit(self)

        self.baidu_ocr_words_label = QLabel('文字识别')
        self.baidu_ocr_words_label.setMaximumHeight(30)
        self.baidu_ocr_words_hbox = QHBoxLayout()
        self.baidu_ocr_words_hbox_wid = QWidget()
        self.baidu_ocr_words_general = QRadioButton('通用文字识别')
        self.baidu_ocr_words_heigh = QRadioButton('高精度文字识别')
        self.baidu_ocr_words_rare = QRadioButton('生僻字文字识别')
        self.baidu_ocr_words_hbox.addWidget(self.baidu_ocr_words_general)
        self.baidu_ocr_words_hbox.addWidget(self.baidu_ocr_words_heigh)
        self.baidu_ocr_words_hbox.addWidget(self.baidu_ocr_words_rare)
        self.baidu_ocr_words_hbox_wid.setLayout(self.baidu_ocr_words_hbox)

        self.last_pic_check_label = QLabel('上一步图像')
        self.last_pic_check_label.setMaximumHeight(30)
        self.last_pic_check_hbox = QHBoxLayout()
        self.last_pic_check_hbox_wid = QWidget()
        self.last_pic_check_show = QRadioButton('显示上一步窗口')
        self.last_pic_check_close = QRadioButton('关闭上一步窗口')
        self.last_pic_check_hbox.addWidget(self.last_pic_check_show)
        self.last_pic_check_hbox.addWidget(self.last_pic_check_close)
        self.last_pic_check_hbox_wid.setLayout(self.last_pic_check_hbox)

        self.plt_pic_check_label = QLabel('直方图图像')
        self.plt_pic_check_label.setMaximumHeight(30)
        self.plt_pic_check_hbox = QHBoxLayout()
        self.plt_pic_check_hbox_wid = QWidget()
        self.plt_pic_check_show = QRadioButton('显示直方图窗口')
        self.plt_pic_check_close = QRadioButton('关闭直方图窗口')
        self.plt_pic_check_hbox.addWidget(self.plt_pic_check_show)
        self.plt_pic_check_hbox.addWidget(self.plt_pic_check_close)
        self.plt_pic_check_hbox_wid.setLayout(self.plt_pic_check_hbox)

        self.check_hbox = QHBoxLayout()
        self.check_hbox_wid = QWidget()
        self.cancel_button = QPushButton('取消')
        self.cancel_button.clicked.connect(self.close)
        self.ok_button = QPushButton('确定')
        self.ok_button.clicked.connect(self.closeEvent)
        self.check_hbox.addWidget(self.cancel_button)
        self.check_hbox.addWidget(self.ok_button)
        self.check_hbox_wid.setLayout(self.check_hbox)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.last_pic_check_label, 1, 1)
        grid_layout.addWidget(self.last_pic_check_hbox_wid, 2, 1, 1, 2)
        grid_layout.addWidget(self.plt_pic_check_label, 3, 1)
        grid_layout.addWidget(self.plt_pic_check_hbox_wid, 4, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_1, 5, 1)
        grid_layout.addWidget(self.label_tip_1_value, 5, 2)
        grid_layout.addWidget(self.threshold_slider_1, 6, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_2, 7, 1)
        grid_layout.addWidget(self.label_tip_2_value, 7, 2)
        grid_layout.addWidget(self.threshold_slider_2, 8, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_3, 9, 1)
        grid_layout.addWidget(self.label_tip_3_value, 9, 2)
        grid_layout.addWidget(self.threshold_slider_3, 10, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_4, 11, 1)
        grid_layout.addWidget(self.label_tip_4_value, 11, 2)
        grid_layout.addWidget(self.threshold_slider_4, 12, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_5, 13, 1)
        grid_layout.addWidget(self.baidu_app_id, 14, 1)
        grid_layout.addWidget(self.baidu_app_id_text, 14, 2)
        grid_layout.addWidget(self.baidu_api_key, 15, 1)
        grid_layout.addWidget(self.baidu_api_key_text, 15, 2)
        grid_layout.addWidget(self.baidu_secret_key, 16, 1)
        grid_layout.addWidget(self.baidu_secret_key_text, 16, 2)
        grid_layout.addWidget(self.baidu_ocr_words_label, 17, 1)
        grid_layout.addWidget(self.baidu_ocr_words_hbox_wid, 18, 1, 1, 2)
        grid_layout.addWidget(self.check_hbox_wid, 19, 1, 1, 2)

        self.setLayout(grid_layout)
        self.setWindowIcon(QIcon('res/img/logo.png'))
        self.show()
        self.__center()

    # 获取并显示设置内容
    def __set_text(self):
        with open('./settings.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            self.baidu_app_id_text.setText(json_data['Baidu_Api']['APP_ID'])
            self.baidu_api_key_text.setText(json_data['Baidu_Api']['API_KEY'])
            self.baidu_secret_key_text.setText(json_data['Baidu_Api']['SECRET_KEY'])
        f.close()

    def __set_model(self):
        with open('./settings.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            model = int(json_data['Baidu_Api']['WORDS_MODEL'])
        if model == 1:
            self.baidu_ocr_words_general.setChecked(True)
        elif model == 2:
            self.baidu_ocr_words_heigh.setChecked(True)
        elif model == 3:
            self.baidu_ocr_words_rare.setChecked(True)
        else:
            pass

    def __get_model(self):
        if self.baidu_ocr_words_general.isChecked():
            return 1
        elif self.baidu_ocr_words_heigh.isChecked():
            return 2
        elif self.baidu_ocr_words_rare.isChecked():
            return 3
        else:
            pass

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __return_value(self):
        self.label_tip_1_value.setText(str(self.threshold_slider_1.value()))
        self.label_tip_2_value.setText(str(self.threshold_slider_2.value()))
        self.label_tip_3_value.setText(str(self.threshold_slider_3.value()))
        self.label_tip_4_value.setText(str(self.threshold_slider_4.value()))
        return self.threshold_slider_1.value(), self.threshold_slider_2.value(), self.threshold_slider_3.value(), self.threshold_slider_4.value()

    def closeEvent(self, event):
        jpg, png, webp, dct_block = self.__return_value()
        app_id = self.baidu_api_key_text.text()
        api_key = self.baidu_api_key_text.text()
        secret_key = self.baidu_secret_key_text.text()
        words_model = self.__get_model()
        ub.CvBasic.program_settings(jpg, png, webp, dct_block, app_id, api_key, secret_key, words_model)
        self.close()
