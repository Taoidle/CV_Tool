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
import matplotlib.pyplot as plt
import PIL.Image as Image


class CvPixelPlt:

    # plt图像格式转为opencv格式
    @staticmethod
    def plt2cv(fig):
        fig.canvas.draw()
        w, h = fig.canvas.get_width_height()
        # buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
        # buf.shape = (w, h, 4)
        # buf = np.roll(buf, 3, axis=2)
        # image = Image.frombytes("RGBA", (w, h), buf.tostring())
        buf = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8)
        buf.shape = (w, h, 3)
        buf = np.roll(buf, 3)
        image = cv2.cvtColor(np.array(Image.frombytes("RGB", (w, h), buf.tostring())), cv2.COLOR_RGBA2BGR)
        return image

    # 灰度图像直方图
    @staticmethod
    def img_his_gray(img):
        fig = plt.figure(figsize=(4, 3))
        x_index = list(np.arange(0, 256))
        histr = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
        histr = list(histr.astype(np.uint8).reshape((1, 256))[0])
        plt.bar(x_index, histr, 1, color='gray')
        w, h = fig.canvas.get_width_height()
        fig = CvPixelPlt.plt2cv(fig)
        return fig

    # 彩色图像直方图
    @staticmethod
    def img_his_rgb(img):
        x_index = list(np.arange(0, 256))
        color = ('blue', 'green', 'red')
        fig = plt.figure(figsize=(4, 3))
        for i, c in enumerate(color):
            histr = cv2.calcHist(images=[img], channels=[i], mask=None, histSize=[256], ranges=[0, 256])
            histr = list(histr.astype(np.uint32).reshape((1, 256))[0])
            plt.bar(x_index, histr, 1, color=c)
        plt.legend(('B', 'G', 'R'), loc='upper right')
        w, h = fig.canvas.get_width_height()
        fig = CvPixelPlt.plt2cv(fig)
        return fig
