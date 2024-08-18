from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QPixmap, QTransform, QImage
import PySide6.QtCore as Qt

from metadata.metadata import read_metadata


class ImageDisplayWidget(QWidget):
    def __init__(self, current_image_path):
        super().__init__()
        self.size = (read_metadata(current_image_path, "File:ImageWidth", "800"),
                     read_metadata(current_image_path, "File:ImageHeight", "600"))

        # create container that holds the images with a darker background
        container = QWidget()
        container.setFixedSize(1000, 800)
        container.setStyleSheet("background-color:#282828;")

        # create the image
        image = QImage(current_image_path)

        # read image orientation from exif data and set the rotation angle depending
        exif_orientation = int(read_metadata(current_image_path, "EXIF:Orientation"))
        rotation_value = 0
        image_aspect = self.size[1] / self.size[0]
        if exif_orientation == 3:
            rotation_value = 180
        elif exif_orientation == 6:
            rotation_value = 90
            image_aspect = self.size[0] / self.size[1]
        elif exif_orientation == 8:
            rotation_value = 270
            image_aspect = self.size[0] / self.size[1]

        rotated_image = image.transformed(QTransform().rotate(rotation_value))
        rotated_image_pixmap = QPixmap.fromImage(rotated_image)

        # create actual image label(display)
        image_label = QLabel()
        image_label.setPixmap(rotated_image_pixmap)
        image_label.setScaledContents(True)
        # image_label.setMaximumSize(container.width(), container.height())

        # set image to fit in the bounding box despite aspect ratio
        shrink_value = 0.9
        if image_aspect > 1:
            image_label.setFixedHeight(int(container.height() * shrink_value))
            image_label.setFixedWidth(int(container.height()/image_aspect * shrink_value) )
        else:
            image_label.setFixedWidth(int(container.width() * shrink_value))
            image_label.setFixedHeight(int(container.width() * image_aspect * shrink_value) )

        image_layout = QVBoxLayout()
        image_layout.addWidget(image_label)
        image_layout.setAlignment(Qt.Qt.AlignmentFlag.AlignCenter)
        # image_layout.setContentsMargins(100, 25, 100, 25)

        container.setLayout(image_layout)

        image_container_layout = QVBoxLayout()
        image_container_layout.addWidget(container)

        self.setLayout(image_container_layout)
