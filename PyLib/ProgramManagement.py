#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 9:40
# @Author  : 柠檬菠萝
# @Email   : yzpmihome@vip.qq.com
# @File    : ProgramManagement.py

import importlib
from PyQt5.QtCore import QThread, pyqtSignal


class runCmd(QThread):
    cmdsign = pyqtSignal(str)

    def __init__(self, name, **kwargs):
        super().__init__()
        self.tmp_dict = kwargs
        self.name = name
        print(self.tmp_dict)

    def get_return(self):
        a = importlib.import_module("PyLib.{0}".format(self.name))
        res = a.RunModule(self.tmp_dict).update()
        print(res,type(res))
        return res

    def run(self):
        self.cmdsign.emit(self.get_return())