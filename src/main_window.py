"""

Copyright (c) 2020 Taoidle
CV Tool is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.

"""

from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout,
                             QAction, QFileDialog, QApplication, QMessageBox, QTabWidget, QDesktopWidget)
from PyQt5.QtGui import QIcon, QImage, QPixmap
import os, cv2, util, sys, ui, time


class MainWindow(QMainWindow):
    last_pic, last_pic_backup, g_pic, img, vid = None, None, None, None, None

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
        self.pic_tools_window.box_1_button_7.clicked.connect(self.img_to_contrast_brightness)
        self.pic_tools_window.box_1_button_8.clicked.connect(self.img_to_basic_roi)
        self.pic_tools_window.box_2_button_1.clicked.connect(self.img_to_horizontal)
        self.pic_tools_window.box_2_button_2.clicked.connect(self.img_to_vertical)
        self.pic_tools_window.box_2_button_3.clicked.connect(self.img_to_rotate_left)
        self.pic_tools_window.box_2_button_4.clicked.connect(self.img_to_rotate_right)
        self.pic_tools_window.box_2_button_5.clicked.connect(self.img_to_rotate_left_any)
        self.pic_tools_window.box_2_button_6.clicked.connect(self.img_to_rotate_right_any)
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
        self.pic_tools_window.box_6_button_1.clicked.connect(self.img_to_erode)
        self.pic_tools_window.box_6_button_2.clicked.connect(self.img_to_dilate)
        self.pic_tools_window.box_6_button_3.clicked.connect(self.img_to_open_operation)
        self.pic_tools_window.box_6_button_4.clicked.connect(self.img_to_close_operation)
        self.pic_tools_window.box_6_button_5.clicked.connect(self.img_to_top_hat)
        self.pic_tools_window.box_6_button_6.clicked.connect(self.img_to_black_hat)
        self.pic_tools_window.box_6_button_7.clicked.connect(self.img_to_gradient)
        self.pic_tools_window.box_7_button_1.clicked.connect(self.lsb_embed)
        self.pic_tools_window.box_8_button_1.clicked.connect(self.lsb_extract)

        self.pic_label_show_window = ui.PicWindow()
        self.pic_label_show_window.pic_show_label.setScaledContents(True)
        self.pic_label_show_window.contrast_show_label.setScaledContents(True)
        self.pic_label_show_window.his_show_label_this.setScaledContents(True)
        self.pic_text_edit_window = ui.TextWindow()

        self.pic_h_box = QHBoxLayout()
        self.pic_h_box.addWidget(self.pic_tools_window)
        self.pic_h_box.addWidget(self.pic_label_show_window)
        self.pic_h_box.addWidget(self.pic_text_edit_window)
        self.pic_h_box.addStretch(0)

        self.vid_tools_window = ui.VidToolsWindow()
        self.vid_tools_window.setFixedWidth(220)

        self.vid_label_show_window = ui.VidWindow()
        self.vid_label_show_window.vid_show_label.setScaledContents(True)
        self.vid_label_show_window.vid_info_show_label.setScaledContents(True)

        self.plt_win = ui.HistogramWindow()

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
        self.tab_wid.addTab(self.plt_win, '直方图')
        self.tab_wid.setStyleSheet("background-color:#f0f0f0")

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.tab_wid)

        self.main_wid = QWidget()

        self.main_wid.setLayout(self.h_box)
        self.setCentralWidget(self.tab_wid)
        self.statusBar()
        # 打开图片文件
        open_pic = QAction('打开图片', self)
        # open_pic.setShortcut('Ctrl+O')
        open_pic.triggered.connect(self.show_pic)
        # 打开视频文件
        open_vid = QAction('打开视频', self)
        open_vid.triggered.connect(self.show_vid)
        # 保存图片
        save_pic = QAction('保存图片', self)
        save_pic.triggered.connect(self.pic_save)
        # 保存视频
        save_vid = QAction('保存视频', self)
        save_vid.setStatusTip('Save a video')
        # save_vid.triggered.connect(self.vid_save)

        # 清除图片
        clear_pic = QAction('清空图片', self)
        clear_pic.triggered.connect(self.clear_img)

        # 退出
        func_exit = QAction('退出', self)
        func_exit.setShortcut('Esc')
        func_exit.triggered.connect(QCoreApplication.instance().quit)

        # 添加File菜单&子菜单
        file_menubar = self.menuBar()
        file_menu = file_menubar.addMenu('文件')
        file_menu.addAction(open_pic)
        file_menu.addAction(save_pic)
        file_menu.addAction(clear_pic)
        file_menu.addAction(open_vid)
        file_menu.addAction(save_vid)
        file_menu.addAction(func_exit)

        # 图像处理菜单
        pic_menubar = self.menuBar()
        pic_menu = pic_menubar.addMenu("图像处理")
        # 显示rgb分量和直方图
        show_his_rgb = QAction('显示RGB分量', self)
        show_his_rgb.triggered.connect(self.img_to_b_g_r)
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
        about_cv_tool = QAction('关于CV Tool', self)
        about_cv_tool.triggered.connect(self.about_cv_tool)
        help_menu.addAction(document_help)
        help_menu.addAction(about_cv_tool)

        self.setWindowTitle('  CV Tools')
        self.setWindowIcon(QIcon('../res/img/logo.png'))
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.center()
        self.show()

    """ ********************************** 我是分割线 ******************************************* """
    """ ******************************* 图像处理调用函数 ***************************************** """

    def pic_save(self):
        if self.img is not None:
            pic_name = 'pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())) + '.png'
            file_name, tmp = QFileDialog.getSaveFileName(self, '保存图片', pic_name, '*.png*.jpg *.bmp')
            if file_name != '':
                cv2.imwrite(file_name, self.img)
            else:
                pass
        else:
            QMessageBox.warning(self, '警告', "当前没有图像！", QMessageBox.Ok)
            pass

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
            self.q_img = QImage(self.img.data, width_1, height_1, bytes_perline_1, QImage.Format_RGB888).rgbSwapped()

            width_1, height_1 = util.shrink_len(width_1, height_1)
            pix_map = QPixmap.fromImage(self.q_img)
            fit_pix_map = pix_map.scaled(width_1, height_1, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.pic_label_show_window.contrast_show_label.resize(width_1, height_1)
            self.pic_label_show_window.contrast_show_label.setPixmap(fit_pix_map)
        else:
            self.tmp = self.img
            self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)
            height_1, width_1, channel_1 = self.img.shape
            self.pic_label_show_window.contrast_show_label.setText('当前图像')
            bytes_perline_1 = 3 * width_1
            self.q_img = QImage(self.img.data, width_1, height_1, bytes_perline_1, QImage.Format_RGB888).rgbSwapped()

            width_1, height_1 = util.shrink_len(width_1, height_1)
            pix_map = QPixmap.fromImage(self.q_img)
            fit_pix_map = pix_map.scaled(width_1, height_1, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.pic_label_show_window.contrast_show_label.resize(width_1, height_1)
            self.pic_label_show_window.contrast_show_label.setPixmap(fit_pix_map)
            self.img = self.tmp

        plt = self.img_plt(self.img, '../res/img/plt_this.png')
        if len(plt.shape) == 2:
            plt = cv2.cvtColor(plt, cv2.COLOR_GRAY2BGR)
        height_3, width_3, channel_3 = plt.shape
        bytes_perline_3 = 3 * width_3
        self.q_img = QImage(plt.data, width_3, height_3, bytes_perline_3, QImage.Format_RGB888).rgbSwapped()

        width_3, height_3 = util.shrink_len(width_3, height_3)
        pix_map = QPixmap.fromImage(self.q_img)
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
            self.re_show_pic()

    def img_to_bin(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 255
            ui.SliderDialog.switch_flag = 1
            self.win = ui.SliderDialog()
            self.win.before_close_signal_1.connect(self.img_to_bin_signal)

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

    def img_to_contrast_brightness(self):
        if self.check_img():
            pass
        else:
            self.win = ui.DoubleSliderDialog()
            self.win.before_close_signal.connect(self.img_to_consrast_brightness_signal)

    @pyqtSlot(int, int, bool)
    def img_to_consrast_brightness_signal(self, connect_1, connect_2, flag):
        if flag:
            self.img = util.img_to_contrast_brightness(self.img, connect_1, connect_2)
            self.re_show_pic()
        else:
            pass

    def img_to_basic_roi(self):
        pass

    @pyqtSlot(int, bool)
    def img_to_basic_roi_signal(self, connect, flag):
        pass

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

    def img_to_rotate_left_any(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 360
            self.win = ui.SliderDialog()
            self.win.setWindowTitle('逆时针旋转')
            self.win.before_close_signal_1.connect(self.img_to_rotate_left_any_signal)

    @pyqtSlot(int, bool)
    def img_to_rotate_left_any_signal(self, connect, flag):
        if flag:
            self.img = util.rotate_img(self.img, -connect)
            self.re_show_pic()
        else:
            pass

    def img_to_rotate_right_any(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 360
            self.win = ui.SliderDialog()
            self.win.setWindowTitle('顺时针旋转')
            self.win.before_close_signal_1.connect(self.img_to_rotate_right_any_signal)

    @pyqtSlot(int, bool)
    def img_to_rotate_right_any_signal(self, connect, flag):
        if flag:
            self.img = util.rotate_img(self.img, connect)
            self.re_show_pic()
        else:
            pass

    def img_impulse_noise(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 1000
            ui.SliderDialog.switch_flag = 2
            self.win = ui.SliderDialog()
            self.win.threshold_slider.setMinimum(1)
            self.win.threshold_slider.setValue(10)
            self.win.before_close_signal_1.connect(self.img_impulse_noise_signal)

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
            self.win.before_close_signal_1.connect(self.img_gaussian_noise_signal)

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
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(1)
            self.win.threshold_slider.setValue(5)
            self.win.before_close_signal_1.connect(self.img_blur_filter_signal)

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
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(1)
            self.win.before_close_signal_1.connect(self.img_gaussian_filter_signal)

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
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(1)
            self.win.threshold_slider.setValue(2)
            self.win.before_close_signal_1.connect(self.img_box_filter_signal)

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
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(1)
            self.win.before_close_signal_1.connect(self.img_gaussian_filter_signal)

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
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(1)
            self.win.before_close_signal_1.connect(self.img_bilateral_filter_signal)

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
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(1)
            self.win.threshold_slider.setValue(1)
            self.win.before_close_signal_1.connect(self.img_canny_operator_signal)

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
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(1)
            self.win.before_close_signal_1.connect(self.img_sobel_operator_signal)

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
            ui.SliderDialog.threshold_max = 3
            ui.SliderDialog.switch_flag = 1
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(0)
            self.win.before_close_signal_1.connect(self.img_laplacian_operator_signal)

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

    def img_to_erode(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 21
            ui.SliderDialog.switch_flag = 1
            ui.SliderDialog.morphology_flag = True
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(3)
            self.win.before_close_signal_2.connect(self.img_to_erode_signal)

    @pyqtSlot(int, int, bool)
    def img_to_erode_signal(self, connect, morphology_val, flag):
        if flag:
            self.img = util.img_to_erode(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    def img_to_dilate(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 21
            ui.SliderDialog.switch_flag = 1
            ui.SliderDialog.morphology_flag = True
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(3)
            self.win.before_close_signal_2.connect(self.img_to_dilate_signal)

    @pyqtSlot(int, int, bool)
    def img_to_dilate_signal(self, connect, morphology_val, flag):
        if flag:
            self.img = util.img_to_dilate(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    def img_to_open_operation(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 21
            ui.SliderDialog.switch_flag = 1
            ui.SliderDialog.morphology_flag = True
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(3)
            self.win.before_close_signal_2.connect(self.img_to_open_operation_signal)

    @pyqtSlot(int, int, bool)
    def img_to_open_operation_signal(self, connect, morphology_val, flag):
        if flag:
            self.img = util.img_to_open_operation(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    def img_to_close_operation(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 21
            ui.SliderDialog.switch_flag = 1
            ui.SliderDialog.morphology_flag = True
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(3)
            self.win.before_close_signal_2.connect(self.img_to_close_operation_signal)

    @pyqtSlot(int, int, bool)
    def img_to_close_operation_signal(self, connect, morphology_val, flag):
        if flag:
            self.img = util.img_to_close_operation(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    def img_to_top_hat(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 21
            ui.SliderDialog.switch_flag = 1
            ui.SliderDialog.morphology_flag = True
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(3)
            self.win.before_close_signal_2.connect(self.img_to_top_hat_signal)

    @pyqtSlot(int, int, bool)
    def img_to_top_hat_signal(self, connect, morphology_val, flag):
        if flag:
            self.img = util.img_to_top_hat(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    def img_to_black_hat(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 21
            ui.SliderDialog.switch_flag = 1
            ui.SliderDialog.morphology_flag = True
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(3)
            self.win.before_close_signal_2.connect(self.img_to_black_hat_signal)

    @pyqtSlot(int, int, bool)
    def img_to_black_hat_signal(self, connect, morphology_val, flag):
        if flag:
            self.img = util.img_to_top_hat(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    def img_to_gradient(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 21
            ui.SliderDialog.switch_flag = 1
            ui.SliderDialog.morphology_flag = True
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            self.win.threshold_slider.setMinimum(0)
            self.win.threshold_slider.setValue(3)
            self.win.before_close_signal_2.connect(self.img_to_gradient_signal)

    @pyqtSlot(int, int, bool)
    def img_to_gradient_signal(self, connect, morphology_val, flag):
        if flag:
            self.img = util.img_to_gradient(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    def lsb_embed(self):
        text = self.pic_text_edit_window.embed_text.toPlainText()
        if self.check_img():
            pass
        else:
            if (text is not None) and (self.img is not None):
                self.img = util.lsb_embed(self.img, str(text))
                pic_name = '../res/embed_img/pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
                cv2.imwrite(pic_name + '.bmp', self.img)
                filename = pic_name + '.txt'
                with open(filename, 'w') as f:
                    f.write(str(len(text) * 8))
                self.re_show_pic()

    def lsb_extract(self):
        if self.check_img():
            pass
        else:
            file_name, tmp = QFileDialog.getOpenFileName(self, '打开文本', 'embed_info', '*.txt')
            if not os.path.exists(file_name):
                QMessageBox.warning(self, '警告', "没有打开嵌入信息文本！", QMessageBox.Ok)
                pass
            else:
                with open(file_name) as f:
                    num = f.read()
                self.pic_text_edit_window.extract_text.setText(util.lsb_extract(self.img, int(num)))

    def check_img(self):
        if self.img is not None:
            return False
        else:
            QMessageBox.warning(self, '警告', "当前没有打开\n任何图像！", QMessageBox.Ok)
            return True

    def img_to_b_g_r(self):
        if self.check_img():
            pass
        else:
            if len(self.img.shape) == 3:
                img_b, img_g, img_r = util.img_to_b_g_r(self.img)
                img_plt = self.img_plt(self.img, '../res/img/plt_this.png')
                img_b_plt = self.img_plt(img_b, '../res/img/img_b_plt.png')
                img_g_plt = self.img_plt(img_g, '../res/img/img_g_plt.png')
                img_r_plt = self.img_plt(img_r, '../res/img/img_r_plt.png')
                img_list = [self.img, img_plt, img_b, img_b_plt, img_g, img_g_plt, img_r, img_r_plt]
                label_list = [self.plt_win.label_show_this_rgb, self.plt_win.his_show_label_this_rgb,
                              self.plt_win.label_show_this_b, self.plt_win.his_show_label_this_b,
                              self.plt_win.label_show_this_g, self.plt_win.his_show_label_this_g,
                              self.plt_win.label_show_this_r, self.plt_win.his_show_label_this_r]
                for i in range(len(img_list)):
                    self.show_label(label_list[i], img_list[i])
                self.tab_wid.setCurrentIndex(2)
            else:
                QMessageBox.warning(self, '警告', "当前图像位灰度图！", QMessageBox.Ok)
                pass

    def show_label(self, label, pic):
        if len(pic.shape) == 2:
            pic = cv2.cvtColor(pic, cv2.COLOR_GRAY2BGR)
        height, width, channel = pic.shape
        bytes_perline = 3 * width
        self.q_img = QImage(pic.data, width, height, bytes_perline, QImage.Format_RGB888).rgbSwapped()
        width, height = util.shrink_len_his(width, height)
        pix_map = QPixmap.fromImage(self.q_img)
        fit_pix_map = pix_map.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        label.resize(width, height)
        label.setPixmap(fit_pix_map)

    def clear_img(self):
        self.last_pic, self.last_pic_backup, self.g_pic, self.img = None, None, None, None
        self.pic_label_show_window.pic_show_label.setPixmap(QPixmap(""))
        self.pic_label_show_window.contrast_show_label.setPixmap(QPixmap(""))
        self.pic_label_show_window.his_show_label_last.setPixmap(QPixmap(""))
        self.pic_label_show_window.his_show_label_this.setPixmap(QPixmap(""))

    def img_plt(self, pic, path):
        if len(pic.shape) == 3:
            util.img_plt_rgb(pic, path)
        else:
            util.img_plt_gray(pic, path)
        plt = cv2.imread(path)
        return plt

    """ ********************************** 我是分割线 ******************************************* """
    """ ******************************* 视频处理调用函数 ***************************************** """

    def show_vid(self):
        # 调用存储文件
        file_name, tmp = QFileDialog.getOpenFileName(self, '打开视频', 'video', '*.mp4')
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
            height, width, channel = frame.shape
            bytes_perline = 3 * width
            self.q_img = QImage(frame.data, width, height, bytes_perline, QImage.Format_RGB888).rgbSwapped()
            self.vid_label_show_window.vid_show_label.setPixmap(QPixmap.fromImage(self.q_img))
            if cv2.waitKey(40) & 0xFF == ord('q'):
                break
        self.vid_reader.release()
        cv2.destroyAllWindows()

    def check_vid(self):
        if self.vid.isOpened() and self.vid is not None:
            return False
        else:
            QMessageBox.warning(self, '警告', "当前没有打开\n任何视频！", QMessageBox.Ok)
            return True

    """ ********************************** 我是分割线 ******************************************* """

    def document_link(self):
        util.document_link()

    def about_cv_tool(self):
        QMessageBox.about(self, ' 关于CV Tool', '当前版本：0.5.1.b4\n开源协议：木兰宽松许可证\n作者：Taoidle')

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', "是否退出当前程序?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    util.check_dir('../res/embed_img/')
    util.check_dir('../res/img/')
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
