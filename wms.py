import mysql.connector

conn = mysql.connector.connect(
    user="root",
    password="3141592",
    host="127.0.0.1",
    database="bot",
    auth_plugin='mysql_native_password'
)
print("Funções: Remover produto, Novo produto, Add, Remove, List, Dados")
print(f"Obs: \nAdd: Adiciona nova quantidade de estoque.\nRemove: Retira uma quantidade do estoque.\nDados: Junta informação unitaria, para uma melhor visualização do produto.")
perg = input("Qual procedimento gostaria de ter agora? ").lower()

def produ():
    confimar = input(f"Você quer adicionar o produto '{produto}' na rua: '{rua}' com {quantidade} unidades? (S/N) ").lower()
    if confimar == "s":
        sql_p = f"insert into wms.estoque (produtos, rua, quantidade) values ('{produto}', '{rua}', {quantidade})"
        c = conn.cursor() 
        c.execute(sql_p)
        conn.commit()
        print("Adicionado com sucesso!")

def add():
    sql_a = f"SELECT * FROM wms.estoque where produtos = '{prg_item}'"
    c = conn.cursor() 
    c.execute(sql_a)
    r = c.fetchall()

    estq = r[0][3]
    print("===== ESTOQUE =====")
    print(f"Item: {r[0][1]}")
    print(f"Rua: {r[0][2]}")
    print(f"Estoque: {r[0][3]}")
    print()

    if prg_qtd > 0:
        confimar = input(f"Você quer adicionar em {prg_item} {prg_qtd} novos produtos? (S/N) ").lower()

        if confimar == "s":
            valor_add = prg_qtd + estq   
            adi = f"update wms.estoque set quantidade = {valor_add} where produtos = '{prg_item}'"
            c = conn.cursor() 
            c.execute(adi)
            conn.commit()
            print(f"Certo! Estoque atualizado: {valor_add}")

        if confimar == "n":
            print("Pedido cancelado!")

def dados():
    sql_d = f"SELECT * FROM wms.estoque where produtos = '{prg_dados}'"
    c = conn.cursor() 
    c.execute(sql_d)
    r = c.fetchall()
    print("=== PRODUTO ===")
    print(f"Item: {r[0][1]}")
    print(f"Rua: {r[0][2]}")
    print(f"Estoque: {r[0][3]}")

def list():
    sql_l = f"Select * from wms.estoque"
    c = conn.cursor() 
    c.execute(sql_l)
    r = c.fetchall()
    print("=== LISTA GERAL ===")
    if len(r) > 0:
        for tupla in r:
            print(f"Item: {tupla[1]} / Rua: {tupla[2]} / Quantidade: {tupla[3]}")

def remove():
    global conn
    sql_r = f"SELECT * FROM wms.estoque where produtos = '{prg_item}'"
    c = conn.cursor()
    c.execute(sql_r)
    r = c.fetchall()
    
    qtd = int(r[0][3])
    valor = qtd - prg_rem
    confimar = input(f"Você quer remover {prg_rem} de {prg_item}? (S/N) ").lower()
    if confimar == "s":
        rem = f"update wms.estoque set quantidade = {valor} where produtos = '{prg_item}'"
        c = conn.cursor() 
        c.execute(rem)
        conn.commit()
        print(f"Certo! Estoque atualizado: {valor}")

    if confimar == "n":
        print("Pedido cancelado!")

def deletar():
    confirmar = input(f"Tem certeza que deseja deletar o produto '{produto}'? (S/N)").lower()
    if confirmar == "s":
        dele = f"delete from wms.estoque where produtos = '{produto}'"
        c = conn.cursor() 
        c.execute(dele)
        conn.commit()
        print("Produto deletado.")
    if confirmar == "n":
        print("Pedido cancelado!")

if perg == "dados":
    prg_dados = input("Qual produto está procurando? ").lower()
    dados()

if perg == "list" or "lista":
    list()

if perg == "add":
    prg_item = input(f"Que item está procurando? ")
    prg_qtd = int(input("Quantos produtos deseja adicionar? "))
    if prg_qtd > 0:
        add()
    else: 
        print("Você não pode adicionar números menores que zero.")

if perg == "remover produto":
    produto = input("Que item quer remover? ")
    deletar()
if perg == "novo produto":
    produto = input("Qual o nome desse produto? ")
    rua = input("Onde ele se localiza? (Rua) ")
    quantidade = int(input("Quantos produtos temos em estoque? "))
    produ()

if perg == "remove" or "remover":
    prg_item = input("Qual produto está procurando? ").lower()
    prg_rem = int(input("Quantos quer remover? "))
    if prg_rem > 0:
        remove()
    else: 
        print("Você não pode remover números menores que zero.")

funcoes = ["add", "list", "dados", "remove", "novo produto", "remover produto", "lista", "adicionar", "remover"]
if perg not in funcoes:
    print("Função não encontrada!")
