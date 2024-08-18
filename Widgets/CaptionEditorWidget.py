from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QWidget

from metadata.metadata import read_metadata, set_metadata


class CaptionEditorWidget(QWidget):
    def __init__(self, current_image_path, rating_bar_height):
        super().__init__()
        self.current_image_path = current_image_path
        current_image_caption = read_metadata(self.current_image_path, "EXIF:XPComment", default_value="Caption")

        caption_layout = QHBoxLayout()

        self.caption_box = QLineEdit()
        self.caption_box.setText(current_image_caption)
        self.caption_box.setFixedHeight(rating_bar_height*2 - 4)
        self.caption_box.setTextMargins(4, 0, 0, 0)

        caption_submit_button = QPushButton("Confirm")
        caption_submit_button.setFixedHeight(rating_bar_height*2)
        caption_submit_button.setStyleSheet('background-color:#282828;')
        caption_submit_button.clicked.connect(self.set_caption_metadata)

        caption_layout.addWidget(self.caption_box, 4)
        caption_layout.addWidget(caption_submit_button, 1)

        self.setLayout(caption_layout)



    def set_caption_metadata(self):
        set_metadata(self.current_image_path, "EXIF:XPComment", self.caption_box.text())