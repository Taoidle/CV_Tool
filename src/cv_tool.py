import sys
from util.basic import CvBasic as cvb
from util.pixel_basic import CvPixelBasic as cpb
from ui.init_ui import InitUI
from ui.main_window import MainWindow
from ui.slider_dialog import SliderDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QFileDialog, QMessageBox


class CVT(MainWindow, InitUI):
    img = None

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
        # 链接图像灰度化
        self.tool_box.box_1_button_3.clicked.connect(self.init_img2gray)
        # 链接图像反相
        self.tool_box.box_1_button_4.clicked.connect(self.init_img2inverse)
        # 链接图像二值化
        self.tool_box.box_1_button_5.clicked.connect(self.init_img2bin)
        # 链接图像自适应阈值二值化
        self.tool_box.box_1_button_6.clicked.connect(self.init_img2bin_auto)

    # 窗口居中
    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 打开图片
    def init_default_open_pic(self):
        # 调用存储文件
        file_name, tmp = QFileDialog.getOpenFileName(self, '打开图片', 'picture', '*.png *.jpg *.bmp *.jpeg *tif')
        if file_name == '':
            return
        # 获取图片
        self.img = cvb.get_pic(file_name)
        # 在窗口中显示
        width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
        # 重置窗口大小
        self.resize(width, height)

    # 保存图片
    def init_default_save_pic(self):
        # 检查图片
        if self.check_img():
            # 创建默认文件名
            default_filename = cvb.create_default_filename('pic_', '.png')
            # 调用存储文件
            file_name, tmp = QFileDialog.getSaveFileName(self, '保存图片', default_filename, '*.png *.jpg *.bmp *.webp')
            if file_name == '':
                return
            # 保存图片
            cvb.save_pic(file_name, self.img)

    # 图像灰度化
    def init_img2gray(self):
        # 检查图片
        if self.check_img():
            # 灰度化
            self.img = cpb.img_to_gray(self.img)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像反相
    def init_img2inverse(self):
        # 检查图片
        if self.check_img():
            # 图片反相
            self.img = cpb.img_to_inverse(self.img)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像二值化
    def init_img2bin(self):
        # 检查图片
        if self.check_img():
            # 调用对话窗口
            self.dialog = SliderDialog()
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img2bin_signal)

    # 图片二值化信号函数
    @pyqtSlot(int, bool)
    def init_img2bin_signal(self, threshold, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 图片二值化
            self.img = cpb.img_to_bin(self.img, threshold)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 自适应阈值二值化
    def init_img2bin_auto(self):
        # 检查图片
        if self.check_img():
            # 自适应阈值二值化
            self.img = cpb.img_to_auto_bin(self.img)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像检查
    def check_img(self):
        # 判断图片是否为空
        if self.img is not None:
            return True
        else:
            # 空图像调用警示窗口
            QMessageBox.warning(self, '警告', "当前没有打开\n任何图像！", QMessageBox.Ok)
            return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CVT()
    sys.exit(app.exec())
