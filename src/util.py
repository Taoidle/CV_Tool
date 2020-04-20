"""

Author: kaiyang
Last edited: April 2020

"""
import cv2, random, time, webbrowser, ui
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox


def re_origin_img(self):
    self.img = self.g_pic
    self.re_show_pic()


def img_to_gray(img):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def img_to_inverse(img):
    if len(img.shape) == 3:
        height, width, channel = img.shape
        for row in range(height):
            for col in range(width):
                for c in range(channel):
                    pixel = img[row, col, c]
                    img[row, col, c] = 255 - pixel
        return img
    elif len(img.shape) == 2:
        height, width = img.shape
        for row in range(height):
            for col in range(width):
                pixel = img[row, col]
                img[row, col] = 255 - pixel
        return img
    else:
        pass


def img_to_bin():
    ui.SliderDialog.threshold_max = 255
    win = ui.SliderDialog()
    win.before_close_signal.connect(img_to_bin_signal)


def img_to_auto_bin(img):
    img = img_to_gray(img)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return img


def img_to_contrast_brightness(img, contrast_value, brightness_value):
    if len(img.shape) == 3:
        height, width, channels = img.shape
    blank = np.zeros([height, width, channels], img.dtype)
    dst = cv2.addWeighted(img, contrast_value, blank, 1 - contrast_value, brightness_value)
    return dst


def img_to_horizontal(img):
    img = cv2.flip(img, 1)
    if img.size == 1:
        return
    return img


def img_to_vertical(img):
    img = cv2.flip(img, 0)
    if img.size == 1:
        return
    return img


def img_to_rotate_left(img):
    img = rotate_img(img, 90)
    return img


def img_to_rotate_right(img):
    img = rotate_img(img, -90)
    return img


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


def img_impulse_noise(img, prob):
    img_noise = np.copy(img)
    threshold = 1 - prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            if rdn < prob:
                img_noise[i][j] = 0
            elif rdn > threshold:
                img_noise[i][j] = 255

    return img_noise


def img_gaussian_noise(img, mean=0, var=0.001):
    img = np.array(img / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, img.shape)
    img_noise = img + noise

    img_noise = np.clip(img_noise, 0, 1.0)
    img_noise = np.uint8(img_noise * 255)

    return img_noise


def img_blur_filter(img, blur_value):
    img = cv2.blur(img, (blur_value, blur_value))
    return img


def img_median_filter(img, median_value):
    img = cv2.medianBlur(img, median_value * 2 + 1)
    return img


def img_box_filter(img, box_value, val):
    img = cv2.boxFilter(img, -1, (box_value, box_value), normalize=val)
    return img


def img_gaussian_filter(img, gaussian_value):
    img = cv2.GaussianBlur(img, (gaussian_value * 2 + 1, gaussian_value * 2 + 1), 0)
    return img


def img_bilateral_filter(img, bilateral_value):
    img = cv2.bilateralFilter(img, bilateral_value, bilateral_value * 2, bilateral_value // 2)
    return img


def img_canny_operator(img, canny_value):
    img = cv2.Canny(img, canny_value, canny_value * 3, 3)
    return img


def img_sobel_operator(img, sobel_value):
    img_x = cv2.Sobel(img, cv2.CV_16S, 1, 0, (2 * sobel_value + 1), 1, 1, cv2.BORDER_DEFAULT)
    img_x = cv2.convertScaleAbs(img_x)
    img_y = cv2.Sobel(img, cv2.CV_16S, 0, 1, (2 * sobel_value + 1), 1, 1, cv2.BORDER_DEFAULT)
    img_y = cv2.convertScaleAbs(img_y)
    img = cv2.addWeighted(img_x, 0.5, img_y, 0.5, 0)
    return img


def img_laplacian_operator(img, laplacian_value):
    img = cv2.Laplacian(img, cv2.CV_16S, (laplacian_value * 2 + 1), 1, 0, cv2.BORDER_DEFAULT)
    return img


def img_scharr_operator(img):
    img_x = cv2.Scharr(img, cv2.CV_16S, 1, 0, 1, 0, cv2.BORDER_DEFAULT)
    img_x = cv2.convertScaleAbs(img_x)
    img_y = cv2.Scharr(img, cv2.CV_16S, 0, 1, 1, 0, cv2.BORDER_DEFAULT)
    img_y = cv2.convertScaleAbs(img_y)
    img = cv2.addWeighted(img_x, 0.5, img_y, 0.5, 0)
    return img


def img_to_erode(img, erode_value, shape):
    element = cv2.getStructuringElement(shape, (erode_value * 2 + 1, erode_value * 2 + 1), (erode_value, erode_value))
    img = cv2.erode(img, element)
    return img


def img_to_dilate(img, dilate_value, shape):
    element = cv2.getStructuringElement(shape, (dilate_value * 2 + 1, dilate_value * 2 + 1),
                                        (dilate_value, dilate_value))
    img = cv2.dilate(img, element)
    return img


def morphology_shape(flag):
    if flag == 1:
        return cv2.MORPH_ELLIPSE
    elif flag == 2:
        return cv2.MORPH_RECT
    elif flag == 3:
        return cv2.MORPH_CROSS
    else:
        pass


def encode(s):
    bin_s = ' '.join([bin(ord(c)).replace('0b', '') for c in s])
    length = len(bin_s)
    # i = 0
    for i in range(length):
        if i % 8 == 0 and i + 7 <= length:
            while bin_s[i + 7] != ' ':
                temp = bin_s[:i] + '0' + bin_s[i:]
                bin_s = temp
        if i == length:
            break
        i += 1
    return bin_s


def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


def lsb_embed(img, s):
    if len(img.shape) == 3:
        # 获取通道数F
        width, height, channel = img.shape
    else:
        width, height = img.shape
        channel = 1
    s = encode(s)
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        else:
            x = i // width
            y = i % width
            channel = i // (height * width)
            value = img[x, y, channel]
            if (value % 2) == int(s[i]):
                continue
            if (value % 2) > int(s[i]):
                img[x, y, channel] = value - 1
                continue
            if (value % 2) < int(s[i]):
                img[x, y, channel] = value + 1
                continue
    return img


def lsb_extract(img, num):
    if len(img.shape) == 3:
        # 获取通道数F
        width, height, channel = img.shape
    else:
        width, height = img.shape
        channel = 1
    s = ''
    for i in range(num - 1):
        x = i // width
        y = i % width
        channel = i // (height * width)
        value = img[x, y, channel]
        if (i + 1) % 8 == 0:
            s += ' '
            continue
        else:
            if value % 2 == 0:
                s += '0'
                continue
            else:
                s += '1'
                continue
    return decode(s)


def pic_save(self):
    pic_name = './pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    cv2.imwrite(pic_name + '.bmp', self.img)

    """ ********************************** 我是分割线 ******************************************* """
    """ ******************************* 视频处理调用函数 ***************************************** """


def show_vid(self):
    # 调用存储文件
    file_name, tmp = QFileDialog.getOpenFileName(self, 'Open Video', 'Video', '*.mp4')
    if file_name is '':
        return
    # 采用OpenCV函数读取数据
    self.vid_reader = cv2.VideoCapture(file_name)
    ret_tmp, tmp = self.vid_reader.read()
    tmp_height, tmp_width, tmp_channel = tmp.shape
    self.resize(tmp_width, tmp_height)

    while (self.vid_reader.isOpened()):
        ret, frame = self.vid_reader.read()
        if not (ret):
            break
        # 提取图像的通道和尺寸，用于将OpenCV下的image转换成Qimage
        if self.vid_horizontal_flag:
            frame = cv2.flip(frame, 1)
        if self.vid_vertical_flag:
            frame = cv2.flip(frame, 0)
        if self.vid_horizontal_vertical_flag:
            frame = cv2.flip(frame, -1)
        height, width, channel = frame.shape
        bytes_perline = 3 * width
        self.q_img = QImage(frame.data, width, height, bytes_perline, QImage.Format_RGB888).rgbSwapped()
        self.label_show.setPixmap(QPixmap.fromImage(self.q_img))
        # wait until key strokes to break
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

    self.vid_reader.release()
    cv2.destroyAllWindows()


def vid_to_horizontal(self, state):
    if self.vid_horizontal_button.isChecked():
        self.vid_horizontal_mirror.setCheckable(True)
    else:
        self.vid_horizontal_mirror.setCheckable(False)
    if state:
        self.vid_horizontal_flag = True
    else:
        self.vid_horizontal_flag = False


def vid_to_vertical(self, state):
    if self.vid_vertical_button.isChecked():
        self.vid_vertical_mirror.setCheckable(True)
    else:
        self.vid_vertical_mirror.setCheckable(False)
    if state:
        self.vid_vertical_flag = True
    else:
        self.vid_vertical_flag = False


def vid_to_horizontal_vertical(self, state):
    if self.vid_horizontal_vertical_mirror.isChecked():
        self.vid_horizontal_vertical_mirror.setCheckable(True)
    else:
        self.vid_horizontal_vertical_mirror.setCheckable(False)
    if state:
        self.vid_horizontal_vertical_flag = True
    else:
        self.vid_horizontal_vertical_flag = False


def lsb_dialog(self):
    text, ok = QInputDialog.getText(self, 'Input', 'Enter your string:')
    if ok:
        # 把得到的字符串放到输入框里
        lsb_embed(self.img, str(text))


def document_link():
    webbrowser.open('https://git.lkyblog.cn/Taoidle/communicate_training/src/branch/master/ct_player')


def img_plt_gray(img, path):
    plt.figure(figsize=(4, 3))
    x_index = list(np.arange(0, 256))
    histr = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    histr = list(histr.astype(np.uint8).reshape((1, 256))[0])
    plt.bar(x_index, histr, 1, color='gray')
    plt.savefig(path)


def img_plt_rgb(img, path):
    x_index = list(np.arange(0, 256))
    color = ('blue', 'green', 'red')
    plt.figure(figsize=(4, 3))
    for i, c in enumerate(color):
        histr = cv2.calcHist(images=[img], channels=[i], mask=None, histSize=[256], ranges=[0, 256])
        histr = list(histr.astype(np.uint32).reshape((1, 256))[0])
        plt.bar(x_index, histr, 1, color=c)
    plt.legend(('B', 'G', 'R'), loc='upper right')
    plt.savefig(path)


def shrink_len(width, height):
    if width > 0 and width < 800:
        width = width // 1
        height = height // 1
    elif width >= 800 and width <= 1200:
        width = width // 2
        height = height // 2
    elif width > 1200 and width <= 2200:
        width = width // 3
        height = height // 3
    elif width > 2200 and width <= 3600:
        width = width // 4
        height = height // 4
    return width, height
