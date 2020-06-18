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
import requests
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout,
                             QAction, QFileDialog, QApplication, QMessageBox, QTabWidget, QDesktopWidget, QMenu)
from PyQt5.QtGui import QIcon, QImage, QPixmap
import json, os, cv2, util, sys, ui, time


class MainWindow(QMainWindow, QWidget):
    last_pic, last_pic_backup, g_pic, img = None, None, None, None
    vid_flag, vid_check_open = False, False
    vid_start_fps = 0
    default_jpeg_quality = 80
    default_png_quality = 3
    default_webp_quality = 80

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_setting()

    def init_ui(self):
        # 图像处理窗口初始化
        # 初始化图像窗口工具栏
        self.pic_tools_window = ui.PicToolsWindow()
        # 设置工具栏大小固定
        self.pic_tools_window.setFixedWidth(220)
        # 给各个工具绑定触发事件
        self.pic_tools_window.box_1_button_1.clicked.connect(self.review_origin_pic)
        self.pic_tools_window.box_1_button_2.clicked.connect(self.review_last_pic)
        self.pic_tools_window.box_1_button_3.clicked.connect(self.img_to_gray)
        self.pic_tools_window.box_1_button_4.clicked.connect(self.img_to_inverse)
        self.pic_tools_window.box_1_button_5.clicked.connect(self.img_to_bin)
        self.pic_tools_window.box_1_button_6.clicked.connect(self.img_to_auto_bin)
        self.pic_tools_window.box_1_button_7.clicked.connect(self.img_to_contrast_brightness)
        self.pic_tools_window.box_1_button_8.clicked.connect(self.img_to_overlay)
        self.pic_tools_window.box_1_button_9.clicked.connect(self.img_to_extract_rgb)
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
        self.pic_tools_window.box_5_button_5.clicked.connect(self.img_houghlines)
        self.pic_tools_window.box_5_button_6.clicked.connect(self.img_houghlines_p)
        self.pic_tools_window.box_5_button_7.clicked.connect(self.img_houghcircles)
        self.pic_tools_window.box_5_button_8.clicked.connect(self.img_dct_basic)
        self.pic_tools_window.box_6_button_1.clicked.connect(self.img_to_erode)
        self.pic_tools_window.box_6_button_2.clicked.connect(self.img_to_dilate)
        self.pic_tools_window.box_6_button_3.clicked.connect(self.img_to_open_operation)
        self.pic_tools_window.box_6_button_4.clicked.connect(self.img_to_close_operation)
        self.pic_tools_window.box_6_button_5.clicked.connect(self.img_to_top_hat)
        self.pic_tools_window.box_6_button_6.clicked.connect(self.img_to_black_hat)
        self.pic_tools_window.box_6_button_7.clicked.connect(self.img_to_gradient)
        self.pic_tools_window.box_7_button_1.clicked.connect(self.img_to_pyrup)
        self.pic_tools_window.box_7_button_2.clicked.connect(self.img_to_pyrdown)
        self.pic_tools_window.box_7_button_3.clicked.connect(self.imt_to_pyr_laplace)
        self.pic_tools_window.box_8_button_1.clicked.connect(self.lsb_embed)
        self.pic_tools_window.box_8_button_2.clicked.connect(self.dct_embed)
        self.pic_tools_window.box_9_button_1.clicked.connect(self.lsb_extract)
        self.pic_tools_window.box_9_button_2.clicked.connect(self.dct_extract)

        # 初始化图像存放窗口
        self.pic_label_show_window = ui.PicWindow()
        # 设置Label自适应
        self.pic_label_show_window.pic_show_label.setScaledContents(True)
        self.pic_label_show_window.contrast_show_label.setScaledContents(True)
        self.pic_label_show_window.his_show_label_this.setScaledContents(True)
        # 初始化文本窗口
        self.pic_text_edit_window = ui.TextWindow()
        # 添加图像窗口布局
        self.pic_h_box = QHBoxLayout()
        self.pic_h_box.addWidget(self.pic_tools_window)
        self.pic_h_box.addWidget(self.pic_label_show_window)
        self.pic_h_box.addWidget(self.pic_text_edit_window)
        self.pic_h_box.addStretch(0)
        # 添加布局到窗口
        self.wid_1_get = QWidget()
        self.wid_1_get.setLayout(self.pic_h_box)

        # 初始化直方图窗口
        self.plt_win = ui.HistogramWindow()

        # 初始化一个Tab窗口
        self.tab_wid = QTabWidget()
        # 将上面窗口添加到Tab窗口中
        self.tab_wid.addTab(self.wid_1_get, '图像处理')
        # self.tab_wid.addTab(self.wid_2_get, '视频处理')
        self.tab_wid.addTab(self.plt_win, '直方图')
        self.tab_wid.setStyleSheet("background-color:#f0f0f0")
        # 初始化一个水平布局
        self.h_box = QHBoxLayout()
        # 将Tab窗口添加到布局中
        self.h_box.addWidget(self.tab_wid)
        # 添加当前窗口布局
        self.setLayout(self.h_box)
        self.setCentralWidget(self.tab_wid)
        # 初始化工具栏
        self.statusBar()
        # 打开图片文件
        open_pic = QAction('打开图片', self)
        # open_pic.setShortcut('Ctrl+O')
        open_pic.triggered.connect(self.show_pic)
        # 保存图片
        save_pic = QAction('保存图片', self)
        save_pic.triggered.connect(self.pic_save)

        # 清除图片
        clear_pic = QAction('清空图片', self)
        clear_pic.triggered.connect(self.clear_img)

        # 设置
        program_setting = QAction('设置', self)
        program_setting.triggered.connect(self.settings)

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
        file_menu.addAction(program_setting)
        file_menu.addAction(func_exit)

        # 图像处理菜单
        pic_menubar = self.menuBar()
        pic_menu = pic_menubar.addMenu("图像处理")

        # 当前图片计算
        cal_now_menu = QMenu('当前图像计算', self)
        # 计算MSE
        cal_now_mse = QAction('计算MSE', self)
        cal_now_mse.triggered.connect(self.show_now_mse)
        # 计算PSNR
        cal_now_psnr = QAction('计算PSNR', self)
        cal_now_psnr.triggered.connect(self.show_now_psnr)
        # 计算SSIM
        cal_now_ssim = QAction('计算SSIM', self)
        cal_now_ssim.triggered.connect(self.show_now_ssim)
        cal_now_menu.addAction(cal_now_mse)
        cal_now_menu.addAction(cal_now_psnr)
        cal_now_menu.addAction(cal_now_ssim)

        # 外部图片计算
        cal_import_menu = QMenu('外部图像计算', self)
        # 计算MSE
        cal_import_mse = QAction('计算MSE', self)
        cal_import_mse.setStatusTip('先导入原图再导入效果图')
        cal_import_mse.triggered.connect(self.show_import_mse)
        # 计算PSNR
        cal_import_psnr = QAction('计算PSNR', self)
        cal_import_psnr.setStatusTip('先导入原图再导入效果图')
        cal_import_psnr.triggered.connect(self.show_import_psnr)
        # 计算SSIM
        cal_import_ssim = QAction('计算SSIM', self)
        cal_import_ssim.setStatusTip('先导入原图再导入效果图')
        cal_import_ssim.triggered.connect(self.show_import_ssim)
        cal_import_menu.addAction(cal_import_mse)
        cal_import_menu.addAction(cal_import_psnr)
        cal_import_menu.addAction(cal_import_ssim)

        # 显示rgb分量和直方图
        show_his_rgb = QAction('显示RGB分量', self)
        show_his_rgb.triggered.connect(self.img_to_b_g_r)
        pic_menu.addMenu(cal_now_menu)
        pic_menu.addMenu(cal_import_menu)
        pic_menu.addAction(show_his_rgb)

        # 百度OCR文字提取
        baidu_ocr_words = QAction('百度OCR文字提取 ', self)
        baidu_ocr_words.triggered.connect(self.baidu_ocr_get_words)
        pic_menu.addAction(baidu_ocr_words)

        # 添加Help菜单&子菜单
        help_menubar = self.menuBar()
        help_menu = help_menubar.addMenu("帮助")
        document_introduce = QAction('介绍', self)
        document_introduce.triggered.connect(self.document_introduce_link)
        document_help = QAction('帮助文档', self)
        document_help.triggered.connect(self.document_help_link)
        about_cv_tool = QAction('关于CV Tool', self)
        about_cv_tool.triggered.connect(self.about_cv_tool)
        help_menu.addAction(document_introduce)
        help_menu.addAction(document_help)
        help_menu.addAction(about_cv_tool)

        # 设置窗口标题
        self.setWindowTitle('  CV Tools')
        self.setWindowIcon(QIcon('res/img/logo.png'))
        # 设置窗口只有最小化和关闭
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.center()
        self.show()

    def init_setting(self):
        json_path = './settings.json'
        if not os.path.exists(json_path):
            os.system(r'touch %s' % json_path)
            json_dict = {"jpg_quality": "80", "png_quality": "3", "webp_quality": "80", "DCT_Block": "8",
                         "Baidu_Api": {"APP_ID": "",
                                       "API_KEY": "",
                                       "SECRET_KEY": "",
                                       "WORDS_MODEL": "1"}
                         }
            with open("./settings.json", "w", encoding='utf-8') as f:
                f.write(json.dumps(json_dict, ensure_ascii=False))
            f.close()

    """ ********************************** 我是分割线 ******************************************* """
    """ ******************************* 图像处理调用函数 ***************************************** """

    # 图像保存
    def pic_save(self):
        if self.img is not None:
            self.get_settings()
            pic_name = 'pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())) + '.png'
            file_name, tmp = QFileDialog.getSaveFileName(self, '保存图片', pic_name, '*.png *.jpg *.bmp *.webp')
            if file_name != '':
                if file_name.endswith('.jpg'):
                    cv2.imwrite(file_name, self.img, [int(cv2.IMWRITE_JPEG_QUALITY), self.default_jpeg_quality])
                elif file_name.endswith('.png'):
                    cv2.imwrite(file_name, self.img, [int(cv2.IMWRITE_PNG_COMPRESSION), self.default_png_quality])
                elif file_name.endswith('.webp'):
                    cv2.imwrite(file_name, self.img, [int(cv2.IMWRITE_WEBP_QUALITY), self.default_webp_quality])
                else:
                    cv2.imwrite(file_name, self.img)
            else:
                pass
        else:
            QMessageBox.warning(self, '警告', "当前没有图像！", QMessageBox.Ok)
            pass

    # 读取设置
    def get_settings(self):
        with open('./settings.json', 'r', encoding='utf-8') as fr:
            json_data = json.load(fr)
            self.default_jpeg_quality = int(json_data["jpg_quality"])
            self.default_png_quality = int(json_data["png_quality"])
            self.default_webp_quality = int(json_data["webp_quality"])
        fr.close()

    # 显示图像
    def show_pic(self):
        # 调用存储文件
        file_name, tmp = QFileDialog.getOpenFileName(self, '打开图片', 'picture', '*.png *.jpg *.bmp *.jpeg *tif')
        if file_name == '':
            return
        # 采用OpenCV函数读取数据
        self.img = cv2.imread(file_name, -1)
        if self.img.size == 1:
            return
        self.g_pic = cv2.imread(file_name, -1)
        self.re_show_pic()

    # 转化图像并显示到Label中
    def re_show_pic(self):
        # 判断图像类型
        if len(self.img.shape) == 3:
            # 提取图像的通道和尺寸，用于将OpenCV下的image转换成QImage
            height_1, width_1, channel_1 = self.img.shape
            self.pic_label_show_window.contrast_show_label.setText('当前图像')
            bytes_perline_1 = 3 * width_1
            # 对cv图像进行转换
            self.q_img = QImage(self.img.data, width_1, height_1, bytes_perline_1, QImage.Format_RGB888).rgbSwapped()
            # 对显示的图像宽高进行缩小
            width_1, height_1 = util.shrink_len(width_1, height_1)
            pix_map = QPixmap.fromImage(self.q_img)
            # 设置图像维持原来比例
            fit_pix_map = pix_map.scaled(width_1, height_1, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            # 重置Label大小
            self.pic_label_show_window.contrast_show_label.resize(width_1, height_1)
            self.pic_label_show_window.contrast_show_label.setPixmap(fit_pix_map)
        else:
            # 将当前图像存放进临时图像
            self.tmp = self.img
            # 将当前图像转换位BGR图像
            self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)
            height_1, width_1, channel_1 = self.img.shape
            self.pic_label_show_window.contrast_show_label.setText('当前图像')
            bytes_perline_1 = 3 * width_1
            # 对cv图像进行转换
            self.q_img = QImage(self.img.data, width_1, height_1, bytes_perline_1, QImage.Format_RGB888).rgbSwapped()
            # 对显示的图像宽高进行缩小
            width_1, height_1 = util.shrink_len(width_1, height_1)
            pix_map = QPixmap.fromImage(self.q_img)
            # 设置图像维持原图比例
            fit_pix_map = pix_map.scaled(width_1, height_1, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            # 重置Label大小
            self.pic_label_show_window.contrast_show_label.resize(width_1, height_1)
            self.pic_label_show_window.contrast_show_label.setPixmap(fit_pix_map)
            # 显示完成后将图像从临时图像中取回
            self.img = self.tmp

        # 设置直方图
        plt = self.img_plt(self.img, 'res/img/plt_this.png')
        # 判断图像类型
        if len(plt.shape) == 2:
            plt = cv2.cvtColor(plt, cv2.COLOR_GRAY2BGR)
        height_3, width_3, channel_3 = plt.shape
        bytes_perline_3 = 3 * width_3
        # 对cv图像进行转换
        self.q_img = QImage(plt.data, width_3, height_3, bytes_perline_3, QImage.Format_RGB888).rgbSwapped()
        # 对显示的图像宽高进行缩小
        width_3, height_3 = util.shrink_len(width_3, height_3)
        pix_map = QPixmap.fromImage(self.q_img)
        # 设置图像维持原图比例
        fit_pix_map = pix_map.scaled(width_3, height_3, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.pic_label_show_window.his_show_label_this.resize(width_3, height_3)
        self.pic_label_show_window.his_show_label_this.setPixmap(fit_pix_map)

        # 设置上一次图像
        if self.last_pic is not None:
            # 判断图像类型
            if len(self.last_pic.shape) == 3:
                height_2, width_2, channel_2 = self.last_pic.shape
                self.pic_label_show_window.pic_label.setText('上一步图像')
                bytes_perline_2 = 3 * width_2
                self.q_img_2 = QImage(self.last_pic.data, width_2, height_2, bytes_perline_2,
                                      QImage.Format_RGB888).rgbSwapped()
                # 对显示的图像宽高进行缩小
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
                # 对显示的图像宽高进行缩小
                width_2, height_2 = util.shrink_len(width_2, height_2)
                pix_map = QPixmap.fromImage(self.q_img_2)
                fit_pix_map = pix_map.scaled(width_2, height_2, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                self.pic_label_show_window.pic_show_label.resize(width_2, height_2)
                self.pic_label_show_window.pic_show_label.setPixmap(fit_pix_map)
                self.last_pic = self.tmp
            # 显示直方图
            plt = self.img_plt(self.last_pic, 'res/img/plt_last.png')
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

    # 恢复原图
    def review_origin_pic(self):
        if self.check_img():
            pass
        else:
            self.img = self.g_pic
            self.re_show_pic()

    # 显示上一步图像
    def review_last_pic(self):
        if self.check_img() or (self.last_pic_backup is None):
            pass
        else:
            self.img = self.last_pic_backup
            self.re_show_pic()

    # 图像灰度化
    def img_to_gray(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_gray(self.img)
            self.re_show_pic()

    # 图像反相
    def img_to_inverse(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_inverse(self.img)
            self.re_show_pic()


    # 图像二值化
    def img_to_bin(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 255
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 初始化窗口
            self.win = ui.SliderDialog()
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_to_bin_signal)

    # 图像二值化信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_to_bin_signal(self, connect, flag, cancel):
        if flag and cancel:
            ret, binary = cv2.threshold(util.img_to_gray(self.img), connect, 255, cv2.THRESH_BINARY)
            self.img = binary
            self.re_show_pic()
        else:
            pass

    # 图像自动二值化
    def img_to_auto_bin(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_auto_bin(self.img)
            self.re_show_pic()

    # 亮度对比度调节
    def img_to_contrast_brightness(self):
        if self.check_img():
            pass
        else:
            # 初始化窗口
            self.win = ui.DoubleSliderDialog()
            # 连接信号槽
            self.win.before_close_signal.connect(self.img_to_consrast_brightness_signal)

    # 信号槽函数
    @pyqtSlot(int, int, bool, bool)
    def img_to_consrast_brightness_signal(self, connect_1, connect_2, flag, cancel):
        if flag and cancel:
            self.img = util.img_to_contrast_brightness(self.img, connect_1, connect_2)
            self.re_show_pic()
        else:
            pass

    # 图像初级混合
    def img_to_overlay(self):
        if self.check_img() or (self.last_pic is None):
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 1000
            # 设置标志位
            ui.SliderDialog.switch_flag = 2
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.setWindowTitle('图像权重')
            # 设置最小值
            self.win.threshold_slider.setMinimum(0)
            # 设置默认值
            self.win.threshold_slider.setValue(500)
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_to_overlay_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_to_overlay_signal(self, connect, flag, cancel):
        if flag and cancel and self.img.shape[0] == self.last_pic_backup.shape[0] and self.img.shape[1] == \
                self.last_pic_backup.shape[1]:
            self.img = util.img_to_overlay(self.img, self.last_pic_backup, connect / 1000)
            self.re_show_pic()
        else:
            pass

    # rgb分量提取
    def img_to_extract_rgb(self):
        if self.check_img():
            pass
        else:
            # 初始化窗口
            self.win = ui.RadioWindow()
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_to_extract_rgb_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_to_extract_rgb_signal(self, connect, flag, cancel):
        if flag and cancel:
            if len(self.img.shape) == 3:
                self.img = util.img_to_extract_rgb(self.img, connect)
                self.re_show_pic()
            else:
                QMessageBox.warning(self, '警告', '当前图像不是rgb图像！')
        else:
            pass

    # 图像水平镜像
    def img_to_horizontal(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_horizontal(self.img)
            self.re_show_pic()

    # 图像垂直镜像
    def img_to_vertical(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_vertical(self.img)
            self.re_show_pic()

    # 逆时针旋转90度
    def img_to_rotate_left(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_rotate_left(self.img)
            self.re_show_pic()

    # 顺时针旋转90度
    def img_to_rotate_right(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_rotate_right(self.img)
            self.re_show_pic()

    # 逆时针旋转任意角
    def img_to_rotate_left_any(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 360
            self.win = ui.SliderDialog()
            self.win.setWindowTitle('逆时针旋转')
            self.win.before_close_signal_1.connect(self.img_to_rotate_left_any_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_to_rotate_left_any_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.rotate_img(self.img, -connect)
            self.re_show_pic()
        else:
            pass

    # 顺时针旋转任意角度
    def img_to_rotate_right_any(self):
        if self.check_img():
            pass
        else:
            ui.SliderDialog.threshold_max = 360
            self.win = ui.SliderDialog()
            self.win.setWindowTitle('顺时针旋转')
            self.win.before_close_signal_1.connect(self.img_to_rotate_right_any_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_to_rotate_right_any_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.rotate_img(self.img, connect)
            self.re_show_pic()
        else:
            pass

    # 椒盐噪声
    def img_impulse_noise(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 1000
            # 设置标志位
            ui.SliderDialog.switch_flag = 2
            # 初始化窗口
            self.win = ui.SliderDialog()
            # 设置最小值
            self.win.threshold_slider.setMinimum(1)
            # 设置默认值
            self.win.threshold_slider.setValue(10)
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_impulse_noise_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_impulse_noise_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.img_impulse_noise(self.img, connect / 1000)
            self.re_show_pic()
        else:
            pass

    # 高斯噪声
    def img_gaussian_noise(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 1000
            # 设置标志位
            ui.SliderDialog.switch_flag = 2
            # 初始化窗口
            self.win = ui.SliderDialog()
            # 设置最小值
            self.win.threshold_slider.setMinimum(1)
            # 设置初始值
            self.win.threshold_slider.setValue(10)
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_gaussian_noise_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_gaussian_noise_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.img_gaussian_noise(self.img, 0, connect / 1000)
            self.re_show_pic()
        else:
            pass

    # 均值滤波
    def img_blur_filter(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 50
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(1)
            # 设置默认值
            self.win.threshold_slider.setValue(5)
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_blur_filter_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_blur_filter_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.img_blur_filter(self.img, connect)
            self.re_show_pic()
        else:
            pass

    # 中值滤波
    def img_median_filter(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 50
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(0)
            # 设置初始值
            self.win.threshold_slider.setValue(1)
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_gaussian_filter_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_median_filter_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.img_median_filter(self.img, connect)
            self.re_show_pic()
        else:
            pass

    # 方框滤波
    def img_box_filter(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 50
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(1)
            # 设置默认值
            self.win.threshold_slider.setValue(2)
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_box_filter_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_box_filter_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.img_box_filter(self.img, connect, val=False)
            self.re_show_pic()
        else:
            pass

    # 高斯滤波
    def img_gaussian_filter(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 50
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(0)
            # 设置默认值
            self.win.threshold_slider.setValue(1)
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_gaussian_filter_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_gaussian_filter_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.img_gaussian_filter(self.img, connect)
            self.re_show_pic()
        else:
            pass

    # 双边滤波
    def img_bilateral_filter(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 50
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(0)
            # 设置初始值
            self.win.threshold_slider.setValue(1)
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_bilateral_filter_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_bilateral_filter_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.img_bilateral_filter(self.img, connect)
            self.re_show_pic()
        else:
            pass

    # Canny算子
    def img_canny_operator(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 120
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(1)
            # 设置初始值
            self.win.threshold_slider.setValue(50)
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_canny_operator_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_canny_operator_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.img_canny_operator(self.img, connect)
            self.re_show_pic()
        else:
            pass

    # Sobel算子
    def img_sobel_operator(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 120
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(0)
            # 设置初始值
            self.win.threshold_slider.setValue(1)
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_sobel_operator_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_sobel_operator_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.img_canny_operator(self.img, connect)
            self.re_show_pic()
        else:
            pass

    # Laplace算子
    def img_laplacian_operator(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 3
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(0)
            # 设置初始值
            self.win.threshold_slider.setValue(0)
            # 连接信号槽
            self.win.before_close_signal_1.connect(self.img_laplacian_operator_signal)

    # 信号槽函数
    @pyqtSlot(int, bool, bool)
    def img_laplacian_operator_signal(self, connect, flag, cancel):
        if flag and cancel:
            self.img = util.img_laplacian_operator(self.img, connect)
            self.re_show_pic()
        else:
            pass

    # Scharr滤波器
    def img_scharr_operator(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_scharr_operator(self.img)
            self.re_show_pic()

    # 标准霍夫变换
    def img_houghlines(self):
        if self.check_img():
            pass
        else:
            self.win = ui.ThreeSliderDialog()
            self.win.before_close_signal.connect(self.img_houghlines_signal)

    # 信号槽函数
    @pyqtSlot(int, int, int, bool, bool)
    def img_houghlines_signal(self, connect_1, connect_2, connect_3, flag, cancel):
        if flag and cancel:
            if len(self.img.shape) == 2:
                self.img = util.img_houghlines(self.img, self.g_pic, connect_1, connect_2, connect_3)
                self.re_show_pic()
            else:
                QMessageBox.warning(self, '警告', '该图像不能进行霍夫变换！')
        else:
            pass

    # 累计霍夫变换
    def img_houghlines_p(self):
        if self.check_img():
            pass
        else:
            self.win = ui.ThreeSliderDialog()
            self.win.before_close_signal.connect(self.img_houghlines_p_signal)

    # 信号槽函数
    @pyqtSlot(int, int, int, bool, bool)
    def img_houghlines_p_signal(self, connect_1, connect_2, connect_3, flag, cancel):
        if flag and cancel:
            if len(self.img.shape) == 2:
                self.img = util.img_houghlines_p(self.img, self.g_pic, connect_1, connect_2, connect_3)
                self.re_show_pic()
            else:
                QMessageBox.warning(self, '警告', '该图像不能进行霍夫变换！')
        else:
            pass

    # 霍夫圆变换
    def img_houghcircles(self):
        if self.check_img():
            pass
        else:
            self.win = ui.ThreeSliderDialog()
            self.win.before_close_signal.connect(self.img_houghcircles_signal)

    # 信号槽函数
    @pyqtSlot(int, int, int, bool, bool)
    def img_houghcircles_signal(self, connect_1, connect_2, connect_3, flag, cancel):
        if flag and cancel:
            if len(self.img.shape) == 2:
                self.img = util.img_houghcircles(self.img, self.g_pic,)
                self.re_show_pic()
            else:
                QMessageBox.warning(self, '警告', '该图像不能进行霍夫变换！')
        else:
            pass

    # DCT变换
    def img_dct_basic(self):
        if self.check_img():
            pass
        else:
            height = self.img.shape[0]
            width = self.img.shape[1]
            ui.FourSliderWindow.threshold_max_1 = width
            ui.FourSliderWindow.threshold_max_2 = width
            ui.FourSliderWindow.threshold_max_3 = height
            ui.FourSliderWindow.threshold_max_4 = height
            self.win = ui.FourSliderWindow()
            self.win.before_close_signal_1.connect(self.img_dct_basic_signal)

    # 信号槽函数
    @pyqtSlot(int, int, int, int, bool, bool)
    def img_dct_basic_signal(self, connect_1, connect_2, connect_3, connect_4, flag, cancel):
        if flag and cancel:
            self.img = util.img_dct_basic(self.img, connect_1, connect_2, connect_3, connect_4)
            self.re_show_pic()
        else:
            pass

    # 膨胀
    def img_to_erode(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 21
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 设置形态学标志
            ui.SliderDialog.morphology_flag = True
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(0)
            # 设置初始值
            self.win.threshold_slider.setValue(3)
            # 连接信号槽
            self.win.before_close_signal_2.connect(self.img_to_erode_signal)

    # 信号槽函数
    @pyqtSlot(int, int, bool, bool)
    def img_to_erode_signal(self, connect, morphology_val, flag, cancel):
        if flag and cancel:
            self.img = util.img_to_erode(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    # 腐蚀
    def img_to_dilate(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 21
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 设置形态学标志
            ui.SliderDialog.morphology_flag = True
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(0)
            # 设置初始值
            self.win.threshold_slider.setValue(3)
            # 连接信号槽
            self.win.before_close_signal_2.connect(self.img_to_dilate_signal)

    # 信号槽函数
    @pyqtSlot(int, int, bool, bool)
    def img_to_dilate_signal(self, connect, morphology_val, flag, cancel):
        if flag and cancel:
            self.img = util.img_to_dilate(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    # 开运算
    def img_to_open_operation(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 21
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 设置形态学标志
            ui.SliderDialog.morphology_flag = True
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(0)
            # 设置初始值
            self.win.threshold_slider.setValue(3)
            # 连接信号槽
            self.win.before_close_signal_2.connect(self.img_to_open_operation_signal)

    # 信号槽函数
    @pyqtSlot(int, int, bool, bool)
    def img_to_open_operation_signal(self, connect, morphology_val, flag, cancel):
        if flag and cancel:
            self.img = util.img_to_open_operation(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    # 闭运算
    def img_to_close_operation(self):
        if self.check_img():
            pass
        else:
            # 设置阈值
            ui.SliderDialog.threshold_max = 21
            # 设置标志位
            ui.SliderDialog.switch_flag = 1
            # 设置形态学标志
            ui.SliderDialog.morphology_flag = True
            # 初始化窗口
            self.win = ui.SliderDialog()
            self.win.label_tip.setText('内核大小:')
            # 设置最小值
            self.win.threshold_slider.setMinimum(0)
            # 设置初始值
            self.win.threshold_slider.setValue(3)
            # 连接信号槽
            self.win.before_close_signal_2.connect(self.img_to_close_operation_signal)

    # 信号槽函数
    @pyqtSlot(int, int, bool, bool)
    def img_to_close_operation_signal(self, connect, morphology_val, flag, cancel):
        if flag and cancel:
            self.img = util.img_to_close_operation(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    # 顶帽
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

    # 信号槽函数
    @pyqtSlot(int, int, bool, bool)
    def img_to_top_hat_signal(self, connect, morphology_val, flag, cancel):
        if flag and cancel:
            self.img = util.img_to_top_hat(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    # 黑帽
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

    # 信号槽函数
    @pyqtSlot(int, int, bool, bool)
    def img_to_black_hat_signal(self, connect, morphology_val, flag, cancel):
        if flag and cancel:
            self.img = util.img_to_top_hat(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    # 形态学梯度
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

    # 信号槽函数
    @pyqtSlot(int, int, bool, bool)
    def img_to_gradient_signal(self, connect, morphology_val, flag, cancel):
        if flag and cancel:
            self.img = util.img_to_gradient(self.img, connect, util.morphology_shape(morphology_val))
            self.re_show_pic()
        else:
            pass

    # 向上采样
    def img_to_pyrup(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_pyrup(self.img)
            self.re_show_pic()

    # 向下采样
    def img_to_pyrdown(self):
        if self.check_img():
            pass
        else:
            self.img = util.img_to_pyrdown(self.img)
            self.re_show_pic()

    def imt_to_pyr_laplace(self):
        if self.check_img():
            pass
        else:
            self.img = util.imt_to_pyr_laplace(self.img)
            self.re_show_pic()

    # lsb嵌入
    def lsb_embed(self):
        text = self.pic_text_edit_window.embed_text.toPlainText()
        if self.check_img():
            pass
        else:
            if (text is not None) and (self.img is not None):
                self.img = util.lsb_embed(self.img, str(text))
                pic_name = './res/embed_img/pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
                cv2.imwrite(pic_name + '.bmp', self.img)
                filename = pic_name + '.txt'
                with open(filename, 'w') as f:
                    f.write(str(len(util.encode(text))))
                f.close()
                self.re_show_pic()

    # lsb提取
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
                f.close()
                self.pic_text_edit_window.extract_text.setText(util.lsb_extract(self.img, int(num)))

    # dct嵌入
    def dct_embed(self):
        text = self.pic_text_edit_window.embed_text.toPlainText()
        if self.check_img():
            pass
        else:
            if (text is not None) and (self.img is not None):
                self.img = util.dct_embed(self.img, str(text))
                pic_name = './res/embed_img/pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
                cv2.imwrite(pic_name + '.bmp', self.img)
                filename = pic_name + '.txt'
                with open(filename, 'w') as f:
                    f.write(str(len(util.encode(text))))
                f.close()
                self.re_show_pic()

    # dct提取
    def dct_extract(self):
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
                f.close()
                self.pic_text_edit_window.extract_text.setText(util.dct_extract(self.img, int(num)))

    # 图像检查
    def check_img(self):
        if self.img is not None:
            return False
        else:
            QMessageBox.warning(self, '警告', "当前没有打开\n任何图像！", QMessageBox.Ok)
            return True

    # 计算MSE
    def show_now_mse(self):
        if self.check_img():
            pass
        else:
            mse = util.get_mse(self.g_pic, self.img)
            self.pic_text_edit_window.mse_label_text.setText(str(mse))

    # 计算PSNR
    def show_now_psnr(self):
        if self.check_img():
            pass
        else:
            psnr = util.get_psnr(self.g_pic, self.img)
            self.pic_text_edit_window.psnr_label_text.setText(str(psnr))

    # 计算SSIM
    def show_now_ssim(self):
        if self.check_img():
            pass
        else:
            ssim = util.get_ssim(self.g_pic, self.img)
            self.pic_text_edit_window.ssim_label_text.setText(str(ssim))

    # 计算MSE
    def show_import_mse(self):
        if self.check_img():
            pass
        else:
            mse = util.get_mse(self.last_pic_backup, self.img)
            self.pic_text_edit_window.mse_label_text.setText(str(mse))

    # 计算PSNR
    def show_import_psnr(self):
        if self.check_img():
            pass
        else:
            psnr = util.get_psnr(self.last_pic_backup, self.img)
            self.pic_text_edit_window.psnr_label_text.setText(str(psnr))

    # 计算SSIM
    def show_import_ssim(self):
        if self.check_img():
            pass
        else:
            ssim = util.get_ssim(self.last_pic_backup, self.img)
            self.pic_text_edit_window.ssim_label_text.setText(str(ssim))

    # 图像分量提取
    def img_to_b_g_r(self):
        if self.check_img():
            pass
        else:
            if len(self.img.shape) == 3:
                img_b, img_g, img_r = util.img_to_b_g_r(self.img)
                img_plt = self.img_plt(self.img, 'res/img/plt_this.png')
                img_b_plt = self.img_plt(img_b, 'res/img/img_b_plt.png')
                img_g_plt = self.img_plt(img_g, 'res/img/img_g_plt.png')
                img_r_plt = self.img_plt(img_r, 'res/img/img_r_plt.png')
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

    # 百度OCR文字提取
    def baidu_ocr_get_words(self):
        self.win = ui.OcrWordsWindow()
        self.win.before_close_signal_1.connect(self.baidu_ocr_get_words_signal)

    @pyqtSlot(str, bool, bool)
    def baidu_ocr_get_words_signal(self, path, flag, cancel):
        if flag and cancel:
            words = util.baidu_ocr_words(path)
            self.pic_text_edit_window.extract_text.setText(words)
            if path.startswith('http'):
                (filepath, tempfilename) = os.path.split(path)
                (filename, extension) = os.path.splitext(tempfilename)
                f = requests.get(path)
                temp_path = "temp" + extension
                with open(temp_path, "wb") as fw:
                    fw.write(f.content)
                self.img = cv2.imread(temp_path, -1)
                if self.img.size == 1:
                    return
                self.g_pic = cv2.imread(temp_path, -1)
                self.re_show_pic()
                os.remove(temp_path)
            else:
                self.img = cv2.imread(path, -1)
                if self.img.size == 1:
                    return
                self.g_pic = cv2.imread(path, -1)
                self.re_show_pic()
        else:
            pass

    # 图像显示
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

    # 清除图像
    def clear_img(self):
        self.last_pic, self.last_pic_backup, self.g_pic, self.img = None, None, None, None
        self.pic_label_show_window.pic_show_label.setPixmap(QPixmap(""))
        self.pic_label_show_window.contrast_show_label.setPixmap(QPixmap(""))
        self.pic_label_show_window.his_show_label_last.setPixmap(QPixmap(""))
        self.pic_label_show_window.his_show_label_this.setPixmap(QPixmap(""))
        self.plt_win.label_show_this_rgb.setPixmap(QPixmap(""))
        self.plt_win.his_show_label_this_rgb.setPixmap(QPixmap(""))
        self.plt_win.label_show_this_b.setPixmap(QPixmap(""))
        self.plt_win.his_show_label_this_b.setPixmap(QPixmap(""))
        self.plt_win.label_show_this_g.setPixmap(QPixmap(""))
        self.plt_win.his_show_label_this_g.setPixmap(QPixmap(""))
        self.plt_win.label_show_this_r.setPixmap(QPixmap(""))
        self.plt_win.his_show_label_this_r.setPixmap(QPixmap(""))

    # 设置
    def settings(self):
        self.win = ui.SettingWindow()

    # 直方图计算
    def img_plt(self, pic, path):
        if len(pic.shape) == 3:
            util.img_plt_rgb(pic, path)
        else:
            util.img_plt_gray(pic, path)
        plt = cv2.imread(path)
        return plt


    """ ********************************** 我是分割线 ******************************************* """

    def document_introduce_link(self):
        util.document_introduce_link()

    def document_help_link(self):
        util.document_help_link()

    def about_cv_tool(self):
        QMessageBox.about(self, ' 关于CV Tool', '当前版本：0.6.2.b3\n开源协议：木兰宽松许可证\n作者：Taoidle')

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
    util.check_dir('res/embed_img/')
    util.check_dir('res/img/')
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
