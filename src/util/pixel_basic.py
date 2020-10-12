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