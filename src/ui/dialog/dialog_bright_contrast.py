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


class BrightContrastDialog(QWidget):
    threshold_max_1, threshold_max_2 = 3000, 100
    # 信号
    close_signal = pyqtSignal(int, int, bool)
    cancel_flag = True

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

        label_tip_1 = QLabel('对比度')
        label_tip_1.setMaximumHeight(20)
        self.label_tip_1_value = QLabel(str(self.threshold_slider_1.value() / 1000))
        self.label_tip_1_value.setMaximumHeight(20)

        label_tip_2 = QLabel('亮度')
        label_tip_2.setMaximumHeight(20)
        self.label_tip_2_value = QLabel(str(self.threshold_slider_2.value()))
        self.label_tip_2_value.setMaximumHeight(20)

        cancel_button = QPushButton('取消')
        cancel_button.setShortcut('Esc')
        cancel_button.clicked.connect(self.cancelEvent)
        ok_button = QPushButton('确定')
        ok_button.setShortcut(Qt.Key_Return)
        ok_button.clicked.connect(self.okEvent)

        grid_layout = QGridLayout()
        grid_layout.addWidget(label_tip_1, 1, 1)
        grid_layout.addWidget(self.label_tip_1_value, 1, 2)
        grid_layout.addWidget(self.threshold_slider_1, 2, 1, 1, 2)
        grid_layout.addWidget(label_tip_2, 3, 1)
        grid_layout.addWidget(self.label_tip_2_value, 3, 2)
        grid_layout.addWidget(self.threshold_slider_2, 4, 1, 1, 2)
        grid_layout.addWidget(cancel_button, 5, 1)
        grid_layout.addWidget(ok_button, 5, 2)
        self.setLayout(grid_layout)
        self.setWindowIcon(QIcon('res/img/logo.png'))
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
        self.label_tip_1_value.setText(str(self.threshold_slider_1.value() / 1000))
        self.label_tip_2_value.setText(str(self.threshold_slider_2.value()))
        return self.threshold_slider_1.value() / 1000, self.threshold_slider_2.value()

    def cancelEvent(self):
        self.cancel_flag = False
        contrast_value, brightness_value = self.return_value()
        self.close_signal.emit(contrast_value, brightness_value, self.cancel_flag)
        self.close()

    def okEvent(self, event):
        contrast_value, brightness_value = self.return_value()
        self.close_signal.emit(contrast_value, brightness_value, self.cancel_flag)
        self.close()