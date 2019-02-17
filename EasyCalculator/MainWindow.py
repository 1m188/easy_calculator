from PySide2.QtWidgets import QWidget, QApplication


#主窗口
class MainWindow(QWidget):
    def __init__(self):
        super().__init__(None)

        #设置窗口大小和标题
        self.setWindowTitle("简单四则运算器")
        self.resize(600, 600)

        #移动到屏幕中央
        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())
