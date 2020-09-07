#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 9:45
# @Author  : 柠檬菠萝
# @Email   : yzpmihome@vip.qq.com
# @File    : main.py

import sys
from PyQt5.QtWidgets import QApplication
from PyLib.Controller import MainWin

app = QApplication(sys.argv)
main_window = MainWin()
main_window.show()
app.exit(app.exec())