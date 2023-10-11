from tkinter import *

# cores ----------------------------------------------
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"  # azul / blue
co5 = "#fff873"  # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"  # vermelha / red
co8 = co4  # + verde
co10 = "#fcfbf7"
fundo = "#3b3b3b"  # preta / black

# criando janela principal ----------------------------------------------
janela = Tk()
janela.title('JOGO DA VELHA')
janela.geometry('260x370')
janela.configure(bg=fundo)

# Criando os Frames ----------------------------------------------
frame_cima = Frame(janela, width=240, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

# Config Frame cima ----------------------------------------------
app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font='Ivy 40 bold', bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font='Ivy 7 bold', bg=co1, fg=co0)
app_x.place(x=17, y=70)
app_xpontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
app_xpontos.place(x=80, y=20)

app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font='Ivy 30 bold', bg=co1,
                      fg=co0)
app_separador.place(x=110, y=17)

app_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font='Ivy 40 bold', bg=co1, fg=co4)
app_o.place(x=170, y=10)
app_o = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font='Ivy 7 bold', bg=co1, fg=co0)
app_o.place(x=165, y=70)
app_opontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
app_opontos.place(x=130, y=20)

# criando logica do app ----------------------------------------------
jogador1 = 'X'
jogador2 = 'O'

pontuacao1 = 0
pontuacao2 = 0

tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
jogando = 'X'
jogador = ''
contador = 0
contador_de_radadas = 0


def iniciar():
    b_jogar.destroy()

    def controlar(i):
        global jogando
        global contador
        global jogador

        # comparando valor dos botões
        if i == str(1):
            # ver posição disponivel
            if b_0['text'] == '':
                contador += 1
                # define quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # definindo cor do texto do simbolo e marcar no tabuleiro
                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0] = jogando
                # trocando jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogador = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogador = 'Jogador 2'

        if i == str(2):
            # ver posição disponivel
            if b_1['text'] == '':
                contador += 1
                # define quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # definindo cor do texto do simbolo e marcar no tabuleiro
                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando
                # trocando jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogador = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogador = 'Jogador 2'

        if i == str(3):
            # ver posição disponivel
            if b_2['text'] == '':
                contador += 1
                # define quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # definindo cor do texto do simbolo e marcar no tabuleiro
                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2] = jogando
                # trocando jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogador = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogador = 'Jogador 2'

        if i == str(4):
            # ver posição disponivel
            if b_3['text'] == '':
                contador += 1
                # define quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # definindo cor do texto do simbolo e marcar no tabuleiro
                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando
                # trocando jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogador = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogador = 'Jogador 2'

        if i == str(5):
            # ver posição disponivel
            if b_4['text'] == '':
                contador += 1
                # define quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # definindo cor do texto do simbolo e marcar no tabuleiro
                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando
                # trocando jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogador = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogador = 'Jogador 2'

        if i == str(6):
            # ver posição disponivel
            if b_5['text'] == '':
                contador += 1
                # define quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # definindo cor do texto do simbolo e marcar no tabuleiro
                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando
                # trocando jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogador = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogador = 'Jogador 2'

        if i == str(7):
            # ver posição disponivel
            if b_6['text'] == '':
                contador += 1
                # define quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # definindo cor do texto do simbolo e marcar no tabuleiro
                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando
                # trocando jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogador = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogador = 'Jogador 2'

        if i == str(8):
            # ver posição disponivel
            if b_7['text'] == '':
                contador += 1
                # define quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # definindo cor do texto do simbolo e marcar no tabuleiro
                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando
                # trocando jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogador = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogador = 'Jogador 2'

        if i == str(9):
            # ver posição disponivel
            if b_8['text'] == '':
                contador += 1
                # define quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # definindo cor do texto do simbolo e marcar no tabuleiro
                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando
                # trocando jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogador = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogador = 'Jogador 2'

        # icrementar contador

        if contador >= 5:
            if tabela[0][0] == tabela[0][1] == tabela[0][2] != '':
                vencedor(jogador)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                vencedor(jogador)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                vencedor(jogador)
            elif tabela[0][0] == tabela[1][0] == tabela[2][0] != '':
                vencedor(jogador)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                vencedor(jogador)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                vencedor(jogador)
            elif tabela[0][0] == tabela[1][1] == tabela[2][2] != '':
                vencedor(jogador)
            elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                vencedor(jogador)
            # Empate
            elif contador >= 9:
                vencedor('Deu Velha')

    def vencedor(i):
        # reiniciar a rodada
        def start():
            global tabela, jogando, contador
            b_0['state'] = 'normal'
            b_1['state'] = 'normal'
            b_2['state'] = 'normal'
            b_3['state'] = 'normal'
            b_4['state'] = 'normal'
            b_5['state'] = 'normal'
            b_6['state'] = 'normal'
            b_7['state'] = 'normal'
            b_8['state'] = 'normal'

            # limpando botões
            b_0['text'] = ''
            b_1['text'] = ''
            b_2['text'] = ''
            b_3['text'] = ''
            b_4['text'] = ''
            b_5['text'] = ''
            b_6['text'] = ''
            b_7['text'] = ''
            b_8['text'] = ''
            app_vencedor.destroy()
            b_jogar.destroy()
            tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            jogando = 'X'
            contador = 0

        def fim_de_jogo():
            b_jogar.destroy()
            app_vencedor.destroy()
            terminar_jogo()

        global pontuacao1, pontuacao2, jogando
        global tabela, contador_de_radadas

        # Botão Jogar
        b_jogar = Button(frame_baixo, command=start, text='JOGAR NOVAMENTE', width=18, height=1, font='Ivy 10 bold',
                         overrelief=RIDGE, relief='raised',
                         bg=fundo, fg=co0)
        b_jogar.place(x=52, y=210)


        # desabilitar botões
        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        # Msg vencedor
        app_vencedor = Label(frame_baixo, text=i + ' Venceu', width=17, relief='flat', anchor='center',
                             font='Ivy 13 bold', bg=fundo, fg=co0)
        app_vencedor.place(x=40, y=185)

        # Pontuação
        if i == 'Jogador 1':
            contador_de_radadas += 1
            pontuacao1 += 1
            app_xpontos['text'] = str(pontuacao1)
        elif i == 'Jogador 2':
            contador_de_radadas += 1
            pontuacao2 += 1
            app_opontos['text'] = str(pontuacao2)
        else:
            app_vencedor['text'] = i

        if contador_de_radadas >= 5:
            fim_de_jogo()

    def terminar_jogo():
        global tabela, contador_de_radadas, pontuacao1, pontuacao2, contador

        # Msg fim de jogo
        app_fim = Label(frame_baixo, text='JOGO ACABOU', width=17, relief='flat', anchor='center',
                        font='Ivy 13 bold', bg=fundo, fg=co0)
        app_fim.place(x=35, y=90)
        if pontuacao1 > pontuacao2:
            ganhou = str('Jogador 1 ganhou o jogo')
        elif pontuacao2 > pontuacao1:
            ganhou = str('Jogador 2 ganhou o jogo')

        # Msg do vencedor
        app_vencedor_jogo = Label(frame_baixo, text=ganhou, width=27, relief='flat',
                                  font='Ivy 10 bold', bg=fundo, fg=co0)
        app_vencedor_jogo.place(x=18, y=120)

        tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        contador = 0
        contador_de_radadas = 0
        pontuacao1 = 0
        pontuacao2 = 0

        # desabilitar botões
        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        # jogar novamente
        def jogar_novamente():
            app_opontos['text'] = '0'
            app_xpontos['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()
            app_vencedor_jogo.destroy()
            iniciar()

        # Botão Jogar
        b_jogar = Button(frame_baixo, command=jogar_novamente, text='JOGAR', width=10, height=1, font='Ivy 10 bold',
                         overrelief=RIDGE, relief='raised',
                         bg=fundo, fg=co0)
        b_jogar.place(x=85, y=210)

    # Config Frame baixo ----------------------------------------------
    # linhas verticais
    app_ = Label(frame_baixo, text='', height=23, pady=5, relief='flat', anchor='center', font='Ivy 5 bold', bg=co0,
                 fg=co7)
    app_.place(x=90, y=15)
    app_ = Label(frame_baixo, text='', height=23, pady=5, relief='flat', anchor='center', font='Ivy 5 bold', bg=co0,
                 fg=co7)
    app_.place(x=160, y=15)

    # linhas horizontais
    app_ = Label(frame_baixo, text='', width=192, padx=2, pady=1, relief='flat', anchor='center', font='Ivy 1 bold',
                 bg=co0,
                 fg=co7)
    app_.place(x=30, y=63)
    app_ = Label(frame_baixo, text='', width=192, padx=2, pady=1, relief='flat', anchor='center', font='Ivy 1 bold',
                 bg=co0,
                 fg=co7)
    app_.place(x=30, y=123)

    # linha 0
    b_0 = Button(frame_baixo, command=lambda: controlar('1'), text='', width=3, font='Ivy 17 bold', overrelief=RIDGE,
                 relief='flat', bg=fundo, fg=co7)
    b_0.place(x=35, y=15)
    b_1 = Button(frame_baixo, command=lambda: controlar('2'), text='', width=3, font='Ivy 17 bold', overrelief=RIDGE,
                 relief='flat', bg=fundo, fg=co7)
    b_1.place(x=102, y=15)
    b_2 = Button(frame_baixo, command=lambda: controlar('3'), text='', width=3, font='Ivy 17 bold', overrelief=RIDGE,
                 relief='flat', bg=fundo, fg=co7)
    b_2.place(x=170, y=15)

    # linha 1
    b_3 = Button(frame_baixo, command=lambda: controlar('4'), text='', width=3, font='Ivy 17 bold', overrelief=RIDGE,
                 relief='flat', bg=fundo, fg=co7)
    b_3.place(x=35, y=75)
    b_4 = Button(frame_baixo, command=lambda: controlar('5'), text='', width=3, font='Ivy 17 bold', overrelief=RIDGE,
                 relief='flat', bg=fundo, fg=co7)
    b_4.place(x=102, y=75)
    b_5 = Button(frame_baixo, command=lambda: controlar('6'), text='', width=3, font='Ivy 17 bold', overrelief=RIDGE,
                 relief='flat', bg=fundo, fg=co7)
    b_5.place(x=170, y=75)

    # linha 2
    b_6 = Button(frame_baixo, command=lambda: controlar('7'), text='', width=3, font='Ivy 17 bold', overrelief=RIDGE,
                 relief='flat', bg=fundo, fg=co7)
    b_6.place(x=35, y=137)
    b_7 = Button(frame_baixo, command=lambda: controlar('8'), text='', width=3, font='Ivy 17 bold', overrelief=RIDGE,
                 relief='flat', bg=fundo, fg=co7)
    b_7.place(x=102, y=137)
    b_8 = Button(frame_baixo, command=lambda: controlar('9'), text='', width=3, font='Ivy 17 bold', overrelief=RIDGE,
                 relief='flat', bg=fundo, fg=co7)
    b_8.place(x=170, y=137)


# Botão Jogar
b_jogar = Button(frame_baixo, command=iniciar, text='JOGAR', width=10, height=1, font='Ivy 10 bold', overrelief=RIDGE,
                 relief='raised',
                 bg=fundo, fg=co0)
b_jogar.place(x=85, y=210)

# fim da janela ---------------------------------------------------------
janela.mainloop()
