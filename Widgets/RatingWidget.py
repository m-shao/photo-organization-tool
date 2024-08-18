from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QPainter, QPolygon, QColor, QPen
from PySide6.QtCore import QPoint

class StarButton(QPushButton):
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.setFixedSize(15, 15)  # Smaller size for the stars
        self.is_selected = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        star_points = [
            QPoint(7, 0), QPoint(9, 5),
            QPoint(15, 5), QPoint(10, 8),
            QPoint(12, 15), QPoint(7, 12),
            QPoint(2, 15), QPoint(4, 8),
            QPoint(0, 5), QPoint(6, 5)
        ]

        star_polygon = QPolygon(star_points)
        painter.setBrush(QColor("#E7D431") if self.is_selected else QColor("#696969"))
        painter.drawPolygon(star_polygon)

class StarRatingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #262626;")
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(5, 1, 5, 1)

        self.stars = []
        for i in range(5):
            star = StarButton(i + 1)
            star.clicked.connect(self.update_rating)
            self.layout.addWidget(star)
            self.stars.append(star)

        self.show()

    def update_rating(self):
        clicked_star = self.sender()
        rating = clicked_star.index

        for i, star in enumerate(self.stars):
            star.is_selected = (i < rating)
            star.update()
