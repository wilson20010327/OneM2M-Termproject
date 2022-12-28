import sys

from PyQt5.QtWidgets import QApplication
import MainWindow

if __name__ == '__main__':

    app = QApplication([])
    mainwindow = MainWindow.MainWindow()
    sys.exit(app.exec_())
