from tkinter import *
from tabuleiro import Tabuleiro
from jogador import Jogador


# Cores
cor1 = '#2b2b2a'  # preta
cor2 = '#ffffff'  # branca
cor3 = '#38576b'  # Azul
cor4 = '#0e1e29'  # Azul-escuro
cor5 = '#FFAB40'  # laranja


# Criando Janela
janela = Tk()
janela.title('JOGO DA VELHA')
janela.geometry('390x427')


# Variaveis globais
tab = Tabuleiro()
usuario = Jogador()
num_jogadas = 0
val_p1 = StringVar()

# Funções
def jog():
    global num_jogadas
    if num_jogadas % 2 == 0:
        val_p1.set(usuario.jogar(tab, '1'))
    else:
        usuario.jogar(tab, '2')
    num_jogadas += 1


# Criando frames
frame_dispay = Frame(janela, width=390, height=100, bg=cor3)
frame_dispay.grid(row=0, column=0)

frame_corpo = Frame(janela, width=390, height=327, bg=cor4)
frame_corpo.grid(row=1, column=0)


# Criando botões
b1 = Button(frame_corpo, command=lambda: jog(), textvariable=val_p1, width=4, height=1, bg=cor4, fg=cor2,
            font='Ivy 40 bold', relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)

b2 = Button(frame_corpo, text='', width=4, height=1, bg=cor4, fg=cor2,
            font='Ivy 40 bold', relief=RAISED, overrelief=RIDGE)
b2.place(x=138, y=0)

b3 = Button(frame_corpo, text='', width=12, height=5, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b3.place(x=260, y=0)

b4 = Button(frame_corpo, text='', width=12, height=5, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=109)
b5 = Button(frame_corpo, text='', width=12, height=5, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b5.place(x=130, y=109)
b6 = Button(frame_corpo, text='', width=12, height=5, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b6.place(x=260, y=109)

b7 = Button(frame_corpo, text='', width=12, height=5, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b7.place(x=0, y=218)
b8 = Button(frame_corpo, text='', width=12, height=5, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b8.place(x=130, y=218)
b9 = Button(frame_corpo, text='', width=12, height=5, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b9.place(x=260, y=218)


janela.mainloop()
