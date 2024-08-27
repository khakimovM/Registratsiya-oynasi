from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QMainWindow, QVBoxLayout, QApplication,
                             QLineEdit, QPushButton, QMessageBox)
from regisga_kirish import RegisgaKirish


class Regis(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.setWindowTitle("Registratsiya oynasi")

        vertikal = QVBoxLayout()

        self.ism = QLineEdit()
        self.ism.setPlaceholderText("Ism")
        vertikal.addWidget(self.ism)

        self.familiya = QLineEdit()
        self.familiya.setPlaceholderText("Familiya")
        vertikal.addWidget(self.familiya)

        self.pochta = QLineEdit()
        self.pochta.setPlaceholderText("Email")
        vertikal.addWidget(self.pochta)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        vertikal.addWidget(self.password)

        tugma = QHBoxLayout()

        ok = QPushButton("Ro'yxatdan o'tish")
        ok.clicked.connect(self.bosildi)
        tugma.addWidget(ok)

        cansel = QPushButton("Ortga qaytish")
        cansel.clicked.connect(self.close_login)
        tugma.addWidget(cansel)

        vertikal.addLayout(tugma)

        widjet = QWidget()
        widjet.setLayout(vertikal)
        self.setCentralWidget(widjet)

        self.yangi_oyna = None

    def bosildi(self):

        if "@gmail.com" in self.pochta.text():
            malumot = {
                "ism": self.ism.text(),
                "familiya": self.familiya.text(),
                "email": self.pochta.text(),
                "password": self.password.text()
            }
            import json
            with open("malumotlar.json") as file:
                server = json.load(file)

            with open("malumotlar.json", "w") as file:
                server.append(malumot)

                json.dump(server, file, indent=4)

            self.hide()
            self.yangi_oyna = RegisgaKirish(self)
            self.yangi_oyna.show()
        else:
            QMessageBox.warning(self, "Xatolik oynasi", "Email kiritishda xatolik bor")


    def close_login(self):
        self.close()
        self.main_window.show()

