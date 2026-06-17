import os 
os.system("cls")
from random import *

pocoes = {}

class Personagem:
    def __init__(self, nome, vida):
        self._nome = nome
        self._vida = vida
    
    def __str__(self):
        return f"Nome: {self._nome}\nVida: {self._vida}"

    def TomarDano(self):
        self._vida -= randint(1, 10)
        return self._vida

class Mago(Personagem):
    def __init__(self, nome, vida, mana : float):
        super().__init__(nome, vida)
        self._mana = mana

    def __add__(self, valor):
        self._mana += valor
        return self._mana
    
    def __sub__(self, valor):
        self._mana = self._mana - valor
        if self._mana < 0:
            self._mana = 0
            return self._mana
        else:
            return self._mana
    
    def __mul__(self, fator: float):
        self._mana *= fator
        return self._mana
    
    def __truediv__(self, valor):
        self._mana = self._mana / valor
        return self._mana
    
    def __str__(self):
        print(super().__str__())
        return f"Mana de {self._nome}: {self._mana}"
        
        

class Barbaro(Personagem):
    def __init__(self, nome, vida, estamina, furia : bool):
        super().__init__(nome, vida)
        self._estamina = estamina
        self._furia = furia
    
    def __add__(self, valor):
        if self._furia == True:
            self._estamina = self._estamina * 1.5
        else:
            self._estamina = self._estamina + valor
        return self._estamina
    
    def __sub__(self, valor):
        self._estamina = self._estamina - valor
        if self._estamina <= 0:
            self._estamina = 5
            self._furia = True
            return self._estamina
        else:
            return self._estamina
    
    def __mul__(self, fator: float):
        if self._furia == True:
            self._estamina = self._estamina * fator
            self._vida = self._vida + 5
            return self._estamina, self._vida
        else:
            self._estamina = self._estamina * fator
        return self._estamina
    
    def __truediv__(self, valor):
        self._estamina = self._estamina / valor
        return self._estamina
    
    def __str__(self):
        print(super().__str__())
        return f"Estamina de {self._nome}: {self._estamina}\nEstado: {self._furia}"
    
while True:
    x = str(input("Oque deseja fazer? ")).lower()
    match x:
        case "cadastrar":
            os.system("cls")
            nome = str(input("Informe o nome: "))
            vida = int(input("Informe a vida: "))
            classe = str(input("Informe a classe: ")).lower()
            if classe == "mago":
                mana = int(input("Informe a mana: "))
                objM = Mago(nome, vida, mana)
            elif classe == "barbaro":
                estamina = int(input("Informe a estamina: "))
                furia = bool(input("Informe a furia: "))
                objB = Barbaro(nome, vida, estamina, furia)
            else:
                print("Classe Inválida!")
        
        case "listar":
            os.system("cls")
            match classe:
                case "mago":
                    print(objM)

                case "barbaro":
                    print(objB)
        
        case "somar":
            os.system("cls")
            valor = int(input("Informe o valor: "))
            match classe:
                case "mago":
                    print(f"Mana de {objM._nome} + {valor} = {objM + valor}")

                case "barbaro":
                    print(f"Estamina de {objB._nome} + {valor} = {objB + valor}")
        
        case "subtrair":
            os.system("cls")
            valor = int(input("Informe o valor: "))
            match classe:
                case "mago":
                    print(f"Mana de {objM._nome} - {valor} = {objM - valor}")

                case "barbaro":
                    print(f"Estamina de {objB._nome} - {valor} = {objB - valor}")
        
        case "multiplicar":
            os.system("cls")
            fator = int(input("Informe o valor: "))
            match classe:
                case "mago":
                    print(f"Mana de {objM._nome} * {fator} = {objM * fator}")

                case "barbaro":
                    print(f"Estamina de {objB._nome} * {fator} = {objB * fator}")
        
        case "dividir":
            os.system("cls")
            valor = int(input("Informe o valor: "))
            match classe:
                case "mago":
                    print(f"Mana de {objM._nome} / {valor} = {objM / valor}")

                case "barbaro":
                    print(f"Estamina de {objB._nome} / {valor} = {objB / valor}")

        case "enfurecer":
            os.system("cls")
            match classe:
                case "mago":
                    print("Essa classe não pode ficar enfurecida!")

                case "barbaro":
                    objB._furia = True
        case "sair":
            os.system("cls")
            break
        
        case "pocao":
            e = str(input("Informe oque deseja fazer com uma poção: ")).lower()
            match e:
                case "criar":
                    os.system("cls")
                    nome = input("Informe o nome: ")
                    poder = int(input("Informe o poder da poção: "))
                    pocoes[nome] = poder
                    
                
                case "usar":
                    os.system("cls")
                    match classe:
                        case "mago":
                            nome = str(input("Informe o nome da poção: "))
                            objM + pocoes[nome]
                    
                        case "barbaro":
                            nome = str(input("Informe o nome da poção: "))
                            objB + pocoes[nome]
                case "listar":
                    os.system("cls")
                    print(pocoes)

        case "atacar":
            os.system("cls")
            a = str(input("Informe o tipo de ataque: ")).lower()
            match a:
                case "normal":
                    os.system("cls")
                    match classe:
                        case "mago":
                            objM.TomarDano()
                            objM - 2
                    
                        case "barbaro":
                            objB.TomarDano()
                            objB - 2
                case "especial":
                    os.system("cls")
                    match classe:
                        case "mago":
                            objM.TomarDano()
                            objM / 2
                    
                        case "barbaro":
                            objB.TomarDano()
                            objB / 2
# Finalizado
