import os
os.system('cls')
from random import *
class Onibus:
    def __init__(self, placa, motorista):
        self._placa = placa
        self._motorista = motorista
        self._numeroassentos = 0
        self._assentos = []
    
    def __len__(self):
        self._numeroassentos = randint(15,40)
        return self._numeroassentos
    
    def __getitem__(self, indice):
        if indice > self._numeroassentos:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
        else:
            return self._assentos[indice].append(random.randint(True, False))
    
    def __setitem__(self, indice, valor):
        if isinstance(valor, bool) and indice < self._numeroassentos:
            return self._assentos[indice].append(valor)
        elif indice < 20:
            raise TypeError(f"Valor deve ser booleano (True/False)")
        else:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")

    def __str__(self):
        for assento in range(0, self._numeroassentos):
            if self._assentos[assento] == True:
                vazio += 1
            else:
                vago += 1
        return f"Placa do Onibus {self._placa}\nMotorista: {self._motorista}\nAssentos Totais: {self._numeroassentos}\nAssentos Vazios: {vazio}\nAssentos Vagos: {vago}"
        
while True:
    x = str(input("Oque deseja fazer: ")).lower()
    if x == "cadastrar":
        placa = str(input("Informe a placa: "))
        motorista = str(input("Informe o nome do motorista: "))
        onibus = Onibus(placa, motorista)
    elif x == "listar":
        os.system("cls")
        len(onibus)
        print(onibus)
    
    elif x == "verifica":
        y = int(input("Informe o indice: "))
        onibus[y]
    
    elif x == "mudar":
        y = int(input("Informe o indice: "))
        w = str(input("Informe o valor(True or False): ")).lower()
        if w == "true":
            onibus[y, w]
        elif w == "false":
            onibus[y, w]
        else:
            print("Valor inváido!")

# não finalizado
