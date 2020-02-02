from PySide2.QtWidgets import QApplication
import sys
from MainWindow import MainWindow

app = QApplication(sys.argv)

mainWindow = MainWindow()
mainWindow.show()

app.exec_()
