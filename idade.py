#Gabarito que eu estou fazendo da OBI 2019 para treinar para proxima, questão da Soma.py ///// QUESTÃO DE NIVEL FÁCIL
class idade():
    def __init__(self):
        self.idadeMae = 0
        self.idadeFilhos = []

    def filhoMaisVelho(self):
        return max(self.idadeFilhos)

    def calcularIdades(self):
        idadetemp = self.idadeMae
        for x in self.idadeFilhos:
            idadetemp -= x
        self.idadeFilhos.append(idadetemp)
        return self.filhoMaisVelho()

    def mainLoop(self):
        self.idadeMae = int(input())
        self.idadeFilhos.append(int(input()))
        self.idadeFilhos.append(int(input()))
        print(self.calcularIdades())

problema = idade()
problema.mainLoop()