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
import cv2
import numpy as np


class CvPixelBasic:

    # 图像灰度化
    @staticmethod
    def img_to_gray(img):
        # 判断是否为彩色图像
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img

    # 图像反相
    @staticmethod
    def img_to_inverse(img):
        if len(img.shape) == 3:
            height, width, channel = img.shape
            for row in range(height):
                for col in range(width):
                    for c in range(channel):
                        pixel = img[row, col, c]
                        img[row, col, c] = 255 - pixel
        else:
            height, width = img.shape
            for row in range(height):
                for col in range(width):
                    pixel = img[row, col]
                    img[row, col] = 255 - pixel
        return img

    # 图像二值化
    @staticmethod
    def img_to_bin(img, threshold):
        # 图像灰度化
        img = CvPixelBasic.img_to_gray(img)
        # 图像二值化
        ret, binary = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        return binary

    # 自适应阈值二值化
    @staticmethod
    def img_to_auto_bin(img):
        # 图像灰度化
        img = CvPixelBasic.img_to_gray(img)
        # 自适应阈值二值化
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
        return img

    # 图像亮度对比度调节
    @staticmethod
    def img_to_contrast_brightness(img, contrast_value, brightness_value):
        if len(img.shape) == 3:
            height, width, channels = img.shape
        else:
            height, width = img.shape
            channels = 1
        blank = np.zeros([height, width, channels], img.dtype)
        dst = cv2.addWeighted(img, contrast_value, blank, 1 - contrast_value, brightness_value)
        return dst

    @staticmethod
    def img_to_overlay(img_1, img_2, weight_val):
        img = cv2.addWeighted(img_1, weight_val, img_2, 1 - weight_val, 0.0)
        return img

    # 图像RGB分量提取
    @staticmethod
    def img_to_extract_rgb(img, rgb_switch):
        img_b, img_g, img_r = cv2.split(img)
        if rgb_switch == 1:
            return img_r
        elif rgb_switch == 2:
            return img_g
        else:
            return img_b

    @staticmethod
    def img_to_b_g_r(img):
        img_b, img_g, img_r = cv2.split(img)
        return img_b, img_g, img_r
