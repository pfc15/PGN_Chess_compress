import chess
import chess.pgn
from priorityQueue import Pq
import bitarray


class Compress():
    def __init__(self):
        pass

class no_arvore():
    def __init__(self, _letra):
        self.letra = _letra
        self.binario = None
        self.pai = None
        self.esquerda = None
        self.direita = None
    
    def volta_raiz(self):
        no = self.pai
        retorno = [self.binario]
        while no != None:
            retorno.append(no.binario)
            no = no.pai
        return retorno


def cria_arvore(lista):
    fila_nos = Pq()
    dicionario_letras = {}
    for l in lista:
        novo_no  = no_arvore(l[1])
        fila_nos.add((l[0], novo_no))
        dicionario_letras[l[1]] = novo_no
    
    while fila_nos.tamanho>1:
        
        n1 = fila_nos.get()
        n2 = fila_nos.get()
        print(f"peson1: {n1[0]}, {n1[1].letra}; peson2:{n2[0]}, {n2[1].letra}")
        if n1[1].letra != " ":
            pai = no_arvore(" ")
            pai.pai = None
            pai.esquerda = n1[1]
            pai.direita = n2[1]
            pai.esquerda.pai = pai
            pai.esquerda.binario = 1
            pai.direita.binario = bin(0)
            pai.direita.pai = pai
            fila_nos.add((n1[0]+n2[0], pai))
        else:
            pai = no_arvore(" ")
            pai.esquerda = n2[1]
            pai.direita = n1[1]
            pai.esquerda.pai = pai
            pai.direita.pai = pai
            pai.esquerda.binario = "1"
            pai.direita.binario = "0"
            fila_nos.add((n1[0]+n2[0], pai))
    
    return dicionario_letras, fila_nos.get()[1]


def printa_arvore(no, direcao, profundidade):
    if no != None:
        print(f'letra: {no.letra}; {direcao}; {profundidade}')
        profundidade += 1
        printa_arvore(no.esquerda, "esquerda", profundidade)
        printa_arvore(no.direita, "direita", profundidade)
        


if __name__ == "__main__":
    frequencia_alfabeto = [(14.63, "a"),
    (12.57, "e"),
    (10.73, "o"),
    (7.81, "s"),
    (6.53, "r"),
    (6.18, "i"),
    (5.05, "n"),
    (4.99, "d"),
    (4.74, "m"),
    (4.63, "u"),
    (4.34, "t"),
    (3.88, "c"),
    (2.78, "l"),
    (2.52, "p"),
    (1.67, "v"),
    (1.30, "g"),
    (1.28, "h"),
    (1.20, "q"),
    (1.04, "b"),
    (1.02, "f"),
    (0.47, "z"),
    (0.40, "j"),
    (0.21, "x"),
    (0.02, "k"),
    (0.01, "w"),
    (0.01, "y")]

    dic, arvore = cria_arvore(frequencia_alfabeto)

    print("".join(reversed(dic["y"].volta_raiz())))

    a = "".join(reversed(dic["y"].volta_raiz()))
    


    """
    
    pgn = open("minhas_partidas.pgn")
    
    quant_jogos = 0
    contra_linha = 0
    linha = pgn.readline()

    while linha:
        palavras = linha.replace('/', " ").split()
        print(linha)
        print('--'*25)
        
        linha = pgn.readline()
    
    pgn.close()
    palavras_chave_lista = Pq()


    while not palavras_chave_lista.empty():
        print(palavras_chave_lista.get(), end=";; ")
    """