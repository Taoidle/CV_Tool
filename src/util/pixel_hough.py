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


class CvPixelHough:

    @staticmethod
    def img_houghlines(current_img, origin_img, rho, theta, threshold):
        img_temp = origin_img
        # 霍夫变换返回的就是极坐标系中的两个参数  rho和 theta
        lines = cv2.HoughLines(current_img, rho, np.pi / theta, threshold)
        # 将数据转换到二维
        lines = lines[:, 0, :]
        for rho, theta in lines:
            a = np.cos(theta)
            b = np.sin(theta)
            # 从图b中可以看出x0 = rho x cos(theta)
            #             y0 = rho x sin(theta)
            x0 = a * rho
            y0 = b * rho
            # 由参数空间向实际坐标点转换
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * a)
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * a)
            cv2.line(img_temp, (x1, y1), (x2, y2), (0, 0, 255), 1)
        return img_temp

    @staticmethod
    def img_houghlines_p(current_img, origin_img, rho, theta, threshold):
        img_temp = origin_img
        lines = cv2.HoughLinesP(current_img, rho, np.pi / theta, threshold)
        lines = lines[:, 0, :]
        for x1, y1, x2, y2 in lines:
            cv2.line(img_temp, (x1, y1), (x2, y2), (0, 0, 255), 1)
        return img_temp

    @staticmethod
    def img_houghcircles(img_1, img_2, dp, minDist, param1, parma2, minRadius, maxRadius):
        circles1 = cv2.HoughCircles(img_1, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=parma2,
                                    minRadius=minRadius, maxRadius=maxRadius)
        circles = circles1[0, :, :]
        circles = np.uint16(np.around(circles))
        for i in circles[:]:
            cv2.circle(img_2, (i[0], i[1]), i[2], (0, 255, 0), 3)
            cv2.circle(img_2, (i[0], i[1]), 2, (255, 0, 255), 10)
        return img_2
