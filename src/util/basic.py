import json, os


class CvBasic:

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
