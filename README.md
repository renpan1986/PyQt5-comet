# PyQt5 开发框架

## 简介：

采用pyqtSlot+QMutex+QThread+pyqtSignal研发的多线程使用框架。

## 安装方法：
```shell script
pip install -i https://test.pypi.org/simple/ PyQt5-comet --prefix="我的项目路径"
复制Lib\site-packages\PyLib和Lib\site-packages\main.py到项目根目录，即可开始使用。
```

## 需要支持模块：
```shell script
pip install pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyqt5-tools -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 安装教程：

首先执行安装PyQt5模块。
```shell script
pip install pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyqt5-tools -i https://pypi.tuna.tsinghua.edu.cn/simple
```

然后执行：
```shell script
pip install -i https://test.pypi.org/simple/ PyQt5-comet --prefix="我的项目路径"
or
pip install PyQt5-comet --prefix="我的项目路径"
```

最后将Lib\site-packages\PyLib和Lib\site-packages\main.py复制到项目根目录运行main.py。

## 使用教程

### 目录结构为：
```
-PyLib
    Controller.py
    MainUi.py
    Module-Test.py
    ProgramManagement.py
    MainUi.ui
main.py
```

### 模块介绍：
main.py 启动GUI
Controller.py 控制器
MainUi.py GUI界面
Module-Test.py 测试模块
ProgramManagement.py 多线程和模块加载器

### 开发教程

开发好需要完成的逻辑，固定class RunModule 方法update 返回值为字符串。

```python
class RunModule:
    def __init__(self, tmp_dict):
        self.log = tmp_dict.get("log")
        pass

    def update(self):
        return self.log
        pass
```

在控制器中加载，name="Module-Test" 是需要加载的模块名称，log=str("TEST LOG PRINT") 是传递的参数。
connect(self._lookTestsLog)是回调函数。

```python
@pyqtSlot()
    def on_pushButton_clicked(self):
        self.q.lock()
        self.runCmd_ = runCmd(name="Module-Test", log=str("TEST LOG PRINT"))
        self.runCmd_.cmdsign.connect(self._lookTestsLog)
        self.runCmd_.start()
        self.runCmd_.wait()
        self.q.unlock()
    def _lookTestsLog(self, log):
        self.label.setText(log)
```

最后运行main.py即可。
