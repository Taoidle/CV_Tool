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
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QPushButton, QGridLayout, QDesktopWidget, QVBoxLayout, \
    QRadioButton, QHBoxLayout


class MorphologyDialog(QWidget):
    threshold_max = 21
    close_signal = pyqtSignal(int, int, bool)
    cancel_flag = True

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
        self.threshold_slider.setValue(3)
        # 刻度位置，刻度下方
        self.threshold_slider.setTickPosition(QSlider.NoTicks)
        # 设置刻度间距
        self.threshold_slider.setTickInterval(5)
        # 设置连接信号槽函数
        self.threshold_slider.valueChanged.connect(self.return_value)
        # 设置标题
        label_tip = QLabel('阈值')
        label_tip.setMaximumHeight(20)

        self.label_tip_value = QLabel(str(self.threshold_slider.value()))
        self.label_tip_value.setMaximumHeight(20)

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

        cancel_button = QPushButton('取消')
        cancel_button.clicked.connect(self.cancelEvent)
        ok_button = QPushButton('确定')
        ok_button.clicked.connect(self.closeEvent)

        grid_layout = QGridLayout()
        grid_layout.addWidget(v_box_wid, 1, 1, 1, 2)
        grid_layout.addWidget(label_tip, 2, 1)
        grid_layout.addWidget(self.label_tip_value, 2, 2)
        grid_layout.addWidget(self.threshold_slider, 3, 1, 1, 2)
        grid_layout.addWidget(cancel_button, 4, 1)
        grid_layout.addWidget(ok_button, 4, 2)
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

    def morphology_check(self):
        if self.h_box_button_1.isChecked():
            return 1
        elif self.h_box_button_2.isChecked():
            return 2
        elif self.h_box_button_3.isChecked():
            return 3
        else:
            pass

    def return_value(self):
        self.label_tip_value.setText(str(self.threshold_slider.value()))
        return self.threshold_slider.value()

    def cancelEvent(self):
        self.cancel_flag = False
        threshold = self.return_value()
        morphology_val = self.morphology_check()
        self.close_signal.emit(threshold, morphology_val, self.cancel_flag)
        self.close()

    def closeEvent(self, event):
        threshold = self.return_value()
        morphology_val = self.morphology_check()
        self.close_signal.emit(threshold, morphology_val, self.cancel_flag)
        self.close()
