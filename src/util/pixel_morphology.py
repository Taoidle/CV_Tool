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


class CvPixelMorphology:

    @staticmethod
    def morphology_shape(flag):
        if flag == 1:
            return cv2.MORPH_ELLIPSE
        elif flag == 2:
            return cv2.MORPH_RECT
        elif flag == 3:
            return cv2.MORPH_CROSS
        else:
            pass

    @staticmethod
    def img_to_erode(img, erode_value, shape):
        element = cv2.getStructuringElement(shape, (erode_value * 2 + 1, erode_value * 2 + 1),
                                            (erode_value, erode_value))
        img = cv2.erode(img, element)
        return img

    @staticmethod
    def img_to_dilate(img, dilate_value, shape):
        element = cv2.getStructuringElement(shape, (dilate_value * 2 + 1, dilate_value * 2 + 1),
                                            (dilate_value, dilate_value))
        img = cv2.dilate(img, element)
        return img

    @staticmethod
    def img_to_open_operation(img, open_val, shape):
        element = cv2.getStructuringElement(shape, (open_val * 2 + 1, open_val * 2 + 1), (open_val, open_val))
        dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
        return dst

    @staticmethod
    def img_to_close_operation(img, close_val, shape):
        element = cv2.getStructuringElement(shape, (close_val * 2 + 1, close_val * 2 + 1), (close_val, close_val))
        dst = cv2.morphologyEx(img, cv2.MORPH_CLOSE, element)
        return dst

    @staticmethod
    def img_to_top_hat(img, top_hat_val, shape):
        element = cv2.getStructuringElement(shape, (top_hat_val * 2 + 1, top_hat_val * 2 + 1),
                                            (top_hat_val, top_hat_val))
        dst = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, element)
        return dst

    @staticmethod
    def img_to_black_hat(img, black_hat_val, shape):
        element = cv2.getStructuringElement(shape, (black_hat_val * 2 + 1, black_hat_val * 2 + 1),
                                            (black_hat_val, black_hat_val))
        dst = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, element)
        return dst

    @staticmethod
    def img_to_gradient(img, gradient_val, shape):
        element = cv2.getStructuringElement(shape, (gradient_val * 2 + 1, gradient_val * 2 + 1))
        dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, element)
        return dst