import chess.pgn
import bitarray
from compress import *

frequencia_alfabeto = [(14.63, "a"),
    (10, " "),
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

with open("teste.bin", "rb") as fp:
    a= bitarray()
    bitarray.fromfile(a,fp)
    no = arvore
    print(len(a))
    for b in a:
        if b:
            no = no.esquerda
            if no.esquerda==None and no.direita ==None:
                print(f'{no.letra}', end="")
                no = arvore
        else:
            no = no.direita
            if no.esquerda==None and no.direita ==None:
                print(f'{no.letra}', end="")
                no = arvore
    print()