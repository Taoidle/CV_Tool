from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QDialogButtonBox, QGridLayout, QPushButton, QDesktopWidget, \
    QCheckBox
from PyQt5.QtCore import Qt, pyqtSignal


class SliderDialog(QWidget):
    threshold_max = 255
    # 信号
    before_close_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Threshold Setting')
        # 只有最小化按钮
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # 阻塞窗口
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(400, 200)

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
        self.threshold_slider.setTickPosition(QSlider.TicksBelow)
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
        self.center()
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
        self.label_tip_value.setText(str(self.threshold_slider.value()))
        return self.threshold_slider.value()

    def closeEvent(self, event):
        content = self.return_value()
        self.before_close_signal.emit(content)
        self.close()


class PositionDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('位置变换')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.label_pic_position = QLabel('图片位置')
        self.label_pic_position.setMaximumHeight(20)
        self.label_vid_position = QLabel('视频位置')
        self.label_vid_position.setMaximumHeight(20)

        self.img_horizontal_button = QPushButton('水平镜像')
        self.img_horizontal_button.clicked.connect(self.img_to_horizontal)
        self.img_vertical_button = QPushButton('垂直镜像')
        self.img_vertical_button.clicked.connect(self.img_to_vertical)
        self.img_rotate_left = QPushButton('顺时针 90°')
        self.img_rotate_left.clicked.connect(self.img_to_rotate_right)
        self.img_rotate_right = QPushButton('逆时针 90°')
        self.img_rotate_right.clicked.connect(self.img_to_rotate_left)

        self.vid_horizontal_button = QCheckBox('水平镜像 ')
        self.vid_horizontal_button.clicked.connect(self.vid_to_horizontal)
        self.vid_vertical_button = QCheckBox('垂直镜像')
        self.vid_vertical_button.clicked.connect(self.vid_to_vertical)
        self.vid_horizontal_vertical_button = QCheckBox('水平垂直镜像')
        self.vid_horizontal_vertical_button.clicked.connect(self.vid_to_horizontal_vertical)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)
        grid_layout.addWidget(self.label_pic_position, 1, 1)
        grid_layout.addWidget(self.img_rotate_left, 2, 1)
        grid_layout.addWidget(self.img_rotate_right, 2, 2)
        grid_layout.addWidget(self.img_horizontal_button, 2, 3)
        grid_layout.addWidget(self.img_horizontal_button, 2, 4)
        grid_layout.addWidget(self.label_vid_position, 3, 1)
        grid_layout.addWidget(self.vid_horizontal_button, 4, 1)
        grid_layout.addWidget(self.vid_vertical_button, 4, 2)
        grid_layout.addWidget(self.vid_horizontal_vertical_button, 4, 3)

        self.setLayout(grid_layout)


    def center(self):
        qr = self.frameGeometry()
        # 获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center()
        # 获取显示器的分辨率，然后得到屏幕中间点的位置
        qr.moveCenter(cp)
        # 然后把主窗口框架的中心点放置到屏幕的中心位置
        self.move(qr.topLeft())
