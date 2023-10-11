from jogador import *
from tabuleiro import Tabuleiro



tab = Tabuleiro()
usuario = Jogador()

print("""Menu de opção:
    1 - Multiplayer
    2 - Computador""")
opcao = int(input('Qual sua opção -> '))
while True:
    if opcao != 1 and opcao != 2:
        print('Opção invalida!!!')
        print("""Menu de opção:
            1 - Multiplayer
            2 - Computador""")
        opcao = int(input('Qual sua opção -> '))
    else:
        break

if opcao == 1:
    comp = Computador()
elif opcao == 2:
    comp = ComputadorA()

tab.mostraTab()
num_jogadas = 0
while True:

    usuario.jogar(tab)
    tab.mostraTab()
    num_jogadas += 1
    if tab.situacao(num_jogadas) != '':
        break

    comp.jogador(tab)
    tab.mostraTab()
    num_jogadas += 1
    if tab.situacao(num_jogadas) != '':
        break


print(tab.situacao(num_jogadas))
