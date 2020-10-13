import random
import numpy as np


class CvPixelNoise:

    # 图像添加椒盐噪声
    @staticmethod
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

    # 图像添加高斯噪声
    @staticmethod
    def img_gaussian_noise(img, mean=0, var=0.001):
        img = np.array(img / 255, dtype=float)
        noise = np.random.normal(mean, var ** 0.5, img.shape)
        img_noise = img + noise

        img_noise = np.clip(img_noise, 0, 1.0)
        img_noise = np.uint8(img_noise * 255)

        return img_noise
