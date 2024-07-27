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

frequencia = [(15.933669933829833, '['),
(7.159190528983247, 'E'), 
(2.667994411314863, 'v'), 
(40.775876062222025, 'e'), 
(7.539776727168664, 'n'), 
(12.235728806785183, 't'), 
(139.50958267445938, ' '), 
(31.867339867659666, '"'),
 (0.6784330743502008, 'G'),
   (4.1370395165791765, 'r'), 
   (1.4348334601342199, 'm'), 
   (19.90126636680331, 'a'), 
   (0.8834092829408037, 'y'), 
   (15.933669933829833, ']'), 
   (28.533099362877856, '\n'), 
   (2.9181211816114905, 'S'), 
   (9.129370161410689, 'i'), 
   (2.146890855234598, 'D'), 
   (38.20493700468824, '1'), 
   (15.675100375571917, '8'), 
   (35.89205359657995, '4'), 
   (29.09157143263026, '6'), 
   (66.41676993175217, '.'), 
   (2.2796261650955616, '?'), 
   (24.449212702681056, 'R'), 
   (8.84047998203962, 'o'), 
   (5.130572120754186, 'u'), 
   (25.64060020734019, 'd'),
    (3.5509632009707297, 'W'),
    (15.911204776298055, 'h'), 
    (0.4741910212344927, 'H'),
    (1.0706189290389545, 'p'), 
    (3.129778205023635, ','), 
    (4.084473984576715, 'C'), 
    (11.054472647679596, 'l'), 
    (23.161503999715734, 'B'),
    (23.696850172008958, 'c'), 
    (4.377695681249662, 'k'), 
    (0.6928959372056266, 'L'),
    (0.2845586620691893, 'w'),
    (0.5096507306719071, 'J'), 
    (12.086474998739089, 'b'), 
    (4.826411507505308, 's'), 
    (12.417725949011581, '0'), 
    (6.8929123382389355, '-'), 
    (8.208665780345234, 'O'), 
    (39.381567984301995, '2'), 
    (33.34034941248841, '5'), 
    (21.900445140489094, 'N'), 
    (37.37034906082794, '3'), 
    (21.833783823368652, 'f'),
    (15.685378552220442, 'g'), 
    (26.36205479251922, 'x'), 
    (18.64681490685072, '7'), 
    (8.185393051791072, '9'), 
    (15.099889560991912, 'Q'), 
    (13.852485993598311, 'K'), 
    (7.64299898693886, '+'), 
    (0.3816140158502699, 'F'), 
    (1.0785478081678175, 'A'), 
    (0.4022437846948112, 'V'), 
    (1.542754314943742, '/'), 
    (1.320892530430561, 'T'), 
    (1.0369211927412874, 'M'), 
    (0.7086802799158628, 'P'), 
    (0.04382908185121414, 'X'), 
    (0.4810186671510135, 'U'), 
    (0.12260396430741645, 'Y'), (0.2845586620691893, 'j'), (0.6221233494257766, 'z'), (0.7192521187543467, 'I'), (0.1548333896552942, '='), 
    (0.23316777882655965, 'Z'), (0.0002936621899578837, '*'), (0.04045196666669848, 'q'), (0.020923431034499215, "'"), (0.03076111439808832, '('), 
    (0.03076111439808832, ')'), (0.002055635329705186, '&'), (0.0024227130671525404, '_'), (7.341554748947093e-05, '`'), (0.00036707773744735464, '#'), 
    (7.341554748947093e-05, '!'),
    (0.01, ":")]

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