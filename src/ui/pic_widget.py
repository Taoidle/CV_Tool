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
