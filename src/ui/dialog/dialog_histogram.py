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
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QDesktopWidget


class HistogramDialog(QWidget):

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
        self.setWindowTitle("RGB分量直方图")
        self.setWindowIcon(QIcon('res/img/logo.png'))
        self.setMinimumSize(1280, 720)
        self.show()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
