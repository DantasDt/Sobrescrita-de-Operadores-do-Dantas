import os
os.system('cls')
from random import *
class Onibus:
    def __init__(self, placa, motorista):
        self._placa = placa
        self._motorista = motorista
        self._numeroassentos = randint(15, 40)
        self._assentos = [False] * self._numeroassentos
    
    def __len__(self):
        return self._numeroassentos
    
    def __getitem__(self, indice):
        if indice < 0 or indice >= self._numeroassentos:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
        else:
            return self._assentos[indice]
    
    def __setitem__(self, indice, valor):
        if isinstance(valor, bool):
            self._assentos[indice] = valor
            return self._assentos[indice]
        else:
            raise IndexError(f"Escolha um valor entre 0 e {len(self._assentos)}")

    def __str__(self):
        vago = self._assentos.count(True)
        vazio = self._assentos.count(False)
        return f"Placa do Onibus {self._placa}\nMotorista: {self._motorista}\nAssentos Totais: {self._numeroassentos}\nAssentos Vazios: {vazio}\nAssentos Vagos: {vago}"
        
while True:
    x = str(input("Oque deseja fazer: ")).lower()
    if x == "cadastrar":
        placa = str(input("Informe a placa: "))
        motorista = str(input("Informe o nome do motorista: "))
        onibus = Onibus(placa, motorista)
    elif x == "listar":
        os.system("cls")
        print(onibus)
    
    elif x == "verifica":
        y = int(input("Informe o indice: "))
        print(onibus[y])
    
    elif x == "mudar":
        y = int(input("Informe o indice: "))
        if y < 0 or y > 40:
            print("Indice inválido!")
        else:
            onibus[y] = True
    # Finalizado!
