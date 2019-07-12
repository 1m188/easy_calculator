from PySide2.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton, QGridLayout, QLabel
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
import ctypes


# 主窗口
class MainWindow(QWidget):
    def __init__(self):
        super().__init__(None)

        # 待计算的表达式字符串
        self.calcStr = ""

        # 获取计算函数
        dll = ctypes.cdll.LoadLibrary("calc.dll")
        dll.calc.restype = ctypes.c_longlong
        self.calcFunc = dll.calc

        # 设置窗口属性
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setAttribute(Qt.WA_QuitOnClose, True)

        # 设置窗口样式
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        # 设置窗口大小和标题
        self.setWindowTitle("简单四则运算器")
        self.resize(500, 600)

        # 移动到屏幕中央
        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

        # 布局
        layout = QGridLayout(self)

        # 表达式输入文本框
        self.inputTextEdit = QTextEdit(self)
        self.inputTextEdit.setFont(QFont("微软雅黑", 20))
        self.inputTextEdit.setReadOnly(True)
        self.inputTextEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.inputTextEdit.viewport().setCursor(Qt.ArrowCursor)
        layout.addWidget(self.inputTextEdit, 0, 0, 1, 4)

        # 各种数字按钮
        for i in range(10):
            button = QPushButton(self)
            button.setObjectName(str(i))
            button.setFont(QFont("微软雅黑", 20))
            button.setText(str(i))
            button.clicked.connect(self.buttonClicked)
            if i == 0:
                layout.addWidget(button, 4, 1, 1, 1)
            elif i >= 1 and i <= 3:
                layout.addWidget(button, 3, i - 1, 1, 1)
            elif i >= 4 and i <= 6:
                layout.addWidget(button, 2, i - 4, 1, 1)
            elif i >= 7 and i <= 9:
                layout.addWidget(button, 1, i - 7, 1, 1)

        # 各种符号按钮
        for i in ["+", "-", "*", "/", "=", "<", "(", ")"]:
            button = QPushButton(self)
            button.setObjectName(i)
            button.setFont(QFont("微软雅黑", 20))
            button.setText(i)
            button.clicked.connect(self.buttonClicked)
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
            elif i == "<":
                layout.addWidget(button, 4, 0, 1, 1)
            elif i == "(":
                layout.addWidget(button, 5, 0, 1, 1)
            elif i == ")":
                layout.addWidget(button, 5, 1, 1, 1)

        # 版本信息
        versionlabel = QLabel(self)
        versionlabel.setAlignment(Qt.AlignCenter)
        versionlabel.setFont(QFont("微软雅黑", 15))
        versionlabel.setText("简易四则运算器-v1.0")
        layout.addWidget(versionlabel, 5, 2, 1, 2)

    # 某个按钮被按下
    def buttonClicked(self):
        senderStr = self.sender().objectName()
        if senderStr == "=":
            # 按下按钮为=时，使用动态链接库里的函数计算结果
            result = self.calcFunc(self.calcStr.encode("utf-8"), len(self.calcStr))
            # 给出结果之后还要另外再加一个回车，防止回退擦除计算结果
            self.inputTextEdit.append(str(result) + '\n')
            self.calcStr = ""
        # 退格
        elif senderStr == "<":
            text = self.inputTextEdit.toPlainText()
            # 不在每一行开头的时候可以回退
            if text != "" and text[-1] != '\n':
                self.calcStr = self.calcStr[:len(self.calcStr) - 1]
                text = text[:len(text) - 1]
                self.inputTextEdit.setText(text)
        # 其他的表达式字符串内容
        else:
            text = self.inputTextEdit.toPlainText()
            text += senderStr
            self.calcStr += senderStr
            self.inputTextEdit.setText(text)
        # 使滑条始终滑到最下方
        scrollBar = self.inputTextEdit.verticalScrollBar()
        if scrollBar:
            scrollBar.setSliderPosition(scrollBar.maximum())
