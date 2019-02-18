from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import Qt


#主窗口
class MainWindow(QWidget):
    def __init__(self):
        super().__init__(None)

        #设置窗口属性
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setAttribute(Qt.WA_QuitOnClose, True)

        #设置窗口样式
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        #设置窗口大小和标题
        self.setWindowTitle("简单四则运算器")
        self.setFixedSize(500, 600)

        #移动到屏幕中央
        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())
