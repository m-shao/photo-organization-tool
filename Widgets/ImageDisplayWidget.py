from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap, QTransform, QImage

from metadata.metadata import read_metadata


class ImageDisplayWidget(QWidget):
    def __init__(self, current_image_path):
        super().__init__()
        self.size = (read_metadata(current_image_path, "File:ImageWidth", "800"),
                     read_metadata(current_image_path, "File:ImageHeight", "600"))

        container = QWidget()
        container.setFixedSize(800, 600)
        container.setStyleSheet("background-color:#282828")
        container.setContentsMargins(100, 25, 100, 25)

        image = QImage(current_image_path)

        exif_orientation = int(read_metadata(current_image_path, "EXIF:Orientation"))
        rotation_value = 0
        if exif_orientation == 3: rotation_value = 180
        elif exif_orientation == 6: rotation_value = 90
        elif exif_orientation == 8: rotation_value = 270

        rotated_image = image.transformed(QTransform().rotate(rotation_value))
        rotated_image_pixmap = QPixmap.fromImage(rotated_image)

        image_label = QLabel()
        image_label.setPixmap(rotated_image_pixmap)
        image_label.setScaledContents(True)
        image_label.setMaximumSize(container.width(), container.height())
        image_aspect = self.size[1]/self.size[0]

        if image_aspect > 1:
            image_label.setFixedHeight(container.height())
            image_label.setFixedWidth(int(container.height()*image_aspect))
        else:
            image_label.setFixedWidth(container.width())
            image_label.setFixedHeight(int(container.width() * image_aspect))

        image_layout = QVBoxLayout()
        image_layout.addWidget(image_label)

        container.setLayout(image_layout)

        image_container_layout = QVBoxLayout()
        image_container_layout.addWidget(container)

        self.setLayout(image_layout)
