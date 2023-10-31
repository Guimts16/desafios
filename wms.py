rua = "a21"
qtd = 20
perg = input("Qual procedimento gostaria de ter agora? ")
item1 = "celular"

def dados():
    if prg == item1:
        print(item1)
        print(rua)

def add():
    valor = qtd - prg
    print(valor) 

if perg == "dados":
    prg = input("Que item está procurando? ").lower()
    
    dados()

if perg == "add":
    prg = int(input("Quantos quer remover? "))

    add()