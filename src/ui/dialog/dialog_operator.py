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
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QPushButton, QGridLayout, QDesktopWidget


class CannySobelDialog(QWidget):
    threshold_max = 120
    # 信号
    close_signal = pyqtSignal(int, bool)
    cancel_flag = True

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('内核')
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
        self.threshold_slider.setValue(1)
        # 刻度位置，刻度下方
        self.threshold_slider.setTickPosition(QSlider.NoTicks)
        # 设置刻度间距
        self.threshold_slider.setTickInterval(5)
        # 设置连接信号槽函数
        self.threshold_slider.valueChanged.connect(self.return_value)
        # 设置标题
        label_tip = QLabel('内核大小:')
        label_tip.setMaximumHeight(20)

        self.label_tip_value = QLabel(str(self.threshold_slider.value()))
        self.label_tip_value.setMaximumHeight(20)

        cancel_button = QPushButton('取消')
        cancel_button.setShortcut('Esc')
        cancel_button.clicked.connect(self.cancelEvent)
        ok_button = QPushButton('确定')
        ok_button.setShortcut(Qt.Key_Return)
        ok_button.clicked.connect(self.okEvent)

        grid_layout = QGridLayout()
        grid_layout.addWidget(label_tip, 1, 1)
        grid_layout.addWidget(self.label_tip_value, 1, 2)
        grid_layout.addWidget(self.threshold_slider, 2, 1, 1, 2)
        grid_layout.addWidget(cancel_button, 3, 1)
        grid_layout.addWidget(ok_button, 3, 2)
        self.setLayout(grid_layout)

        self.setWindowIcon(QIcon('res/img/logo.png'))
        # self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.show()
        self.__center()

    def __center(self):
        qr = self.frameGeometry()
        # 获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center()
        # 获取显示器的分辨率，然后得到屏幕中间点的位置
        qr.moveCenter(cp)
        # 然后把主窗口框架的中心点放置到屏幕的中心位置
        self.move(qr.topLeft())

    def return_value(self):
        self.label_tip_value.setText(str(self.threshold_slider.value()))
        return self.threshold_slider.value()

    def cancelEvent(self):
        self.cancel_flag = False
        threshold = self.return_value()
        self.close_signal.emit(threshold, self.cancel_flag)
        self.close()

    def okEvent(self, event):
        threshold = self.return_value()
        self.close_signal.emit(threshold, self.cancel_flag)
        self.close()


class LaplacianDialog(QWidget):
    threshold_max = 3
    close_signal = pyqtSignal(int, bool)
    cancel_flag = True

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('内核')
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
        self.threshold_slider.setValue(0)
        # 刻度位置，刻度下方
        self.threshold_slider.setTickPosition(QSlider.NoTicks)
        # 设置刻度间距
        self.threshold_slider.setTickInterval(5)
        # 设置连接信号槽函数
        self.threshold_slider.valueChanged.connect(self.return_value)
        # 设置标题
        label_tip = QLabel('内核大小:')
        label_tip.setMaximumHeight(20)

        self.label_tip_value = QLabel(str(self.threshold_slider.value()))
        self.label_tip_value.setMaximumHeight(20)

        cancel_button = QPushButton('取消')
        cancel_button.setShortcut('Esc')
        cancel_button.clicked.connect(self.cancelEvent)
        ok_button = QPushButton('确定')
        ok_button.setShortcut(Qt.Key_Return)
        ok_button.clicked.connect(self.okEvent)

        grid_layout = QGridLayout()
        grid_layout.addWidget(label_tip, 1, 1)
        grid_layout.addWidget(self.label_tip_value, 1, 2)
        grid_layout.addWidget(self.threshold_slider, 2, 1, 1, 2)
        grid_layout.addWidget(cancel_button, 3, 1)
        grid_layout.addWidget(ok_button, 3, 2)
        self.setLayout(grid_layout)

        self.setWindowIcon(QIcon('res/img/logo.png'))
        # self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.show()
        self.__center()

    def __center(self):
        qr = self.frameGeometry()
        # 获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center()
        # 获取显示器的分辨率，然后得到屏幕中间点的位置
        qr.moveCenter(cp)
        # 然后把主窗口框架的中心点放置到屏幕的中心位置
        self.move(qr.topLeft())

    def return_value(self):
        self.label_tip_value.setText(str(self.threshold_slider.value()))
        return self.threshold_slider.value()

    def cancelEvent(self):
        self.cancel_flag = False
        threshold = self.return_value()
        self.close_signal.emit(threshold, self.cancel_flag)
        self.close()

    def okEvent(self, event):
        threshold = self.return_value()
        self.close_signal.emit(threshold, self.cancel_flag)
        self.close()