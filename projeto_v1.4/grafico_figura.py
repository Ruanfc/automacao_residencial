import matplotlib.pyplot as plt  
y = []
x = []
import threading

def gera_graf():
    with open('dados.txt', 'r') as f:
    # f= open(, 'r')
        dados = f.read()
        for linha in dados.split('\n'):
            if len(linha) == 0:
                continue
            xi, yi = linha.split(',')
            x.append(float(xi))
            y.append(float(yi))
        # y = []
        # x = []#x = ['Lâmpada 1', 'Lâmpada 2', 'Lâmpada 3', 'lâmpada 4']
        # y = [2, 5, 7, 10]

    figura = plt.figure(figsize=(10,6))
    figura.suptitle('Gráfico de acionamento das lâmpadas')

    figura.add_subplot(111)
    plt.bar(x, y, color='g',)
    plt.ylabel('Quantidade de horas')
    plt.xlabel('Lâmpadas')
    plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11,12])
    #plt.axis(ymin=0,ymax=12)


    plt.savefig('C:\\Users\\adm\\Documents\\projetos\\python\\aulas\\aulas\\PROJETO\\projeto_v1.4\\Figure_1.png', dpi =100)
    # plt.savefig('gaficos img\\Figure_1.png', dpi =100)
    # plt.show()
    

