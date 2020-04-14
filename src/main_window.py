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

class MainWindow(QMainWindow,QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

