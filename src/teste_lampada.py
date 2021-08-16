#!/usr/bin/env python3
import sys
import random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel as Label
from PyQt5.QtWidgets import QPushButton as Button

# import serial
import socket


class Lamp(QtWidgets.QHBoxLayout):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self.toggle = Button("toggle")
        self.update = Button("update")

        self.red = QPixmap("red.png")
        self.red = self.red.scaledToWidth(20)
        self.green = QPixmap("green.png")
        self.green = self.green.scaledToWidth(20)
        self.gray = QPixmap("gray.png")
        self.gray = self.gray.scaledToWidth(20)
        self.indicator = Label("")
        self.state = "gray"
        self.indicator.setPixmap(self.gray)
        self.indicator.resize(self.red.width() / 10, self.red.width() / 10)

        # Cria o layout de fato
        super().__init__()
        self.addWidget(self.update)
        self.addWidget(self.toggle)
        self.addWidget(self.indicator)

        self.toggle.clicked.connect(self.toggle_clicked)
        self.update.clicked.connect(self.update_clicked)
        #
        # Cria um servidor tcp
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(10)
        self.s.connect((self.ip, self.port))

    def toggle_clicked(self):
        if self.state == "green":
            self.s.sendall("turn off".encode())
            self.state = "red"
            self.indicator.setPixmap(self.red)
        elif self.state == "red":
            self.s.sendall("turn on".encode())
            self.state = "green"
            self.indicator.setPixmap(self.green)
        print(self.s.recv(1024).decode())

    def update_clicked(self):
        self.s.sendall("_get state".encode())
        # blocking function
        self.state = self.s.recv(1024).decode()
        print(self.state)
        if "green" in self.state:
            self.state = "green"
            self.indicator.setPixmap(self.green)
        elif "red" in self.state:
            self.state = "red"
            self.indicator.setPixmap(self.red)


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.header = Label("Light controller")
        self.lamp1 = Lamp("192.168.1.180", 8266)
        self.lamp2 = Lamp("192.168.1.181", 8266)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addLayout(self.lamp1)
        self.layout.addLayout(self.lamp2)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    # widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
