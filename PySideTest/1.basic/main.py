from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Version 1")

button = QPushButton()
button.setText("PRESS ME")

window.setCentralWidget(button)

window.show()
app.exec()
