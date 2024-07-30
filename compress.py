import chess
import chess.pgn
from priorityQueue import Pq
from bitarray import bitarray


class no_arvore():
    def __init__(self, _letra):
        self.letra = _letra
        self.binario = bitarray()
        self.pai = None
        self.esquerda = None
        self.direita = None
    
    def volta_raiz(self):
        no = self.pai
        retorno = bitarray() + self.binario
        while no != None:
            retorno += no.binario
            no = no.pai
        return retorno

frequencia = [(36.27654381254577, '['), 
    (3.026604832804491, 'E'), 
    (1.5682206492555528, 'v'), 
    (19.593605076885527, 'e'), 
    (8.75640712716622, 'n'), 
    (8.7686111789114, 't'), 
    (121.22284598486698, ' '), 
    (17.939956065413718, '"'), 
    (0.9275079326336344, 'L'), 
    (8.786917256529168, 'i'), 
    (4.149377593360996, 'C'), 
    (6.132536001952649, 'h'), 
    (6.91969733951672, 's'), 
    (36.27654381254577, ']'), 
    (10.666341225286795, '\n'), 
    (1.0129362948498901, 'S'), 
    (84.39711984378813, '.'), 
    (35.95313644129851, 'c'), 
    (7.072247986331462, 'o'), 
    (4.845008542836221, 'm'), 
    (1.6719550890895778, 'D'), 
    (7.3224310471076395, 'a'), 
    (28.84427629973151, '2'), 
    (70.58213326824506, '0'), 
    (25.21967293141323, '4'), 
    (17.27483524530144, '7'), 
    (5.632169880400293, 'R'), 
    (1.6414449597266292, 'u'), 
    (7.017329753478155, 'd'), 
    (4.710763973639248, '-'), 
    (0.8725896997803271, 'W'),
    (31.230168415914083, 'l'),
    (4.283622162557969, 'r'), 
    (0.5918965096412009, 'y'), 
    (3.844276299731511, 'K'),
    (4.436172809372712, 'g'), 
    (29.03954112765438, '1'),
    (5.4979253112033195, 'B'), 
    (29.399560654137172, 'k'), 
    (3.758847937515255, 'p'), 
    (5.870148889431291, 'f'), 
    (26.049548450085428, '5'), 
    (2.23944349524042, 'P'), 
    (6.883085184281182, '/'), 
    (23.889431291188675, '3'), 
    (4.741274103002197, 'N'), 
    (0.2318769831584086, 'q'), 
    (3.356114229924335, 'w'), 
    (3.8747864290944594, 'T'), 
    (0.5308762509153039, 'z'),
    (1.7085672443251159, 'U'), 
    (2.3492799609470345, 'O'), 
    (58.030266048328045, ':'), 
    (0.2257749572858189, 'F'), 
    (6.91359531364413, 'x'), 
    (0.2989992677568953, 'V'), 
    (17.28093727117403, '6'), 
    (3.6429094459360507, 'b'), 
    (16.634122528679523, '8'), 
    (27.306565779838905, '{'), 
    (27.306565779838905, '%'), 
    (27.306565779838905, '}'), 
    (19.648523309738835, '9'), 
    (3.4049304369050524, 'Q'), 
    (2.2699536246033682, '+'),
    (0.1769587503051013, 'G'),
    (0.0122040517451794, 'I'), 
    (0.1342445691969734, 'M'), 
    (0.12204051745179399, '#'), 
    (0.1647546985599219, 'A'), 
    (0.0183060776177691, '_'), 
    (0.0122040517451794, 'Y'), 
    (0.0549182328533073, 'H'), 
    (0.0549182328533073, 'j'), 
    (0.07932633634366609, '='), 
    (0.0061020258725897, 'Z'), 
    (0.0061020258725897, 'J')]

def cria_arvore(lista=frequencia):
    fila_nos = Pq()
    dicionario_letras = {}
    for l in lista:
        novo_no  = no_arvore(l[1])
        fila_nos.add((l[0], novo_no))
        dicionario_letras[l[1]] = novo_no
    
    while fila_nos.tamanho>1:
        n1 = fila_nos.get()
        n2 = fila_nos.get()
        if n1[1].letra != "":
            pai = no_arvore("")
            pai.pai = None
            pai.esquerda = n1[1]
            pai.direita = n2[1]
            pai.esquerda.pai = pai
            pai.esquerda.binario = bitarray([True])
            pai.direita.binario = bitarray([False])
            pai.direita.pai = pai
            fila_nos.add((n1[0]+n2[0], pai))
        else:
            pai = no_arvore("")
            pai.esquerda = n2[1]
            pai.direita = n1[1]
            pai.esquerda.pai = pai
            pai.direita.pai = pai
            pai.esquerda.binario = bitarray([True])
            pai.direita.binario = bitarray([False])
            fila_nos.add((n1[0]+n2[0], pai))
    
    return dicionario_letras, fila_nos.get()[1]


def printa_arvore(no, direcao, profundidade):
    if no != None:
        print(f'letra: {no.letra}; {direcao}; {profundidade}')
        profundidade += 1
        printa_arvore(no.esquerda, "esquerda", profundidade)
        printa_arvore(no.direita, "direita", profundidade)

def compress(path):
    texto = ""
    dic_jogo, arvore = cria_arvore()
    with open(path, 'r') as fp:
        linha = fp.readline()
        
        while linha !="":
            texto += linha
            linha = fp.readline()
    
    total = bitarray()
    novo_path = path[:-4] + ".pgnin"
    with open(f"{novo_path}", "wb") as fp:
        
        for letra in texto:
            codificado = dic_jogo[letra].volta_raiz()
            codificado.reverse()
            total += codificado
        fp.write(total)