from PySide6.QtWidgets import QWidget, QGroupBox, QCheckBox, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTabWidget


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTabs")

        tab_widget = QTabWidget(self)

        widget_form = QWidget()
        full_name_label = QLabel("Full Name: ")
        full_name_line_edit = QLineEdit()

        h_layout = QHBoxLayout()
        h_layout.addWidget(full_name_label)
        h_layout.addWidget(full_name_line_edit)

        widget_form.setLayout(h_layout)

        widget_buttons = QWidget()
        button_1 = QPushButton("Button 1")
        button_1.clicked.connect(self.button_1_clicked)
        button_2 = QPushButton("Button 2")
        button_2.clicked.connect(self.button_2_clicked)
        button_3 = QPushButton("Button 3")
        button_3.clicked.connect(self.button_3_clicked)

        v_layout = QVBoxLayout()
        v_layout.addWidget(button_1)
        v_layout.addWidget(button_2)
        v_layout.addWidget(button_3)

        widget_buttons.setLayout(v_layout)

        tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_buttons, "Buttons")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)

    def button_1_clicked(self):
        print("button_1_clicked")

    def button_2_clicked(self):
        print("button_2_clicked")

    def button_3_clicked(self):
        print("button_3_clicked")

