class Jogador:

    def jogar(self, tab, pos):
        if tab.verifica(pos):
            tab.jogada(pos, 'X')
            return 'X'



# from random import randint
# from time import sleep
#
#
# class Jogador:
#
#     def jogar(self, tab):
#         print('\nSua vez de jogar...\n')
#         sleep(1)
#         pos_usuario = input('Escolha uma posição para jogar: ')
#
#         while (not tab.verifica(pos_usuario)):
#             print('Jogada inválida!!!')
#             pos_usuario = input('Escolha outra posição para jogar: ')
#
#         tab.jogada(pos_usuario, 'X')
#
#
# class Computador(Jogador):
#
#     def jogar(self, tab):
#         print('\nSua vez de jogar...\n')
#         sleep(1)
#         pos_usuario = input('Escolha uma posição para jogar: ')
#
#         while (not tab.verifica(pos_usuario)):
#             print('Jogada inválida!!!')
#             pos_usuario = input('Escolha outra posição para jogar: ')
#
#         tab.jogada(pos_usuario, 'O')
#
# class ComputadorA(Computador):
#
#     def jogar(self, tab):
#         print('\nComputador jogando...\n')
#         sleep(1)
#         num = randint(1, 9)
#         pos_comp = str(num)
#
#         while (not tab.verifica(pos_comp)):
#             num = randint(1, 9)
#             pos_comp = str(num)
#
#         tab.jogada(pos_comp, 'O')
