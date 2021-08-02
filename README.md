
# Table of Contents

1.  [Motivação](#org6f0cbf6)
2.  [Objetivos](#orgfb813d0)
3.  [Detalhamento do projeto](#org8b22299)
    1.  [Lâmpadas](#orge8bab3c)
        1.  [Descrição do circuito](#org892c029)
        2.  [Componentes utilizados (por lâmpada)](#orgcfa7a18)
    2.  [Descrição do software](#org9ddc428)
        1.  [Conectividade e gerenciamento de ações](#org3a479d0)
        2.  [GUI](#orgb188323)
        3.  [Geração de relatórios](#orgc759a60)



<a id="org6f0cbf6"></a>

# Motivação

Um projeto de automação residencial foi demandado. Primeira coisa que vem em mente é poder controlar as lâmdas de casa individualemente como meio de gerenciar o uso de cargas residenciais, viabilizando a economia de energia elétrica. Assim, pretende-se usar um módulo de ESP01 com relé (vide figura \ref{fig:module_esp01}) para cada ponto de interruptor de lâmpada para poder ter conexão com o computador central (raspberry pi).


<a id="orgfb813d0"></a>

# Objetivos

Gerenciar o funcionamento das lâmpadas de casa, cujo funcionamento deve ser por comando de voz ou de forma manual. Este gerenciamento também inclui a formação de relatórios sobre consumo elétrico (estimado) em cada dispositivo, apresentando as informações em histogramas.


<a id="org8b22299"></a>

# Detalhamento do projeto


<a id="orge8bab3c"></a>

## Lâmpadas


<a id="org892c029"></a>

### Descrição do circuito

Um pequeno trafo recebe a energia da tomada, é retificada por uma ponte retificadora e então o módulo relé com o esp8266 controla o chaveamento da lâmpada. Para fazer o controle da lâmpada ser manual torna-se necessário detectar a existência de fase no pino Normalmente Aberto (NA) do relé, como na figura \ref{fig:tomada}.

![img](./tomada.png "Circuito a ser implementado para detecção de fase")

Não é intenção deste projeto confeccionar placa de circuito impresso para simplificar o projeto e também no momento é impossível para mim imprimir sem uma impressora adequada.


<a id="orgcfa7a18"></a>

### Componentes utilizados (por lâmpada)

-   [X] 1 Trafo de carregador;
-   [X] 4 Diodos 1n4007;
-   [X] 1 Capacitor eletrolítico (47uF);
-   [X] 1 Capacitor cerâmico (100nF);
-   [X] 1 Sensor piroelétrico
-   [X] 1 Módulo de acionamento de relé por ESP8266 (figura \ref{fig:module_esp01};
-   [X] 2 transistores de uso geral para para detecção de fase;
-   [X] Resistores diversos

![img](./module_esp01.png "Módulo relé com ESP01 utilizado")

O módulo de relé possui o esquemático como na figura \ref{schematic_relay}

![img](./schematic_relay.png "Esquema do circuito do módulo com relé")


<a id="org9ddc428"></a>

## Descrição do software

O projeto de software é dividor em 3 partes: Conectividade e gerenciamento de ações; GUI; geração de relatórios


<a id="org3a479d0"></a>

### Conectividade e gerenciamento de ações

Esta parte consiste em fazer os ESP8266 se conectarem com o raspberryPI por rede para estabelecer comunicação (vide figura \ref{fig:lan_concept}) e também consiste nas tomadas de decisão para o raspberryPI, determinando o comportamento de cada lâmpada e dando prioridade aos comandos.
Os esp8266 das tomadas devem entrar em um ponto de acesso central e então ficar à espera de comandos. Ele age como escravo para responder aos comandos do computador central.

![img](./lan_concept.png "Visão conceitual para conectividade LAN dos dispositivos")

-   Atividades de pesquisa e implementação:
    -   Protocolo de comunicação (http)
        -   Usar os esps como servidores, de modo que o raspberry consiga solicitar informações.
    -   Secure shell (ssh) para compartilhar tela
    -   Programação dos ESP8266
        -   frameworks: Arduino, micropython, RTOS?
-   Procedimentos a serem utilizados na cpu principal:
    -   get state() # Retorna o estado atual lâmpada;
    -   turn(boolean state) # Pede para ligar/desligar a lâmpada
    -   get switch() # Retorna a posição do interruptor;

![img](diagrama_uso.png "Diagrama de caso de uso")


<a id="orgb188323"></a>

### GUI

Uma interface gráfica para o usuário como a da figura \ref{fig:gui} é tida como meio de centralizar as informações de forma que fique acessível ao usuário. Esta será feita no raspberryPI IOs com a biblioteca Qt for python, que é uma versão alternativa ao PyQt com licensa LGPL, para caso o projeto futuramente se torne comercial.

![img](./gui.png "GUI a ser implementada no RaspberryPI OS")

-   Atividades de pesquisa e implementação
    TODO!!!


<a id="orgc759a60"></a>

### Geração de relatórios

Esta parte do projeto consiste em trabalhar com as informações obtidas com as lâmpadas, visa calcular consumos e gerar um histrograma para o consumo de energia dos dispositivos.

-   Atividades de pesquisa e implementação
    TODO!!!

