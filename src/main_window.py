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

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar()
        self.tools_window = ui.ToolsWindow()
        self.tools_window.setFixedWidth(220)
        self.label_show_window = ui.PicWindow()
        self.label_show_window.pic_show_label.setScaledContents(True)
        self.label_show_window.contrast_show_label.setScaledContents(True)
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
        self.re_show_pic()

    def re_show_pic(self):
        # 提取图像的通道和尺寸，用于将OpenCV下的image转换成Qimage
        height_1, width_1, channel_1 = self.img.shape
        self.label_show_window.contrast_show_label.setText('处理图')
        self.label_show_window.contrast_show_label.resize(width_1, height_1)
        bytes_perline_1 = 3 * width_1
        self.q_img_1 = QImage(self.img.data, width_1, height_1, bytes_perline_1, QImage.Format_RGB888).rgbSwapped()
        # 将QImage显示出来
        self.label_show_window.contrast_show_label.setPixmap(QPixmap.fromImage(self.q_img_1))

        if self.last_pic is not None:
            height_2, width_2, channel_2 = self.last_pic.shape
            self.label_show_window.pic_label.setText('图像')
            self.label_show_window.pic_show_label.resize(width_2, height_2)
            bytes_perline_2 = 3 * width_2
            self.q_img_2 = QImage(self.last_pic.data, width_2, height_2, bytes_perline_2,
                                  QImage.Format_RGB888).rgbSwapped()
            # 将QImage显示出来
            self.label_show_window.pic_show_label.setPixmap(QPixmap.fromImage(self.q_img_2))
        self.last_pic = self.img

    def document_link(self):
        webbrowser.open('https://git.lkyblog.cn/Taoidle/cv_tools/src/branch/master')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
