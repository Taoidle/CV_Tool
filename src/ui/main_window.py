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
import json, os
from ui.toolbox import ToolBox
from ui.pic_widget import PicWidget
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, QMenu, QHBoxLayout, QTabWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from util.basic import CvBasic as cvb


class MainWindow(QMainWindow, QWidget):

    def init_default_statusbar(self):
        # 初始化工具栏
        self.statusBar()
        # 打开图片文件
        self.open_pic = QAction('打开图片', self)
        self.open_pic.setShortcut('Ctrl+O')
        # 保存图片
        self.save_pic = QAction('保存图片', self)
        # 清除图片
        self.clear_pic = QAction('清空图片', self)
        # 设置
        self.program_setting = QAction('设置', self)
        # 退出
        func_exit = QAction('退出', self)
        func_exit.setShortcut('Esc')
        func_exit.triggered.connect(QCoreApplication.instance().quit)
        # 添加File菜单&子菜单
        file_menubar = self.menuBar()
        file_menu = file_menubar.addMenu('文件')
        file_menu.addAction(self.open_pic)
        file_menu.addAction(self.save_pic)
        file_menu.addAction(self.clear_pic)
        file_menu.addAction(self.program_setting)
        file_menu.addAction(func_exit)
        # 图像处理菜单
        pic_menubar = self.menuBar()
        pic_menu = pic_menubar.addMenu("图像处理")
        # 当前图片计算
        cal_now_menu = QMenu('当前图像计算', self)
        # 计算MSE
        self.cal_now_mse = QAction('计算MSE', self)
        # 计算PSNR
        self.cal_now_psnr = QAction('计算PSNR', self)
        # 计算SSIM
        self.cal_now_ssim = QAction('计算SSIM', self)
        cal_now_menu.addAction(self.cal_now_mse)
        cal_now_menu.addAction(self.cal_now_psnr)
        cal_now_menu.addAction(self.cal_now_ssim)
        # 外部图片计算
        cal_import_menu = QMenu('外部图像计算', self)
        # 计算MSE
        self.cal_import_mse = QAction('计算MSE', self)
        self.cal_import_mse.setStatusTip('先导入原图再导入效果图')
        # 计算PSNR
        self.cal_import_psnr = QAction('计算PSNR', self)
        self.cal_import_psnr.setStatusTip('先导入原图再导入效果图')
        # 计算SSIM
        self.cal_import_ssim = QAction('计算SSIM', self)
        self.cal_import_ssim.setStatusTip('先导入原图再导入效果图')
        cal_import_menu.addAction(self.cal_import_mse)
        cal_import_menu.addAction(self.cal_import_psnr)
        cal_import_menu.addAction(self.cal_import_ssim)
        # 显示rgb分量和直方图
        self.show_his_rgb = QAction('显示RGB分量', self)
        # 显示直方图
        self.show_plt_his = QAction('显示直方图', self)
        self.show_plt_his.setShortcut('Shift+P')
        pic_menu.addAction(self.show_plt_his)
        pic_menu.addMenu(cal_now_menu)
        pic_menu.addMenu(cal_import_menu)
        pic_menu.addAction(self.show_his_rgb)
        # 百度OCR文字提取
        baidu_ocr_words = QAction('百度OCR文字提取 ', self)
        pic_menu.addAction(baidu_ocr_words)
        # 添加Help菜单&子菜单
        help_menubar = self.menuBar()
        help_menu = help_menubar.addMenu("帮助")
        document_introduce = QAction('介绍', self)
        document_help = QAction('帮助文档', self)
        about_cv_tool = QAction('关于CV Tool', self)
        help_menu.addAction(document_introduce)
        help_menu.addAction(document_help)
        help_menu.addAction(about_cv_tool)

    def init_default_window_widget(self):
        # 初始化左侧工具箱
        self.tool_box = ToolBox()
        self.tool_box.init_default_box()
        self.tool_box.setFixedWidth(300)
        # 初始化图像显示区
        self.current_pic_widget = PicWidget()
        self.current_pic_widget.init_default_wid()
        self.current_pic_widget.pic_label.setText('当前图像')
        self.last_pic_widget = PicWidget()
        self.last_pic_widget.init_default_wid()
        self.last_pic_widget.pic_label.setText('上一步图像')
        # 初始化图像显示区布局
        self.pic_wid_h_box = QHBoxLayout()
        self.pic_wid_h_box.addWidget(self.tool_box)
        self.pic_wid_h_box.addWidget(self.current_pic_widget)
        self.pic_wid_h_box.addWidget(self.last_pic_widget)
        self.pic_wid = QWidget()
        self.pic_wid.setLayout(self.pic_wid_h_box)
        # 初始化一个Tab窗口
        self.tab_wid = QTabWidget()
        # 将上面窗口添加到Tab窗口中
        self.tab_wid.addTab(self.pic_wid, '图像处理')
        self.tab_wid.setStyleSheet("background-color:#f0f0f0")
        # 初始化一个水平布局
        h_box = QHBoxLayout()
        # 将Tab窗口添加到布局中
        h_box.addWidget(self.tab_wid)
        # 添加当前窗口布局
        self.setLayout(h_box)
        self.setCentralWidget(self.tab_wid)

        self.current_pic_widget.pic_show_label.setScaledContents(True)
        self.last_pic_widget.pic_show_label.setScaledContents(True)

    def init_default_window_setting(self):
        # 设置窗口标题
        self.setWindowTitle('CV Tools')
        self.setWindowIcon(QIcon('res/img/logo.png'))
        # 设置窗口只有最小化和关闭
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

    # 初始化默认设置
    @staticmethod
    def init_default_setting():
        # 目录检查
        cvb.check_dir('res/embed_img/')
        cvb.check_dir('res/img/')
        json_path = 'settings.json'
        if not os.path.exists(json_path):
            os.system(r'touch %s' % json_path)
            json_dict = {"jpg_quality": "80", "png_quality": "3", "webp_quality": "80", "DCT_Block": "8",
                         "Baidu_Api": {"APP_ID": "",
                                       "API_KEY": "",
                                       "SECRET_KEY": "",
                                       "WORDS_MODEL": "1"}
                         }
            with open("./settings.json", "w", encoding='utf-8') as f:
                f.write(json.dumps(json_dict, ensure_ascii=False))
            f.close()
