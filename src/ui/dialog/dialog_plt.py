from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QDesktopWidget, QMenu, QAction


class PltDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.createContextMenu()
        self.init_ui()

    def init_ui(self):
        self.plt_label = QLabel("图片显示区")
        self.plt_label.setScaledContents(True)

        layout = QVBoxLayout()
        layout.addWidget(self.plt_label)

        self.setLayout(layout)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.setWindowIcon(QIcon('res/img/logo.png'))
        self.setMinimumSize(600, 400)
        self.show()
        self.__center()

    # 创建右键菜单
    def createContextMenu(self):
        # 将 ContextMenuPolicy设置为 Qt.CustomContextMenu使用 customContextMenuRequested信号
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.contextMenu = QMenu(self)
        self.save_plt = QAction('保存图片', self)
        # self.save_plt = self.contextMenu.addAction("保存图片")
        self.contextMenu.addAction(self.save_plt)

    # 调用时显示菜单
    def showContextMenu(self):
        self.contextMenu.move(QCursor().pos())
        self.contextMenu.show()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
