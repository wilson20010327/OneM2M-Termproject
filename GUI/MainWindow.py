from PyQt5.QtWidgets import (
    QLabel, QPushButton, QMainWindow, QVBoxLayout, QWidget, QDesktopWidget, QApplication, QStyleFactory, QGridLayout, QGroupBox, QComboBox, QLineEdit)
from PyQt5.QtGui import QFont

import utils


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.height = 400
        self.width = 600

        # window setting
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle("IoT final project")
        app_font = QFont("Courier New", 11)
        app_font.setBold(True)
        QApplication.setFont(app_font)

        # set window style
        QApplication.setStyle(QStyleFactory.create("Fusion"))

        self.start_simulation_btn = QPushButton("Start pest event", self)
        self.start_simulation_btn.setGeometry(200, 250, 200, 100)

        self.generate_farmland_btn = QPushButton("Generate Farmland", self)
        self.generate_farmland_btn.setGeometry(200, 100, 200, 100)

        # mainLayout.addWidget(self.generate_farmland_btn)

        # maincontainer = QWidget()
        # maincontainer.setLayout(mainLayout)

        # self.setCentralWidget(maincontainer)
        self.move_to_center()

        self.show()

        # bind btns to
        self.bindBtns()

    def move_to_center(self):
        # get the geometry (QRect) of mainwindow
        geo = self.frameGeometry()
        # get the center point of screen
        center_p = QDesktopWidget().availableGeometry().center()
        # move the center of QRect object to screen center
        geo.moveCenter(center_p)
        # move the topleft of mainwindow to the QRect object's topleft
        self.move(geo.topLeft())

    def bindBtns(self):
        self.generate_farmland_btn.clicked.connect(utils.generate_Farmland)
        self.start_simulation_btn.clicked.connect(utils.pest_event)
