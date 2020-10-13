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


class CvPixelPyramid:

    # 向上采样
    @staticmethod
    def img_to_pyrup(img):
        img = cv2.pyrUp(img)
        return img

    # 向下采样
    @staticmethod
    def img_to_pyrdown(img):
        img = cv2.pyrDown(img)
        return img

    # 图像金字塔
    @staticmethod
    def img_to_pyr_laplace(img):
        img_1 = cv2.pyrDown(img)  # 高斯金字塔
        img_2 = cv2.pyrDown(img_1)
        img_3 = cv2.pyrUp(img_2)
        img_4 = img_1 - img_3  # 拉普拉斯金字塔
        return img_4