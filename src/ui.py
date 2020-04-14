
"""
This example is about opencv with pyqt5

Aauthor: kaiyang
Website: www.lkyblog.cn git.lkyblog.cn
Last edited: April 2020

"""

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QDialogButtonBox, QGridLayout, QPushButton, QDesktopWidget, \
    QCheckBox, QToolBox, QGroupBox, QVBoxLayout, QToolButton, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QSize


class ToolsWindow(QToolBox):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.pic_basic_box = QGroupBox("图像基础处理", self)
        self.pic_position_box = QGroupBox("图像位置变换", self)
        self.pic_filter_box = QGroupBox("图像滤波处理", self)

        self.pic_basic_box_layout = QVBoxLayout()
        self.pic_position_box_layout = QVBoxLayout()
        self.pic_filter_box_layout = QVBoxLayout()

        pic_origin_button = QToolButton(self)
        toolButton_2 = QToolButton(self)
        toolButton_3 = QToolButton(self)
        toolButton_4 = QToolButton(self)
        toolButton_5 = QToolButton(self)
        toolButton_6 = QToolButton(self)
        toolButton_7 = QToolButton(self)
        toolButton_8 = QToolButton(self)
        toolButton_9 = QToolButton(self)

        # pic_origin_button.setIconSize(QSize(80, 80))
        pic_origin_button.setFont(QFont("微软雅黑", 16, QFont.Bold))
        pic_origin_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        pic_origin_button.setAutoRaise(True)
        pic_origin_button.setText('恢复原图')

        toolButton_2.setIconSize(QSize(80, 80))
        toolButton_2.setFont(QFont("微软雅黑", 16, QFont.Bold))
        toolButton_2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolButton_2.setAutoRaise(True)
        toolButton_2.setText('Button_1')

        toolButton_3.setIconSize(QSize(80, 80))
        toolButton_3.setFont(QFont("微软雅黑", 16, QFont.Bold))
        toolButton_3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolButton_3.setAutoRaise(True)
        toolButton_3.setText('Button_1')

        toolButton_4.setIconSize(QSize(80, 80))
        toolButton_4.setFont(QFont("微软雅黑", 16, QFont.Bold))
        toolButton_4.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolButton_4.setAutoRaise(True)
        toolButton_4.setText('Button_1')

        toolButton_5.setIconSize(QSize(80, 80))
        toolButton_5.setFont(QFont("微软雅黑", 16, QFont.Bold))
        toolButton_5.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolButton_5.setAutoRaise(True)
        toolButton_5.setText('Button_1')

        toolButton_6.setIconSize(QSize(80, 80))
        toolButton_6.setFont(QFont("微软雅黑", 16, QFont.Bold))
        toolButton_6.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolButton_6.setAutoRaise(True)
        toolButton_6.setText('Button_1')

        toolButton_7.setIconSize(QSize(80, 80))
        toolButton_7.setFont(QFont("微软雅黑", 16, QFont.Bold))
        toolButton_7.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolButton_7.setAutoRaise(True)
        toolButton_7.setText('Button_1')

        toolButton_8.setIconSize(QSize(80, 80))
        toolButton_8.setFont(QFont("微软雅黑", 16, QFont.Bold))
        toolButton_8.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolButton_8.setAutoRaise(True)
        toolButton_8.setText('Button_1')

        toolButton_9.setIconSize(QSize(80, 80))
        toolButton_9.setFont(QFont("微软雅黑", 16, QFont.Bold))
        toolButton_9.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolButton_9.setAutoRaise(True)
        toolButton_9.setText('Button_1')

        self.pic_basic_box_layout.addWidget(pic_origin_button)
        self.pic_basic_box_layout.addWidget(toolButton_2)
        self.pic_basic_box_layout.addWidget(toolButton_3)
        self.pic_position_box_layout.addWidget(toolButton_4)
        self.pic_position_box_layout.addWidget(toolButton_5)
        self.pic_position_box_layout.addWidget(toolButton_6)
        self.pic_filter_box_layout.addWidget(toolButton_7)
        self.pic_filter_box_layout.addWidget(toolButton_8)
        self.pic_filter_box_layout.addWidget(toolButton_9)
        self.pic_basic_box_layout.setAlignment(Qt.AlignCenter)
        self.pic_position_box_layout.setAlignment(Qt.AlignCenter)
        self.pic_filter_box_layout.setAlignment(Qt.AlignCenter)

        self.pic_basic_box.setLayout(self.pic_basic_box_layout)
        self.pic_position_box.setLayout(self.pic_position_box_layout)
        self.pic_filter_box.setLayout(self.pic_filter_box_layout)

        self.addItem(self.pic_basic_box, "搜索引擎！")
        self.addItem(self.pic_position_box, "视频网站！")
        self.addItem(self.pic_filter_box, "购物网站！")


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

    def closeEvent(self, event):
        # 我们创建了一个消息框，上面有俩按钮：Yes和No.
        # 第一个字符串显示在消息框的标题栏，第二个字符串显示在对话框，第三个参数是消息框的俩按钮，最后一个参数是默认按钮，这个按钮是默认选中的。返回值在变量reply里。
        reply = QMessageBox.question(self, 'Message', "Are you sure to exit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def return_value(self):
        self.label_tip_value.setText(str(self.threshold_slider.value()))
        return self.threshold_slider.value()





