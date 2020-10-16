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


class CvPixelOperator:

    # Canny双子
    @staticmethod
    def img_canny_operator(img, canny_value):
        img = cv2.Canny(img, canny_value, canny_value * 3, 3)
        return img

    # Sobel算子
    @staticmethod
    def img_sobel_operator(img, sobel_value):
        img_x = cv2.Sobel(img, cv2.CV_16S, 1, 0, (2 * sobel_value + 1), 1, 1, cv2.BORDER_DEFAULT)
        img_x = cv2.convertScaleAbs(img_x)
        img_y = cv2.Sobel(img, cv2.CV_16S, 0, 1, (2 * sobel_value + 1), 1, 1, cv2.BORDER_DEFAULT)
        img_y = cv2.convertScaleAbs(img_y)
        img = cv2.addWeighted(img_x, 0.5, img_y, 0.5, 0)
        return img

    # Laplacian算子
    @staticmethod
    def img_laplacian_operator(img, laplacian_value):
        img = cv2.Laplacian(img, -1, (laplacian_value * 2 + 1))
        img = cv2.convertScaleAbs(img)
        return img

    # Scharr滤波器
    @staticmethod
    def img_scharr_operator(img):
        img_x = cv2.Scharr(img, cv2.CV_16S, 1, 0, 1, 0, cv2.BORDER_DEFAULT)
        img_x = cv2.convertScaleAbs(img_x)
        img_y = cv2.Scharr(img, cv2.CV_16S, 0, 1, 1, 0, cv2.BORDER_DEFAULT)
        img_y = cv2.convertScaleAbs(img_y)
        img = cv2.addWeighted(img_x, 0.5, img_y, 0.5, 0)
        return img