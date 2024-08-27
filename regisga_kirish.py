from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QMainWindow, QVBoxLayout, QApplication,
                             QLineEdit, QPushButton, QMessageBox, QLabel)


class RegisgaKirish(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        label = QLabel("Tabriklaymiz, siz muvaffaqiyatli ro'yxatdan o'tdingiz")
        verikal = QVBoxLayout()
        verikal.addWidget(label)

        btn = QPushButton("Asosiy oynaga qaytish")
        verikal.addWidget(btn)
        btn.clicked.connect(self.bosildi)

        widjet = QWidget()
        widjet.setLayout(verikal)
        self.setCentralWidget(widjet)

    def bosildi(self):
        self.close()
        self.parent.main_window.show()
