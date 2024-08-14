from PySide6.QtWidgets import QApplication
from widget import Widget

app = QApplication()

widget = Widget()
widget.show()

app.exec()
