import cv2
import numpy as np


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
    for i in range(num-1):
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
