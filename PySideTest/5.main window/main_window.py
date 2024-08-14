from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar


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
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Settings")
        menu_bar.addMenu("Help")

        # toolbars
        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # add action to toolbar
        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("../start.png"), "Some Other Action", self)
        action2.setStatusTip("Status message for another action")
        # action2.setCheckable(True)
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar_button = QPushButton("Click Here")
        toolbar_button.clicked.connect(self.toolbar_button_click)
        toolbar.addWidget(toolbar_button)

        status_bar = QStatusBar(self)
        self.setStatusBar(status_bar)

        button1 = QPushButton("Central Button")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)

    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app", 3000)

    def button1_clicked(self):
        self.statusBar().showMessage("BUTTON WAS PRESSED", 1000)