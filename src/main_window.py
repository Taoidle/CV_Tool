"""
This example is about opencv with pyqt5

Aauthor: kaiyang
Website: www.lkyblog.cn git.lkyblog.cn
Last edited: April 2020

"""

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QCheckBox, QLineEdit, QHBoxLayout,
                             QAction, QFileDialog, QApplication, QDesktopWidget, QMenu, QMessageBox, QInputDialog,
                             QPushButton, QGridLayout)
from PyQt5.QtGui import QIcon, QImage, QPixmap

import cv2, util, sys, webbrowser, ui, time


class MainWindow(QMainWindow, QWidget):
    last_pic = None
    g_pic = None

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar()

        self.tools_window = ui.ToolsWindow()
        self.tools_window.setFixedWidth(220)
        self.tools_window.box_1_button_1.clicked.connect(self.review_origin_pic)
        self.tools_window.box_1_button_2.clicked.connect(self.img_to_gray)

        self.tools_window.box_1_button_4.clicked.connect(self.img_to_auto_bin)
        self.tools_window.box_2_button_1.clicked.connect(self.img_to_horizontal)
        self.tools_window.box_2_button_2.clicked.connect(self.img_to_vertical)
        self.tools_window.box_2_button_3.clicked.connect(self.img_to_rotate_left)
        self.tools_window.box_2_button_4.clicked.connect(self.img_to_rotate_right)
        self.tools_window.box_3_button_1.clicked.connect(self.img_impulse_noise)
        self.tools_window.box_3_button_2.clicked.connect(self.img_gaussian_noise)
        self.tools_window.box_4_button_1.clicked.connect(self.img_blur_filter)
        self.tools_window.box_4_button_2.clicked.connect(self.img_median_filter)

        self.tools_window.box_4_button_4.clicked.connect(self.img_gaussian_filter)
        self.tools_window.box_4_button_5.clicked.connect(self.img_bilateral_filter)

        self.label_show_window = ui.PicWindow()
        self.label_show_window.pic_show_label.setScaledContents(True)
        self.label_show_window.contrast_show_label.setScaledContents(True)
        self.label_show_window.his_show_label.setScaledContents(True)
        self.text_edit_window = ui.TextWindow()

        self.grid = QHBoxLayout()
        self.grid.addWidget(self.tools_window)
        self.grid.addWidget(self.label_show_window)
        self.grid.addWidget(self.text_edit_window)

        # 打开图片文件
        open_pic = QAction('打开图片', self)
        # open_pic.setShortcut('Ctrl+O')
        open_pic.triggered.connect(self.show_pic)
        # 打开视频文件
        open_vid = QAction('打开视频', self)
        # open_vid.triggered.connect(self.show_vid)
        # 保存图片
        save_pic = QAction('保存图片', self)
        save_pic.setStatusTip('Save a picture')
        # save_pic.triggered.connect(self.pic_save)
        # 保存视频
        save_vid = QAction('保存视频', self)
        save_vid.setStatusTip('Save a video')
        # save_vid.triggered.connect(self.vid_save)

        # 退出
        func_exit = QAction('退出', self)
        func_exit.setShortcut('Esc')
        func_exit.triggered.connect(QCoreApplication.instance().quit)

        # 添加File菜单&子菜单
        file_menubar = self.menuBar()
        file_menu = file_menubar.addMenu('文件')
        file_menu.addAction(open_pic)
        file_menu.addAction(save_pic)
        file_menu.addAction(open_vid)
        file_menu.addAction(save_vid)
        file_menu.addAction(func_exit)

        # 添加Help菜单&子菜单
        help_menubar = self.menuBar()
        help_menu = help_menubar.addMenu("帮助")
        document_help = QAction('文档', self)
        document_help.setStatusTip('帮助文档')
        document_help.triggered.connect(self.document_link)
        help_menu.addAction(document_help)

        self.setWindowTitle('CV Tools')
        self.setWindowIcon(QIcon('../res/img/icon.jpg'))
        self.wid_get = QWidget()
        self.wid_get.setLayout(self.grid)
        self.setCentralWidget(self.wid_get)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.resize(980, 720)
        self.show()

    def show_pic(self):
        # 调用存储文件
        file_name, tmp = QFileDialog.getOpenFileName(self, 'Open Image', 'Image', '*.png *.jpg *.bmp')
        if file_name is '':
            return
        # 采用OpenCV函数读取数据
        self.img = cv2.imread(file_name, -1)
        if self.img.size == 1:
            return
        self.g_pic = cv2.imread(file_name, -1)
        self.re_show_pic()

    def re_show_pic(self):
        if len(self.img.shape) == 3:
            # 提取图像的通道和尺寸，用于将OpenCV下的image转换成QImage
            height_1, width_1, channel_1 = self.img.shape
            self.label_show_window.contrast_show_label.setText('处理图')
            self.label_show_window.contrast_show_label.resize(width_1, height_1)
            bytes_perline_1 = 3 * width_1
            self.q_img_1 = QImage(self.img.data, width_1, height_1, bytes_perline_1, QImage.Format_RGB888).rgbSwapped()
            # 将QImage显示出来
            self.label_show_window.contrast_show_label.setPixmap(QPixmap.fromImage(self.q_img_1))
        else:
            self.tmp = self.img
            self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)
            # 提取图像的通道和尺寸，用于将OpenCV下的image转换成QImage
            height_1, width_1, channel_1 = self.img.shape
            self.label_show_window.contrast_show_label.setText('处理图')
            self.label_show_window.contrast_show_label.resize(width_1, height_1)
            bytes_perline_1 = 3 * width_1
            self.q_img_1 = QImage(self.img.data, width_1, height_1, bytes_perline_1, QImage.Format_RGB888).rgbSwapped()
            # 将QImage显示出来
            self.label_show_window.contrast_show_label.setPixmap(QPixmap.fromImage(self.q_img_1))
            self.img = self.tmp

        plt = self.img_plt()
        if len(plt.shape) == 2:
            plt = cv2.cvtColor(plt, cv2.COLOR_GRAY2BGR)
        height_3, width_3, channel_3 = plt.shape
        self.label_show_window.his_show_label.resize(width_3, height_3)
        bytes_perline_3 = 3 * width_3
        self.q_img_3 = QImage(plt.data, width_3, height_3, bytes_perline_3, QImage.Format_RGB888).rgbSwapped()
        # 将QImage显示出来
        self.label_show_window.his_show_label.setPixmap(QPixmap.fromImage(self.q_img_3))
        if self.last_pic is not None:
            if len(self.last_pic.shape) == 3:
                height_2, width_2, channel_2 = self.last_pic.shape
                self.label_show_window.pic_label.setText('图像')
                self.label_show_window.pic_show_label.resize(width_2, height_2)
                bytes_perline_2 = 3 * width_2
                self.q_img_2 = QImage(self.last_pic.data, width_2, height_2, bytes_perline_2,
                                      QImage.Format_RGB888).rgbSwapped()
                # 将QImage显示出来
                self.label_show_window.pic_show_label.setPixmap(QPixmap.fromImage(self.q_img_2))
            else:
                self.tmp = self.last_pic
                self.last_pic = cv2.cvtColor(self.last_pic, cv2.COLOR_GRAY2BGR)
                height_2, width_2, channel_2 = self.last_pic.shape
                self.label_show_window.pic_label.setText('图像')
                self.label_show_window.pic_show_label.resize(width_2, height_2)
                bytes_perline_2 = 3 * width_2
                self.q_img_2 = QImage(self.last_pic.data, width_2, height_2, bytes_perline_2,
                                      QImage.Format_RGB888).rgbSwapped()
                # 将QImage显示出来
                self.label_show_window.pic_show_label.setPixmap(QPixmap.fromImage(self.q_img_2))
                self.last_pic = self.tmp
        self.last_pic = self.img

    def review_origin_pic(self):
        self.img = self.g_pic
        self.re_show_pic()

    def img_to_gray(self):
        self.img = util.img_to_gray(self.img)
        self.re_show_pic()

    def img_to_auto_bin(self):
        self.img = util.img_to_auto_bin(self.img)
        self.re_show_pic()

    def img_to_horizontal(self):
        self.img = util.img_to_horizontal(self.img)
        self.re_show_pic()

    def img_to_vertical(self):
        self.img = util.img_to_vertical(self.img)
        self.re_show_pic()

    def img_to_rotate_left(self):
        self.img = util.img_to_rotate_left(self.img)
        self.re_show_pic()

    def img_to_rotate_right(self):
        self.img = util.img_to_rotate_right(self.img)
        self.re_show_pic()

    def img_impulse_noise(self):
        self.img = util.img_impulse_noise(self.img, 0.01)
        self.re_show_pic()

    def img_gaussian_noise(self):
        self.img = util.img_gaussian_noise(self.img, 0, 0.01)
        self.re_show_pic()

    def img_blur_filter(self):
        self.img = util.img_blur_filter(self.img)
        self.re_show_pic()

    def img_median_filter(self):
        self.img = util.img_median_filter(self.img)
        self.re_show_pic()

    def img_gaussian_filter(self):
        self.img = util.img_gaussian_filter(self.img)
        self.re_show_pic()

    def img_bilateral_filter(self):
        self.img = util.img_bilateral_filter(self.img)
        self.re_show_pic()

    def img_plt(self):
        if len(self.img.shape) == 3:
            util.img_plt_rgb(self.img)
        else:
            util.img_plt_gray(self.img)
        plt = cv2.imread("./plt.png")
        return plt

    def document_link(self):
        util.document_link()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
