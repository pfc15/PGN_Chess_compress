import chess.pgn
import bitarray
import time
from compress import *


def ler_arquivo(path, output="reconstrucao.pgn"):
    dic, arvore = cria_arvore()
    texto = ""

    with open(path, "rb") as fp:
        a= bitarray()
        bitarray.fromfile(a,fp)
        no = arvore
        for b in a:
            if b:
                no = no.esquerda
                if no.esquerda==None and no.direita ==None:
                    texto += no.letra
                    no = arvore
                    
            else:
                no = no.direita
                if no.esquerda==None and no.direita ==None:
                    texto += no.letra
                    no = arvore
    novo_path = path[:-6]+'.pgn'
    print(novo_path)
    with open(novo_path, 'w') as fp:
        fp.write(texto)