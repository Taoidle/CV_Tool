"""
This example is about opencv with pyqt5

Aauthor: kaiyang
Website: www.lkyblog.cn git.lkyblog.cn
Last edited: April 2020

"""

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QCheckBox, QLineEdit,
                             QAction, QFileDialog, QApplication, QDesktopWidget, QMenu, QMessageBox, QInputDialog,
                             QPushButton, QGridLayout)
from PyQt5.QtGui import QIcon, QImage, QPixmap

import cv2, util, sys, webbrowser, ui_custom, time


class UI(QMainWindow, QWidget):
    vid_horizontal_flag = False
    vid_vertical_flag = False
    vid_horizontal_vertical_flag = False
    g_pic = 0

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.statusBar()
        self.label_show = QLabel()
        self.label_show.resize(512, 512)
        self.label_show.setText('This is a Picture Label')
        self.label_cv_basic = QLabel('CV Basic')
        self.label_cv_basic.setMaximumHeight(20)
        self.label_pic_position = QLabel('IMG Position')
        self.label_pic_position.setMaximumHeight(20)
        self.label_vid_position = QLabel('VID Position')
        self.label_vid_position.setMaximumHeight(20)
        self.label_filter = QLabel('Filter')
        self.label_filter.setMaximumHeight(20)
        self.label_embed = QLabel('Embed')
        self.label_embed.setMaximumHeight(20)
        self.label_extract = QLabel('Extract')
        self.label_extract.setMaximumHeight(20)

        self.label_show.setScaledContents(True)
        self.setCentralWidget(self.label_show)

        self.embed_input = QLineEdit('Input your string')
        self.lsb_embed_button = QPushButton('LSB')
        self.lsb_embed_button.clicked.connect(self.lsb_embed)
        self.extract_output = QLineEdit('Extract string')
        self.lsb_extract_button = QPushButton('LSB')
        self.lsb_extract_button.clicked.connect(self.lsb_extract)


        self.origin_pic_button = QPushButton('Origin IMG', self)
        self.origin_pic_button.clicked.connect(self.re_origin_img)
        self.pic_gray_button = QPushButton('Gray', self)
        self.pic_gray_button.clicked.connect(self.img_to_gray)
        self.pic_bin_button = QPushButton('Binarization', self)
        self.pic_bin_button.clicked.connect(self.img_to_bin)
        self.pic_auto_bin_button = QPushButton('Auto Binarization', self)
        self.pic_auto_bin_button.clicked.connect(self.img_to_auto_bin)

        self.blur_button = QPushButton('Blur', self)
        self.blur_button.clicked.connect(self.img_blur_filter)
        self.median_blur_button = QPushButton('Median Filter', self)
        self.median_blur_button.clicked.connect(self.img_median_filter)
        self.gaussian_button = QPushButton('Gaussian Filter', self)
        self.gaussian_button.clicked.connect(self.img_gaussian_filter)
        self.bilateral_button = QPushButton('Bilateral Filter', self)
        self.blur_button.clicked.connect(self.img_bilateral_filter)

        self.grid = QGridLayout()
        # self.grid.setSpacing(10)
        self.grid.addWidget(self.label_show, 1, 1, 20, 1)
        self.grid.addWidget(self.label_pic_position, 1, 2)
        self.grid.addWidget(self.img_horizontal_button, 2, 2)
        self.grid.addWidget(self.img_vertical_button, 2, 3)
        self.grid.addWidget(self.img_rotate_left, 2, 4)
        self.grid.addWidget(self.img_rotate_right, 2, 5)
        self.grid.addWidget(self.label_vid_position, 3, 2)
        self.grid.addWidget(self.vid_horizontal_button, 4, 2)
        self.grid.addWidget(self.vid_vertical_button, 4, 3)
        self.grid.addWidget(self.vid_horizontal_vertical_button, 4, 4)
        self.grid.addWidget(self.label_cv_basic, 5, 2)
        self.grid.addWidget(self.origin_pic_button, 6, 2)
        self.grid.addWidget(self.pic_gray_button, 6, 3)
        self.grid.addWidget(self.pic_bin_button, 6, 4)
        self.grid.addWidget(self.pic_auto_bin_button, 6, 5)
        self.grid.addWidget(self.label_filter, 7, 2)
        self.grid.addWidget(self.blur_button, 8, 2)
        self.grid.addWidget(self.median_blur_button, 8, 3)
        self.grid.addWidget(self.gaussian_button, 8, 4)
        self.grid.addWidget(self.bilateral_button, 8, 5)
        self.grid.addWidget(self.label_embed, 9, 2)
        self.grid.addWidget(self.embed_input, 10, 2)
        self.grid.addWidget(self.lsb_embed_button, 10, 3)
        self.grid.addWidget(self.label_extract, 11, 2)
        self.grid.addWidget(self.extract_output, 12, 2)
        self.grid.addWidget(self.lsb_extract_button, 12, 3)

        self.wid_get = QWidget()
        self.wid_get.setLayout(self.grid)
        self.setCentralWidget(self.wid_get)

        # 打开图片文件
        open_pic = QAction('Open Picture', self)
        # open_pic.setShortcut('Ctrl+O')
        open_pic.setStatusTip('Open New Picture')
        open_pic.triggered.connect(self.show_pic)
        # 打开视频文件
        open_vid = QAction('Open Video', self)
        open_vid.setStatusTip('Open New Video')
        open_vid.triggered.connect(self.show_vid)
        # 保存图片
        save_pic = QAction('Save Picture', self)
        save_pic.setStatusTip('Save a picture')
        save_pic.triggered.connect(self.pic_save)
        # 保存视频
        save_vid = QAction('Save Video', self)
        save_vid.setStatusTip('Save a video')
        # save_vid.triggered.connect(self.vid_save)

        # 退出
        func_exit = QAction('Exit', self)
        func_exit.setShortcut('Esc')
        func_exit.setStatusTip('Exit the program')
        func_exit.triggered.connect(QCoreApplication.instance().quit)

        # 添加File菜单&子菜单
        file_menubar = self.menuBar()
        file_menu = file_menubar.addMenu('&File')
        file_menu.addAction(open_pic)
        file_menu.addAction(save_pic)
        file_menu.addAction(open_vid)
        file_menu.addAction(save_vid)
        file_menu.addAction(func_exit)

        # 添加Util菜单&子菜单
        util_menubar = self.menuBar()
        util_menu = util_menubar.addMenu("&Util")
        # 使用QMenu创建菜单
        img_position_menu = QMenu('IMG_Position', self)
        vid_position_menu = QMenu('VID_Position', self)
        filter_menu = QMenu('Filter', self)
        embed_menu = QMenu('Embed', self)

        # 使用addAction添加一个动作
        img_horizontal_mirror = QAction('horizontal mirror', self)
        img_horizontal_mirror.setStatusTip('水平镜像')
        img_horizontal_mirror.triggered.connect(self.img_to_horizontal)
        img_vertical_mirror = QAction('vertical mirror', self)
        img_vertical_mirror.setStatusTip('垂直镜像')
        img_vertical_mirror.triggered.connect(self.img_to_vertical)
        img_position_menu.addAction(img_horizontal_mirror)
        img_position_menu.addAction(img_vertical_mirror)
        util_menu.addMenu(img_position_menu)

        self.vid_horizontal_mirror = QAction('horizontal mirror', self, checkable=True)
        self.vid_horizontal_mirror.setStatusTip('水平镜像')
        self.vid_horizontal_mirror.triggered.connect(self.vid_to_horizontal)
        self.vid_vertical_mirror = QAction('vertical mirror', self, checkable=True)
        self.vid_vertical_mirror.setStatusTip('垂直镜像')
        self.vid_vertical_mirror.triggered.connect(self.vid_to_vertical)
        self.vid_horizontal_vertical_mirror = QAction('horizontal & vertical', self, checkable=True)
        self.vid_horizontal_vertical_mirror.setStatusTip('水平垂直镜像')
        self.vid_horizontal_vertical_mirror.triggered.connect(self.vid_to_horizontal_vertical)
        vid_position_menu.addAction(self.vid_horizontal_mirror)
        vid_position_menu.addAction(self.vid_vertical_mirror)
        vid_position_menu.addAction(self.vid_horizontal_vertical_mirror)
        util_menu.addMenu(vid_position_menu)

        blur_filter = QAction('blur', self)
        blur_filter.setStatusTip('均值滤波')
        blur_filter.triggered.connect(self.img_blur_filter)
        median_filter = QAction('median', self)
        median_filter.setStatusTip('中值滤波')
        median_filter.triggered.connect(self.img_median_filter)
        gaussian_filter = QAction('gaussian blur', self)
        gaussian_filter.setStatusTip('高斯滤波')
        gaussian_filter.triggered.connect(self.img_gaussian_filter)
        bilateral_blur = QAction('bilateral', self)
        bilateral_blur.setStatusTip('双边滤波')
        bilateral_blur.triggered.connect(self.img_bilateral_filter)

        filter_menu.addAction(blur_filter)
        filter_menu.addAction(median_filter)
        filter_menu.addAction(gaussian_filter)
        filter_menu.addAction(bilateral_blur)
        util_menu.addMenu(filter_menu)

        lsb_embed = QAction('lsb embed', self)
        lsb_embed.setStatusTip('lsb嵌入')
        lsb_embed.triggered.connect(self.lsb_dialog)
        embed_menu.addAction(lsb_embed)
        util_menu.addMenu(embed_menu)

        # 添加Help菜单&子菜单
        help_menubar = self.menuBar()
        help_menu = help_menubar.addMenu("&Help")
        document_help = QAction('Document', self)
        document_help.setStatusTip('帮助文档')
        document_help.triggered.connect(self.document_link)
        help_menu.addAction(document_help)

        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.resize(720, 480)
        self.center()
        self.setWindowIcon(QIcon('../res/img/icon.jpg'))
        self.setWindowTitle('CV_Tools')
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




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())
