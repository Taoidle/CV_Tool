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
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget, QSlider, QLabel, QGridLayout, QPushButton, QWidget


class HoughLinesDialog(QWidget):
    threshold_max_1 = 3000
    threshold_max_2 = 360
    threshold_max_3 = 1000
    # 信号
    close_signal = pyqtSignal(int, int, int, bool)
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

        label_tip_1 = QLabel('r')
        label_tip_1.setMaximumHeight(20)
        self.label_tip_1_value = QLabel(str(self.threshold_slider_1.value() / 100))
        self.label_tip_1_value.setMaximumHeight(20)
        label_tip_2 = QLabel('角度θ')
        label_tip_2.setMaximumHeight(20)
        self.label_tip_2_value = QLabel(str(180 / self.threshold_slider_2.value()))
        self.label_tip_2_value.setMaximumHeight(20)
        label_tip_3 = QLabel('累加数')
        label_tip_3.setMaximumHeight(20)
        self.label_tip_3_value = QLabel(str(self.threshold_slider_3.value()))
        self.label_tip_3_value.setMaximumHeight(20)

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
        grid_layout.addWidget(label_tip_3, 5, 1)
        grid_layout.addWidget(self.label_tip_3_value, 5, 2)
        grid_layout.addWidget(self.threshold_slider_3, 6, 1, 1, 2)
        grid_layout.addWidget(cancel_button, 7, 1)
        grid_layout.addWidget(ok_button, 7, 2)
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
        self.label_tip_1_value.setText(str(self.threshold_slider_1.value() / 100))
        self.label_tip_2_value.setText(str(180 / self.threshold_slider_2.value()))
        self.label_tip_3_value.setText(str(self.threshold_slider_3.value()))
        return self.threshold_slider_1.value() / 100, self.threshold_slider_2.value(), self.threshold_slider_3.value()

    def cancelEvent(self):
        self.cancel_flag = False
        rho, theta, threshold = self.return_value()
        self.close_signal.emit(rho, theta, threshold, self.cancel_flag)
        self.close()

    def okEvent(self):
        rho, theta, threshold = self.return_value()
        self.close_signal.emit(rho, theta, threshold, self.cancel_flag)
        self.close()


class HoughCirclesWindow(QWidget):
    close_signal = pyqtSignal(int, int, int, int, int, int, bool)
    threshold_max_1, threshold_max_2, threshold_max_3, threshold_max_4, threshold_max_5, threshold_max_6 = 10, 0, 0, 0, 0, 0
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

        label_tip_1 = QLabel('累加器:')
        label_tip_1.setMaximumHeight(20)
        self.label_tip_1_value = QLabel(str(self.threshold_slider_1.value()))
        self.label_tip_1_value.setMaximumHeight(20)
        label_tip_2 = QLabel('圆心最小距离:')
        label_tip_2.setMaximumHeight(20)
        self.label_tip_2_value = QLabel(str(self.threshold_slider_2.value()))
        self.label_tip_2_value.setMaximumHeight(20)
        label_tip_3 = QLabel('阈值：')
        label_tip_3.setMaximumHeight(20)
        self.label_tip_3_value = QLabel(str(self.threshold_slider_3.value()))
        self.label_tip_3_value.setMaximumHeight(20)
        label_tip_4 = QLabel('累加器阈值：')
        label_tip_4.setMaximumHeight(20)
        self.label_tip_4_value = QLabel(str(self.threshold_slider_4.value()))
        self.label_tip_4_value.setMaximumHeight(20)
        label_tip_5 = QLabel('圆半径最小值：')
        label_tip_5.setMaximumHeight(20)
        self.label_tip_5_value = QLabel(str(self.threshold_slider_5.value()))
        self.label_tip_5_value.setMaximumHeight(20)
        label_tip_6 = QLabel('圆半径最大值：')
        label_tip_6.setMaximumHeight(20)
        self.label_tip_6_value = QLabel(str(self.threshold_slider_6.value()))
        self.label_tip_6_value.setMaximumHeight(20)

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
        grid_layout.addWidget(label_tip_3, 5, 1)
        grid_layout.addWidget(self.label_tip_3_value, 5, 2)
        grid_layout.addWidget(self.threshold_slider_3, 6, 1, 1, 2)
        grid_layout.addWidget(label_tip_4, 7, 1)
        grid_layout.addWidget(self.label_tip_4_value, 7, 2)
        grid_layout.addWidget(self.threshold_slider_4, 8, 1, 1, 2)
        grid_layout.addWidget(label_tip_5, 9, 1)
        grid_layout.addWidget(self.label_tip_5_value, 9, 2)
        grid_layout.addWidget(self.threshold_slider_5, 10, 1, 1, 2)
        grid_layout.addWidget(label_tip_6, 11, 1)
        grid_layout.addWidget(self.label_tip_6_value, 11, 2)
        grid_layout.addWidget(self.threshold_slider_6, 12, 1, 1, 2)
        grid_layout.addWidget(cancel_button, 13, 1)
        grid_layout.addWidget(ok_button, 13, 2)
        self.setLayout(grid_layout)
        self.show()
        self.__center()

    def __center(self):
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
        dp, minDist, param1, parma2, minRadius, maxRadius = self.return_value()
        self.close_signal.emit(dp, minDist, param1, parma2, minRadius, maxRadius, self.cancel_flag)
        self.close()

    def okEvent(self):
        dp, minDist, param1, parma2, minRadius, maxRadius = self.return_value()
        self.close_signal.emit(dp, minDist, param1, parma2, minRadius, maxRadius, self.cancel_flag)
        self.close()
