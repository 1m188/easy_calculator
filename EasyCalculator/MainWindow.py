from PySide2.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton, QGridLayout
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont


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
        self.resize(500, 600)

        #移动到屏幕中央
        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

        #布局
        layout = QGridLayout(self)

        #表达式输入文本框
        inputTextEdit = QTextEdit(self)
        inputTextEdit.setReadOnly(True)
        inputTextEdit.setContextMenuPolicy(Qt.NoContextMenu)
        inputTextEdit.viewport().setCursor(Qt.ArrowCursor)
        layout.addWidget(inputTextEdit, 0, 0, 1, 4)

        #各种数字按钮
        for i in range(10):
            button = QPushButton(self)
            button.setObjectName(str(i))
            button.setFont(QFont("微软雅黑", 20))
            button.setText(str(i))
            if i == 0:
                layout.addWidget(button, 4, 1, 1, 1)
            elif i >= 1 and i <= 3:
                layout.addWidget(button, 3, i - 1, 1, 1)
            elif i >= 4 and i <= 6:
                layout.addWidget(button, 2, i - 4, 1, 1)
            elif i >= 7 and i <= 9:
                layout.addWidget(button, 1, i - 7, 1, 1)

        #各种符号按钮
        for i in ["+", "-", "*", "/", "="]:
            button = QPushButton(self)
            button.setObjectName(i)
            button.setFont(QFont("微软雅黑", 20))
            button.setText(i)
            if i == "+":
                layout.addWidget(button, 1, 3, 1, 1)
            elif i == "-":
                layout.addWidget(button, 2, 3, 1, 1)
            elif i == "*":
                layout.addWidget(button, 3, 3, 1, 1)
            elif i == "/":
                layout.addWidget(button, 4, 3, 1, 1)
            elif i == "=":
                layout.addWidget(button, 4, 2, 1, 1)
