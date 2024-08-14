# Version 1: Signals and Slots

from PySide6.QtWidgets import QApplication, QPushButton
import sys


def button_clicked():
    print("YOU CLICKED")


app = QApplication(sys.argv)

button = QPushButton("PRESS ME")
button.clicked.connect(button_clicked)

button.show()
app.exec()