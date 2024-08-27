from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QMainWindow, QVBoxLayout, QApplication,
                             QLineEdit, QPushButton, QMessageBox)
from loginga_kirish import LogingaKirish


class Login(QMainWindow):
    def __init__(self, vorislik):
        super().__init__()
        self.vorislik = vorislik

        self.setWindowTitle("Registratsiya oynasi")

        vertikal = QVBoxLayout()

        self.pochta = QLineEdit()
        self.pochta.setPlaceholderText("Email kiriting")
        vertikal.addWidget(self.pochta)

        self.parol = QLineEdit()
        self.parol.setPlaceholderText("password")
        vertikal.addWidget(self.parol)

        btn = QPushButton("Kirish")
        vertikal.addWidget(btn)
        btn.clicked.connect(self.bosildi)

        widjet = QWidget()
        widjet.setLayout(vertikal)
        self.setCentralWidget(widjet)

        self.yangi_oyna = None

    def bosildi(self):
        email = self.pochta.text()
        parol = self.parol.text()
        if len(email) > 11 and len(parol) > 0:

            if "@gmail.com" in email:
                with open("malumotlar.json") as file:
                    import json
                    server = json.load(file)
                    temp = 0
                    for item in server:
                        if item["email"] == email and item["password"] == parol:
                            temp = 1
                        if item["email"] == email and item["password"] != parol:
                            temp = 2
                    if temp == 1:
                        self.hide()
                        self.yangi_oyna = LogingaKirish()
                        self.yangi_oyna.show()
                    elif temp == 0:
                        tanlov = QMessageBox.information(self, "Ogohlantirish", "Siz ro'yxatdan o'tmagansiz", QMessageBox.Ok | QMessageBox.Cancel)
                        if tanlov == QMessageBox.Cancel:
                            self.close()
                            self.vorislik.show()
                    else:
                        QMessageBox.warning(self, "Ogohlantirish", "Siz parolni xato kiritdingiz")
            else:
                QMessageBox.warning(self, "Ogohlantirish", "Siz noto'g'ri email kiritdingiz")
        else:
            QMessageBox.warning(self, "Ogohlantirish", "Siz ma'lumotlarni to'liq kiritmadingiz")
