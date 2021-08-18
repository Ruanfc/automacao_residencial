# projeto de automação residencial
# autor Flávio Cândido, Ruan Flaneto, Diego Rosas
# v1.0

from PyQt5 import uic, QtWidgets
from grafico_figura import *
from time import sleep
import socket


def liga_lampada(id):
    s[id].sendall("turn on".encode())
    print(s[id].recv(1024).decode())
    eval("tela.frame_desligado" + index[id]).close()
    eval("tela.frame_ligado" + index[id]).show()


def desliga_lampada(id):
    s[id].sendall("turn off".encode())
    print(s[id].recv(1024).decode())
    eval("tela.frame_desligado" + index[id]).show()
    eval("tela.frame_ligado" + index[id]).close()


def lampadas():
    tela.luz_frame.show()
    tela.grafico_frame.close()


def grafico():
    tela.luz_frame.close()
    gera_graf()
    # sleep()
    # tela.grafico_frame=MatplotlibWidget()
    tela.grafico_frame.show()
    # tela.grafWid.show()


index = ["", "_2", "_7", "_8", "_9"]
n = len(index)
used_lamps = 3
ipIndex = []
s = []
for i, id in enumerate(index):
    ipIndex.append("192.168.1.18" + str(i))
    s.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    s[-1].settimeout(10)
    # Precisa ter cuidado ao não conectar, talvez um timeout sirva
    if i < used_lamps:
        s[-1].connect((ipIndex[-1], 8266))
    pass


aplicacao = QtWidgets.QApplication([])
tela = uic.loadUi("untitled.ui")
tela.btn_grafico.clicked.connect(grafico)
tela.btn_luzes.clicked.connect(lampadas)
for i in range(used_lamps):
    eval(
        "tela.btn_liga"
        + index[i]
        + ".clicked.connect(lambda i"
        + ": liga_lampada("
        + str(i)
        + "))"
    )
    eval(
        "tela.btn_desliga"
        + index[i]
        + ".clicked.connect(lambda i"
        + ": desliga_lampada("
        + str(i)
        + "))"
    )

tela.show()
aplicacao.exec()
