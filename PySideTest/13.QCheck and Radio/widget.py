from PySide6.QtWidgets import QWidget, QGroupBox, QCheckBox, QVBoxLayout, QHBoxLayout, QButtonGroup, QRadioButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        # Checkboxes : operating system
        os = QGroupBox("Choose operating system")

        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)

        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)

        # Exclusive checkboxes : Drinks
        drinks = QGroupBox("Choose your drink")

        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffe = QCheckBox("Coffe")
        beer.setChecked(True)

        # Make the checkboxes exclusive
        exclusive_button_group = QButtonGroup(self)  # The self parent is needed here.
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffe)
        exclusive_button_group.setExclusive(True)
        exclusive_button_group.buttonClicked.connect(self.exclusive_button_group_clicked)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffe)
        drinks.setLayout(drink_layout)

        # Radio buttons : answers
        answers = QGroupBox("Choose Answer")
        radio_group = QButtonGroup(self)
        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")
        answer_a.setChecked(True)
        radio_group.addButton(answer_a)
        radio_group.addButton(answer_b)
        radio_group.addButton(answer_c)
        radio_group.buttonClicked.connect(self.exclusive_button_group_clicked)

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)
        answers.setLayout(answers_layout)

        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answers)

        self.setLayout(v_layout)

    def windows_box_toggled(self, checked):
        if (checked):
            print("Windows box checked")
        else:
            print("Windows box unchecked")

    def linux_box_toggled(self, checked):
        if (checked):
            print("Linux box checked")
        else:
            print("Linux box unchecked")

    def mac_box_toggled(self, checked):
        if (checked):
            print("Mac box checked")
        else:
            print("Mac box unchecked")

    def exclusive_button_group_clicked(self, button):
        print(button.text())