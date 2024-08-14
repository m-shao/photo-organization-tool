from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
import os.path


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Images with QLabel")
        self.setMinimumSize(800, 800)

        image_label = QLabel()

        curr_dir = os.path.dirname(os.path.realpath(__file__))
        file_name = os.path.join(curr_dir, "images/minions.png")
        image_label.setPixmap(QPixmap(file_name))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)