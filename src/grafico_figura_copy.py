import matplotlib.pyplot as plt  
y = []
x = ['Lâmpada 1', 'Lâmpada 2', 'Lâmpada 3']

def gera_graf():
    with open('registo_time.txt', 'r') as f:
        dados = f.read()
        for linha in dados.split('\n'):
            if len(linha) == 0:
                continue
            yi = linha
            y.append(float(yi))

    figura = plt.figure(figsize=(10,6))
    figura.suptitle('Gráfico de acionamento das lâmpadas')

    figura.add_subplot(111)
    plt.bar(x, y, color='g',)
    plt.ylabel('Quantidade de horas')
    plt.xlabel('Lâmpadas')
    #plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11,12])
    #plt.axis(ymin=0,ymax=12)


    plt.savefig('Figure_1.png', dpi =100)
    # plt.savefig('gaficos img\\Figure_1.png', dpi =100)
    #plt.show()
    

