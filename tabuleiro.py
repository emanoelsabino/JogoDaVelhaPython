class Tabuleiro:
    tab = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    def mostraTab(self):
        print('TABULEIRO')
        for l in range(0, len(self.tab)):
            for c in range(0, len(self.tab)):
                print(self.tab[l][c], end='   ')
            print()

    def verifica(self, pos):
        for l in range(0, len(self.tab)):
            for c in range(0, len(self.tab)):
                if self.tab[l][c] == pos:
                    return True
        return False

    def jogada(self, pos, jog):
        if pos == '1':
            self.tab[0][0] = jog
        elif pos == '2':
            self.tab[0][1] = jog
        elif pos == '3':
            self.tab[0][2] = jog
        elif pos == '4':
            self.tab[1][0] = jog
        elif pos == '5':
            self.tab[1][1] = jog
        elif pos == '6':
            self.tab[1][2] = jog
        elif pos == '7':
            self.tab[2][0] = jog
        elif pos == '8':
            self.tab[2][1] = jog
        elif pos == '9':
            self.tab[2][2] = jog

    def situacao(self, jogadas):
        jogadaGanha = [1, 2, 3, 4, 5, 6, 7, 8]
        vencedor = ''
        if jogadas == 9:
            vencedor = 'Deu Velha'

        jogadaGanha[0] = self.tab[0][0] + self.tab[0][1] + self.tab[0][2]
        jogadaGanha[1] = self.tab[1][0] + self.tab[1][1] + self.tab[1][2]
        jogadaGanha[2] = self.tab[2][0] + self.tab[2][1] + self.tab[2][2]

        jogadaGanha[3] = self.tab[0][0] + self.tab[1][0] + self.tab[2][0]
        jogadaGanha[4] = self.tab[0][1] + self.tab[1][1] + self.tab[2][1]
        jogadaGanha[5] = self.tab[0][2] + self.tab[1][2] + self.tab[2][2]

        jogadaGanha[6] = self.tab[0][0] + self.tab[1][1] + self.tab[2][2]
        jogadaGanha[7] = self.tab[0][2] + self.tab[1][1] + self.tab[2][0]

        for i in range(0, len(jogadaGanha)):
            if jogadaGanha[i] == 'XXX':
                vencedor = 'Você Ganhou!!!'
            elif jogadaGanha[i] == 'OOO':
                vencedor = 'Computador venceu!!!'
        return vencedor
