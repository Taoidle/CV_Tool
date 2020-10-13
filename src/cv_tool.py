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
import sys
from ui.init_ui import InitUI
from ui.main_window import MainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QFileDialog, QMessageBox
from util.basic import CvBasic as cvb
from util.pixel_basic import CvPixelBasic as cpb
from util.pixel_position import CvPixelPosition as cpp
from util.pixel_noise import CvPixelNoise as cpn
from util.pixel_filter import CvPixelFilter as cpf


class CVT(MainWindow, InitUI):
    img, origin_img = None, None

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
        # 链接清空图片
        self.clear_pic.triggered.connect(self.init_default_clear_pic)
        # 链接设置窗口
        self.program_setting.triggered.connect(self._InitUI__init_default_setting_window)
        # 链接恢复原图
        self.tool_box.box_1_button_1.clicked.connect(self.init_origin_pic)
        # 链接图像灰度化
        self.tool_box.box_1_button_3.clicked.connect(self.init_img2gray)
        # 链接图像反相
        self.tool_box.box_1_button_4.clicked.connect(self.init_img2inverse)
        # 链接图像二值化
        self.tool_box.box_1_button_5.clicked.connect(self.init_img2bin)
        # 链接图像自适应阈值二值化
        self.tool_box.box_1_button_6.clicked.connect(self.init_img2bin_auto)
        # 链接图像亮度对比度调节
        self.tool_box.box_1_button_7.clicked.connect(self.init_img2bright_contrast)
        # 链接图像RGB分量提取
        self.tool_box.box_1_button_9.clicked.connect(self.init_img2extract_rgb)
        # 链接图像水平镜像
        self.tool_box.box_2_button_1.clicked.connect(self.init_img2horizontal)
        # 链接图像垂直镜像
        self.tool_box.box_2_button_2.clicked.connect(self.init_img2vertical)
        # 链接图像逆时针旋转90度
        self.tool_box.box_2_button_3.clicked.connect(self.init_img2rotate_left)
        # 链接图像顺时针旋转90度
        self.tool_box.box_2_button_4.clicked.connect(self.init_img2rotate_right)
        # 链接图像逆时针旋转任意角度
        self.tool_box.box_2_button_5.clicked.connect(self.init_img2rotate_left_any)
        # 链接图像顺时针旋转任意角度
        self.tool_box.box_2_button_6.clicked.connect(self.init_img2rotate_right_any)
        # 链接图像添加椒盐噪声
        self.tool_box.box_3_button_1.clicked.connect(self.init_img_impulse_noise)
        # 链接图像添加高斯噪声
        self.tool_box.box_3_button_2.clicked.connect(self.init_img_gaussian_noise)
        # 链接图像均值滤波
        self.tool_box.box_4_button_1.clicked.connect(self.init_img_blur_filter)
        # 链接图像中值滤波
        self.tool_box.box_4_button_2.clicked.connect(self.init_img_median_filter)
        # 链接图像方框滤波
        self.tool_box.box_4_button_3.clicked.connect(self.init_img_box_filter)
        # 链接图像高斯滤波
        self.tool_box.box_4_button_4.clicked.connect(self.init_img_gaussian_filter)
        # 链接图像双边滤波
        self.tool_box.box_4_button_5.clicked.connect(self.init_img_bilateral_filter)


    # 窗口居中
    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 图像检查
    def __check_img(self):
        # 判断图片是否为空
        if self.img is not None:
            return True
        else:
            # 空图像调用警示窗口
            QMessageBox.warning(self, '警告', "当前没有打开\n任何图像！", QMessageBox.Ok)
            return False

    # 打开图片
    def init_default_open_pic(self):
        # 调用存储文件
        file_name, tmp = QFileDialog.getOpenFileName(self, '打开图片', 'picture', '*.png *.jpg *.bmp *.jpeg *tif')
        if file_name == '':
            return
        # 获取图片
        self.img = cvb.get_pic(file_name)
        self.origin_img = self.img
        # 在窗口中显示
        width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
        # 重置窗口大小
        self.resize(width, height)

    # 保存图片
    def init_default_save_pic(self):
        # 检查图片
        if self.__check_img():
            # 创建默认文件名
            default_filename = cvb.create_default_filename('pic_', '.png')
            # 调用存储文件
            file_name, tmp = QFileDialog.getSaveFileName(self, '保存图片', default_filename, '*.png *.jpg *.bmp *.webp')
            if file_name == '':
                return
            # 保存图片
            cvb.save_pic(file_name, self.img)

    # 清空图片
    def init_default_clear_pic(self):
        self.img = None
        self.current_pic_widget.pic_show_label.setPixmap(QPixmap(""))
        self.current_pic_widget.pic_show_label.setText("图片显示区")

    # 恢复原图
    def init_origin_pic(self):
        # 检查图片
        if self.__check_img():
            self.img = self.origin_img
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像灰度化
    def init_img2gray(self):
        # 检查图片
        if self.__check_img():
            # 灰度化
            self.img = cpb.img_to_gray(self.img)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像反相
    def init_img2inverse(self):
        # 检查图片
        if self.__check_img():
            # 图片反相
            self.img = cpb.img_to_inverse(self.img)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像二值化
    def init_img2bin(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_threshold_dialog()
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
        if self.__check_img():
            # 自适应阈值二值化
            self.img = cpb.img_to_auto_bin(self.img)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像亮度对比度调节
    def init_img2bright_contrast(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_bright_contrast_dialog()
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img2bright_contrast_signal)

    # 图像亮度对比度调节信号函数
    @pyqtSlot(int, int, bool)
    def init_img2bright_contrast_signal(self, contrast_value, brightness_value, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 图片亮度对比度调节
            self.img = cpb.img_to_contrast_brightness(self.img, contrast_value, brightness_value)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像RGB分量提取
    def init_img2extract_rgb(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_extract_rgb()
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img2extract_rgb_signal)

    # 图像RGB分量提取信号函数
    @pyqtSlot(int, bool)
    def init_img2extract_rgb_signal(self, rgb_switch, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 图片RGB分量提取
            self.img = cpb.img_to_extract_rgb(self.img, rgb_switch)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像水平镜像
    def init_img2horizontal(self):
        # 检查图片
        if self.__check_img():
            # 图像水平镜像
            self.img = cpp.img_to_horizontal(self.img)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像垂直镜像
    def init_img2vertical(self):
        # 检查图片
        if self.__check_img():
            # 图像垂直镜像
            self.img = cpp.img_to_vertical(self.img)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像逆时针旋转90度
    def init_img2rotate_left(self):
        # 检查图片
        if self.__check_img():
            # 图像逆时针旋转90度
            self.img = cpp.img_to_rotate_left(self.img)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像顺时针旋转90度
    def init_img2rotate_right(self):
        # 检查图片
        if self.__check_img():
            # 图像顺时针旋转90度
            self.img = cpp.img_to_rotate_right(self.img)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像逆时针旋转任意角度
    def init_img2rotate_left_any(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_rotate_dialog()
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img2rotate_left_any_signal)

    # 图像逆时针旋转任意角度信号函数
    @pyqtSlot(int, bool)
    def init_img2rotate_left_any_signal(self, angle, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 图像旋转
            self.img = cpp.rotate_img(self.img, -angle)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像顺时针旋转任意角度
    def init_img2rotate_right_any(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_rotate_dialog()
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img2rotate_left_any_signal)

    # 图像顺时针旋转任意角度信号函数
    @pyqtSlot(int, bool)
    def init_img2rotate_right_any_signal(self, angle, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 图像旋转
            self.img = cpp.rotate_img(self.img, angle)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像添加椒盐噪声
    def init_img_impulse_noise(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_noise_dialog()
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img_impulse_noise_signal)

    # 图像添加椒盐噪声信号函数
    @pyqtSlot(float, bool)
    def init_img_impulse_noise_signal(self, prob, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 图像添加椒盐噪声
            self.img = cpn.img_impulse_noise(self.img, prob)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像添加高斯噪声
    def init_img_gaussian_noise(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_noise_dialog()
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img_gaussian_noise_signal)

    # 图像添加高斯噪声信号函数
    @pyqtSlot(float, bool)
    def init_img_gaussian_noise_signal(self, var, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 图像添加高斯噪声
            self.img = cpn.img_gaussian_noise(self.img, 0, var)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像均值滤波
    def init_img_blur_filter(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_filter_dialog()
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img_blur_filter_signal)

    # 图像均值滤波信号函数
    @pyqtSlot(int, bool)
    def init_img_blur_filter_signal(self, blur_value, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 均值滤波
            self.img = cpf.img_blur_filter(self.img, blur_value)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像中值滤波
    def init_img_median_filter(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_filter_dialog()
            # 设置中值滤波最小值
            self.dialog.threshold_slider.setMinimum(0)
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img_median_filter_signal)

    # 图像中值滤波信号函数
    @pyqtSlot(int, bool)
    def init_img_median_filter_signal(self, median_value, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 中值滤波
            self.img = cpf.img_median_filter(self.img, median_value)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像方框滤波
    def init_img_box_filter(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_filter_dialog()
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img_box_filter_signal)

    # 图像方框滤波信号函数
    @pyqtSlot(int, bool)
    def init_img_box_filter_signal(self, box_value, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 方框滤波
            self.img = cpf.img_box_filter(self.img, box_value, val=False)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像高斯滤波
    def init_img_gaussian_filter(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_filter_dialog()
            # 设置高斯滤波最小值
            self.dialog.threshold_slider.setMinimum(0)
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img_gaussian_filter_signal)

    # 图像高斯滤波信号函数
    @pyqtSlot(int, bool)
    def init_img_gaussian_filter_signal(self, gaussian_value, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 高斯滤波
            self.img = cpf.img_gaussian_filter(self.img, gaussian_value)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

    # 图像双边滤波
    def init_img_bilateral_filter(self):
        # 检查图片
        if self.__check_img():
            # 调用对话窗口
            self._InitUI__init_default_filter_dialog()
            # 设置双边滤波最小值
            self.dialog.threshold_slider.setMinimum(0)
            # 链接窗口信号函数
            self.dialog.close_signal.connect(self.init_img_bilateral_filter_signal)

    # 图像双边滤波信号函数
    @pyqtSlot(int, bool)
    def init_img_bilateral_filter_signal(self, bilateral_value, cancel_flag):
        # 取消操作判断
        if cancel_flag:
            # 高斯滤波
            self.img = cpf.img_bilateral_filter(self.img, bilateral_value)
            # 在窗口中显示
            width, height = cvb.show_pic(self.img, self.current_pic_widget.pic_show_label)
            # 重置窗口大小
            self.resize(width, height)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CVT()
    sys.exit(app.exec())
