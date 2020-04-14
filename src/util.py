import time, webbrowser,ui

import cv2
import numpy as np
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog, QInputDialog


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


def show_pic(self):
    # 调用存储文件
    file_name, tmp = QFileDialog.getOpenFileName(self, 'Open Image', 'Image', '*.png *.jpg *.bmp')
    if file_name is '':
        return
    # 采用OpenCV函数读取数据
    self.img = cv2.imread(file_name, -1)
    self.g_pic = cv2.imread(file_name, -1)
    if self.img.size == 1:
        return
    self.re_show_pic()

def pic_save(self):
    pic_name = './pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    cv2.imwrite(pic_name + '.bmp', self.img)

def re_show_pic(self):
    # 提取图像的通道和尺寸，用于将OpenCV下的image转换成Qimage
    height, width, channel = self.img.shape
    self.label_show.resize(width, height)
    bytes_perline = 3 * width
    self.q_img = QImage(self.img.data, width, height, bytes_perline, QImage.Format_RGB888).rgbSwapped()
    # 将QImage显示出来
    self.label_show.setPixmap(QPixmap.fromImage(self.q_img))

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


def img_to_horizontal(self):
    self.img = cv2.flip(self.img, 1)
    if self.img.size == 1:
        return
    self.re_show_pic()


def img_to_vertical(self):
    self.img = cv2.flip(self.img, 0)
    if self.img.size == 1:
        return
    self.re_show_pic()


def img_to_rotate_left(self):
    self.img = rotate_img(self.img, 90)
    self.re_show_pic()


def img_to_rotate_right(self):
    self.img = rotate_img(self.img, -90)
    self.re_show_pic()


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


def img_to_gray(self):
    self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
    self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)
    self.re_show_pic()


def img_to_bin(self):
    ui_custom.SliderDialog.threshold_max = 255
    self.win = ui_custom.SliderDialog()
    self.win.before_close_signal.connect(self.img_to_bin_signal)


def img_to_auto_bin(self):
    self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
    self.img = cv2.adaptiveThreshold(self.img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
    self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)
    self.re_show_pic()


def img_blur_filter(self):
    self.img = cv2.blur(self.img, (5, 5))
    self.re_show_pic()


def img_median_filter(self):
    self.img = cv2.medianBlur(self.img, 5)
    self.re_show_pic()


def img_gaussian_filter(self):
    self.img = cv2.GaussianBlur(self.img, (5, 5), 0)
    self.re_show_pic()


def img_bilateral_filter(self):
    self.img = cv2.bilateralFilter(self.img, 9, 75, 75)
    self.re_show_pic()


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


# 信号槽函数
def img_to_bin_signal(self, connect):
    self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(self.img, connect, 255, cv2.THRESH_BINARY)
    self.img = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    self.re_show_pic()
