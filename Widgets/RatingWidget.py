from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QPainter, QPolygon, QColor, QPen
from PySide6.QtCore import QPoint
import PySide6.QtGui as Qt

import threading
from typing import override

from metadata.metadata import set_metadata, read_metadata


class StarButton(QPushButton):
    def __init__(self, index, selected=False):
        super().__init__()
        self.index = index
        self.setFixedSize(15, 15)  # Smaller size for the stars
        self.is_selected = selected

    @override
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
    def __init__(self, current_image_path):
        super().__init__()
        self.current_image_path = current_image_path
        self.setStyleSheet("background-color: #262626;")
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(5, 1, 5, 1)

        self.rating = int(read_metadata(current_image_path, "XMP:Rating", "0"))
        self.stars = []
        for i in range(5):
            star = StarButton(i + 1, i < self.rating)
            star.clicked.connect(self.update_rating)
            star.update()
            self.layout.addWidget(star)
            self.stars.append(star)

        self.show()

    def update_rating(self):
        clicked_star = self.sender()
        rating = clicked_star.index

        for i, star in enumerate(self.stars):
            star.is_selected = (i < rating)
            star.update()

        # show the feedback in the GUI to the user while the metadata changes in the background
        rating_thread = threading.Thread(target=set_metadata, args=(self.current_image_path, "Rating", str(rating)))
        rating_thread.start()

