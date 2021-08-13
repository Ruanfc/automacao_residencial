#!/usr/bin/env python3
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel as Label
from PySide6.QtWidgets import QPushButton as Button

# import serial
import socket

HOST = "192.168.1.184"
PORT = 8266


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.header = Label("Light controller")
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

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.header, 0, 0)
        self.layout.addWidget(self.update, 1, 0)
        self.layout.addWidget(self.toggle, 1, 1)
        self.layout.addWidget(self.indicator, 1, 2)

        self.toggle.clicked.connect(self.toggle_clicked)
        self.update.clicked.connect(self.update_clicked)

        # Cria um servidor tcp
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, 8266))

    @QtCore.Slot()
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


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
