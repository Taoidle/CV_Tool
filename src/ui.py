"""

Copyright (c) 2020 Taoidle
CV Tool is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.

"""

import json, util
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QGridLayout, QPushButton, QDesktopWidget, QToolBox, QGroupBox, \
    QHBoxLayout, QVBoxLayout, QToolButton, QTextEdit, QRadioButton, QLineEdit, QFileDialog
from PyQt5.QtCore import Qt, pyqtSignal


class PicToolsWindow(QWidget):

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
        self.v_box_5 = QVBoxLayout()

        self.group_box_6 = QGroupBox()
        self.group_box_6.setMaximumWidth(200)
        self.v_box_6 = QVBoxLayout()

        self.group_box_7 = QGroupBox()
        self.group_box_7.setMaximumWidth(200)
        self.v_box_7 = QVBoxLayout()

        self.group_box_8 = QGroupBox()
        self.group_box_8.setMaximumWidth(200)
        self.v_box_8 = QVBoxLayout()

        self.group_box_9 = QGroupBox()
        self.group_box_9.setMaximumWidth(200)
        self.v_box_9 = QVBoxLayout()

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
        self.box_1_button_7 = QToolButton()
        self.box_1_button_7.setText('亮度对比度')
        self.box_1_button_7.setAutoRaise(True)
        self.box_1_button_8 = QToolButton()
        self.box_1_button_8.setText('图像叠加')
        self.box_1_button_8.setAutoRaise(True)
        self.box_1_button_9 = QToolButton()
        self.box_1_button_9.setText('分量提取')
        self.box_1_button_9.setAutoRaise(True)

        self.box_2_button_1 = QToolButton()
        self.box_2_button_1.setText('水平镜像')
        self.box_2_button_1.setAutoRaise(True)
        self.box_2_button_2 = QToolButton()
        self.box_2_button_2.setText('垂直镜像')
        self.box_2_button_2.setAutoRaise(True)
        self.box_2_button_3 = QToolButton()
        self.box_2_button_3.setText('逆时针 90°')
        self.box_2_button_3.setAutoRaise(True)
        self.box_2_button_4 = QToolButton()
        self.box_2_button_4.setText('顺时针 90°')
        self.box_2_button_4.setAutoRaise(True)
        self.box_2_button_5 = QToolButton()
        self.box_2_button_5.setText('逆时针旋转')
        self.box_2_button_5.setAutoRaise(True)
        self.box_2_button_6 = QToolButton()
        self.box_2_button_6.setText('顺时针旋转')
        self.box_2_button_6.setAutoRaise(True)

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

        self.box_5_button_1 = QToolButton()
        self.box_5_button_1.setText("Canny算子")
        self.box_5_button_1.setAutoRaise(True)
        self.box_5_button_2 = QToolButton()
        self.box_5_button_2.setText("Sobel算子")
        self.box_5_button_2.setAutoRaise(True)
        self.box_5_button_3 = QToolButton()
        self.box_5_button_3.setText("Laplacian算子")
        self.box_5_button_3.setAutoRaise(True)
        self.box_5_button_4 = QToolButton()
        self.box_5_button_4.setText("Scharr滤波器")
        self.box_5_button_4.setAutoRaise(True)
        self.box_5_button_5 = QToolButton()
        self.box_5_button_5.setText('标准霍夫变换')
        self.box_5_button_5.setAutoRaise(True)
        self.box_5_button_6 = QToolButton()
        self.box_5_button_6.setText('累计概率霍夫变换')
        self.box_5_button_6.setAutoRaise(True)
        self.box_5_button_7 = QToolButton()
        self.box_5_button_7.setText('霍夫圆变换')
        self.box_5_button_7.setAutoRaise(True)
        self.box_5_button_8 = QToolButton()
        self.box_5_button_8.setText('DCT变换')
        self.box_5_button_8.setAutoRaise(True)

        self.box_6_button_1 = QToolButton()
        self.box_6_button_1.setText("膨胀")
        self.box_6_button_1.setAutoRaise(True)
        self.box_6_button_2 = QToolButton()
        self.box_6_button_2.setText("腐蚀")
        self.box_6_button_2.setAutoRaise(True)
        self.box_6_button_3 = QToolButton()
        self.box_6_button_3.setText("开运算")
        self.box_6_button_3.setAutoRaise(True)
        self.box_6_button_4 = QToolButton()
        self.box_6_button_4.setText("闭运算")
        self.box_6_button_4.setAutoRaise(True)
        self.box_6_button_5 = QToolButton()
        self.box_6_button_5.setText("顶帽")
        self.box_6_button_5.setAutoRaise(True)
        self.box_6_button_6 = QToolButton()
        self.box_6_button_6.setText("黑帽")
        self.box_6_button_6.setAutoRaise(True)
        self.box_6_button_7 = QToolButton()
        self.box_6_button_7.setText("形态学梯度")
        self.box_6_button_7.setAutoRaise(True)

        self.box_7_button_1 = QToolButton()
        self.box_7_button_1.setText("向上采样 ")
        self.box_7_button_1.setAutoRaise(True)
        self.box_7_button_2 = QToolButton()
        self.box_7_button_2.setText("向下采样")
        self.box_7_button_2.setAutoRaise(True)
        self.box_7_button_3 = QToolButton()
        self.box_7_button_3.setText('拉普拉斯金字塔')
        self.box_7_button_3.setAutoRaise(True)

        self.box_8_button_1 = QToolButton()
        self.box_8_button_1.setText("LSB嵌入")
        self.box_8_button_1.setAutoRaise(True)
        self.box_8_button_2 = QToolButton()
        self.box_8_button_2.setText("DCT嵌入")
        self.box_8_button_2.setAutoRaise(True)

        self.box_9_button_1 = QToolButton()
        self.box_9_button_1.setText("LSB提取")
        self.box_9_button_1.setAutoRaise(True)
        self.box_9_button_2 = QToolButton()
        self.box_9_button_2.setText("DCT提取")
        self.box_9_button_2.setAutoRaise(True)

        self.v_box_1.addWidget(self.box_1_button_1)
        self.v_box_1.addWidget(self.box_1_button_2)
        self.v_box_1.addWidget(self.box_1_button_3)
        self.v_box_1.addWidget(self.box_1_button_4)
        self.v_box_1.addWidget(self.box_1_button_5)
        self.v_box_1.addWidget(self.box_1_button_6)
        self.v_box_1.addWidget(self.box_1_button_7)
        self.v_box_1.addWidget(self.box_1_button_8)
        self.v_box_1.addWidget(self.box_1_button_9)
        self.v_box_1.addStretch(0)
        self.group_box_1.setLayout(self.v_box_1)

        self.v_box_2.addWidget(self.box_2_button_1)
        self.v_box_2.addWidget(self.box_2_button_2)
        self.v_box_2.addWidget(self.box_2_button_3)
        self.v_box_2.addWidget(self.box_2_button_4)
        self.v_box_2.addWidget(self.box_2_button_5)
        self.v_box_2.addWidget(self.box_2_button_6)
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

        self.v_box_5.addWidget(self.box_5_button_1)
        self.v_box_5.addWidget(self.box_5_button_2)
        self.v_box_5.addWidget(self.box_5_button_3)
        self.v_box_5.addWidget(self.box_5_button_4)
        self.v_box_5.addWidget(self.box_5_button_5)
        self.v_box_5.addWidget(self.box_5_button_6)
        self.v_box_5.addWidget(self.box_5_button_7)
        self.v_box_5.addWidget(self.box_5_button_8)
        self.v_box_5.addStretch(0)
        self.group_box_5.setLayout(self.v_box_5)

        self.v_box_6.addWidget(self.box_6_button_1)
        self.v_box_6.addWidget(self.box_6_button_2)
        self.v_box_6.addWidget(self.box_6_button_3)
        self.v_box_6.addWidget(self.box_6_button_4)
        self.v_box_6.addWidget(self.box_6_button_5)
        self.v_box_6.addWidget(self.box_6_button_6)
        self.v_box_6.addWidget(self.box_6_button_7)
        self.v_box_6.addStretch(0)
        self.group_box_6.setLayout(self.v_box_6)

        self.v_box_7.addWidget(self.box_7_button_1)
        self.v_box_7.addWidget(self.box_7_button_2)
        self.v_box_7.addWidget(self.box_7_button_3)
        self.v_box_7.addStretch(0)
        self.group_box_7.setLayout(self.v_box_7)

        self.v_box_8.addWidget(self.box_8_button_1)
        self.v_box_8.addWidget(self.box_8_button_2)
        self.v_box_8.addStretch(0)
        self.group_box_8.setLayout(self.v_box_8)

        self.v_box_9.addWidget(self.box_9_button_1)
        self.v_box_9.addWidget(self.box_9_button_2)
        self.v_box_9.addStretch(0)
        self.group_box_9.setLayout(self.v_box_9)

        self.tool_box.addItem(self.group_box_1, "图像基本处理")
        self.tool_box.addItem(self.group_box_2, "图像位置变换")
        self.tool_box.addItem(self.group_box_3, "图像噪声添加")
        self.tool_box.addItem(self.group_box_4, "图像滤波处理")
        self.tool_box.addItem(self.group_box_5, "图像变换")
        self.tool_box.addItem(self.group_box_6, "图像形态学操作")
        self.tool_box.addItem(self.group_box_7, "图像金字塔")
        self.tool_box.addItem(self.group_box_8, "图像信息嵌入")
        self.tool_box.addItem(self.group_box_9, "图像信息提取")

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
        self.v_box_1.addSpacing(20)
        self.v_box_1.addWidget(self.pic_show_label)

        self.contrast_label = QLabel('当前图像')
        self.contrast_label.setMaximumHeight(20)
        self.contrast_show_label = QLabel('图片显示区')
        self.contrast_show_label.setStyleSheet('background-color:#fff')

        self.v_box_2.addWidget(self.contrast_label)
        self.v_box_2.addSpacing(20)
        self.v_box_2.addWidget(self.contrast_show_label)

        self.his_label_this = QLabel('当前图像直方图')
        self.his_label_this.setMaximumHeight(20)
        self.his_show_label_this = QLabel('直方图显示区')
        self.his_show_label_this.setStyleSheet('background-color:#fff')
        self.his_label_last = QLabel('上一图像直方图')
        self.his_label_last.setMaximumHeight(20)
        self.his_show_label_last = QLabel('直方图显示区')
        self.his_show_label_last.setStyleSheet('background-color:#fff')

        self.v_box_3.addWidget(self.his_label_this)
        self.v_box_3.addSpacing(20)
        self.v_box_3.addWidget(self.his_show_label_this)
        self.v_box_3.addSpacing(20)
        self.v_box_3.addWidget(self.his_label_last)
        self.v_box_3.addSpacing(20)
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
        self.mse_label = QLabel("MSE:")
        self.mse_label.setMaximumHeight(20)
        self.mse_label_text = QLabel("")
        self.mse_label_text.setMaximumHeight(20)
        self.mse_box = QHBoxLayout()
        self.mse_box.addWidget(self.mse_label)
        self.mse_box.addWidget(self.mse_label_text)
        self.mse_box_wid = QWidget()
        self.mse_box_wid.setLayout(self.mse_box)

        self.psnr_label = QLabel("PSNR:")
        self.psnr_label.setMaximumHeight(20)
        self.psnr_label_text = QLabel("")
        self.psnr_label_text.setMaximumHeight(20)
        self.psnr_box = QHBoxLayout()
        self.psnr_box.addWidget(self.psnr_label)
        self.psnr_box.addWidget(self.psnr_label_text)
        self.psnr_box_wid = QWidget()
        self.psnr_box_wid.setLayout(self.psnr_box)

        self.ssim_label = QLabel("SSIM:")
        self.ssim_label.setMaximumHeight(20)
        self.ssim_label_text = QLabel("")
        self.ssim_label_text.setMaximumHeight(20)
        self.ssim_box = QHBoxLayout()
        self.ssim_box.addWidget(self.ssim_label)
        self.ssim_box.addWidget(self.ssim_label_text)
        self.ssim_box_wid = QWidget()
        self.ssim_box_wid.setLayout(self.ssim_box)

        self.embed_label = QLabel("嵌入信息文本框")
        self.embed_label.setMaximumHeight(20)
        self.embed_text = QTextEdit("input...")
        self.embed_text.setMaximumWidth(300)

        self.extract_label = QLabel("提取信息文本框")
        self.extract_label.setMaximumHeight(20)
        self.extract_text = QTextEdit("output...")
        self.extract_text.setMaximumWidth(300)

        self.text_box = QVBoxLayout()
        self.text_box.addWidget(self.embed_label)
        self.text_box.addWidget(self.embed_text)
        self.text_box.addWidget(self.extract_label)
        self.text_box.addWidget(self.extract_text)
        self.text_box_wid = QWidget()
        self.text_box_wid.setLayout(self.text_box)

        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.mse_box_wid)
        self.v_box.addWidget(self.psnr_box_wid)
        self.v_box.addWidget(self.ssim_box_wid)
        self.v_box.addWidget(self.text_box_wid)
        self.setLayout(self.v_box)


class SliderDialog(QWidget):
    threshold_max = 255
    # 信号
    before_close_signal_1 = pyqtSignal(int, bool, bool)
    before_close_signal_2 = pyqtSignal(int, int, bool, bool)
    signal_flag, morphology_flag = False, False
    cancel_flag = True
    switch_flag = 1

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('阈值设置')
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
        if self.switch_flag == 1:
            self.label_tip_value = QLabel(str(self.threshold_slider.value()))
        else:
            self.label_tip_value = QLabel(str(self.threshold_slider.value() / 1000))
        self.label_tip_value.setMaximumHeight(20)

        self.cancel_button = QPushButton('取消')
        self.cancel_button.clicked.connect(self.cancelEvent)
        self.ok_button = QPushButton('确定')
        self.ok_button.clicked.connect(self.closeEvent)

        if self.morphology_flag:
            self.morphology_init()
        else:
            grid_layout = QGridLayout()
            grid_layout.addWidget(self.label_tip, 1, 1)
            grid_layout.addWidget(self.label_tip_value, 1, 2)
            grid_layout.addWidget(self.threshold_slider, 2, 1, 1, 2)
            grid_layout.addWidget(self.cancel_button, 3, 1)
            grid_layout.addWidget(self.ok_button, 3, 2)
            self.setLayout(grid_layout)
        self.setWindowIcon(QIcon('res/img/logo.png'))
        # self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.show()
        self.center()

    def morphology_init(self):

        self.h_box_button_1 = QRadioButton('椭圆形')
        self.h_box_button_1.setChecked(True)
        self.h_box_button_2 = QRadioButton('矩形')
        self.h_box_button_3 = QRadioButton('十字形')

        h_box = QHBoxLayout()
        h_box.setSpacing(10)
        h_box.addWidget(self.h_box_button_1)
        h_box.addWidget(self.h_box_button_2)
        h_box.addWidget(self.h_box_button_3)

        h_box_wid = QWidget()
        h_box_wid.setLayout(h_box)

        title_label = QLabel('结构元素:')

        v_box = QVBoxLayout()
        v_box.setSpacing(10)
        v_box.addWidget(title_label)
        v_box.addWidget(h_box_wid)

        v_box_wid = QWidget()
        v_box_wid.setLayout(v_box)

        grid_layout = QGridLayout()
        grid_layout.addWidget(v_box_wid, 1, 1, 1, 2)
        grid_layout.addWidget(self.label_tip, 2, 1)
        grid_layout.addWidget(self.label_tip_value, 2, 2)
        grid_layout.addWidget(self.threshold_slider, 3, 1, 1, 2)
        grid_layout.addWidget(self.cancel_button, 4, 1)
        grid_layout.addWidget(self.ok_button, 4, 2)
        self.setLayout(grid_layout)

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

    def morphology_check(self):
        if self.h_box_button_1.isChecked():
            return 1
        elif self.h_box_button_2.isChecked():
            return 2
        elif self.h_box_button_3.isChecked():
            return 3
        else:
            pass

    def cancelEvent(self):
        self.cancel_flag = False
        if self.morphology_flag:
            content = self.return_value()
            morphology_val = self.morphology_check()
            self.before_close_signal_2.emit(content, morphology_val, self.signal_flag, self.cancel_flag)
            self.close()
        else:
            content = self.return_value()
            self.before_close_signal_1.emit(content, self.signal_flag, self.cancel_flag)
            self.close()

    def closeEvent(self, event):
        if self.morphology_flag:
            content = self.return_value()
            morphology_val = self.morphology_check()
            if self.signal_flag:
                self.signal_flag = False
            else:
                self.signal_flag = True
            self.before_close_signal_2.emit(content, morphology_val, self.signal_flag, self.cancel_flag)
            self.close()
        else:
            content = self.return_value()
            if self.signal_flag:
                self.signal_flag = False
            else:
                self.signal_flag = True
            self.before_close_signal_1.emit(content, self.signal_flag, self.cancel_flag)
            self.close()


class DoubleSliderDialog(QWidget):
    threshold_max_1 = 3000
    threshold_max_2 = 100
    # 信号
    before_close_signal = pyqtSignal(int, int, bool, bool)
    cancel_flag = True
    signal_flag = False
    switch_flag = 1

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('对比度亮度调节')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # 阻塞窗口
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(500, 200)
        self.threshold_slider_1 = QSlider(Qt.Horizontal)
        self.threshold_slider_1.setMaximumHeight(20)
        self.threshold_slider_1.setMinimum(0)
        self.threshold_slider_1.setMaximum(self.threshold_max_1)
        self.threshold_slider_1.setSingleStep(1)
        self.threshold_slider_1.setValue(1200)
        self.threshold_slider_1.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_1.setTickInterval(5)
        self.threshold_slider_1.valueChanged.connect(self.return_value)

        self.threshold_slider_2 = QSlider(Qt.Horizontal)
        self.threshold_slider_2.setMaximumHeight(20)
        self.threshold_slider_2.setMinimum(0)
        self.threshold_slider_2.setMaximum(self.threshold_max_2)
        self.threshold_slider_2.setSingleStep(1)
        self.threshold_slider_2.setValue(100)
        self.threshold_slider_2.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_2.setTickInterval(5)
        self.threshold_slider_2.valueChanged.connect(self.return_value)

        self.label_tip_1 = QLabel('对比度')
        self.label_tip_1.setMaximumHeight(20)
        if self.switch_flag == 1:
            self.label_tip_1_value = QLabel(str(self.threshold_slider_1.value() / 1000))
        else:
            self.label_tip_1_value = QLabel(str(self.threshold_slider_1.value()))
        self.label_tip_1_value.setMaximumHeight(20)
        self.label_tip_2 = QLabel('亮度')
        self.label_tip_2.setMaximumHeight(20)
        self.label_tip_2_value = QLabel(str(self.threshold_slider_2.value()))
        self.label_tip_2_value.setMaximumHeight(20)

        self.cancel_button = QPushButton('取消')
        self.cancel_button.clicked.connect(self.cancelEvent)
        self.ok_button = QPushButton('确定')
        self.ok_button.clicked.connect(self.closeEvent)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.label_tip_1, 1, 1)
        grid_layout.addWidget(self.label_tip_1_value, 1, 2)
        grid_layout.addWidget(self.threshold_slider_1, 2, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_2, 3, 1)
        grid_layout.addWidget(self.label_tip_2_value, 3, 2)
        grid_layout.addWidget(self.threshold_slider_2, 4, 1, 1, 2)
        grid_layout.addWidget(self.cancel_button, 5, 1)
        grid_layout.addWidget(self.ok_button, 5, 2)
        self.setLayout(grid_layout)
        self.setWindowIcon(QIcon('res/img/logo.png'))
        self.show()
        self.center()

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
            self.label_tip_1_value.setText(str(self.threshold_slider_1.value() / 1000))
            self.label_tip_2_value.setText(str(self.threshold_slider_2.value()))
            return self.threshold_slider_1.value() / 1000, self.threshold_slider_2.value()
        else:
            self.label_tip_1_value.setText(str(self.threshold_slider_1.value()))
            self.label_tip_2_value.setText(str(self.threshold_slider_2.value()))
            return self.threshold_slider_1.value(), self.threshold_slider_2.value()

    def cancelEvent(self):
        self.cancel_flag = False
        content_1, content_2 = self.return_value()
        self.before_close_signal.emit(content_1, content_2, self.signal_flag, self.cancel_flag)
        self.close()

    def closeEvent(self, event):
        content_1, content_2 = self.return_value()
        if self.signal_flag:
            self.signal_flag = False
        else:
            self.signal_flag = True
        self.before_close_signal.emit(content_1, content_2, self.signal_flag, self.cancel_flag)
        self.close()


class ThreeSliderDialog(QWidget):
    threshold_max_1 = 3000
    threshold_max_2 = 360
    threshold_max_3 = 1000
    # 信号
    before_close_signal = pyqtSignal(int, int, int, bool, bool)
    signal_flag = False
    switch_flag = 1
    cancel_flag = True

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('霍夫变换')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(500, 200)

        self.threshold_slider_1 = QSlider(Qt.Horizontal)
        self.threshold_slider_1.setMaximumHeight(20)
        self.threshold_slider_1.setMinimum(1)
        self.threshold_slider_1.setMaximum(self.threshold_max_1)
        self.threshold_slider_1.setSingleStep(1)
        self.threshold_slider_1.setValue(100)
        self.threshold_slider_1.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_1.setTickInterval(5)
        self.threshold_slider_1.valueChanged.connect(self.return_value)

        self.threshold_slider_2 = QSlider(Qt.Horizontal)
        self.threshold_slider_2.setMaximumHeight(20)
        self.threshold_slider_2.setMinimum(1)
        self.threshold_slider_2.setMaximum(self.threshold_max_2)
        self.threshold_slider_2.setSingleStep(1)
        self.threshold_slider_2.setValue(180)
        self.threshold_slider_2.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_2.setTickInterval(5)
        self.threshold_slider_2.valueChanged.connect(self.return_value)

        self.threshold_slider_3 = QSlider(Qt.Horizontal)
        self.threshold_slider_3.setMaximumHeight(20)
        self.threshold_slider_3.setMinimum(0)
        self.threshold_slider_3.setMaximum(self.threshold_max_3)
        self.threshold_slider_3.setSingleStep(1)
        self.threshold_slider_3.setValue(200)
        self.threshold_slider_3.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_3.setTickInterval(5)
        self.threshold_slider_3.valueChanged.connect(self.return_value)

        self.label_tip_1 = QLabel('r')
        self.label_tip_1.setMaximumHeight(20)
        self.label_tip_1_value = QLabel(str(self.threshold_slider_1.value() / 100))
        self.label_tip_1_value.setMaximumHeight(20)
        self.label_tip_2 = QLabel('角度θ')
        self.label_tip_2.setMaximumHeight(20)
        self.label_tip_2_value = QLabel(str(180 / self.threshold_slider_2.value()))
        self.label_tip_2_value.setMaximumHeight(20)
        self.label_tip_3 = QLabel('累加数')
        self.label_tip_3.setMaximumHeight(20)
        self.label_tip_3_value = QLabel(str(self.threshold_slider_3.value()))
        self.label_tip_3_value.setMaximumHeight(20)

        self.cancel_button = QPushButton('取消')
        self.cancel_button.clicked.connect(self.cancelEvent)
        self.ok_button = QPushButton('确定')
        self.ok_button.clicked.connect(self.closeEvent)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.label_tip_1, 1, 1)
        grid_layout.addWidget(self.label_tip_1_value, 1, 2)
        grid_layout.addWidget(self.threshold_slider_1, 2, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_2, 3, 1)
        grid_layout.addWidget(self.label_tip_2_value, 3, 2)
        grid_layout.addWidget(self.threshold_slider_2, 4, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_3, 5, 1)
        grid_layout.addWidget(self.label_tip_3_value, 5, 2)
        grid_layout.addWidget(self.threshold_slider_3, 6, 1, 1, 2)
        grid_layout.addWidget(self.cancel_button, 7, 1)
        grid_layout.addWidget(self.ok_button, 7, 2)
        self.setLayout(grid_layout)
        self.setWindowIcon(QIcon('res/img/logo.png'))
        self.show()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        # 获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center()
        # 获取显示器的分辨率，然后得到屏幕中间点的位置
        qr.moveCenter(cp)
        # 然后把主窗口框架的中心点放置到屏幕的中心位置
        self.move(qr.topLeft())

    def return_value(self):
        self.label_tip_1_value.setText(str(self.threshold_slider_1.value() / 100))
        self.label_tip_2_value.setText(str(180 / self.threshold_slider_2.value()))
        self.label_tip_3_value.setText(str(self.threshold_slider_3.value()))
        return self.threshold_slider_1.value() / 100, self.threshold_slider_2.value(), self.threshold_slider_3.value()

    def cancelEvent(self):
        self.cancel_flag = False
        content_1, content_2, content_3 = self.return_value()
        self.before_close_signal.emit(content_1, content_2, content_3, self.signal_flag, self.cancel_flag)
        self.close()

    def closeEvent(self, event):
        content_1, content_2, content_3 = self.return_value()
        if self.signal_flag:
            self.signal_flag = False
        else:
            self.signal_flag = True
        self.before_close_signal.emit(content_1, content_2, content_3, self.signal_flag, self.cancel_flag)
        self.close()


class FourSliderWindow(QWidget):
    switch_flag = 1
    before_close_signal_1 = pyqtSignal(int, int, int, int, bool, bool)
    threshold_max_1, threshold_max_2, threshold_max_3, threshold_max_4 = 0, 0, 0, 0
    signal_flag = False
    cancel_flag = True

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        if self.switch_flag == 1:
            self.dct_slider()

    def dct_slider(self):
        self.setWindowTitle('DCT变换')
        # 只有最小化按钮
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # 阻塞窗口
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(500, 200)

        self.threshold_slider_1 = QSlider(Qt.Horizontal)
        self.threshold_slider_1.setMaximumHeight(20)
        self.threshold_slider_1.setMinimum(0)
        self.threshold_slider_1.setMaximum(self.threshold_max_1)
        self.threshold_slider_1.setSingleStep(1)
        self.threshold_slider_1.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_1.setTickInterval(5)
        self.threshold_slider_1.valueChanged.connect(self.return_value)

        self.threshold_slider_2 = QSlider(Qt.Horizontal)
        self.threshold_slider_2.setMaximumHeight(20)
        self.threshold_slider_2.setMinimum(0)
        self.threshold_slider_2.setMaximum(self.threshold_max_2)
        self.threshold_slider_2.setSingleStep(1)
        self.threshold_slider_2.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_2.setTickInterval(5)
        self.threshold_slider_2.valueChanged.connect(self.return_value)

        self.threshold_slider_3 = QSlider(Qt.Horizontal)
        self.threshold_slider_3.setMaximumHeight(20)
        self.threshold_slider_3.setMinimum(0)
        self.threshold_slider_3.setMaximum(self.threshold_max_3)
        self.threshold_slider_3.setSingleStep(1)
        self.threshold_slider_3.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_3.setTickInterval(5)
        self.threshold_slider_3.valueChanged.connect(self.return_value)

        self.threshold_slider_4 = QSlider(Qt.Horizontal)
        self.threshold_slider_4.setMaximumHeight(20)
        self.threshold_slider_4.setMinimum(0)
        self.threshold_slider_4.setMaximum(self.threshold_max_4)
        self.threshold_slider_4.setSingleStep(1)
        self.threshold_slider_4.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_4.setTickInterval(5)
        self.threshold_slider_4.valueChanged.connect(self.return_value)

        self.label_tip_1 = QLabel('y轴起始点:')
        self.label_tip_1.setMaximumHeight(20)
        self.label_tip_1_value = QLabel(str(self.threshold_slider_1.value()))
        self.label_tip_1_value.setMaximumHeight(20)
        self.label_tip_2 = QLabel('y轴末点:')
        self.label_tip_2.setMaximumHeight(20)
        self.label_tip_2_value = QLabel(str(self.threshold_slider_2.value()))
        self.label_tip_2_value.setMaximumHeight(20)
        self.label_tip_3 = QLabel('x轴起始点')
        self.label_tip_3.setMaximumHeight(20)
        self.label_tip_3_value = QLabel(str(self.threshold_slider_3.value()))
        self.label_tip_3_value.setMaximumHeight(20)
        self.label_tip_4 = QLabel('x轴末点')
        self.label_tip_4.setMaximumHeight(20)
        self.label_tip_4_value = QLabel(str(self.threshold_slider_4.value()))
        self.label_tip_4_value.setMaximumHeight(20)

        self.cancel_button = QPushButton('取消')
        self.cancel_button.clicked.connect(self.cancelEvent)
        self.ok_button = QPushButton('确定')
        self.ok_button.clicked.connect(self.closeEvent)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.label_tip_1, 1, 1)
        grid_layout.addWidget(self.label_tip_1_value, 1, 2)
        grid_layout.addWidget(self.threshold_slider_1, 2, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_2, 3, 1)
        grid_layout.addWidget(self.label_tip_2_value, 3, 2)
        grid_layout.addWidget(self.threshold_slider_2, 4, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_3, 5, 1)
        grid_layout.addWidget(self.label_tip_3_value, 5, 2)
        grid_layout.addWidget(self.threshold_slider_3, 6, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_4, 7, 1)
        grid_layout.addWidget(self.label_tip_4_value, 7, 2)
        grid_layout.addWidget(self.threshold_slider_4, 8, 1, 1, 2)
        grid_layout.addWidget(self.cancel_button, 9, 1)
        grid_layout.addWidget(self.ok_button, 9, 2)
        self.setLayout(grid_layout)
        self.setWindowIcon(QIcon('res/img/logo.png'))
        self.show()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def return_value(self):
        self.label_tip_1_value.setText(str(self.threshold_slider_1.value()))
        self.label_tip_2_value.setText(str(self.threshold_slider_2.value()))
        self.label_tip_3_value.setText(str(self.threshold_slider_3.value()))
        self.label_tip_4_value.setText(str(self.threshold_slider_4.value()))
        return self.threshold_slider_1.value(), self.threshold_slider_2.value(), self.threshold_slider_3.value(), self.threshold_slider_4.value()

    def cancelEvent(self):
        self.cancel_flag = False
        content_1, content_2, content_3, content_4 = self.return_value()
        self.before_close_signal_1.emit(content_1, content_2, content_3, content_4, self.signal_flag, self.cancel_flag)
        self.close()

    def closeEvent(self, event):
        content_1, content_2, content_3, content_4 = self.return_value()
        if self.signal_flag:
            self.signal_flag = False
        else:
            self.signal_flag = True
        self.before_close_signal_1.emit(content_1, content_2, content_3, content_4, self.signal_flag, self.cancel_flag)
        self.close()


class HoughCirclesWindow(QWidget):
    before_close_signal_1 = pyqtSignal(int, int, int, int, int, int, bool, bool)
    threshold_max_1, threshold_max_2, threshold_max_3, threshold_max_4, threshold_max_5, threshold_max_6 = 10, 0, 0, 0, 0, 0
    signal_flag = False
    cancel_flag = True

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('霍夫圆变换')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(500, 200)

        self.threshold_slider_1 = QSlider(Qt.Horizontal)
        self.threshold_slider_1.setMaximumHeight(20)
        self.threshold_slider_1.setMinimum(0)
        self.threshold_slider_1.setMaximum(self.threshold_max_1)
        self.threshold_slider_1.setValue(1)
        self.threshold_slider_1.setSingleStep(1)
        self.threshold_slider_1.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_1.setTickInterval(5)
        self.threshold_slider_1.valueChanged.connect(self.return_value)

        self.threshold_slider_2 = QSlider(Qt.Horizontal)
        self.threshold_slider_2.setMaximumHeight(20)
        self.threshold_slider_2.setMinimum(0)
        self.threshold_slider_2.setMaximum(self.threshold_max_2)
        self.threshold_slider_2.setSingleStep(1)
        self.threshold_slider_2.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_2.setTickInterval(5)
        self.threshold_slider_2.valueChanged.connect(self.return_value)

        self.threshold_slider_3 = QSlider(Qt.Horizontal)
        self.threshold_slider_3.setMaximumHeight(20)
        self.threshold_slider_3.setMinimum(0)
        self.threshold_slider_3.setMaximum(self.threshold_max_3)
        self.threshold_slider_3.setSingleStep(1)
        self.threshold_slider_3.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_3.setTickInterval(5)
        self.threshold_slider_3.valueChanged.connect(self.return_value)

        self.threshold_slider_4 = QSlider(Qt.Horizontal)
        self.threshold_slider_4.setMaximumHeight(20)
        self.threshold_slider_4.setMinimum(0)
        self.threshold_slider_4.setMaximum(self.threshold_max_4)
        self.threshold_slider_4.setSingleStep(1)
        self.threshold_slider_4.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_4.setTickInterval(5)
        self.threshold_slider_4.valueChanged.connect(self.return_value)

        self.threshold_slider_5 = QSlider(Qt.Horizontal)
        self.threshold_slider_5.setMaximumHeight(20)
        self.threshold_slider_5.setMinimum(0)
        self.threshold_slider_5.setMaximum(self.threshold_max_5)
        self.threshold_slider_5.setSingleStep(1)
        self.threshold_slider_5.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_5.setTickInterval(5)
        self.threshold_slider_5.valueChanged.connect(self.return_value)

        self.threshold_slider_6 = QSlider(Qt.Horizontal)
        self.threshold_slider_6.setMaximumHeight(20)
        self.threshold_slider_6.setMinimum(0)
        self.threshold_slider_6.setMaximum(self.threshold_max_6)
        self.threshold_slider_6.setSingleStep(1)
        self.threshold_slider_6.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_6.setTickInterval(5)
        self.threshold_slider_6.valueChanged.connect(self.return_value)

        self.label_tip_1 = QLabel('累加器:')
        self.label_tip_1.setMaximumHeight(20)
        self.label_tip_1_value = QLabel(str(self.threshold_slider_1.value()))
        self.label_tip_1_value.setMaximumHeight(20)
        self.label_tip_2 = QLabel('圆心最小距离:')
        self.label_tip_2.setMaximumHeight(20)
        self.label_tip_2_value = QLabel(str(self.threshold_slider_2.value()))
        self.label_tip_2_value.setMaximumHeight(20)
        self.label_tip_3 = QLabel('阈值：')
        self.label_tip_3.setMaximumHeight(20)
        self.label_tip_3_value = QLabel(str(self.threshold_slider_3.value()))
        self.label_tip_3_value.setMaximumHeight(20)
        self.label_tip_4 = QLabel('累加器阈值：')
        self.label_tip_4.setMaximumHeight(20)
        self.label_tip_4_value = QLabel(str(self.threshold_slider_4.value()))
        self.label_tip_4_value.setMaximumHeight(20)
        self.label_tip_5 = QLabel('圆半径最小值：')
        self.label_tip_5.setMaximumHeight(20)
        self.label_tip_5_value = QLabel(str(self.threshold_slider_5.value()))
        self.label_tip_5_value.setMaximumHeight(20)
        self.label_tip_6 = QLabel('圆半径最大值：')
        self.label_tip_6.setMaximumHeight(20)
        self.label_tip_6_value = QLabel(str(self.threshold_slider_6.value()))
        self.label_tip_6_value.setMaximumHeight(20)

        self.cancel_button = QPushButton('取消')
        self.cancel_button.clicked.connect(self.cancelEvent)
        self.ok_button = QPushButton('确定')
        self.ok_button.clicked.connect(self.closeEvent)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.label_tip_1, 1, 1)
        grid_layout.addWidget(self.label_tip_1_value, 1, 2)
        grid_layout.addWidget(self.threshold_slider_1, 2, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_2, 3, 1)
        grid_layout.addWidget(self.label_tip_2_value, 3, 2)
        grid_layout.addWidget(self.threshold_slider_2, 4, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_3, 5, 1)
        grid_layout.addWidget(self.label_tip_3_value, 5, 2)
        grid_layout.addWidget(self.threshold_slider_3, 6, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_4, 7, 1)
        grid_layout.addWidget(self.label_tip_4_value, 7, 2)
        grid_layout.addWidget(self.threshold_slider_4, 8, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_5, 9, 1)
        grid_layout.addWidget(self.label_tip_5_value, 9, 2)
        grid_layout.addWidget(self.threshold_slider_5, 10, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_6, 11, 1)
        grid_layout.addWidget(self.label_tip_6_value, 11, 2)
        grid_layout.addWidget(self.threshold_slider_6, 12, 1, 1, 2)
        grid_layout.addWidget(self.cancel_button, 13, 1)
        grid_layout.addWidget(self.ok_button, 13, 2)
        self.setLayout(grid_layout)

        self.show()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def return_value(self):
        self.label_tip_1_value.setText(str(self.threshold_slider_1.value()))
        self.label_tip_2_value.setText(str(self.threshold_slider_2.value()))
        self.label_tip_3_value.setText(str(self.threshold_slider_3.value()))
        self.label_tip_4_value.setText(str(self.threshold_slider_4.value()))
        self.label_tip_5_value.setText(str(self.threshold_slider_5.value()))
        self.label_tip_6_value.setText(str(self.threshold_slider_6.value()))
        return self.threshold_slider_1.value(), self.threshold_slider_2.value(), self.threshold_slider_3.value(), self.threshold_slider_4.value(), self.threshold_slider_5.value(), self.threshold_slider_6.value()

    def cancelEvent(self):
        self.cancel_flag = False
        content_1, content_2, content_3, content_4, content_5, content_6 = self.return_value()
        self.before_close_signal_1.emit(content_1, content_2, content_3, content_4, content_5, content_6,
                                        self.signal_flag, self.cancel_flag)
        self.close()

    def closeEvent(self, event):
        content_1, content_2, content_3, content_4, content_5, content_6 = self.return_value()
        if self.signal_flag:
            self.signal_flag = False
        else:
            self.signal_flag = True
        self.before_close_signal_1.emit(content_1, content_2, content_3, content_4, content_5, content_6,
                                        self.signal_flag, self.cancel_flag)
        self.close()


class HistogramWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label_this_rgb = QLabel('当前图像')
        self.label_this_rgb.setMaximumHeight(20)
        self.label_show_this_rgb = QLabel('图像显示区')
        self.label_show_this_rgb.setStyleSheet('background-color:#fff')
        self.label_show_this_rgb.setScaledContents(True)

        self.his_label_this_rgb = QLabel('当前图像直方图')
        self.his_label_this_rgb.setMaximumHeight(20)
        self.his_show_label_this_rgb = QLabel('直方图显示区')
        self.his_show_label_this_rgb.setStyleSheet('background-color:#fff')
        self.his_show_label_this_rgb.setScaledContents(True)

        self.label_this_r = QLabel('R分量图像')
        self.label_this_r.setMaximumHeight(20)
        self.label_show_this_r = QLabel('图像显示区')
        self.label_show_this_r.setStyleSheet('background-color:#fff')
        self.label_show_this_r.setScaledContents(True)

        self.his_label_this_r = QLabel('R分量直方图')
        self.his_label_this_r.setMaximumHeight(20)
        self.his_show_label_this_r = QLabel('直方图显示区')
        self.his_show_label_this_r.setStyleSheet('background-color:#fff')
        self.his_show_label_this_r.setScaledContents(True)

        self.label_this_g = QLabel('G分量图像')
        self.label_this_g.setMaximumHeight(20)
        self.label_show_this_g = QLabel('图像显示区')
        self.label_show_this_g.setStyleSheet('background-color:#fff')
        self.label_show_this_g.setScaledContents(True)

        self.his_label_this_g = QLabel('G分量直方图')
        self.his_label_this_g.setMaximumHeight(20)
        self.his_show_label_this_g = QLabel('直方图显示区')
        self.his_show_label_this_g.setStyleSheet('background-color:#fff')
        self.his_show_label_this_g.setScaledContents(True)

        self.label_this_b = QLabel('B分量图像')
        self.label_this_b.setMaximumHeight(20)
        self.label_show_this_b = QLabel('图像显示区')
        self.label_show_this_b.setStyleSheet('background-color:#fff')
        self.label_show_this_b.setScaledContents(True)

        self.his_label_this_b = QLabel('B分量直方图')
        self.his_label_this_b.setMaximumHeight(20)
        self.his_show_label_this_b = QLabel('直方图显示区')
        self.his_show_label_this_b.setStyleSheet('background-color:#fff')
        self.his_show_label_this_b.setScaledContents(True)

        self.v_box_1 = QVBoxLayout()
        self.v_box_2 = QVBoxLayout()
        self.v_box_3 = QVBoxLayout()
        self.v_box_4 = QVBoxLayout()
        self.v_box_5 = QVBoxLayout()
        self.v_box_6 = QVBoxLayout()
        self.v_box_7 = QVBoxLayout()
        self.v_box_8 = QVBoxLayout()

        self.v_box_1.addWidget(self.label_this_rgb)
        self.v_box_1.addWidget(self.label_show_this_rgb)

        self.v_box_2.addWidget(self.his_label_this_rgb)
        self.v_box_2.addWidget(self.his_show_label_this_rgb)

        self.v_box_3.addWidget(self.label_this_r)
        self.v_box_3.addWidget(self.label_show_this_r)

        self.v_box_4.addWidget(self.his_label_this_r)
        self.v_box_4.addWidget(self.his_show_label_this_r)

        self.v_box_5.addWidget(self.label_this_g)
        self.v_box_5.addWidget(self.label_show_this_g)

        self.v_box_6.addWidget(self.his_label_this_g)
        self.v_box_6.addWidget(self.his_show_label_this_g)

        self.v_box_7.addWidget(self.label_this_b)
        self.v_box_7.addWidget(self.label_show_this_b)

        self.v_box_8.addWidget(self.his_label_this_b)
        self.v_box_8.addWidget(self.his_show_label_this_b)

        self.v_box_1_wid = QWidget()
        self.v_box_2_wid = QWidget()
        self.v_box_3_wid = QWidget()
        self.v_box_4_wid = QWidget()
        self.v_box_5_wid = QWidget()
        self.v_box_6_wid = QWidget()
        self.v_box_7_wid = QWidget()
        self.v_box_8_wid = QWidget()

        self.v_box_1_wid.setLayout(self.v_box_1)
        self.v_box_2_wid.setLayout(self.v_box_2)
        self.v_box_3_wid.setLayout(self.v_box_3)
        self.v_box_4_wid.setLayout(self.v_box_4)
        self.v_box_5_wid.setLayout(self.v_box_5)
        self.v_box_6_wid.setLayout(self.v_box_6)
        self.v_box_7_wid.setLayout(self.v_box_7)
        self.v_box_8_wid.setLayout(self.v_box_8)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.v_box_1_wid, 1, 1)
        self.grid_layout.addWidget(self.v_box_2_wid, 1, 2)
        self.grid_layout.addWidget(self.v_box_3_wid, 1, 3)
        self.grid_layout.addWidget(self.v_box_4_wid, 1, 4)
        self.grid_layout.addWidget(self.v_box_5_wid, 2, 1)
        self.grid_layout.addWidget(self.v_box_6_wid, 2, 2)
        self.grid_layout.addWidget(self.v_box_7_wid, 2, 3)
        self.grid_layout.addWidget(self.v_box_8_wid, 2, 4)

        self.setLayout(self.grid_layout)


class RadioWindow(QWidget):
    switch_flag = 1
    before_close_signal_1 = pyqtSignal(int, bool, bool)
    cancel_flag = True
    signal_flag = False

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        if self.switch_flag == 1:
            self.rgb_switch_init()
        else:
            pass

    def rgb_switch_init(self):

        self.setWindowTitle('RGB分量')
        # 只有最小化按钮
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # 阻塞窗口
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(500, 200)

        self.r_radio_button = QRadioButton('R分量')
        self.r_radio_button.setChecked(True)
        self.g_radio_button = QRadioButton('G分量')
        self.b_radio_button = QRadioButton('B分量')

        h_box = QHBoxLayout()
        h_box.setSpacing(10)
        h_box.addWidget(self.r_radio_button)
        h_box.addWidget(self.g_radio_button)
        h_box.addWidget(self.b_radio_button)

        h_box_wid = QWidget()
        h_box_wid.setLayout(h_box)

        title_label = QLabel('分量选择')

        self.cancel_button = QPushButton('取消')
        self.cancel_button.clicked.connect(self.cancelEvent)
        self.ok_button = QPushButton('确定')
        self.ok_button.clicked.connect(self.closeEvent)

        grid_layout = QGridLayout()
        grid_layout.addWidget(title_label, 1, 1)
        grid_layout.addWidget(self.r_radio_button, 2, 1)
        grid_layout.addWidget(self.g_radio_button, 2, 2)
        grid_layout.addWidget(self.b_radio_button, 2, 3)
        grid_layout.addWidget(self.cancel_button, 3, 1)
        grid_layout.addWidget(self.ok_button, 3, 3)
        self.setLayout(grid_layout)

        self.setWindowIcon(QIcon('res/img/logo.png'))
        # self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.show()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def return_value(self):
        if self.r_radio_button.isChecked():
            return 1
        elif self.g_radio_button.isChecked():
            return 2
        elif self.b_radio_button.isChecked():
            return 3
        else:
            pass

    def cancelEvent(self):
        self.cancel_flag = False
        self.before_close_signal_1.emit(self.return_value(), self.signal_flag, self.cancel_flag)
        self.close()

    def closeEvent(self, event):
        if self.switch_flag == 1:
            radio_val = self.return_value()
            if self.signal_flag:
                self.signal_flag = False
            else:
                self.signal_flag = True
            self.before_close_signal_1.emit(radio_val, self.signal_flag, self.cancel_flag)
            self.close()
        else:
            pass


class OcrWordsWindow(QWidget):
    cancel_flag = True
    signal_flag = False
    before_close_signal_1 = pyqtSignal(str, bool, bool)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        path_button = QPushButton('选择文件')
        path_button.clicked.connect(self.get_path)
        self.path_text = QLineEdit()

        self.check_hbox = QHBoxLayout()
        self.check_hbox_wid = QWidget()
        self.cancel_button = QPushButton('取消')
        self.cancel_button.clicked.connect(self.cancelEvent)
        self.ok_button = QPushButton('确定')
        self.ok_button.clicked.connect(self.closeEvent)
        self.check_hbox.addWidget(self.cancel_button)
        self.check_hbox.addWidget(self.ok_button)
        self.check_hbox_wid.setLayout(self.check_hbox)

        grid_layout = QGridLayout()
        grid_layout.addWidget(path_button, 1, 1)
        grid_layout.addWidget(self.path_text, 1, 2)
        grid_layout.addWidget(self.check_hbox_wid, 2, 1, 1, 2)

        self.setLayout(grid_layout)
        self.setWindowTitle('OCR识别')
        self.setWindowIcon(QIcon('res/img/logo.png'))
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.show()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def get_path(self):
        file_name, tmp = QFileDialog.getOpenFileName(self, '打开图片', 'picture', '*.png *.jpg *.bmp')
        if file_name == '':
            return
        self.path_text.setText(file_name)

    def cancelEvent(self):
        path = self.path_text.text()
        self.cancel_flag = False
        self.before_close_signal_1.emit(path, self.signal_flag, self.cancel_flag)
        self.close()

    def closeEvent(self, event):
        path = self.path_text.text()
        if self.signal_flag:
            self.signal_flag = False
        else:
            self.signal_flag = True
        self.before_close_signal_1.emit(path, self.signal_flag, self.cancel_flag)
        self.close()


class SettingWindow(QWidget):
    threshold_max_1 = 100
    threshold_max_2 = 10
    threshold_max_3 = 100
    threshold_max_4 = 512
    signal_flag = False
    switch_flag = 1

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.set_text()
        self.set_model()

    def init_ui(self):

        with open('./settings.json', 'r', encoding='utf-8') as fr:
            json_data = json.load(fr)
            self.default_jpeg_quality = int(json_data["jpg_quality"])
            self.default_png_quality = int(json_data["png_quality"])
            self.default_webp_quality = int(json_data["webp_quality"])
            self.defalut_dct_block = int(json_data['DCT_Block'])
        fr.close()

        self.setWindowTitle('设置')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(500, 300)

        self.threshold_slider_1 = QSlider(Qt.Horizontal)
        self.threshold_slider_1.setMaximumHeight(20)
        self.threshold_slider_1.setMinimum(1)
        self.threshold_slider_1.setMaximum(self.threshold_max_1)
        self.threshold_slider_1.setSingleStep(1)
        self.threshold_slider_1.setValue(self.default_jpeg_quality)
        self.threshold_slider_1.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_1.setTickInterval(5)
        self.threshold_slider_1.valueChanged.connect(self.return_value)

        self.threshold_slider_2 = QSlider(Qt.Horizontal)
        self.threshold_slider_2.setMaximumHeight(20)
        self.threshold_slider_2.setMinimum(1)
        self.threshold_slider_2.setMaximum(self.threshold_max_2)
        self.threshold_slider_2.setSingleStep(1)
        self.threshold_slider_2.setValue(self.default_png_quality)
        self.threshold_slider_2.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_2.setTickInterval(5)
        self.threshold_slider_2.valueChanged.connect(self.return_value)

        self.threshold_slider_3 = QSlider(Qt.Horizontal)
        self.threshold_slider_3.setMaximumHeight(20)
        self.threshold_slider_3.setMinimum(0)
        self.threshold_slider_3.setMaximum(self.threshold_max_3)
        self.threshold_slider_3.setSingleStep(1)
        self.threshold_slider_3.setValue(self.default_webp_quality)
        self.threshold_slider_3.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_3.setTickInterval(5)
        self.threshold_slider_3.valueChanged.connect(self.return_value)

        self.threshold_slider_4 = QSlider(Qt.Horizontal)
        self.threshold_slider_4.setMaximumHeight(20)
        self.threshold_slider_4.setMinimum(1)
        self.threshold_slider_4.setMaximum(self.threshold_max_4)
        self.threshold_slider_4.setSingleStep(1)
        self.threshold_slider_4.setValue(self.defalut_dct_block)
        self.threshold_slider_4.setTickPosition(QSlider.NoTicks)
        self.threshold_slider_4.setTickInterval(5)
        self.threshold_slider_4.valueChanged.connect(self.return_value)

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
        grid_layout.addWidget(self.label_tip_1, 1, 1)
        grid_layout.addWidget(self.label_tip_1_value, 1, 2)
        grid_layout.addWidget(self.threshold_slider_1, 2, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_2, 3, 1)
        grid_layout.addWidget(self.label_tip_2_value, 3, 2)
        grid_layout.addWidget(self.threshold_slider_2, 4, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_3, 5, 1)
        grid_layout.addWidget(self.label_tip_3_value, 5, 2)
        grid_layout.addWidget(self.threshold_slider_3, 6, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_4, 7, 1)
        grid_layout.addWidget(self.label_tip_4_value, 7, 2)
        grid_layout.addWidget(self.threshold_slider_4, 8, 1, 1, 2)
        grid_layout.addWidget(self.label_tip_5, 9, 1)
        grid_layout.addWidget(self.baidu_app_id, 10, 1)
        grid_layout.addWidget(self.baidu_app_id_text, 10, 2)
        grid_layout.addWidget(self.baidu_api_key, 11, 1)
        grid_layout.addWidget(self.baidu_api_key_text, 11, 2)
        grid_layout.addWidget(self.baidu_secret_key, 12, 1)
        grid_layout.addWidget(self.baidu_secret_key_text, 12, 2)
        grid_layout.addWidget(self.baidu_ocr_words_label, 13, 1)
        grid_layout.addWidget(self.baidu_ocr_words_hbox_wid, 14, 1, 1, 2)
        grid_layout.addWidget(self.check_hbox_wid, 15, 1, 1, 2)

        self.setLayout(grid_layout)
        self.setWindowIcon(QIcon('res/img/logo.png'))
        self.show()
        self.center()

    def set_text(self):
        with open('./settings.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            self.baidu_app_id_text.setText(json_data['Baidu_Api']['APP_ID'])
            self.baidu_api_key_text.setText(json_data['Baidu_Api']['API_KEY'])
            self.baidu_secret_key_text.setText(json_data['Baidu_Api']['SECRET_KEY'])
        f.close()

    def set_model(self):
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

    def get_model(self):
        if self.baidu_ocr_words_general.isChecked():
            return 1
        elif self.baidu_ocr_words_heigh.isChecked():
            return 2
        elif self.baidu_ocr_words_rare.isChecked():
            return 3
        else:
            pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def return_value(self):
        self.label_tip_1_value.setText(str(self.threshold_slider_1.value()))
        self.label_tip_2_value.setText(str(self.threshold_slider_2.value()))
        self.label_tip_3_value.setText(str(self.threshold_slider_3.value()))
        self.label_tip_4_value.setText(str(self.threshold_slider_4.value()))
        return self.threshold_slider_1.value(), self.threshold_slider_2.value(), self.threshold_slider_3.value(), self.threshold_slider_4.value()

    def closeEvent(self, event):
        jpg, png, webp, dct_block = self.return_value()
        app_id = self.baidu_api_key_text.text()
        api_key = self.baidu_api_key_text.text()
        secret_key = self.baidu_secret_key_text.text()
        words_model = self.get_model()
        util.program_settings(jpg, png, webp, dct_block, app_id, api_key, secret_key, words_model)
        self.close()
