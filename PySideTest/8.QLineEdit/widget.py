from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and QLineEdit")

        label = QLabel("Fullname: ")
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.text_changed)
        self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Grab Data")
        button.clicked.connect(self.button_clicked)

        self.text_holder_label = QLabel("I AM HERE")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)

    # Slots
    def button_clicked(self):
        self.text_holder_label.setText(f"Fullname: {self.line_edit.text()}")

    def text_changed(self):
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_position_changed(self, old_pos, new_pos):
        print(f"Old Position: {old_pos} \nNew Position: {new_pos}")

    def editing_finished(self):
        print("Editing Finished: Enter Pressed")

    def selection_changed(self):
        print("Selection Changed: ", self.line_edit.selectedText())

    def text_edited(self, new_text):
        print(f"New Text: {new_text}")