"""
This example is about opencv with pyqt5

Aauthor: kaiyang
Website: www.lkyblog.cn git.lkyblog.cn
Last edited: April 2020

"""

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QCheckBox, QLineEdit,
                             QAction, QFileDialog, QApplication, QDesktopWidget, QMenu, QMessageBox, QInputDialog,
                             QPushButton, QGridLayout)
from PyQt5.QtGui import QIcon, QImage, QPixmap

import cv2, util, sys, webbrowser, ui, time


class MainWindow(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar()
        self.tools_window = ui.ToolsWindow()
        self.tools_window.setMaximumWidth(200)

        self.label_show = QLabel()
        self.label_show.setText('This is a Picture Label')


        self.grid = QGridLayout()
        self.grid.addWidget(self.tools_window, 1, 1)
        self.grid.addWidget(self.label_show, 1, 2)

        self.wid_get = QWidget()
        self.wid_get.setLayout(self.grid)
        self.setCentralWidget(self.wid_get)
        self.resize(720, 480)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
