from PySide2.QtWidgets import QWidget


#主窗口
class MainWindow(QWidget):
    def __init__(self):
        super().__init__(None)

        #设置窗口大小和标题
        self.setWindowTitle("简单四则运算器")
        self.resize(600, 600)
