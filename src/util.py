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

import json, cv2, random, time, webbrowser, ui, os
import numpy as np
import matplotlib.pyplot as plt
from aip import AipOcr
from skimage.metrics import structural_similarity
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog, QInputDialog


def check_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


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
    else:
        height, width = img.shape
        for row in range(height):
            for col in range(width):
                pixel = img[row, col]
                img[row, col] = 255 - pixel
    return img


def img_to_bin():
    ui.SliderDialog.threshold_max = 255
    win = ui.SliderDialog()
    win.before_close_signal_1.connect(img_to_bin_signal)


def img_to_auto_bin(img):
    img = img_to_gray(img)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return img


def img_to_contrast_brightness(img, contrast_value, brightness_value):
    if len(img.shape) == 3:
        height, width, channels = img.shape
    else:
        height, width = img.shape
        channels = 1
    blank = np.zeros([height, width, channels], img.dtype)
    dst = cv2.addWeighted(img, contrast_value, blank, 1 - contrast_value, brightness_value)
    return dst


def img_to_overlay(img_1, img_2, weight_val):
    img = cv2.addWeighted(img_1, weight_val, img_2, 1 - weight_val, 0.0)
    return img


def img_to_extract_rgb(img, rgb_switch):
    if rgb_switch == 1:
        img = img[:, :, 2]
    elif rgb_switch == 2:
        img = img[:, :, 1]
    else:
        img = img[:, :, 0]
    return img


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
    img = rotate_img(img, -90)
    return img


def img_to_rotate_right(img):
    img = rotate_img(img, 90)
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
    img = cv2.Laplacian(img, -1, (laplacian_value * 2 + 1))
    img = cv2.convertScaleAbs(img)
    return img


def img_scharr_operator(img):
    img_x = cv2.Scharr(img, cv2.CV_16S, 1, 0, 1, 0, cv2.BORDER_DEFAULT)
    img_x = cv2.convertScaleAbs(img_x)
    img_y = cv2.Scharr(img, cv2.CV_16S, 0, 1, 1, 0, cv2.BORDER_DEFAULT)
    img_y = cv2.convertScaleAbs(img_y)
    img = cv2.addWeighted(img_x, 0.5, img_y, 0.5, 0)
    return img


def img_houghlines(img_1, img_2, connect_1, connect_2, connnect_3):
    img_temp = img_2
    lines = cv2.HoughLines(img_1, connect_1, np.pi / connect_2, connnect_3)  # 霍夫变换返回的就是极坐标系中的两个参数  rho和theta
    # print(np.shape(lines))
    lines = lines[:, 0, :]  # 将数据转换到二维
    for rho, theta in lines:
        a = np.cos(theta)
        b = np.sin(theta)
        # 从图b中可以看出x0 = rho x cos(theta)
        #               y0 = rho x sin(theta)
        x0 = a * rho
        y0 = b * rho
        # 由参数空间向实际坐标点转换
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(img_temp, (x1, y1), (x2, y2), (0, 0, 255), 1)
    return img_temp


def img_houghlines_p(img_1, img_2, connect_1, connect_2, connnect_3):
    img_temp = img_2
    lines = cv2.HoughLinesP(img_1, connect_1, np.pi / connect_2, connnect_3)
    lines = lines[:, 0, :]
    for x1, y1, x2, y2 in lines:
        cv2.line(img_temp, (x1, y1), (x2, y2), (0, 0, 255), 1)
    return img_temp


def img_houghcircles(img_1, img_2, dp, minDist, param1, parma2, minRadius, maxRadius):
    circles1 = cv2.HoughCircles(img_1, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=parma2,
                                minRadius=minRadius, maxRadius=maxRadius)
    circles = circles1[0, :, :]
    circles = np.uint16(np.around(circles))
    for i in circles[:]:
        cv2.circle(img_2, (i[0], i[1]), i[2], (0, 255, 0), 3)
        cv2.circle(img_2, (i[0], i[1]), 2, (255, 0, 255), 10)
    return img_2


def img_dct_basic(img, y1, y2, x1, x2):
    if len(img.shape) == 2:
        height, width = img.shape
        img_dct = cv2.dct(np.array(img, np.float32))
        img_dct[y1:y2, x1:x2] = 0
        img = np.array(cv2.idct(img_dct), np.uint8).reshape(height, width)
    else:
        height, width, channels = img.shape
        img_b = img[:, :, 0]
        img_g = img[:, :, 1]
        img_r = img[:, :, 2]
        img_b_dct = cv2.dct(np.array(img_b, np.float32))
        img_b_dct[y1:y2, x1:x2] = 0
        img_b = np.array(cv2.idct(img_b_dct), np.uint8).reshape(height, width)
        img_g_dct = cv2.dct(np.array(img_g, np.float32))
        img_g_dct[y1:y2, x1:x2] = 0
        img_g = np.array(cv2.idct(img_g_dct), np.uint8).reshape(height, width)
        img_r_dct = cv2.dct(np.array(img_r, np.float32))
        img_r_dct[y1:y2, x1:x2] = 0
        img_r = np.array(cv2.idct(img_r_dct), np.uint8).reshape(height, width)
        img = cv2.merge([img_b, img_g, img_r])
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


def img_to_open_operation(img, open_val, shape):
    element = cv2.getStructuringElement(shape, (open_val * 2 + 1, open_val * 2 + 1), (open_val, open_val))
    dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
    return dst


def img_to_close_operation(img, close_val, shape):
    element = cv2.getStructuringElement(shape, (close_val * 2 + 1, close_val * 2 + 1), (close_val, close_val))
    dst = cv2.morphologyEx(img, cv2.MORPH_CLOSE, element)
    return dst


def img_to_top_hat(img, top_hat_val, shape):
    element = cv2.getStructuringElement(shape, (top_hat_val * 2 + 1, top_hat_val * 2 + 1), (top_hat_val, top_hat_val))
    dst = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, element)
    return dst


def img_to_black_hat(img, black_hat_val, shape):
    element = cv2.getStructuringElement(shape, (black_hat_val * 2 + 1, black_hat_val * 2 + 1),
                                        (black_hat_val, black_hat_val))
    dst = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, element)
    return dst


def img_to_gradient(img, gradient_val, shape):
    element = cv2.getStructuringElement(shape, (gradient_val * 2 + 1, gradient_val * 2 + 1))
    dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, element)
    return dst


def morphology_shape(flag):
    if flag == 1:
        return cv2.MORPH_ELLIPSE
    elif flag == 2:
        return cv2.MORPH_RECT
    elif flag == 3:
        return cv2.MORPH_CROSS
    else:
        pass


def img_to_pyrup(img):
    img = cv2.pyrUp(img)
    return img


def img_to_pyrdown(img):
    img = cv2.pyrDown(img)
    return img


def imt_to_pyr_laplace(img):
    img_1 = cv2.pyrDown(img)  # 高斯金字塔
    img_2 = cv2.pyrDown(img_1)
    img_3 = cv2.pyrUp(img_2)
    img_4 = img_1 - img_3  # 拉普拉斯金字塔
    return img_4


def encode(s, width=8):
    bin_str = ''.join([(bin(c).replace('0b', '')).zfill(width) for c in s.encode(encoding="utf-8")])
    return bin_str


def decode(s):
    s = [np.uint8(c) for c in s]
    bin_str = ''.join([bin(b & 1).strip('0b').zfill(1) for b in s])
    str = np.zeros(np.int(len(s) / 8)).astype(np.int)
    for i in range(0, len(str)):
        str[i] = int('0b' + bin_str[(8 * i):(8 * (i + 1))], 2)
    return bytes(str.astype(np.int8)).decode()


def lsb_embed(img, s):
    if len(img.shape) == 3:
        # 获取通道数F
        width, height, channel = img.shape
        s = encode(s)
        for i in range(len(s)):
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
    else:
        width, height = img.shape
        s = encode(s)
        for i in range(len(s)):
            x = i // width
            y = i % width
            value = img[x, y]
            if (value % 2) == int(s[i]):
                continue
            if (value % 2) > int(s[i]):
                img[x, y] = value - 1
                continue
            if (value % 2) < int(s[i]):
                img[x, y] = value + 1
                continue
    return img


def lsb_extract(img, num):
    if len(img.shape) == 3:
        # 获取通道数F
        width, height, channel = img.shape
        s = ''
        for i in range(num):
            x = i // width
            y = i % width
            channel = i // (height * width)
            value = img[x, y, channel]
            if value % 2 == 0:
                s += '0'
                continue
            else:
                s += '1'
                continue
    else:
        width, height = img.shape
        s = ''
        for i in range(num):
            x = i // width
            y = i % width
            value = img[x, y]
            if value % 2 == 0:
                s += '0'
                continue
            else:
                s += '1'
                continue
    return decode(s)


def dct_embed(img_gray, msg, dct_block, seed=2020):
    if len(img_gray.shape) > 2:
        img_b = img_gray[:, :, 0]
        img_g = img_gray[:, :, 1]
        img_r = img_gray[:, :, 2]
        img_b = dct_embed_fuction(img_b, msg, dct_block, seed=2020)
        img_marked = cv2.merge([img_b, img_g, img_r])
        return img_marked
    else:
        img_marked = dct_embed_fuction(img_gray, msg, dct_block, seed=2020)
        return img_marked


def dct_embed_fuction(img_gray, msg, dct_block, seed=2020):
    msg = [np.uint8(c) for c in encode(msg)]
    len_msg = len(msg)

    Block = dct_block
    height, width = img_gray.shape
    embed_capacity = np.int((height) * (width) / Block / Block)
    if embed_capacity < len_msg:
        print('Embedding Capacity {} not enough'.format(embed_capacity))
        return img_gray

    random.seed(seed)
    s = [random.randint(0, 1) for i in range(len_msg)]
    bits2embed = np.bitwise_xor(msg, np.uint8(s))

    img_marked = img_gray.copy()
    height, width = img_marked.shape
    cnt = 0
    delta = 10
    r0, c0 = 2, 3
    for row in np.arange(0, height - Block, Block):
        if cnt >= len_msg:
            break

        for col in np.arange(0, width - Block, Block):
            if cnt >= len_msg:
                break

            block = np.array(img_marked[row:(row + Block), col:(col + Block)], np.float32)
            block_dct = cv2.dct(block)
            a, b = (block_dct[r0, c0], block_dct[c0, r0]) if block_dct[r0, c0] > block_dct[c0, r0] else (
                block_dct[c0, r0], block_dct[r0, c0])
            a += delta
            b -= delta
            block_dct[r0, c0] = (a if bits2embed[cnt] == 1 else b)
            block_dct[c0, r0] = (b if bits2embed[cnt] == 1 else a)

            cnt += 1
            img_marked[row:(row + Block), col:(col + Block)] = np.array(cv2.idct(block_dct), np.uint8)
    return img_marked


def dct_extract(img_marked, len_msg, dct_block, seed=2020):
    if len(img_marked.shape) > 2:
        img_b = img_marked[:, :, 0]
        msg = dct_extract_fuction(img_b, len_msg, dct_block, seed=2020)
        return msg
    else:
        msg = dct_extract_fuction(img_marked, len_msg, dct_block, seed=2020)
        return msg


def dct_extract_fuction(img_marked, len_msg, dct_block, seed=2020):
    N = dct_block
    height, width = img_marked.shape
    msg_embedded = ''
    cnt = 0
    r0, c0 = 2, 3
    for row in np.arange(0, height - N, N):
        if cnt >= len_msg:
            break

        for col in np.arange(0, width - N, N):
            if cnt >= len_msg:
                break

            block = np.array(img_marked[row:(row + N), col:(col + N)], np.float32)
            block_dct = cv2.dct(block)
            msg_embedded += ('1' if block_dct[r0, c0] > block_dct[c0, r0] else '0')
            cnt += 1

    bits_extracted = [np.uint8(c) for c in msg_embedded]

    random.seed(seed)
    s = [random.randint(0, 1) for i in range(len_msg)]
    msgbits = np.bitwise_xor(bits_extracted, np.uint8(s))
    msg = decode(msgbits)
    return msg


# MSE
def get_mse(origin_img, target_img):
    diff = origin_img.astype("float") - target_img.astype("float")
    return np.square(diff).sum() / (origin_img.shape[0] * origin_img.shape[1])


# PSNR
def get_psnr(origin_img, target_img, max_val=256):
    diff = origin_img.astype(np.float32) - target_img.astype(np.float32)
    MSE = np.sum(np.mean((np.power(diff, 2))))
    if MSE < 1.0e-10:
        return 100

    psnr = -10 * np.log10(MSE / ((max_val - 1.0) ** 2))
    return psnr


# SSIM
def get_ssim(origin_img, target_img):
    if len(origin_img.shape) == 3:
        origin_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
    if len(target_img.shape) == 3:
        target_img = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
    ssim = structural_similarity(origin_img, target_img)
    return ssim


def pic_save(self):
    pic_name = './pic_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    cv2.imwrite(pic_name + '.bmp', self.img)

    """ ********************************** 我是分割线 ******************************************* """
    """ ******************************* 视频处理调用函数 ***************************************** """


def show_vid(self):
    # 调用存储文件
    file_name, tmp = QFileDialog.getOpenFileName(self, 'Open Video', 'Video', '*.mp4')
    if file_name == '':
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


def document_introduce_link():
    webbrowser.open('https://www.taoidle.cn/%e5%85%b3%e4%ba%8ecv-tool%e5%b0%8f%e5%b7%a5%e5%85%b7.html')


def document_help_link():
    webbrowser.open('https://www.taoidle.cn/%e5%85%b3%e4%ba%8ecv-tool%e5%b0%8f%e5%b7%a5%e5%85%b7.html')


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


def img_to_b_g_r(img):
    img_b = img[:, :, 0]
    img_g = img[:, :, 1]
    img_r = img[:, :, 2]
    return img_b, img_g, img_r


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
    elif width > 3600 and width <= 4800:
        width = width // 5
        height = height // 5
    elif width > 4800 and width <= 6000:
        width = width // 6
        height = height // 6
    elif width > 6000 and width <= 7200:
        width = width // 7
        height = height // 7
    elif width > 7200 and width <= 8400:
        width = width // 8
        height = height // 8
    elif width > 8400 and width <= 9600:
        width = width // 9
        height = height // 9
    elif width > 9600 and width <= 10800:
        width = width // 10
        height = height // 10
    elif width > 10800 and width <= 12000:
        width = width // 11
        height = height // 11
    elif width > 12000 and width <= 13200:
        width = width // 12
        height = height // 12
    return width, height


def shrink_len_his(width, height):
    if width > 0 and width <= 250:
        width = width // 1
        height = height // 1
    elif width > 250 and width <= 500:
        width = width // 2
        height = height // 2
    elif width > 500 and width <= 750:
        width = width // 3
        height = height // 3
    elif width > 750 and width <= 1000:
        width = width // 4
        height = height // 4
    elif width > 1000 and width <= 1250:
        width = width // 5
        height = height // 5
    elif width > 1250 and width <= 1500:
        width = width // 6
        height = height // 6
    return width, height


def program_settings(jpg, png, webp, dct_block, app_id, api_key, secret_key, words_model):
    with open('./settings.json', 'r', encoding='utf-8') as fr:
        json_data = json.load(fr)
        json_data["jpg_quality"] = str(jpg)
        json_data["png_quality"] = str(png)
        json_data["webp_quality"] = str(webp)
        json_data["DCT_Block"] = str(dct_block)
        json_data['Baidu_Api']['APP_ID'] = app_id
        json_data['Baidu_Api']['API_KEY'] = api_key
        json_data['Baidu_Api']['SECRET_KEY'] = secret_key
        json_data['Baidu_Api']['WORDS_MODEL'] = str(words_model)
    with open('./settings.json', 'w', encoding='utf-8') as fw:
        json.dump(json_data, fw, ensure_ascii=False)
    fw.close()
    fr.close()


def baidu_ocr_words(path):
    with open('./settings.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        app_id = json_data['Baidu_Api']['APP_ID']
        api_key = json_data['Baidu_Api']['API_KEY']
        secret_key = json_data['Baidu_Api']['SECRET_KEY']
        words_model = int(json_data['Baidu_Api']['WORDS_MODEL'])
    f.close()
    client = AipOcr(app_id, api_key, secret_key)
    if path.startswith('http'):
        if words_model == 1:
            json_data = client.basicGeneralUrl(path)
            return baidu_ocr_words_tostring(json_data)
        elif words_model == 2:
            json_data = client.basicGeneralUrl(path)
            return baidu_ocr_words_tostring(json_data)
        elif words_model == 3:
            json_data = client.enhancedGeneralUrl(path)
            return baidu_ocr_words_tostring(json_data)

    else:
        with open(path, 'rb') as fp:
            img = fp.read()
        if words_model == 1:
            json_data = client.basicGeneral(img)
            return baidu_ocr_words_tostring(json_data)
        elif words_model == 2:
            json_data = client.basicAccurate(img)
            return baidu_ocr_words_tostring(json_data)
        elif words_model == 3:
            json_data = client.enhancedGeneral(img)
            return baidu_ocr_words_tostring(json_data)
        else:
            pass


def baidu_ocr_words_tostring(json_data):
    words = ""
    length = int(json_data['words_result_num'])
    for i in range(length):
        words = words + json_data['words_result'][i]['words']
    return words
