import sys
from util.basic import CvBasic as cvb
from ui.init_ui import InitUI
from ui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication, QDesktopWidget


class CVT(MainWindow, InitUI):

    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__signal_connect()
        self.show()
        self.__center()

    def __init_ui(self):
        # 初始化默认工具栏
        self.init_default_statusbar()
        # 初始化默认程序设置
        self.init_default_setting()
        # 初始化默认窗口设置
        self.init_default_window_setting()

    def __signal_connect(self):
        self.program_setting.triggered.connect(self.init_setting_window)

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CVT()
    sys.exit(app.exec())
