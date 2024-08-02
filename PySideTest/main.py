# Version 1

# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
# import sys
#
# app = QApplication(sys.argv)
#
# window = QMainWindow()
# window.setWindowTitle("Version 1")
#
# button = QPushButton()
# button.setText("PRESS ME")
#
# window.setCentralWidget(button)
#
# window.show()
# app.exec()


# Version 2
# import sys
# from PySide6.QtWidgets import QApplication
#
# from button_holder import ButtonHolder
#
#
# def main():
#     app = QApplication(sys.argv)
#     window = ButtonHolder()
#     window.show()
#     app.exec()
#
#
# if __name__ == "__main__":
#     main()

# Version 1: Signals and Slots

# from PySide6.QtWidgets import QApplication, QPushButton
# import sys
#
#
# def button_clicked():
#     print("YOU CLICKED")
#
#
# app = QApplication(sys.argv)
#
# button = QPushButton("PRESS ME")
# button.clicked.connect(button_clicked)
#
# button.show()
# app.exec()

# Version 2: Signals and Slots

# from PySide6.QtWidgets import QApplication, QPushButton
# import sys
#
#
# def button_clicked(data):
#     print(f"YOU CLICKED: {data}")
#
#
# app = QApplication(sys.argv)
#
# button = QPushButton("PRESS ME")
# button.setCheckable(True)
# button.clicked.connect(button_clicked)
#
# button.show()
# app.exec()

# Version 3: Signals and Slots

# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QSlider
# import sys
#
#
# def respond_to_slider(data):
#     print(f"slider moved to {data}")
#
#
# app = QApplication(sys.argv)
#
# slider = QSlider(Qt.Horizontal)
# slider.setMinimum(1)
# slider.setMaximum(100)
# slider.setValue(25)
#
# slider.valueChanged.connect(respond_to_slider)
# slider.show()
#
# app.exec()

# Version 1: Widgets

from PySide6.QtWidgets import QApplication
from rock_widget import RockWidget
import sys

app = QApplication(sys.argv)

window = RockWidget()
window.show()

app.exec()