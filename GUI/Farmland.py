from PyQt5.QtWidgets import (QLabel, QGridLayout, QWidget)


class Farmland(QWidget):
    def __init__(self, index):
        super().__init__()

        self.id = index
        self.num_plant = 4
        self.plants = []
        self.defend_strength = 20

        self._initialize()

    def _initialize(self):
        self.setGeometry(500, 500, 400, 400)
        self.setWindowTitle(f"Farmland{self.id}")
        self._generate_plants()
        self.show()

    def _generate_plants(self):
        if len(self.plants) != 0:
            self.plants = []
        for i in range(self.num_plant):
            tmp = QLabel()
            tmp.setFixedSize(100, 100)
            tmp.setStyleSheet(
                "background-color: green; border: 3px solid green; border-radius: 50px")

            self.plants.append(tmp)

        self._draw_plants()

    def _draw_plants(self):
        self.layout = QGridLayout()
        i = 0
        j = 0
        for plant in self.plants:
            self.layout.addWidget(plant, i, j)
            j += 1
            if j > 1:
                j = 0
                i += 1

        self.setLayout(self.layout)
