from bitarray import *
from compress import *
import time


def frequencia_jogos():
    texto = ""
    with open("jogos_pfc15.pgn", 'r') as fp:
        linha = fp.readline()
        
        while linha !="":
            texto += linha
            linha = fp.readline()

    dic = {}
    quant = 0
    for letra in texto:
        if letra in dic.keys():
            dic[letra] +=1
        else:
            dic[letra] = 1
        quant+=1
    tupla = []
    for k, v in dic.items():
        tupla.append((v*1000/quant, k))
    return texto, tupla


texto, tupla = frequencia_jogos()
print(tupla)
dic_jogo, arvore_jogo = cria_arvore(tupla)


quant =0
total = bitarray()
with open("teste.bin", "wb") as fp:
    
    for letra in texto:
        codificado = dic_jogo[letra].volta_raiz()
        codificado.reverse()
        total += codificado
        quant += len(codificado)
    fp.write(total)
