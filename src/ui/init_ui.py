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
from ui.dialog.dialog_threshold import ThresholdDialog
from ui.dialog.dialog_bright_contrast import BrightContrastDialog
from ui.dialog.dialog_overlay import OverlayDialog
from ui.dialog.dialog_extract_rgb import ExtractRGB
from ui.dialog.dialog_rotate import RotateDialog
from ui.dialog.dialog_noise import NoiseDialog
from ui.dialog.dialog_filter import FilterDialog
from ui.dialog.dialog_operator import CannySobelDialog, LaplacianDialog
from ui.dialog.dialog_morphology import MorphologyDialog
from ui.dialog.dialog_plt import PltDialog
from ui.dialog.dialog_histogram import HistogramDialog
from ui.dialog.dialog_setting import SettingWindow


class InitUI:

    # 初始化设置窗口
    def __init_default_setting_window(self):
        self.dialog = SettingWindow()

    # 初始化二值化窗口
    def __init_default_threshold_dialog(self):
        self.dialog = ThresholdDialog()

    # 初始化亮度对比度窗口
    def __init_default_bright_contrast_dialog(self):
        self.dialog = BrightContrastDialog()

    # 初始化图像叠加窗口
    def __init_default_overlay_dialog(self):
        self.dialog = OverlayDialog()

    # 初始化RGB分量提取窗口
    def __init_default_extract_rgb(self):
        self.dialog = ExtractRGB()

    # 初始化图像旋转窗口
    def __init_default_rotate_dialog(self):
        self.dialog = RotateDialog()

    # 初始化噪声添加窗口
    def __init_default_noise_dialog(self):
        self.dialog = NoiseDialog()

    # 初始化滤波窗口
    def __init_default_filter_dialog(self):
        self.dialog = FilterDialog()

    # 初始化Canny Sobel算子窗口
    def __init_default_canny_sobel_dialog(self):
        self.dialog = CannySobelDialog()

    # 初始化Laplacian算子窗口
    def __init_default_laplacian_dialog(self):
        self.dialog = LaplacianDialog()

    # 初始化形态学窗口
    def __init_default_morphology_dialog(self):
        self.dialog = MorphologyDialog()

    # 初始化Plt窗口
    def __init_default_plt_dialog(self):
        self.dialog = PltDialog()

    # 初始化直方图窗口
    def __init_default_histogram_dialog(self):
        self.dialog = HistogramDialog()