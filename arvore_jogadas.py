from bitarray import *
from compress import *
def frequencia_jogos():
    texto = ""
    with open("minhas_partidas.pgn", 'r') as fp:
        linha = fp.readline()
        
        while linha !="":
            print(linha)
            if linha[:2] == "1.":
                texto += linha
            elif '"' in linha:
                print("-="*25)
                print(f"linha do ANTES negocio: {linha}")
                print("-="*25)
                i = linha.index('"')+1
                linha = linha[i:linha[i+1:].index('"')+i+1]
                print("-="*25)
                print(f"linha do negocio: {linha}")
                print("-="*25)
                print('oi')
                texto += linha+'\n'
            else:
                texto += linha
            
            linha = fp.readline()

    dic = {}
    for letra in texto:
        if letra in dic.keys():
            dic[letra] +=1
        else:
            dic[letra] = 1
    print(dic.keys())
    tupla = []
    for k, v in dic.items():
        tupla.append((v, k))
    return texto, tupla


texto, tupla = frequencia_jogos()
"""
tupla = [(18155, 'e'), 
         (17774, '4'), 
         (92390, ' '), 
         (14536, '6'), 
         (16893, 'd'), 
         (13720, 'c'), 
         (16950, '5'), 
         (14287, '3'), 
         (22176, 'x'), 
         (14959, 'N'), 
         (15204, 'f'), 
         (14059, 'B'),
         (9068, 'b'),
         (7378, '+'),
         (7201, '2'), 
         (11284, 'Q'), 
         (6373, 'a'), 
         (7791, '7'), 
         (4820, 'O'), 
         (4047, '-'), 
         (13586, 'R'), 
         (6836, '1'), 
         (10324, 'g'), 
         (1351, '0'), 
         (5129, '8'), 
         (9733, 'K'), 
         (7118, 'h'), 
         (254, '='), 
         (403, '#'), 
         (116, '/')]

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
"""

print(tupla)
dic_jogo, arvore_jogo = cria_arvore(tupla)
texto = ""
with open("Vienna.pgn", 'r') as fp:
        linha = fp.readline()
        
        while linha !="":
            print(linha)
            if linha[:2] == "1.":
                texto += linha
            elif '"' in linha:
                print("-="*25)
                print(f"linha do ANTES negocio: {linha}")
                print("-="*25)
                i = linha.index('"')+1
                linha = linha[i:linha[i+1:].index('"')+i+1]
                print("-="*25)
                print(f"linha do negocio: {linha}")
                print("-="*25)
                print('oi')
                texto += linha+'\n'
            
            linha = fp.readline()
            while linha == '\n':
                linha = fp.readline()

print(texto)

quant =0
total = bitarray()
with open("teste.bin", "wb") as fp:
    for letra in texto:
        codificado = dic_jogo[letra].volta_raiz()
        codificado.reverse()
        total += codificado
        quant += len(codificado)
    fp.write(total)

