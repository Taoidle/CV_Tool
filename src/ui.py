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
        self.label_cv_basic = QLabel('基本变换')
        self.label_cv_basic.setMaximumHeight(20)
        self.label_pic_position = QLabel('图像位置')
        self.label_pic_position.setMaximumHeight(20)
        self.label_vid_position = QLabel('视频位置')
        self.label_vid_position.setMaximumHeight(20)
        self.label_filter = QLabel('图像滤波')
        self.label_filter.setMaximumHeight(20)
        self.label_embed = QLabel('信息嵌入')
        self.label_embed.setMaximumHeight(20)
        self.label_extract = QLabel('信息提取')
        self.label_extract.setMaximumHeight(20)

        self.label_show.setScaledContents(True)
        self.setCentralWidget(self.label_show)

        self.embed_input = QLineEdit('Input your string')
        self.lsb_embed_button = QPushButton('LSB')
        self.lsb_embed_button.clicked.connect(self.lsb_embed)
        self.extract_output = QLineEdit('Extract string')
        self.lsb_extract_button = QPushButton('LSB')
        self.lsb_extract_button.clicked.connect(self.lsb_extract)

        self.img_horizontal_button = QPushButton('水平镜像')
        self.img_horizontal_button.clicked.connect(self.img_to_horizontal)
        self.img_vertical_button = QPushButton('垂直镜像')
        self.img_vertical_button.clicked.connect(self.img_to_vertical)
        self.img_rotate_left = QPushButton('顺时针 90')
        self.img_rotate_left.clicked.connect(self.img_to_rotate_right)
        self.img_rotate_right = QPushButton('逆时针 90')
        self.img_rotate_right.clicked.connect(self.img_to_rotate_left)

        self.vid_horizontal_button = QCheckBox('水平镜像')
        self.vid_horizontal_button.clicked.connect(self.vid_to_horizontal)
        self.vid_vertical_button = QCheckBox('垂直镜像')
        self.vid_vertical_button.clicked.connect(self.vid_to_vertical)
        self.vid_horizontal_vertical_button = QCheckBox('水平垂直 ')
        self.vid_horizontal_vertical_button.clicked.connect(self.vid_to_horizontal_vertical)

        self.origin_pic_button = QPushButton('恢复原图', self)
        self.origin_pic_button.clicked.connect(self.re_origin_img)
        self.pic_gray_button = QPushButton('灰度化', self)
        self.pic_gray_button.clicked.connect(self.img_to_gray)
        self.pic_bin_button = QPushButton('二值化', self)
        self.pic_bin_button.clicked.connect(self.img_to_bin)
        self.pic_auto_bin_button = QPushButton('自动阈值二值化', self)
        self.pic_auto_bin_button.clicked.connect(self.img_to_auto_bin)

        self.blur_button = QPushButton('均值滤波', self)
        self.blur_button.clicked.connect(self.img_blur_filter)
        self.median_blur_button = QPushButton('中值滤波', self)
        self.median_blur_button.clicked.connect(self.img_median_filter)
        self.gaussian_button = QPushButton('高斯滤波', self)
        self.gaussian_button.clicked.connect(self.img_gaussian_filter)
        self.bilateral_button = QPushButton('双边滤波', self)
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
        self.grid.addWidget(self.lsb_embed_button, 11, 2)
        self.grid.addWidget(self.label_extract, 12, 2)
        self.grid.addWidget(self.extract_output, 13, 2)
        self.grid.addWidget(self.lsb_extract_button, 14, 2)

        self.wid_get = QWidget()
        self.wid_get.setLayout(self.grid)
        self.setCentralWidget(self.wid_get)

        # 打开图片文件
        open_pic = QAction('打开图片', self)
        # open_pic.setShortcut('Ctrl+O')
        open_pic.triggered.connect(self.show_pic)
        # 打开视频文件
        open_vid = QAction('打开视频', self)
        open_vid.triggered.connect(self.show_vid)
        # 保存图片
        save_pic = QAction('保存图片', self)
        save_pic.setStatusTip('Save a picture')
        save_pic.triggered.connect(self.pic_save)
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

        # 添加Util菜单&子菜单
        util_menubar = self.menuBar()
        util_menu = util_menubar.addMenu("工具")
        # 使用QMenu创建菜单
        img_position_menu = QMenu('图片位置', self)
        vid_position_menu = QMenu('视频位置', self)
        filter_menu = QMenu('图像滤波', self)
        embed_menu = QMenu('信息嵌入', self)

        # 使用addAction添加一个动作
        img_horizontal_mirror = QAction('水平镜像', self)
        img_horizontal_mirror.triggered.connect(self.img_to_horizontal)
        img_vertical_mirror = QAction('垂直镜像', self)
        img_vertical_mirror.triggered.connect(self.img_to_vertical)
        img_position_menu.addAction(img_horizontal_mirror)
        img_position_menu.addAction(img_vertical_mirror)
        util_menu.addMenu(img_position_menu)

        self.vid_horizontal_mirror = QAction('水平镜像', self, checkable=True)
        self.vid_horizontal_mirror.setStatusTip('水平镜像')
        self.vid_horizontal_mirror.triggered.connect(self.vid_to_horizontal)
        self.vid_vertical_mirror = QAction('垂直镜像', self, checkable=True)
        self.vid_vertical_mirror.setStatusTip('垂直镜像')
        self.vid_vertical_mirror.triggered.connect(self.vid_to_vertical)
        self.vid_horizontal_vertical_mirror = QAction('水平垂直镜像', self, checkable=True)
        self.vid_horizontal_vertical_mirror.triggered.connect(self.vid_to_horizontal_vertical)
        vid_position_menu.addAction(self.vid_horizontal_mirror)
        vid_position_menu.addAction(self.vid_vertical_mirror)
        vid_position_menu.addAction(self.vid_horizontal_vertical_mirror)
        util_menu.addMenu(vid_position_menu)

        blur_filter = QAction('均值滤波 ', self)
        blur_filter.triggered.connect(self.img_blur_filter)
        median_filter = QAction('中值滤波', self)
        median_filter.triggered.connect(self.img_median_filter)
        gaussian_filter = QAction('高斯滤波', self)
        gaussian_filter.triggered.connect(self.img_gaussian_filter)
        bilateral_blur = QAction('双边滤波', self)
        bilateral_blur.triggered.connect(self.img_bilateral_filter)

        filter_menu.addAction(blur_filter)
        filter_menu.addAction(median_filter)
        filter_menu.addAction(gaussian_filter)
        filter_menu.addAction(bilateral_blur)
        util_menu.addMenu(filter_menu)

        lsb_embed = QAction('LSB嵌入', self)
        lsb_embed.triggered.connect(self.lsb_dialog)
        embed_menu.addAction(lsb_embed)
        util_menu.addMenu(embed_menu)

        # 添加Help菜单&子菜单
        help_menubar = self.menuBar()
        help_menu = help_menubar.addMenu("帮助")
        document_help = QAction('帮助文档', self)
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

    def show_pic(self):
        # 调用存储文件
        file_name, tmp = QFileDialog.getOpenFileName(self, 'Open Image', 'Image', '*.png *.jpg *.bmp')
        if file_name is '':
            return
        # 采用OpenCV函数读取数据
        self.img = cv2.imread(file_name, -1)
        self.g_pic = cv2.imread(file_name, -1)
        if self.img.size == 1:
            return
        self.re_show_pic()

    def pic_save(self):
        pic_name = './pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        cv2.imwrite(pic_name + '.bmp', self.img)

    def re_show_pic(self):
        # 提取图像的通道和尺寸，用于将OpenCV下的image转换成Qimage
        height, width, channel = self.img.shape
        self.label_show.resize(width, height)
        bytes_perline = 3 * width
        self.q_img = QImage(self.img.data, width, height, bytes_perline, QImage.Format_RGB888).rgbSwapped()
        # 将QImage显示出来
        self.label_show.setPixmap(QPixmap.fromImage(self.q_img))

    def show_vid(self):
        # 调用存储文件
        file_name, tmp = QFileDialog.getOpenFileName(self, 'Open Video', 'Video', '*.mp4')
        if file_name is '':
            return
        # 采用OpenCV函数读取数据
        self.vid_reader = cv2.VideoCapture(file_name)
        ret_tmp, tmp = self.vid_reader.read()
        tmp_height, tmp_width, tmp_channel = tmp.shape
        self.resize(tmp_width, tmp_height)

        while (self.vid_reader.isOpened()):
            ret, frame = self.vid_reader.read()
            if not (ret):
                break
            # 提取图像的通道和尺寸，用于将OpenCV下的image转换成Qimage
            if self.vid_horizontal_flag:
                frame = cv2.flip(frame, 1)
            if self.vid_vertical_flag:
                frame = cv2.flip(frame, 0)
            if self.vid_horizontal_vertical_flag:
                frame = cv2.flip(frame, -1)
            height, width, channel = frame.shape
            bytes_perline = 3 * width
            self.q_img = QImage(frame.data, width, height, bytes_perline, QImage.Format_RGB888).rgbSwapped()
            self.label_show.setPixmap(QPixmap.fromImage(self.q_img))
            # wait until key strokes to break
            if cv2.waitKey(40) & 0xFF == ord('q'):
                break

        self.vid_reader.release()
        cv2.destroyAllWindows()

    def img_to_horizontal(self):
        self.img = cv2.flip(self.img, 1)
        if self.img.size == 1:
            return
        self.re_show_pic()

    def img_to_vertical(self):
        self.img = cv2.flip(self.img, 0)
        if self.img.size == 1:
            return
        self.re_show_pic()

    def img_to_rotate_left(self):
        self.img = util.rotate_img(self.img, 90)
        self.re_show_pic()

    def img_to_rotate_right(self):
        self.img = util.rotate_img(self.img, -90)
        self.re_show_pic()

    def vid_to_horizontal(self, state):
        if self.vid_horizontal_button.isChecked():
            self.vid_horizontal_mirror.setCheckable(True)
        else:
            self.vid_horizontal_mirror.setCheckable(False)
        if state:
            self.vid_horizontal_flag = True
        else:
            self.vid_horizontal_flag = False

    def vid_to_vertical(self, state):
        if self.vid_vertical_button.isChecked():
            self.vid_vertical_mirror.setCheckable(True)
        else:
            self.vid_vertical_mirror.setCheckable(False)
        if state:
            self.vid_vertical_flag = True
        else:
            self.vid_vertical_flag = False

    def vid_to_horizontal_vertical(self, state):
        if self.vid_horizontal_vertical_mirror.isChecked():
            self.vid_horizontal_vertical_mirror.setCheckable(True)
        else:
            self.vid_horizontal_vertical_mirror.setCheckable(False)
        if state:
            self.vid_horizontal_vertical_flag = True
        else:
            self.vid_horizontal_vertical_flag = False

    def re_origin_img(self):
        self.img = self.g_pic
        self.re_show_pic()

    def img_to_gray(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)
        self.re_show_pic()

    def img_to_bin(self):
        ui_custom.SliderDialog.threshold_max = 255
        self.win = ui_custom.SliderDialog()
        self.win.before_close_signal.connect(self.img_to_bin_signal)

    def img_to_auto_bin(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        self.img = cv2.adaptiveThreshold(self.img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)
        self.re_show_pic()

    def img_blur_filter(self):
        self.img = cv2.blur(self.img, (5, 5))
        self.re_show_pic()

    def img_median_filter(self):
        self.img = cv2.medianBlur(self.img, 5)
        self.re_show_pic()

    def img_gaussian_filter(self):
        self.img = cv2.GaussianBlur(self.img, (5, 5), 0)
        self.re_show_pic()

    def img_bilateral_filter(self):
        self.img = cv2.bilateralFilter(self.img, 9, 75, 75)
        self.re_show_pic()

    def lsb_dialog(self):
        text, ok = QInputDialog.getText(self, 'Input', 'Enter your string:')
        if ok:
            # 把得到的字符串放到输入框里
            util.lsb_embed(self.img, str(text))

    def lsb_embed(self):
        text = self.embed_input.text()
        if text is not None:
            self.img = util.lsb_embed(self.img, str(text))
            pic_name = '../res/embed_img/pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
            cv2.imwrite(pic_name + '.bmp', self.img)
            filename = pic_name + '.txt'
            with open(filename, 'w') as f:
                f.write(str(len(text) * 8))
            self.re_show_pic()

    def lsb_extract(self):
        file_name, tmp = QFileDialog.getOpenFileName(self, 'Open embed_txt', 'txt', '*.txt')
        with open(file_name) as f:
            num = f.read()
        self.extract_output.setText(util.lsb_extract(self.img,int(num)))

    def document_link(self):
        webbrowser.open('https://git.lkyblog.cn/Taoidle/cv_tools/src/branch/master')

    # 信号槽函数
    def img_to_bin_signal(self, connect):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        ret, binary = cv2.threshold(self.img, connect, 255, cv2.THRESH_BINARY)
        self.img = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
        self.re_show_pic()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())
