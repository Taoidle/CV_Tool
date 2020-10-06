import json, os, cv2, time
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from skimage import io


class CvBasic(QWidget):

    # 目录校验
    @staticmethod
    def check_dir(path):
        if not os.path.exists(path):
            os.makedirs(path)

    # 读取设置
    @staticmethod
    def get_settings():
        with open('settings.json', 'r', encoding='utf-8') as fr:
            json_data = json.load(fr)
            default_jpeg_quality = int(json_data["jpg_quality"])
            default_png_quality = int(json_data["png_quality"])
            default_webp_quality = int(json_data["webp_quality"])
        fr.close()
        return default_jpeg_quality, default_png_quality, default_webp_quality

    # 写入设置
    @staticmethod
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

    # 显示图像
    @staticmethod
    def get_pic(file_name):
        # # 调用存储文件
        # file_name, tmp = QFileDialog.getOpenFileName(self, '打开图片', 'picture', '*.png *.jpg *.bmp *.jpeg *tif')
        # if file_name == '':
        #     return
        # 采用OpenCV函数读取数据
        img = io.imread(file_name)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        if img.size == 1:
            return
        else:
            return img

    # 图像保存
    @staticmethod
    def create_default_filename(prefix: str, suffix: str):
        filename = prefix + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())) + suffix
        return filename

    # 图像保存
    @staticmethod
    def save_pic(file_name, img):
        if file_name != '':
            if file_name.endswith('.jpg'):
                cv2.imwrite(file_name, img, [int(cv2.IMWRITE_JPEG_QUALITY), self.default_jpeg_quality])
            elif file_name.endswith('.png'):
                cv2.imwrite(file_name, img, [int(cv2.IMWRITE_PNG_COMPRESSION), self.default_png_quality])
            elif file_name.endswith('.webp'):
                cv2.imwrite(file_name, img, [int(cv2.IMWRITE_WEBP_QUALITY), self.default_webp_quality])
            else:
                cv2.imwrite(file_name, img)
        else:
            pass

    # 图像显示
    @staticmethod
    def show_pic(img, space: QLabel):
        # 将OpenCV下的image转换成QImage
        q_img, width, height = CvBasic.img_cv2qt(img)
        # 对显示的图像宽高进行缩小
        width, height = CvBasic.shrink_len(width, height)
        pix_map = QPixmap.fromImage(q_img)
        # 设置图像维持原来比例
        fit_pix_map = pix_map.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # 重置Label大小
        space.resize(width, height)
        space.setPixmap(fit_pix_map)
        return width, height


    @staticmethod
    def img_cv2qt(img):
        if len(img.shape) == 3:
            # 提取图像的通道和尺寸，用于将OpenCV下的image转换成QImage
            height, width, channel = img.shape
            bytes_perline_1 = 3 * width
            # 对cv图像进行转换
            q_img = QImage(img.data, width, height, bytes_perline_1, QImage.Format_RGB888).rgbSwapped()
            return q_img, width, height
        else:
            # 将当前图像转换位BGR图像
            height, width = img.shape
            # 对cv图像进行转换
            q_img = QImage(img.data, width, height, width, QImage.Format_Grayscale8)
            return q_img, width, height

    @staticmethod
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
