from PyQt5.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QApplication, QLineEdit, QPushButton
from regis import Regis
from login import Login


class Kirish(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kirish")
        vertikal = QVBoxLayout()

        self.login = QPushButton("Login")
        self.login.clicked.connect(self.login_bosildi)
        vertikal.addWidget(self.login)

        self.registr = QPushButton("Registratsiya")
        self.registr.clicked.connect(self.registr_bosildi)
        vertikal.addWidget(self.registr)

        widjet = QWidget()
        widjet.setLayout(vertikal)
        self.setCentralWidget(widjet)

        self.login_oyna = None
        self.reg_oyna = None

    def login_bosildi(self):
        self.hide()
        self.reg_oyna = Login(self)
        self.reg_oyna.show()

    def registr_bosildi(self):
        self.hide()
        self.login_oyna = Regis(self)
        self.login_oyna.show()


app = QApplication([])

oyna = Kirish()
oyna.show()

app.exec_()
