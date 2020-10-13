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


class CvPixelFilter:

    # 均值滤波
    @staticmethod
    def img_blur_filter(img, blur_value):
        img = cv2.blur(img, (blur_value, blur_value))
        return img

    # 中值滤波
    @staticmethod
    def img_median_filter(img, median_value):
        img = cv2.medianBlur(img, median_value * 2 + 1)
        return img

    # 方框滤波
    @staticmethod
    def img_box_filter(img, box_value, val):
        img = cv2.boxFilter(img, -1, (box_value, box_value), normalize=val)
        return img

    # 高斯滤波
    @staticmethod
    def img_gaussian_filter(img, gaussian_value):
        img = cv2.GaussianBlur(img, (gaussian_value * 2 + 1, gaussian_value * 2 + 1), 0)
        return img

    # 双边滤波
    @staticmethod
    def img_bilateral_filter(img, bilateral_value):
        img = cv2.bilateralFilter(img, bilateral_value, bilateral_value * 2, bilateral_value // 2)
        return img