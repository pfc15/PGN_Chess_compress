class Pq():
    def __init__(self):
        self.lista = [""]
        self.tamanho = 0
    
    def add(self, elemento):
        self.lista.append(elemento)
        self.tamanho +=1
        if self.tamanho >1:
            self.heap_up()

    def heap_up(self):
        index = self.tamanho
        print(f'index: {index}; tamanho: {self.tamanho}; real_tamanho: {len(self.lista)}')
        while self.lista[index//2][0] > self.lista[index][0]:
            print(f'index: {index}; tamanho: {self.tamanho}; real_tamanho: {len(self.lista)}')
            aux = self.lista[index]
            self.lista[index] = self.lista[index//2]
            self.lista[index//2] = aux
            index = index//2
            if index == 1:
                break
        
    def get(self):
        retorno = self.lista[1]
        self.lista[1] = self.lista[self.tamanho]
        self.lista.pop(self.tamanho)
        self.tamanho -= 1
        self.heap_down()
        return retorno
    
    def heap_down(self):
        index = 1
        while True:
            if (index*2)+1<=self.tamanho:
                if self.lista[index*2][0] < self.lista[index*2+1][0]:
                    direcao=index*2
                else:
                    direcao = index*2+1
                if self.lista[direcao][0] < self.lista[index][0]:
                    aux = self.lista[direcao]
                    self.lista[direcao] = self.lista[index]
                    self.lista[index] = aux
                    index = direcao
                else: 
                    break
            elif index*2 == self.tamanho:
                if self.lista[index][0] >self.lista[index*2][0]:
                    direcao = index*2 
                    aux = self.lista[direcao]
                    self.lista[direcao] = self.lista[index]
                    self.lista[index] = aux
                    index = direcao
                else:
                    break
            else:
                break
        
