# projeto de automação residencial
# autor Flávio Cândido
# v1.0

import types
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
from grafico_figura_copy import*
from time import sleep
import time
estado=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def liga_lampada0():
        tela.frame_desligado.close()
        tela.frame_ligado.show()
        global estado
        if estado[0]==0:
                time_liga("0")
                estado[0] = 1

def desliga_lampada0():
        tela.frame_desligado.show()
        tela.frame_ligado.close()
        global estado
        if estado[0]==1:
                time_desliga("0")
                estado[0] = 0

        

def liga_lampada1():
        tela.frame_desligado_2.close()
        tela.frame_ligado_2.show()
        global estado
        if estado[1]==0:
                time_liga("1")
                estado[1] = 1
       
def desliga_lampada1():
        tela.frame_desligado_2.show()
        tela.frame_ligado_2.close()
        global estado
        if estado[1]==1:
                time_desliga("1")
                estado[1] = 0


def liga_quarto1():
        tela.frame_desligado_7.close()
        tela.frame_ligado_7.show()
        global estado
        if estado[2]==0:
                time_liga(" quarto 1")
                estado[2] = 1
       
def desliga_quarto1():
        tela.frame_desligado_7.show()
        tela.frame_ligado_7.close() 
        global estado
        if estado[2]==1:
                time_desliga(" quarto 1")
                estado[2] = 0


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
    tela.grafico_frame.close()
        
def grafico():
    tela.luz_frame.close()
    gera_graf()
    # sleep()
    # tela.grafico_frame=MatplotlibWidget()
    tela.grafico_frame.show()
    # tela.grafWid.show()

#teste = 10
#teste de funcao de contagem de tempo da lampada ligada    
total_ligou = 0
dia_lig = 0
def time_liga(lampada):
        #dia que ligou
        global dia_lig
        dia_lig = int(time.strftime('%d'))
        #hora e minuto que ligou
        timeL = time.strftime('%H:%M')
        h = float(time.strftime('%H'))
        m = float(time.strftime('%M'))
        print('Lampada {} ligada as: {}'.format(lampada,timeL))  
        total_h_ligou = h * 60
        total_m_ligou = m
        global total_ligou
        total_ligou = total_h_ligou + total_m_ligou #tempo que ligou em minutos
        #print(total_ligou)         
        


total_desligou = 0
dia_deslig = 0
dia_c = 0
def time_desliga(lampada):
        
        #dia que desligou
        global dia_deslig
        dia_deslig = int(time.strftime('%d'))
        #hora e minuto que ligou
        timeD = time.strftime('%H:%M')
        H = float(time.strftime('%H'))
        M = float(time.strftime('%M'))
        print('Lampada {} desligada as: {}'.format(lampada,timeD)) 
        total_h_desligou = H * 60
        total_m_desligou = M
        global total_desligou
        total_desligou = total_h_desligou + total_m_desligou
        #print(total_desligou)
        global dia_c
        dia_c = 24 * 60 #um dia completo = 1440 min
        #print(dia_c)




def tempo_ligada():
        
        #faz os calculos para ver se a lampada foi ligada no mesmo dia ou nao
        if dia_deslig > dia_lig:
                dia_total = dia_deslig - dia_lig
        else:
                dia_total = dia_lig - dia_deslig
        print('qtd dias: ', dia_total)

        #faz os calculos para ver quanto tempo a lampada ficou ligada
        if dia_total == 0 and total_ligou < total_desligou  : #calcula o tempo a partir de quando a lampada eh ligada ate ser desligada no mesmo dia 
                t_ligada = total_desligou - total_ligou          #para o tempo total em minutos                                 
                t_ligada = t_ligada / 60                     #para o tempo total em horas
                t_ligada = round(t_ligada, 2)
                with open('registo_time.txt', 'a+') as arquivo:
                        conteudo = arquivo.write('{}\n'.format(t_ligada))
                print('tempo total ligada: {}'.format(t_ligada))

        if dia_total > 0 and total_ligou > total_desligou:  #calcula o tempo a partir de quando a lampada eh ligada ate ser desligada em dias diferentes 
                t_ligada = total_ligou - total_desligou 
                #print(t_ligada)
                t_ligada = (dia_c - t_ligada) / 60     #passa o tempo total em horas
                t_ligada = round(t_ligada, 2)
                with open('registo_time.txt', 'a+') as arquivo:
                        conteudo = arquivo.write('{}\n'.format(t_ligada))
                print('tempo total ligada: {}'.format(t_ligada))
                
        if dia_total > 0 and total_ligou < total_desligou:  #calcula o tempo a partir de quando a lampada eh ligada ate ser desligada em dias diferentes 
                t_ligada = total_desligou - total_ligou 
                #print(t_ligada)
                t_ligada = (dia_c + t_ligada) / 60     #passa o tempo total em horas
                t_ligada = round(t_ligada, 2)
                with open('registo_time.txt', 'a+') as arquivo:
                        conteudo = arquivo.write('{}\n'.format(t_ligada))
                print('tempo total ligada: {}'.format(t_ligada))




#incia o programa e carrega o arquigo da GUI    
aplicacao=QtWidgets.QApplication([])
tela=uic.loadUi("untitled.ui")#C:\Users\adm\Documents\projetos\python\aulas\aulas\PROJETO\projeto_v2\Projeto\graficos - matiplotlib\untitled.ui

#comandos de acao da troca de frames lampadas e graficos 
tela.btn_grafico.clicked.connect(grafico)
tela.btn_luzes.clicked.connect(lampadas)

#comandos de acao para ligar/desligas as lampadas
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

#acoes dos botoes para ligar o contador do tempo em que a lampada foi ligada/desligada
# tela.btn_liga.clicked.connect(time_liga)
#tela.btn_desliga.clicked.connect(teste)
tela.btn_desliga.clicked.connect(tempo_ligada)


tela.show()
aplicacao.exec()