

class Tabuleiro():
    def __init__(self):
        self.matriz = self.init_tabuleiro()
        self.registro_partida = ""

    def printa_tabuleiro(self):
        index = list(range(1, 9))
        index_alfabeto = [chr(i) for i in range(ord('a'), ord('h') + 1)]
        print("    ", end="")
        for i in range(8):
            print(f"  {index_alfabeto[i]}  ", end="")
        print()
        
        for i in range(8):
            print(f' {index[i]} |',end="")
            for carac in self.matriz[i].values():
                print(f' {carac} |', end="")
            print()


    def init_tabuleiro(self):
        matriz = []
        template = {}
        for carac in [chr(i) for i in range(ord('a'), ord('h') + 1)]:
            template[carac] = "  "
        for i in range(8):
            matriz.append(template.copy())

        matriz[0] = {'a':"Tb", 'b':"Cb", 'c':"Bb", 'd':"Qb", 'e':"Rb", 'f':"Bb", 'g':"Cb", 'h':"Tb"}
        
        matriz[7] = {'a':"Tp", 'b':"Cp", 'c':"Bp", 'd':"Qp", 'e':"Rp", 'f':"Bp", 'g':"Cp", 'h':"Tp"}
        for carac in matriz[0].keys():
            matriz[1][carac] = "Pb"
            matriz[6][carac] = "Pp"
        return matriz

    def fazer_movimento(self, pos_ant, pos_prox):
        peca = self.matriz[int(pos_ant[1])-1][pos_ant[0]]
        self.matriz[int(pos_ant[1])-1][pos_ant[0]] = "  "
        self.matriz[int(pos_prox[1])-1][pos_prox[0]] = peca
        self.escrever_movimento(pos_ant+pos_prox, True if peca[1]=="p" else False)

    def escrever_movimento(self, jogada, quebra_linha):
        if quebra_linha:
            jogada += '\n'
        else:
            jogada += ' '
        self.registro_partida += jogada

    def acabar_jogo(self):
        self.registro_partida += "0-0-0\n"
        with open("partida.txt", 'w') as fp:
            fp.write(self.registro_partida)



if __name__ == "__main__":
    jogo = Tabuleiro()
    jogo.fazer_movimento('e2', 'e4')
    jogo.fazer_movimento('e8', 'e5')
    jogo.fazer_movimento('b1', 'c3')



