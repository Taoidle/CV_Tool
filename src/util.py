import random
import time, webbrowser, ui

import cv2
import numpy as np
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog, QInputDialog
import matplotlib.pyplot as plt


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
    # 获取通道数F
    width, height, channel = img.shape
    s = encode(s)
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        else:
            x = i // width
            y = i % width
            channel = i // (height * width)
            value = img[x, y, channel]
            print('x: ' + str(x) + '\t' + 'y: ' + str(y) + '\t' + 'channel: ' + str(channel) + '\t' + 'value: ' + str(
                value))
            if (value % 2) == int(s[i]):
                print('new value' + str(img[x, y, channel]))
                continue
            if (value % 2) > int(s[i]):
                img[x, y, channel] = value - 1
                print('new value' + str(img[x, y, channel]))
                continue
            if (value % 2) < int(s[i]):
                img[x, y, channel] = value + 1
                print('new value' + str(img[x, y, channel]))
                continue
    return img


def lsb_extract(img, num):
    width, height, channel = img.shape
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


def pic_save(self):
    pic_name = './pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    cv2.imwrite(pic_name + '.bmp', self.img)


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


def re_origin_img(self):
    self.img = self.g_pic
    self.re_show_pic()


def img_to_gray(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def img_to_bin(self):
    ui_custom.SliderDialog.threshold_max = 255
    self.win = ui_custom.SliderDialog()
    self.win.before_close_signal.connect(self.img_to_bin_signal)


def img_to_auto_bin(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return img


def img_blur_filter(img):
    img = cv2.blur(img, (5, 5))
    return img


def img_median_filter(img):
    img = cv2.medianBlur(img, 5)
    return img


def img_gaussian_filter(img):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    return img


def img_bilateral_filter(img):
    img = cv2.bilateralFilter(img, 9, 75, 75)
    return img


def lsb_dialog(self):
    text, ok = QInputDialog.getText(self, 'Input', 'Enter your string:')
    if ok:
        # 把得到的字符串放到输入框里
        lsb_embed(self.img, str(text))


def lsb_embed(self):
    text = self.embed_input.text()
    if text is not None:
        self.img = lsb_embed(self.img, str(text))
        pic_name = '../res/embed_img/pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        cv2.imwrite(pic_name + '.bmp', self.img)
        filename = pic_name + '.txt'
        with open(filename, 'w') as f:
            f.write(str(len(text) * 8))
        self.re_show_pic()


def lsb_extract(self):
    file_name, tmp = QFileDialog.getOpenFileName(self, 'Open embed_txt', 'txt', '*.txt')
    with open(file_name) as f:
        num = f.read()
    self.extract_output.setText(lsb_extract(self.img, int(num)))


def document_link(self):
    webbrowser.open('https://git.lkyblog.cn/Taoidle/communicate_training/src/branch/master/ct_player')


def img_plt_gray(img):
    plt.figure(figsize=(4, 3))
    x_index = list(np.arange(0, 256))
    histr = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    histr = list(histr.astype(np.uint8).reshape((1, 256))[0])
    plt.bar(x_index, histr, 1, color='gray')
    plt.savefig("./plt.png")


def img_plt_rgb(img):
    x_index = list(np.arange(0, 256))
    color = ('blue', 'green', 'red')
    plt.figure(figsize=(4, 3))
    for i, c in enumerate(color):
        histr = cv2.calcHist(images=[img], channels=[i], mask=None, histSize=[256], ranges=[0, 256])
        histr = list(histr.astype(np.uint32).reshape((1, 256))[0])
        plt.bar(x_index, histr, 1, color=c)
    plt.legend(('B', 'G', 'R'), loc='upper right')
    plt.savefig("./plt.png")


# 信号槽函数
def img_to_bin_signal(self, connect):
    self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(self.img, connect, 255, cv2.THRESH_BINARY)
    self.img = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    self.re_show_pic()
