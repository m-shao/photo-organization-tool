# Version 2: Signals and Slots
from PySide6.QtWidgets import QApplication, QPushButton
import sys


def button_clicked(data):
    print(f"YOU CLICKED: {data}")


app = QApplication(sys.argv)

button = QPushButton("PRESS ME")
button.setCheckable(True)
button.clicked.connect(button_clicked)

button.show()
app.exec()