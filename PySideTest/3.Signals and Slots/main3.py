# Version 3: Signals and Slots

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider
import sys


def respond_to_slider(data):
    print(f"slider moved to {data}")


app = QApplication(sys.argv)

slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(respond_to_slider)
slider.show()

app.exec()
