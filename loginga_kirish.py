from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QMainWindow, QVBoxLayout, QApplication,
                             QLineEdit, QPushButton, QMessageBox, QLabel)


class LogingaKirish(QMainWindow):
    def __init__(self):
        super().__init__()

        vertikal = QVBoxLayout()

        label = QLabel("Siz tizimga muvaffaqiyatli kirdingiz")
        vertikal.addWidget(label)

        widjet = QWidget()
        widjet.setLayout(vertikal)
        self.setCentralWidget(widjet)
