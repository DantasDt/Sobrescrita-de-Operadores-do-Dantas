import os 
os.system("cls")
from random import *

class Personagem:
    def __init__(self, nome, vida):
        self._nome = nome
        self._vida = vida
    
    def __str__(self):
        return f"Nome: {self._nome}\nVida: {self._vida}"

    def TomarDano(self):
        return self._vida - randint(1, 10)

class Mago(Personagem):
    def __init__(self, nome, vida, mana : float):
        super().__init__(nome, vida)
        self._mana = mana

    def __add__(self, valor):
        return self._mana + valor
    
    def __sub__(self, valor):
        self._mana - valor
        if self._mana < 0:
            self._mana = 0
            return self._mana
        else:
            return self._mana
    
    def __mul__(self, fator: float):
        return self._mana * fator
    
    def __truediv__(self, valor):
        return self._mana / valor
    
    def __str__(self):
        super().__str__()
        return f"Mana de {self._nome}: {self._mana}"
        
        

class Barbaro(Personagem):
    def __init__(self, nome, vida, estamina, furia):
        super().__init__(nome, vida)
        self._estamina = estamina
        self._furia = False
    
    def __add__(self, valor):
        return self._estamina + valor
    
    def __sub__(self, valor):
        self._estamina - valor
        if self._estamina < 0:
            self._estamina = 0
            return self._mana
        else:
            return self._mana
    
    def __mul__(self, fator: float):
        return self._mana * fator
    
    def __truediv__(self, valor):
        return self._mana / valor
    
    def __str__(self):
        super().__str__()
        return f"Mana de {self._nome}: {self._mana}"

  # A finalizar
