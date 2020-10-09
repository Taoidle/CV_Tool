import cv2


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

    @staticmethod
    def img_to_auto_bin(img):
        img = img_to_gray(img)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
        # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        return img
