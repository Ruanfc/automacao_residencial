# projeto de automação residencial
# autor Flávio Cândido
# v1.0

from PyQt5 import uic,QtWidgets, QtGui
from numpy import true_divide
from grafico_figura import*
from time import sleep
caminho = 0
Tcaminho = ''
def liga_lampada0():
        tela.frame_desligado.close()
        tela.frame_ligado.show()
       
def desliga_lampada0():
        tela.frame_desligado.show()
        tela.frame_ligado.close()

def liga_lampada1():
        tela.frame_desligado_2.close()
        tela.frame_ligado_2.show()
       
def desliga_lampada1():
        tela.frame_desligado_2.show()
        tela.frame_ligado_2.close()

def liga_quarto1():
        tela.frame_desligado_7.close()
        tela.frame_ligado_7.show()
       
def desliga_quarto1():
        tela.frame_desligado_7.show()
        tela.frame_ligado_7.close() 

def liga_quarto2():
        tela.frame_desligado_9.close()
        tela.frame_ligado_9.show()
       
def desliga_quarto2():
        tela.frame_desligado_9.show()
        tela.frame_ligado_9.close()

def liga_cozinha():
        tela.frame_desligado_8.close()
        tela.frame_ligado_8.show()
       
def desliga_cozinha():
        tela.frame_desligado_8.show()
        tela.frame_ligado_8.close()   

def liga_terraco():
        tela.frame_desligado_10.close()
        tela.frame_ligado_10.show()
       
def desliga_terraco():
        tela.frame_desligado_10.show()
        tela.frame_ligado_10.close() 

def lampadas():
    tela.luz_frame.show()
    
#     os.remove('Figure_1.png')
    tela.grafico_frame.close()

def grafico():
    global caminho
#     tela.ATUALIZE.clicked=True
#     sleep(1)
#     tela.ATUALIZE.clicked=False
    
    if caminho == 0:
        
        caminho= caminho + 1
        Tcaminho = "figure_1.png"
        print(Tcaminho)
    else:
        Tcaminho="figure2.png"
        caminho = 0
        print(Tcaminho)

    tela.luz_frame.close()
    gera_graf(Tcaminho)
    tela.figure.setPixmap(QtGui.QPixmap(Tcaminho))
    tela.grafico_frame.show()
  
    

    
aplicacao=QtWidgets.QApplication([])
tela=uic.loadUi("untitled.ui")#C:\Users\adm\Documents\projetos\python\aulas\aulas\PROJETO\projeto_v2\Projeto\graficos - matiplotlib\untitled.ui
tela.btn_grafico.clicked.connect(grafico)
tela.btn_luzes.clicked.connect(lampadas)
tela.btn_liga.clicked.connect(liga_lampada0)
tela.btn_desliga.clicked.connect(desliga_lampada0)
tela.btn_liga_2.clicked.connect(liga_lampada1)
tela.btn_desliga_2.clicked.connect(desliga_lampada1)
tela.btn_liga_7.clicked.connect(liga_quarto1)
tela.btn_desliga_7.clicked.connect(desliga_quarto1)
tela.btn_liga_8.clicked.connect(liga_cozinha)
tela.btn_desliga_8.clicked.connect(desliga_cozinha)
tela.btn_liga_9.clicked.connect(liga_quarto2)
tela.btn_desliga_9.clicked.connect(desliga_quarto2)
tela.btn_liga_10.clicked.connect(liga_terraco)
tela.btn_desliga_10.clicked.connect(desliga_terraco)
tela.ATUALIZE.clicked.connect(grafico)
tela.show()
aplicacao.exec()
