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
from ui.threshold_dialog import ThresholdDialog
from ui.bright_contrast_dialog import BrightContrastDialog
from ui.extract_rgb_dialog import ExtractRGB
from ui.setting_dialog import SettingWindow


class InitUI:

    def __init_default_setting_window(self):
        self.dialog = SettingWindow()

    def __init_default_threshold_dialog(self):
        self.dialog = ThresholdDialog()

    def __init_default_bright_contrast_dialog(self):
        self.dialog = BrightContrastDialog()

    def __init_default_extract_rgb(self):
        self.dialog = ExtractRGB()
