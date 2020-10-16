from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QDesktopWidget


class PltDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.plt_label = QLabel("图片显示区")
        layout = QVBoxLayout()
        layout.addWidget(self.plt_label)
        self.setLayout(layout)

        self.plt_label.setScaledContents(True)
        self.setWindowIcon(QIcon('res/img/logo.png'))
        self.show()
        self.__center()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
