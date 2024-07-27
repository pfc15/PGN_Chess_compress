import chess.pgn
import bitarray
from compress import *
def frequencia_jogos():
    texto = ""
    with open("Vienna.pgn", 'r') as fp:
        linha = fp.readline()
        while linha !="":
            texto+=linha
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


dic, arvore = cria_arvore(tupla)
cabecalho = ['[Event "', '"]',
'[Site "', '"]',
'[Date "', '"]',
'[Round "', '"]',
'[White "', '"]',
'[Black "', '"]',
'[Result "', '"]',
'[CurrentPosition "', '"]',
'[Timezone "', '"]',
'[ECO "', '"]',
'[ECOUrl "', '"]',
'[UTCDate "', '"]',
'[UTCTime "', '"]',
'[WhiteElo "', '"]',
'[BlackElo "', '"]',
'[TimeControl "', '"]',
'[Termination "', '"]',
'[StartTime "', '"]',
'[EndDate "', '"]',
'[EndTime "', '"]',
'[Link "', '"]"', "\n", "\n"]
texto = ""

with open("teste.bin", "rb") as fp:
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

with open("reconstrucao.pgn", 'w') as fp:
    fp.write(texto)
