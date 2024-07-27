import chess.pgn
import bitarray
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
                i = linha.index('"')+1
                linha = linha[i:linha[i+1:].index('"')+i+1]
                texto += linha+'\n'
            else:
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

with open("teste.bin", "rb") as fp:
    a= bitarray()
    bitarray.fromfile(a,fp)
    no = arvore
    print()
    index_cabecalho = 1
    contagem_jogada = 0
    print(cabecalho[0], end="")
    for b in a:
        if b:
            no = no.esquerda
            if no.esquerda==None and no.direita ==None:
                    
                
                if no.letra == '\n':
                    print(cabecalho[index_cabecalho], end="")
                    index_cabecalho = (index_cabecalho+1)%len(cabecalho)
                    print("")
                    print(cabecalho[index_cabecalho], end="")
                    index_cabecalho = (index_cabecalho+1)%len(cabecalho)
                    
                else:
                    print(f'{no.letra}', end="")
                no = arvore
                
        else:
            
            no = no.direita
            if no.esquerda==None and no.direita ==None:
                
                if no.letra == '\n':
                    print(cabecalho[index_cabecalho], end="")
                    index_cabecalho = (index_cabecalho+1)%len(index_cabecalho)
                    print(cabecalho[index_cabecalho], end="")
                    index_cabecalho = (index_cabecalho+1)%len(cabecalho)
                else:
                    print(f'{no.letra}', end="")
                no = arvore
    print()
