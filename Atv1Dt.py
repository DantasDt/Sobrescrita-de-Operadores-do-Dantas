import os
os.system("cls")
class moeda:
    def __init__(self, moeda, saldo):
        self._moeda = moeda
        self._saldo = saldo

    def __str__(self):
        return f"Carteira atual {self._moeda} saldo atual {self._saldo}"
    
    def __add__(self, valor):
        if self._moeda == 'USD':
            conversao = valor * 0.14
            return f"Soma a Carteira de USD de {valor} yuan = {self._saldo + conversao}"
        elif self._moeda == 'BRL':
            conversao = valor * 0.85
            return f"Soma a Carteira de BRL de {valor} yuan = {self._saldo + conversao}"
        elif self._moeda == 'YUAN':
            return f"Soma a Carteira de BRL de {valor} yuan = {self._saldo + valor}"
        else:
            return ("Valor incorreto!")
    def __sub__(self, valor):
        if self._moeda == 'USD':
            conversao = valor * 0.14
            return f"Retirada na Carteira de USD de {valor} yuan = {self._saldo - (conversao)}"
        elif self._moeda == 'BRL':
            conversao = valor * 0.85
            return f"Retirada na Carteira de BRL de {valor} yuan = {self._saldo - (conversao)}"
        elif self._moeda == 'YUAN':
            return f"Retirada na Carteira de BRL de {valor} yuan = {self._saldo - valor}"
        else:
            return ("Valor incorreto!")
        
usd = moeda("USD", 10)
brl = moeda("BRL", 20)
yuan = moeda("YUAN", 30)
print(usd)
print(brl)
print(yuan)
print(usd + 10)
print(brl - 10)
print(yuan + 100)

# Ainda farei o main certinho dessa atividade!