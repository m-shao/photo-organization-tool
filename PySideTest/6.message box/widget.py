from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")
        self.setMinimumSize(300, 200)

        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)


    def button_clicked_hard(self):  # the hard way
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Hard")
        message.setText("This is Hard")
        message.setInformativeText("Do you want to do something about it?")
        # only differnce is the icon we want to show, for ex. QMessageBox.Warning
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)

        # Show the message box
        result = message.exec()
        if result == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Cancel")

    def button_clicked_critical(self):
        result = QMessageBox.critical(self, "Critical", "This is Critical", QMessageBox.Ok | QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Cancel")

    def button_clicked_question(self):
        result = QMessageBox.question(self, "Question?", "This is Question?", QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            print("User chose Yes")
        else:
            print("User chose No")

    def button_clicked_information(self):
        result = QMessageBox.information(self, "Information", "This is Information", QMessageBox.Ok | QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Cancel")

    def button_clicked_warning(self):
        result = QMessageBox.warning(self, "Warning", "This is Warning", QMessageBox.Apply | QMessageBox.Discard)
        if result == QMessageBox.Apply:
            print("User chose Apply")
        else:
            print("User chose Discard")

    def button_clicked_about(self):
        # doesn't return anything
        QMessageBox.about(self, "About", "This is about")

'''
    Types of Message Boxes:
        def about()
        def aboutQt()
        def critical()
        def information()
        def question()
        def standardIcon()
        def warning()
    Types of Standard Buttons:
        QMessageBox.Ok | An “OK” button defined with the AcceptRole .
        QMessageBox.Open | An “Open” button defined with the AcceptRole .
        QMessageBox.Save | A “Save” button defined with the AcceptRole .
        QMessageBox.Cancel | A “Cancel” button defined with the RejectRole .
        QMessageBox.Close | A “Close” button defined with the RejectRole .
        QMessageBox.Discard | A “Discard” or “Don’t Save” button, depending on the platform, defined with the DestructiveRole .
        QMessageBox.Apply | An “Apply” button defined with the ApplyRole .
        QMessageBox.Reset | A “Reset” button defined with the ResetRole .
        QMessageBox.RestoreDefaults | A “Restore Defaults” button defined with the ResetRole .
        QMessageBox.Help | A “Help” button defined with the HelpRole .
        QMessageBox.SaveAll | A “Save All” button defined with the AcceptRole .
        QMessageBox.Yes | A “Yes” button defined with the YesRole .
        QMessageBox.YesToAll | A “Yes to All” button defined with the YesRole .
        QMessageBox.No | A “No” button defined with the NoRole .
        QMessageBox.NoToAll | A “No to All” button defined with the NoRole .
        QMessageBox.Abort | An “Abort” button defined with the RejectRole .
        QMessageBox.Retry | A “Retry” button defined with the AcceptRole .
        QMessageBox.Ignore | An “Ignore” button defined with the AcceptRole .
        QMessageBox.NoButton | An invalid button.
    '''