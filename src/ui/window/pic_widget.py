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
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class PicWidget(QWidget):

    def init_default_wid(self):
        v_box = QVBoxLayout()
        self.pic_label = QLabel('')
        self.pic_label.setMaximumHeight(20)
        self.pic_show_label = QLabel('图片显示区')
        self.pic_show_label.setStyleSheet('background-color:#fff')
        v_box.addWidget(self.pic_label)
        v_box.addSpacing(20)
        v_box.addWidget(self.pic_show_label)
        self.setLayout(v_box)
