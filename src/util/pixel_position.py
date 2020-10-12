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


class CvPixelPosition:

    @staticmethod
    def img_to_horizontal(img):
        img = cv2.flip(img, 1)
        if img.size == 1:
            return
        return img

    @staticmethod
    def img_to_vertical(img):
        img = cv2.flip(img, 0)
        if img.size == 1:
            return
        return img

    @staticmethod
    def img_to_rotate_left(img):
        img = CvPixelPosition.rotate_img(img, -90)
        return img

    @staticmethod
    def img_to_rotate_right(img):
        img = CvPixelPosition.rotate_img(img, 90)
        return img

    @staticmethod
    def rotate_img(img, angle):
        (h, w) = img.shape[:2]
        (cX, cY) = (w // 2, h // 2)

        rotate_img = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
        cos = np.abs(rotate_img[0, 0])
        sin = np.abs(rotate_img[0, 1])

        rotate_img_width = int((h * sin) + (w * cos))
        rotate_img_high = int((h * cos) + (w * sin))

        rotate_img[0, 2] += (rotate_img_width / 2) - cX
        rotate_img[1, 2] += (rotate_img_high / 2) - cY

        return cv2.warpAffine(img, rotate_img, (rotate_img_width, rotate_img_high))
