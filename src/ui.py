"""
This example is about opencv with pyqt5

Aauthor: kaiyang
Website: www.lkyblog.cn git.lkyblog.cn
Last edited: April 2020

"""

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QDialogButtonBox, QGridLayout, QPushButton, QDesktopWidget, \
    QCheckBox, QToolBox, QGroupBox, QVBoxLayout, QToolButton, QMainWindow, QMessageBox, QListWidget, QListView, \
    QListWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal, QSize, QStringListModel


class ToolsWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.tool_box = QToolBox()
        # self.tool_box.setStyleSheet('background-color:#fff')

        self.group_box_1 = QGroupBox()
        self.group_box_1.setMinimumWidth(150)
        self.group_box_1.setMaximumWidth(200)
        self.v_box_1 = QVBoxLayout()

        self.group_box_2 = QGroupBox()
        self.group_box_2.setMinimumWidth(150)
        self.group_box_2.setMaximumWidth(200)
        self.v_box_2 = QVBoxLayout()

        self.group_box_3 = QGroupBox()
        self.group_box_3.setMinimumWidth(150)
        self.group_box_3.setMaximumWidth(200)
        self.v_box_3 = QVBoxLayout()

        self.group_box_4 = QGroupBox()
        self.group_box_4.setMinimumWidth(150)
        self.group_box_4.setMaximumWidth(200)
        self.v_box_4 = QVBoxLayout()

        self.group_box_5 = QGroupBox()
        self.group_box_5.setMinimumWidth(150)
        self.group_box_5.setMaximumWidth(200)
        self.v_box_5 = QVBoxLayout()

        self.group_box_6 = QGroupBox()
        self.group_box_6.setMinimumWidth(150)
        self.group_box_6.setMaximumWidth(200)
        self.v_box_6 = QVBoxLayout()

        self.box_1_button_1 = QToolButton()
        self.box_1_button_1.setText('恢复原图')
        self.box_1_button_1.setAutoRaise(True)
        self.box_1_button_2 = QToolButton()
        self.box_1_button_2.setText('灰度化')
        self.box_1_button_2.setAutoRaise(True)
        self.box_1_button_3 = QToolButton()
        self.box_1_button_3.setText('二值化')
        self.box_1_button_3.setAutoRaise(True)
        self.box_1_button_4 = QToolButton()
        self.box_1_button_4.setText('自动二值化')
        self.box_1_button_4.setAutoRaise(True)

        self.box_2_button_1 = QToolButton()
        self.box_2_button_1.setText('水平镜像')
        self.box_2_button_1.setAutoRaise(True)
        self.box_2_button_2 = QToolButton()
        self.box_2_button_2.setText('垂直镜像')
        self.box_2_button_2.setAutoRaise(True)
        self.box_2_button_3 = QToolButton()
        self.box_2_button_3.setText('顺时针 90°')
        self.box_2_button_3.setAutoRaise(True)
        self.box_2_button_4 = QToolButton()
        self.box_2_button_4.setText('逆时针 90°')
        self.box_2_button_4.setAutoRaise(True)

        self.box_3_button_1 = QToolButton()
        self.box_3_button_1.setText('均值滤波')
        self.box_3_button_1.setAutoRaise(True)
        self.box_3_button_2 = QToolButton()
        self.box_3_button_2.setText('中值滤波')
        self.box_3_button_2.setAutoRaise(True)
        self.box_3_button_3 = QToolButton()
        self.box_3_button_3.setText('方框滤波')
        self.box_3_button_3.setAutoRaise(True)
        self.box_3_button_4 = QToolButton()
        self.box_3_button_4.setText('高斯滤波')
        self.box_3_button_4.setAutoRaise(True)
        self.box_3_button_5 = QToolButton()
        self.box_3_button_5.setText('双边滤波')
        self.box_3_button_5.setAutoRaise(True)

        self.v_box_1.addWidget(self.box_1_button_1)
        self.v_box_1.addWidget(self.box_1_button_2)
        self.v_box_1.addWidget(self.box_1_button_3)
        self.v_box_1.addWidget(self.box_1_button_4)
        self.v_box_1.addStretch(0)
        self.group_box_1.setLayout(self.v_box_1)

        self.v_box_2.addWidget(self.box_2_button_1)
        self.v_box_2.addWidget(self.box_2_button_2)
        self.v_box_2.addWidget(self.box_2_button_3)
        self.v_box_2.addWidget(self.box_2_button_4)
        self.v_box_2.addStretch(0)
        self.group_box_2.setLayout(self.v_box_2)

        self.v_box_3.addWidget(self.box_3_button_1)
        self.v_box_3.addWidget(self.box_3_button_2)
        self.v_box_3.addWidget(self.box_3_button_3)
        self.v_box_3.addWidget(self.box_3_button_4)
        self.v_box_3.addWidget(self.box_3_button_5)
        self.v_box_3.addStretch(0)
        self.group_box_2.setLayout(self.v_box_3)

        self.tool_box.addItem(self.group_box_1, "图像基本处理")
        self.tool_box.addItem(self.group_box_2, "图像位置变换")
        self.tool_box.addItem(self.group_box_3, "图像滤波处理")
        self.tool_box.addItem(self.group_box_4, "图像边缘检测")
        self.tool_box.addItem(self.group_box_5, "图像信息嵌入")
        self.tool_box.addItem(self.group_box_6, "图像信息提取")

        # self.tool_box.setCurrentIndex(0)
        vbox = QVBoxLayout()
        vbox.addWidget(self.tool_box)
        self.setLayout(vbox)
        self.show()


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
