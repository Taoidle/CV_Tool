import sys
from util.basic import CvBasic as cvb
from ui.init_ui import InitUI
from ui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QFileDialog


class CVT(MainWindow, InitUI):

    def __init__(self):
        super().__init__()
        # 初始化UI界面
        self.__init_ui()
        # 信号链接
        self.__signal_connect()
        # 显示界面
        self.show()
        self.resize(1200, 900)
        # 居中显示
        self.__center()

    def __init_ui(self):
        # 初始化默认工具栏
        self.init_default_statusbar()
        # 初始化主窗口
        self.init_default_window_widget()
        # 初始化默认程序设置
        self.init_default_setting()
        # 初始化默认窗口设置
        self.init_default_window_setting()

    def __signal_connect(self):
        # 链接打开图片
        self.open_pic.triggered.connect(self.init_default_open_pic)
        # 链接保存图片
        self.save_pic.triggered.connect(self.init_default_save_pic)
        # 链接设置窗口
        self.program_setting.triggered.connect(self.init_default_setting_window)

    # 窗口居中
    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 打开图片
    def init_default_open_pic(self):
        file_name, tmp = QFileDialog.getOpenFileName(self, '打开图片', 'picture', '*.png *.jpg *.bmp *.jpeg *tif')
        if file_name == '':
            return
        self.img = cvb.get_pic(file_name)
        width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
        self.resize(width, height)

    # 保存图片
    def init_default_save_pic(self):
        default_filename = cvb.create_default_filename('pic_', '.png')
        file_name, tmp = QFileDialog.getSaveFileName(self, '保存图片', default_filename, '*.png *.jpg *.bmp *.webp')
        if file_name == '':
            return
        # cvb.save_pic(file_name, img)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CVT()
    sys.exit(app.exec())
