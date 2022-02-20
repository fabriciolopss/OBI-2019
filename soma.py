#Gabarito que eu estou fazendo da OBI 2019 para treinar para proxima, questão da Soma.py /////// QUESTÃO DE NÍVEL MÉDIO QUASE DIFICIL
class Soma():
    def __init__(self):
        self.tamanhoLinha = 0
        self.valorDesejado = 0
        self.linha = []
        self.numQuadrados = 0
    def testarQuadrados(self):
        for y in range(self.tamanhoLinha):
            somaTemp = 0
            for x in range(self.tamanhoLinha):
                z = x + y
                if (z < self.tamanhoLinha):
                    somaTemp += self.linha[z]
                    if (somaTemp == self.valorDesejado):
                        self.numQuadrados += 1

    def mainLoop(self):
        self.tamanhoLinha = int(input())
        self.valorDesejado = int(input())
        for x in range(self.tamanhoLinha):
            self.linha.append(int(input()))
        self.testarQuadrados()
        print(self.numQuadrados)

soma = Soma()
soma.mainLoop()