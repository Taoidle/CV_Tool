"""

Author: kaiyang
Last edited: April 2020

"""

from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QDialogButtonBox, QGridLayout, QPushButton, QDesktopWidget, \
    QCheckBox, QToolBox, QGroupBox, QVBoxLayout, QToolButton, QMainWindow, QMessageBox, QListWidget, QListView, \
    QListWidgetItem, QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal, QSize, QStringListModel


class ToolsWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.tool_box = QToolBox()

        self.group_box_1 = QGroupBox()
        self.group_box_1.setMaximumWidth(200)
        self.v_box_1 = QVBoxLayout()

        self.group_box_2 = QGroupBox()
        self.group_box_2.setMaximumWidth(200)
        self.v_box_2 = QVBoxLayout()

        self.group_box_3 = QGroupBox()
        self.group_box_3.setMaximumWidth(200)
        self.v_box_3 = QVBoxLayout()

        self.group_box_4 = QGroupBox()
        self.group_box_4.setMaximumWidth(200)
        self.v_box_4 = QVBoxLayout()

        self.group_box_5 = QGroupBox()
        self.group_box_5.setMaximumWidth(200)
        self.v_box_4 = QVBoxLayout()

        self.group_box_6 = QGroupBox()
        self.group_box_6.setMaximumWidth(200)
        self.v_box_5 = QVBoxLayout()

        self.group_box_7 = QGroupBox()
        self.group_box_7.setMaximumWidth(200)
        self.v_box_6 = QVBoxLayout()

        self.box_1_button_1 = QToolButton()
        self.box_1_button_1.setText('恢复原图')
        self.box_1_button_1.setAutoRaise(True)
        self.box_1_button_2 = QToolButton()
        self.box_1_button_2.setText('上一步图像')
        self.box_1_button_2.setAutoRaise(True)
        self.box_1_button_3 = QToolButton()
        self.box_1_button_3.setText('灰度化')
        self.box_1_button_3.setAutoRaise(True)
        self.box_1_button_4 = QToolButton()
        self.box_1_button_4.setText('反相')
        self.box_1_button_4.setAutoRaise(True)
        self.box_1_button_5 = QToolButton()
        self.box_1_button_5.setText('二值化')
        self.box_1_button_5.setAutoRaise(True)
        self.box_1_button_6 = QToolButton()
        self.box_1_button_6.setText('自动二值化')
        self.box_1_button_6.setAutoRaise(True)

        self.box_2_button_1 = QToolButton()
        self.box_2_button_1.setText('水平镜像')
        self.box_2_button_1.setAutoRaise(True)
        self.box_2_button_2 = QToolButton()
        self.box_2_button_2.setText('垂直镜像')
        self.box_2_button_2.setAutoRaise(True)
        self.box_2_button_3 = QToolButton()
        self.box_2_button_3.setText('顺时针 90°')
        self.box_2_button_3.setAutoRaise(True)
        self.box_2_button_4 = QToolButton()
        self.box_2_button_4.setText('逆时针 90°')
        self.box_2_button_4.setAutoRaise(True)

        self.box_3_button_1 = QToolButton()
        self.box_3_button_1.setText('椒盐噪声')
        self.box_3_button_1.setAutoRaise(True)
        self.box_3_button_2 = QToolButton()
        self.box_3_button_2.setText('高斯噪声')
        self.box_3_button_2.setAutoRaise(True)

        self.box_4_button_1 = QToolButton()
        self.box_4_button_1.setText('均值滤波')
        self.box_4_button_1.setAutoRaise(True)
        self.box_4_button_2 = QToolButton()
        self.box_4_button_2.setText('中值滤波')
        self.box_4_button_2.setAutoRaise(True)
        self.box_4_button_3 = QToolButton()
        self.box_4_button_3.setText('方框滤波')
        self.box_4_button_3.setAutoRaise(True)
        self.box_4_button_4 = QToolButton()
        self.box_4_button_4.setText('高斯滤波')
        self.box_4_button_4.setAutoRaise(True)
        self.box_4_button_5 = QToolButton()
        self.box_4_button_5.setText('双边滤波')
        self.box_4_button_5.setAutoRaise(True)

        self.v_box_1.addWidget(self.box_1_button_1)
        self.v_box_1.addWidget(self.box_1_button_2)
        self.v_box_1.addWidget(self.box_1_button_3)
        self.v_box_1.addWidget(self.box_1_button_4)
        self.v_box_1.addWidget(self.box_1_button_5)
        self.v_box_1.addWidget(self.box_1_button_6)
        self.v_box_1.addStretch(0)
        self.group_box_1.setLayout(self.v_box_1)

        self.v_box_2.addWidget(self.box_2_button_1)
        self.v_box_2.addWidget(self.box_2_button_2)
        self.v_box_2.addWidget(self.box_2_button_3)
        self.v_box_2.addWidget(self.box_2_button_4)
        self.v_box_2.addStretch(0)
        self.group_box_2.setLayout(self.v_box_2)

        self.v_box_3.addWidget(self.box_3_button_1)
        self.v_box_3.addWidget(self.box_3_button_2)
        self.v_box_3.addStretch(0)
        self.group_box_3.setLayout(self.v_box_3)

        self.v_box_4.addWidget(self.box_4_button_1)
        self.v_box_4.addWidget(self.box_4_button_2)
        self.v_box_4.addWidget(self.box_4_button_3)
        self.v_box_4.addWidget(self.box_4_button_4)
        self.v_box_4.addWidget(self.box_4_button_5)
        self.v_box_4.addStretch(0)
        self.group_box_4.setLayout(self.v_box_4)

        self.tool_box.addItem(self.group_box_1, "图像基本处理")
        self.tool_box.addItem(self.group_box_2, "图像位置变换")
        self.tool_box.addItem(self.group_box_3, "图像噪声添加")
        self.tool_box.addItem(self.group_box_4, "图像滤波处理")
        self.tool_box.addItem(self.group_box_5, "图像边缘检测")
        self.tool_box.addItem(self.group_box_6, "图像信息嵌入")
        self.tool_box.addItem(self.group_box_7, "图像信息提取")

        # self.tool_box.setCurrentIndex(0)
        vbox = QVBoxLayout()
        vbox.addWidget(self.tool_box)
        self.setLayout(vbox)


class PicWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.v_box_1 = QVBoxLayout()
        self.v_box_1_wid = QWidget()
        self.v_box_2 = QVBoxLayout()
        self.v_box_2_wid = QWidget()
        self.v_box_3 = QVBoxLayout()
        self.v_box_3_wid = QWidget()

        self.pic_label = QLabel('上一步图形')
        self.pic_label.setMaximumHeight(20)
        self.pic_show_label = QLabel('图片显示区')
        self.pic_show_label.setStyleSheet('background-color:#fff')

        self.v_box_1.addWidget(self.pic_label)
        self.v_box_1.addSpacing(30)
        self.v_box_1.addWidget(self.pic_show_label)

        self.contrast_label = QLabel('当前图像')
        self.contrast_label.setMaximumHeight(20)
        self.contrast_show_label = QLabel('图片显示区')
        self.contrast_show_label.setStyleSheet('background-color:#fff')

        self.v_box_2.addWidget(self.contrast_label)
        self.v_box_2.addSpacing(30)
        self.v_box_2.addWidget(self.contrast_show_label)

        self.his_label_this = QLabel('当天图像直方图')
        self.his_label_this.setMaximumHeight(20)
        self.his_show_label_this = QLabel('直方图显示区')
        self.his_show_label_this.setStyleSheet('background-color:#fff')
        self.his_label_last = QLabel('上一图像直方图')
        self.his_label_last.setMaximumHeight(20)
        self.his_show_label_last = QLabel('直方图显示区')
        self.his_show_label_last.setStyleSheet('background-color:#fff')

        self.v_box_3.addWidget(self.his_label_this)
        self.v_box_3.addWidget(self.his_show_label_this)
        self.v_box_3.addWidget(self.his_label_last)
        self.v_box_3.addWidget(self.his_show_label_last)

        self.v_box_1_wid.setLayout(self.v_box_1)
        self.v_box_2_wid.setLayout(self.v_box_2)
        self.v_box_3_wid.setLayout(self.v_box_3)

        self.grid.addWidget(self.v_box_1_wid, 1, 1, 8, 5)
        self.grid.addWidget(self.v_box_2_wid, 1, 6, 8, 5)
        self.grid.addWidget(self.v_box_3_wid, 1, 11, 9, 5)

        self.setLayout(self.grid)


class TextWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.v_box = QVBoxLayout()

        self.embed_label = QLabel("嵌入信息文本框")
        self.embed_label.setMaximumHeight(20)
        self.embed_text = QTextEdit("嵌入信息...")

        self.extract_label = QLabel("提取信息文本框")
        self.extract_label.setMaximumHeight(20)
        self.extract_text = QTextEdit("提取信息...")

        self.v_box.addWidget(self.embed_label)
        self.v_box.addWidget(self.embed_text)
        self.v_box.addWidget(self.extract_label)
        self.v_box.addWidget(self.extract_text)
        self.setLayout(self.v_box)


class SliderDialog(QWidget):
    threshold_max = 255
    # 信号
    before_close_signal = pyqtSignal(int, bool)
    signal_flag = False
    switch_flag = 1

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Threshold Setting')
        # 只有最小化按钮
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # 阻塞窗口
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(500, 200)

        # 创建水平方向滑动条
        self.threshold_slider = QSlider(Qt.Horizontal)
        self.threshold_slider.setMaximumHeight(20)
        # 设置最小值
        self.threshold_slider.setMinimum(0)
        # 设置最大值
        self.threshold_slider.setMaximum(self.threshold_max)
        # 步长
        self.threshold_slider.setSingleStep(1)
        # 设置当前值
        self.threshold_slider.setValue(self.threshold_max / 2)
        # 刻度位置，刻度下方
        self.threshold_slider.setTickPosition(QSlider.NoTicks)
        # 设置刻度间距
        self.threshold_slider.setTickInterval(5)
        # 设置连接信号槽函数
        self.threshold_slider.valueChanged.connect(self.return_value)

        self.label_tip = QLabel('Threshold Value')
        self.label_tip.setMaximumHeight(20)
        self.label_tip_value = QLabel(str(self.threshold_slider.value()))
        self.label_tip_value.setMaximumHeight(20)

        self.ok_button = QPushButton('OK')
        self.ok_button.clicked.connect(self.closeEvent)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.label_tip, 1, 1)
        grid_layout.addWidget(self.label_tip_value, 1, 2)
        grid_layout.addWidget(self.threshold_slider, 2, 1, 2, 2)
        grid_layout.addWidget(self.ok_button, 3, 2)
        self.setLayout(grid_layout)
        # self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        # 获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center()
        # 获取显示器的分辨率，然后得到屏幕中间点的位置
        qr.moveCenter(cp)
        # 然后把主窗口框架的中心点放置到屏幕的中心位置
        self.move(qr.topLeft())

    def return_value(self):
        if self.switch_flag == 1:
            self.label_tip_value.setText(str(self.threshold_slider.value()))
        elif self.switch_flag == 2:
            self.label_tip_value.setText(str(self.threshold_slider.value() / 1000))
        return self.threshold_slider.value()

    def closeEvent(self, event):
        content = self.return_value()
        if self.signal_flag:
            self.signal_flag = False
        else:
            self.signal_flag = True
        self.before_close_signal.emit(content, self.signal_flag)
        self.close()
