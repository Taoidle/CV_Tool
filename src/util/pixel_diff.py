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
from skimage.metrics import structural_similarity


class CvPixelDiff:

    # MSE
    @staticmethod
    def get_mse(origin_img, target_img):
        diff = origin_img.astype("float") - target_img.astype("float")
        return np.square(diff).sum() / (origin_img.shape[0] * origin_img.shape[1])

    # PSNR
    @staticmethod
    def get_psnr(origin_img, target_img, max_val=256):
        diff = origin_img.astype(np.float32) - target_img.astype(np.float32)
        MSE = np.sum(np.mean((np.power(diff, 2))))
        if MSE < 1.0e-10:
            return 100

        psnr = -10 * np.log10(MSE / ((max_val - 1.0) ** 2))
        return psnr

    # SSIM
    @staticmethod
    def get_ssim(origin_img, target_img):
        if len(origin_img.shape) == 3:
            origin_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
        if len(target_img.shape) == 3:
            target_img = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
        ssim = structural_similarity(origin_img, target_img)
        return ssim
