import os 
os.system("cls")
class Pessoa:
    def __init__(self, nome, altura):
        self._nome = nome
        self._altura = altura
    
    def __str__(self):
        return f"Nome: {self._nome} altura: {self._altura}"
    
    def __gt__(self, pessoa2):
        return self._altura > pessoa2._altura

    def __lt__(self, pessoa2):
        return self._altura < pessoa2._altura
        
x = int(input("Informe a quantidade de pessoas a serem cadastradas: "))
pessoas = []
for i in range(x):
    nome = str(input("Informe o nome: "))
    altura = float(input("Informe a altura: "))
    pessoas.append(Pessoa(nome, altura))

for pessoa in sorted(pessoas):
    print(Pessoa)

# A finalizar