from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QRadioButton, QHBoxLayout, QLabel, QPushButton, QGridLayout, QDesktopWidget


class ExtractRGB(QWidget):
    close_signal = pyqtSignal(int, bool)
    cancel_flag = True

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.rgb_switch_init()

    def rgb_switch_init(self):

        self.setWindowTitle('RGB分量')
        # 只有最小化按钮
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # 阻塞窗口
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(500, 200)

        self.r_radio_button = QRadioButton('R分量')
        self.r_radio_button.setChecked(True)
        self.g_radio_button = QRadioButton('G分量')
        self.b_radio_button = QRadioButton('B分量')

        h_box = QHBoxLayout()
        h_box.setSpacing(10)
        h_box.addWidget(self.r_radio_button)
        h_box.addWidget(self.g_radio_button)
        h_box.addWidget(self.b_radio_button)

        h_box_wid = QWidget()
        h_box_wid.setLayout(h_box)

        title_label = QLabel('分量选择')

        cancel_button = QPushButton('取消')
        cancel_button.setShortcut('Esc')
        cancel_button.clicked.connect(self.cancelEvent)
        ok_button = QPushButton('确定')
        ok_button.setShortcut(Qt.Key_Return)
        ok_button.clicked.connect(self.okEvent)

        grid_layout = QGridLayout()
        grid_layout.addWidget(title_label, 1, 1)
        grid_layout.addWidget(self.r_radio_button, 2, 1)
        grid_layout.addWidget(self.g_radio_button, 2, 2)
        grid_layout.addWidget(self.b_radio_button, 2, 3)
        grid_layout.addWidget(cancel_button, 3, 1)
        grid_layout.addWidget(ok_button, 3, 3)
        self.setLayout(grid_layout)

        self.setWindowIcon(QIcon('res/img/logo.png'))
        # self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.show()
        self.__center()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def return_value(self):
        if self.r_radio_button.isChecked():
            return 1
        elif self.g_radio_button.isChecked():
            return 2
        elif self.b_radio_button.isChecked():
            return 3
        else:
            pass

    def cancelEvent(self):
        self.cancel_flag = False
        self.close_signal.emit(self.return_value(), self.cancel_flag)
        self.close()

    def okEvent(self, event):
        self.close_signal.emit(self.return_value(), self.cancel_flag)
        self.close()
