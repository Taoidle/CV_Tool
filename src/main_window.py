"""

Author: kaiyang
Last edited: April 2020

"""

from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QCheckBox, QLineEdit, QHBoxLayout,
                             QAction, QFileDialog, QApplication, QDesktopWidget, QMenu, QMessageBox, QInputDialog,
                             QPushButton, QGridLayout, QTabWidget)
from PyQt5.QtGui import QIcon, QImage, QPixmap
import cv2, util, sys, ui, time


class MainWindow(QMainWindow, QWidget):
    last_pic = None
    last_pic_backup = None
    g_pic = None
    img = None

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.pic_tools_window = ui.PicToolsWindow()
        self.pic_tools_window.setFixedWidth(220)
        self.pic_tools_window.box_1_button_1.clicked.connect(self.review_origin_pic)
        self.pic_tools_window.box_1_button_2.clicked.connect(self.review_last_pic)
        self.pic_tools_window.box_1_button_3.clicked.connect(self.img_to_gray)
        self.pic_tools_window.box_1_button_4.clicked.connect(self.img_to_inverse)
        self.pic_tools_window.box_1_button_5.clicked.connect(self.img_to_bin)
        self.pic_tools_window.box_1_button_6.clicked.connect(self.img_to_auto_bin)
        self.pic_tools_window.box_2_button_1.clicked.connect(self.img_to_horizontal)
        self.pic_tools_window.box_2_button_2.clicked.connect(self.img_to_vertical)
        self.pic_tools_window.box_2_button_3.clicked.connect(self.img_to_rotate_left)
        self.pic_tools_window.box_2_button_4.clicked.connect(self.img_to_rotate_right)
        self.pic_tools_window.box_3_button_1.clicked.connect(self.img_impulse_noise)
        self.pic_tools_window.box_3_button_2.clicked.connect(self.img_gaussian_noise)
        self.pic_tools_window.box_4_button_1.clicked.connect(self.img_blur_filter)
        self.pic_tools_window.box_4_button_2.clicked.connect(self.img_median_filter)
        self.pic_tools_window.box_4_button_3.clicked.connect(self.img_box_filter)
        self.pic_tools_window.box_4_button_4.clicked.connect(self.img_gaussian_filter)
        self.pic_tools_window.box_4_button_5.clicked.connect(self.img_bilateral_filter)
        self.pic_tools_window.box_5_button_1.clicked.connect(self.img_canny_operator)
        self.pic_tools_window.box_5_button_2.clicked.connect(self.img_sobel_operator)
        self.pic_tools_window.box_5_button_3.clicked.connect(self.img_laplacian_operator)
        self.pic_tools_window.box_5_button_4.clicked.connect(self.img_scharr_operator)

        self.pic_label_show_window = ui.PicWindow()
        self.pic_label_show_window.pic_show_label.setScaledContents(True)
        self.pic_label_show_window.contrast_show_label.setScaledContents(True)
        self.pic_label_show_window.his_show_label_this.setScaledContents(True)
        self.pic_text_edit_window = ui.TextWindow()

        self.pic_h_box = QHBoxLayout()
        self.pic_h_box.addWidget(self.pic_tools_window)
        self.pic_h_box.addWidget(self.pic_label_show_window)
        self.pic_h_box.addWidget(self.pic_text_edit_window)

        self.vid_tools_window = ui.VidToolsWindow()
        self.vid_tools_window.setFixedWidth(220)

        self.vid_label_show_window = ui.VidWindow()
        self.vid_label_show_window.vid_show_label.setScaledContents(True)
        self.vid_label_show_window.vid_info_show_label.setScaledContents(True)

        self.vid_h_box = QHBoxLayout()
        self.vid_h_box.addWidget(self.vid_tools_window)
        self.vid_h_box.addWidget(self.vid_label_show_window)

        self.wid_1_get = QWidget()
        self.wid_1_get.setLayout(self.pic_h_box)
        self.wid_2_get = QWidget()
        self.wid_2_get.setLayout(self.vid_h_box)

        self.tab_wid = QTabWidget()
        self.tab_wid.addTab(self.wid_1_get, '图像处理')
        self.tab_wid.addTab(self.wid_2_get, '视频处理')
        self.tab_wid.setStyleSheet("background-color:#f0f0f0")

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.tab_wid)

        self.setLayout(self.h_box)
        self.setCentralWidget(self.tab_wid)

        self.statusBar()
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

        # 图像处理菜单
        pic_menubar = self.menuBar()
        pic_menu = pic_menubar.addMenu("图像处理")
        # 显示rgb分量和直方图
        show_his_rgb = QAction('RGB分量', self)
        pic_menu.addAction(show_his_rgb)

        # 视频处理菜单
        vid_menubar = self.menuBar()
        vid_menu = vid_menubar.addMenu("视频处理")


        # 添加Help菜单&子菜单
        help_menubar = self.menuBar()
        help_menu = help_menubar.addMenu("帮助")
        document_help = QAction('文档', self)
        document_help.setStatusTip('帮助文档')
        document_help.triggered.connect(self.document_link)
        help_menu.addAction(document_help)

        self.setWindowTitle('CV Tools')
        self.setWindowIcon(QIcon('../res/img/icon.jpg'))
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
            self.pic_label_show_window.contrast_show_label.setText('当前图像')
            bytes_perline_1 = 3 * width_1
            self.q_img_1 = QImage(self.img.data, width_1, height_1, bytes_perline_1, QImage.Format_RGB888).rgbSwapped()

            width_1, height_1 = util.shrink_len(width_1, height_1)
            pix_map = QPixmap.fromImage(self.q_img_1)
            fit_pix_map = pix_map.scaled(width_1, height_1, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.pic_label_show_window.contrast_show_label.resize(width_1, height_1)
            self.pic_label_show_window.contrast_show_label.setPixmap(fit_pix_map)
        else:
            self.tmp = self.img
            self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)
            height_1, width_1, channel_1 = self.img.shape
            self.pic_label_show_window.contrast_show_label.setText('当前图像')
            bytes_perline_1 = 3 * width_1
            self.q_img_1 = QImage(self.img.data, width_1, height_1, bytes_perline_1, QImage.Format_RGB888).rgbSwapped()

            width_1, height_1 = util.shrink_len(width_1, height_1)
            pix_map = QPixmap.fromImage(self.q_img_1)
            fit_pix_map = pix_map.scaled(width_1, height_1, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.pic_label_show_window.contrast_show_label.resize(width_1, height_1)
            self.pic_label_show_window.contrast_show_label.setPixmap(fit_pix_map)
            self.img = self.tmp

        plt = self.img_plt(self.img, '../res/img/plt_this.png')
        if len(plt.shape) == 2:
            plt = cv2.cvtColor(plt, cv2.COLOR_GRAY2BGR)
        height_3, width_3, channel_3 = plt.shape
        bytes_perline_3 = 3 * width_3
        self.q_img_3 = QImage(plt.data, width_3, height_3, bytes_perline_3, QImage.Format_RGB888).rgbSwapped()

        width_3, height_3 = util.shrink_len(width_3, height_3)
        pix_map = QPixmap.fromImage(self.q_img_3)
        fit_pix_map = pix_map.scaled(width_3, height_3, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.pic_label_show_window.his_show_label_this.resize(width_3, height_3)
        self.pic_label_show_window.his_show_label_this.setPixmap(fit_pix_map)

        if self.last_pic is not None:
            if len(self.last_pic.shape) == 3:
                height_2, width_2, channel_2 = self.last_pic.shape
                self.pic_label_show_window.pic_label.setText('上一步图像')
                bytes_perline_2 = 3 * width_2
                self.q_img_2 = QImage(self.last_pic.data, width_2, height_2, bytes_perline_2,
                                      QImage.Format_RGB888).rgbSwapped()

                width_2, height_2 = util.shrink_len(width_2, height_2)
                pix_map = QPixmap.fromImage(self.q_img_2)
                fit_pix_map = pix_map.scaled(width_2, height_2, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                self.pic_label_show_window.pic_show_label.resize(width_2, height_2)
                self.pic_label_show_window.pic_show_label.setPixmap(fit_pix_map)
            else:
                self.tmp = self.last_pic
                self.last_pic = cv2.cvtColor(self.last_pic, cv2.COLOR_GRAY2BGR)
                height_2, width_2, channel_2 = self.last_pic.shape
                self.pic_label_show_window.pic_label.setText('上一步图像')
                bytes_perline_2 = 3 * width_2
                self.q_img_2 = QImage(self.last_pic.data, width_2, height_2, bytes_perline_2,
                                      QImage.Format_RGB888).rgbSwapped()

                width_2, height_2 = util.shrink_len(width_2, height_2)
                pix_map = QPixmap.fromImage(self.q_img_2)
                fit_pix_map = pix_map.scaled(width_2, height_2, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                self.pic_label_show_window.pic_show_label.resize(width_2, height_2)
                self.pic_label_show_window.pic_show_label.setPixmap(fit_pix_map)
                self.last_pic = self.tmp
            plt = self.img_plt(self.last_pic, '../res/img/plt_last.png')
            if len(plt.shape) == 2:
                plt = cv2.cvtColor(plt, cv2.COLOR_GRAY2BGR)
            height_4, width_4, channel_4 = plt.shape
            bytes_perline_4 = 3 * width_4
            self.q_img_4 = QImage(plt.data, width_4, height_4, bytes_perline_4, QImage.Format_RGB888).rgbSwapped()

            width_4, height_4 = util.shrink_len(width_4, height_4)
            pix_map = QPixmap.fromImage(self.q_img_4)
            fit_pix_map = pix_map.scaled(width_4, height_4, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.pic_label_show_window.his_show_label_last.resize(width_4, height_4)
            self.pic_label_show_window.his_show_label_last.setPixmap(fit_pix_map)
        self.last_pic_backup = self.last_pic
        self.last_pic = self.img

    def review_origin_pic(self):
        if self.check_img():
            pass
        else:
            self.img = self.g_pic
            self.re_show_pic()

    def review_last_pic(self):
        if self.check_img() or (self.last_pic_backup is None):
            pass
        else:
            self.img = self.last_pic_backup
            self.re_show_pic()

    def img_to_gray(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_gray(self.img)
            self.re_show_pic()

    def img_to_inverse(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_inverse(self.img)
            print('check')
            self.re_show_pic()

    def img_to_bin(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 255
            ui.SliderDialog.switch_flag = 1
            self.win = ui.SliderDialog()
            self.win.before_close_signal.connect(self.img_to_bin_signal)

    @pyqtSlot(int, bool)
    def img_to_bin_signal(self, connect, flag):
        if flag:
            ret, binary = cv2.threshold(util.img_to_gray(self.img), connect, 255, cv2.THRESH_BINARY)
            self.img = binary
            self.re_show_pic()
        else:
            pass

    def img_to_auto_bin(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_auto_bin(self.img)
            self.re_show_pic()

    def img_to_horizontal(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_horizontal(self.img)
            self.re_show_pic()

    def img_to_vertical(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_vertical(self.img)
            self.re_show_pic()

    def img_to_rotate_left(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_rotate_left(self.img)
            self.re_show_pic()

    def img_to_rotate_right(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_rotate_right(self.img)
            self.re_show_pic()

    def img_impulse_noise(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 1000
            ui.SliderDialog.switch_flag = 2
            self.win = ui.SliderDialog()
            self.win.threshold_slider.setMinimum(1)
            self.win.threshold_slider.setValue(10)
            self.win.before_close_signal.connect(self.img_impulse_noise_signal)

    @pyqtSlot(int, bool)
    def img_impulse_noise_signal(self, connect, flag):
        if flag:
            self.img = util.img_impulse_noise(self.img, connect / 1000)
            self.re_show_pic()
        else:
            pass

    def img_gaussian_noise(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 1000
            ui.SliderDialog.switch_flag = 2
            self.win = ui.SliderDialog()
            self.win.threshold_slider.setMinimum(1)
            self.win.threshold_slider.setValue(10)
            self.win.before_close_signal.connect(self.img_gaussian_noise_signal)

    @pyqtSlot(int, bool)
    def img_gaussian_noise_signal(self, connect, flag):
        if flag:
            self.img = util.img_gaussian_noise(self.img, 0, connect / 1000)
            self.re_show_pic()
        else:
            pass

    def img_blur_filter(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 50
            ui.SliderDialog.switch_flag = 1
            self.win = ui.SliderDialog()
            self.win.threshold_slider.setMinimum(1)
            self.win.threshold_slider.setValue(5)
            self.win.before_close_signal.connect(self.img_blur_filter_signal)

    @pyqtSlot(int, bool)
    def img_blur_filter_signal(self, connect, flag):
        if flag:
            self.img = util.img_blur_filter(self.img, connect)
            self.re_show_pic()
        else:
            pass

    def img_median_filter(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 50
            ui.SliderDialog.switch_flag = 1
            self.win = ui.SliderDialog()
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(1)
            self.win.before_close_signal.connect(self.img_gaussian_filter_signal)

    @pyqtSlot(int, bool)
    def img_median_filter_signal(self, connect, flag):
        if flag:
            self.img = util.img_median_filter(self.img, connect)
            self.re_show_pic()
        else:
            pass

    def img_box_filter(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 50
            ui.SliderDialog.switch_flag = 1
            self.win = ui.SliderDialog()
            self.win.threshold_slider.setMinimum(1)
            self.win.threshold_slider.setValue(2)
            self.win.before_close_signal.connect(self.img_box_filter_signal)

    @pyqtSlot(int, bool)
    def img_box_filter_signal(self, connect, flag):
        if flag:
            self.img = util.img_box_filter(self.img, connect, val=False)
            self.re_show_pic()
        else:
            pass

    def img_gaussian_filter(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 50
            ui.SliderDialog.switch_flag = 1
            self.win = ui.SliderDialog()
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(1)
            self.win.before_close_signal.connect(self.img_gaussian_filter_signal)

    @pyqtSlot(int, bool)
    def img_gaussian_filter_signal(self, connect, flag):
        if flag:
            self.img = util.img_gaussian_filter(self.img, connect)
            self.re_show_pic()
        else:
            pass

    def img_bilateral_filter(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 50
            ui.SliderDialog.switch_flag = 1
            self.win = ui.SliderDialog()
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(1)
            self.win.before_close_signal.connect(self.img_bilateral_filter_signal)

    @pyqtSlot(int, bool)
    def img_bilateral_filter_signal(self, connect, flag):
        if flag:
            self.img = util.img_bilateral_filter(self.img, connect)
            self.re_show_pic()
        else:
            pass

    def img_canny_operator(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 120
            ui.SliderDialog.switch_flag = 1
            self.win = ui.SliderDialog()
            self.win.threshold_slider.setMinimum(1)
            self.win.threshold_slider.setValue(1)
            self.win.before_close_signal.connect(self.img_canny_operator_signal)

    @pyqtSlot(int, bool)
    def img_canny_operator_signal(self, connect, flag):
        if flag:
            self.img = util.img_canny_operator(self.img, connect)
            self.re_show_pic()
        else:
            pass

    def img_sobel_operator(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 120
            ui.SliderDialog.switch_flag = 1
            self.win = ui.SliderDialog()
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(1)
            self.win.before_close_signal.connect(self.img_sobel_operator_signal)

    @pyqtSlot(int, bool)
    def img_sobel_operator_signal(self, connect, flag):
        if flag:
            self.img = util.img_canny_operator(self.img, connect)
            self.re_show_pic()
        else:
            pass

    def img_laplacian_operator(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 120
            ui.SliderDialog.switch_flag = 1
            self.win = ui.SliderDialog()
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(1)
            self.win.before_close_signal.connect(self.img_laplacian_operator_signal)

    @pyqtSlot(int, bool)
    def img_laplacian_operator_signal(self, connect, flag):
        if flag:
            self.img = util.img_laplacian_operator(self.img, connect)
            self.re_show_pic()
        else:
            pass

    def img_scharr_operator(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_scharr_operator(self.img)
            self.re_show_pic()

    def img_plt(self, pic, path):
        if len(pic.shape) == 3:
            util.img_plt_rgb(pic, path)
        else:
            util.img_plt_gray(pic, path)
        plt = cv2.imread(path)
        return plt

    def document_link(self):
        util.document_link()

    def check_img(self):
        if self.img is not None:
            return False
        else:
            QMessageBox.warning(self, '警告', "当前没有打开\n任何图像！", QMessageBox.Ok)
            return True

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to exit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
