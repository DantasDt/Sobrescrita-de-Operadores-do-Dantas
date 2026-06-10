import os 
os.system("cls")
class Pessoa:
    def __init__(self, nome, altura):
        self._nome = nome
        self._altura = altura
    
    def __str__(self):
        return f"Nome: {self._nome}\nAltura: {self._altura}\n"
    
    def __gt__(self, pessoa2):
        return self._altura > pessoa2._altura

    def __lt__(self, pessoa2):
        return self._altura < pessoa2._altura
    
pessoas = [] 
while True:
    y = str(input("Oque deseja fazer: ")).lower()
    if y == "cadastrar":
        x = int(input("Informe a quantidade de pessoas a serem cadastradas: "))
        for i in range(x):
            nome = str(input("Informe o nome: "))
            altura = float(input("Informe a altura: "))
            os.system("cls")
            pessoas.append(Pessoa(nome, altura))
    elif y == "listar":
        for pessoa in sorted(pessoas, reverse=True):
            print(pessoa)
    elif y == "comparar":
        p1 = str(input("Informe a primeira pessoa: "))
        p2 = str(input("Informe a segunda pessoa: "))
        for pessoa in pessoas:
            if pessoa._nome == p1:
                pessoa1 = pessoa
            if pessoa._nome == p2:
                pessoa2 = pessoa
        print(p1 > p2)
        print(p1 < p2)
    elif y == "sair":
        break
