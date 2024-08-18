from PySide6.QtWidgets import QLineEdit, QApplication, QLabel, QPushButton, QListWidget, QMainWindow, QStatusBar, QToolBar, QHBoxLayout, QVBoxLayout, QWidget, QSizePolicy
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon, QPalette, QColor, QPixmap

from Widgets.RatingWidget import StarRatingWidget
from Widgets.CaptionEditorWidget import CaptionEditorWidget
from Widgets.ImageDisplayWidget import ImageDisplayWidget

import sys
import os

current_image = "assets/Ben.JPG"

current_dir = os.getcwd()
current_image_path = os.path.join(current_dir, current_image)


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")

        # initiate menu
        menu_bar = self.menuBar()

        # create menu options
        file_menu = menu_bar.addMenu("File")
        # add actions to the menu with a signal
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        # add actions to the menu
        # edit_menu.addAction("Copy")
        # edit_menu.addAction("Cut")
        # edit_menu.addAction("Paste")
        # edit_menu.addAction("Undo")
        # edit_menu.addAction("Redo")

        menu_bar.addMenu("Help")

        # toolbars
        toolbar = QToolBar("Toolbar")

        status_bar = QStatusBar(self)
        self.setStatusBar(status_bar)

        main_layout = QVBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        rating_bar = StarRatingWidget()

        star_layout = QHBoxLayout()
        star_layout.addWidget(rating_bar)
        star_widget_container = QWidget()
        star_widget_container.setLayout(star_layout)
        star_widget_container.setStyleSheet(f"background-color:#282828; border-radius:{rating_bar.height()}")
        star_widget_container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        caption_editor = CaptionEditorWidget(current_image_path, rating_bar.height())

        rating_caption_layout = QHBoxLayout()
        rating_caption_layout.addWidget(star_widget_container, 1)
        rating_caption_layout.addWidget(caption_editor, 5)

        image_display = ImageDisplayWidget(current_image_path)

        # image.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        main_layout.addWidget(image_display)
        main_layout.addLayout(rating_caption_layout)
        main_layout.setSpacing(4)

        self.setLayout(main_layout)

        self.setCentralWidget(central_widget)


    def quit_app(self):
        self.app.quit()
    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app", 3000)

    def button1_clicked(self):
        self.statusBar().showMessage("BUTTON WAS PRESSED", 1000)

def main():
    app = QApplication(sys.argv)

    window = MainWindow(app)
    window.setStyleSheet('background-color:#4D4D4D; color:white;')
    window.show()

    app.exec()


if __name__ == "__main__":
    main()