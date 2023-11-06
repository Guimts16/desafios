import mysql.connector
import tkinter as tk
from tkinter import messagebox
import string
from random import choice

conn = mysql.connector.connect(
    user="root",
    password="3141592",
    host="127.0.0.1",
    database="wms",
    auth_plugin='mysql_native_password'
)

def Adicionar():
    prg_itemAdicionar = item_entry.get()
    prg_qtd = int(quantity_entry.get())
    if prg_itemAdicionar == "":
        messagebox.showinfo("Erro", "Adicione um produto na tabela para continuarmos!")
    else:
        sql_a = f"SELECT * FROM wms.estoque where id = '{prg_itemAdicionar}'"
        c = conn.cursor()
        c.execute(sql_a)
        r = c.fetchall()
        if r:
            confirmation = messagebox.askquestion("Confirmação", f"Você quer adicionar à '{r[0][1]}' {prg_qtd} unidades?")

            if confirmation == "yes":

                estq = int(r[0][3])

                if prg_qtd > 0:

                    valor_adicionar = prg_qtd + estq
                    adi = f"update wms.estoque set quantidade = {valor_adicionar} where id = '{prg_itemAdicionar}'"
                    c = conn.cursor()
                    c.execute(adi)
                    conn.commit()
                    messagebox.showinfo("Sucesso", f"Estoque de {r[0][1]} atualizado para: {valor_adicionar} UNIDADES")
                else:
                    messagebox.showinfo("Cancelado", "Não é possível adicionar número menores que zero.")
            else:
                messagebox.showinfo("Cancelado", "Pedido cancelado!")
        else:
            messagebox.showinfo("Erro", "Este produto não existe. Verifique-o na lista!")
def list_products():
    sql_l = f"Select * from wms.estoque"
    c = conn.cursor()
    c.execute(sql_l)
    r = c.fetchall()

    product_list = "\n".join(f"ID: {row[0]}, Produto: {row[1]}, Quantidade: {row[3]}, Rua: {row[2]}\n" for row in r)

    messagebox.showinfo("Lista Geral", product_list)


def show_data():
    prg_dados = item_entry.get()
    sql_d = f"SELECT * FROM wms.estoque where produtos = '{prg_dados}'"
    c = conn.cursor()
    c.execute(sql_d)
    r = c.fetchall()
    if r:
        produto_data = "\n".join(f"ID: {row[0]}, Produto: {row[1]}, Quantidade: {row[3]}, Rua: {row[2]}\n" for row in r)
        messagebox.showinfo("Dados do Produto", produto_data)
    else:
        messagebox.showinfo("Erro", "Este produto não existe.")

def id_r(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(choice(chars) for _ in range(size))

def adicionar_produto():
    nome = item_entry.get()
    quantidade = quantity_entry.get()
    rua = rua_entry.get()

    confirmation = messagebox.askquestion("Confirmação", f"Você quer adicionar o produto {nome} com {quantidade} unidades na rua {rua}?")

    if int(quantidade) > 0:
        if confirmation == "yes":
            add = f"insert into wms.estoque (id, produtos, rua, quantidade) values ('{id_r()}', '{nome}', '{rua}', '{quantidade}')"
            c = conn.cursor()
            c.execute(add)
            conn.commit()
            messagebox.showinfo("Sucesso", "Produto adicionado! Caso não tenha adicionado a rua, utilize o comando 'Atualizar' com o nome!")
    else:
        messagebox.showinfo("Erro", f"{quantidade} não é um número inteiro.")

def atualizar():
    nome = item_entry.get()
    quantidade = int(quantity_entry.get())
    rua = rua_entry.get()
    sql = f"SELECT * FROM wms.estoque where id = '{nome}'"
    c = conn.cursor()
    c.execute(sql)
    r = c.fetchall()
    if r:
        confirmation = messagebox.askquestion("Confirmação", f"Você deseja atualizar o produto {r[0][1]} com {quantidade} unidades na rua {rua}?")

        if confirmation == "yes":
            if rua:
                rua = f"update wms.estoque set rua = '{rua}' where id = '{nome}'"
                c = conn.cursor() 
                c.execute(rua)
                conn.commit()
            else:
                messagebox.showinfo("Verificação", "Você não adicionou um endereço. Caso queria adicionar, repita o processo!")
            if quantidade:
                qtdf = f"update wms.estoque set quantidade = {quantidade} where id = '{nome}'"
                c = conn.cursor()
                c.execute(qtdf)
                conn.commit()
            messagebox.showinfo("Sucesso", "Alterado com sucesso.")

        else:
            messagebox.showinfo("Cancelado", "Atualização cancelada.")
    else:
        messagebox.showinfo("Erro", "Produto inexistente, verifique a ortografia ou veja-o na lista.")
def remover():
    prg_itemAdicionar = item_entry.get()
    prg_qtd = int(quantity_entry.get())
    if prg_itemAdicionar == "":
        messagebox.showinfo("Erro", "Adicione um produto na tabela para continuarmos!")
    else:
        sql_a = f"SELECT * FROM wms.estoque where id = '{prg_itemAdicionar}'"
        c = conn.cursor()
        c.execute(sql_a)
        r = c.fetchall()
        if r:
            confirmation = messagebox.askquestion("Confirmação", f"Você quer remover à '{r[0][1]}' {prg_qtd} unidades?")

            if confirmation == "yes":

                estq = int(r[0][3])

                if prg_qtd > 0:

                    valor_adicionar = prg_qtd - estq
                    adi = f"update wms.estoque set quantidade = {valor_adicionar} where id = '{prg_itemAdicionar}'"
                    c = conn.cursor()
                    c.execute(adi)
                    conn.commit()
                    messagebox.showinfo("Sucesso", f"Estoque de {r[0][1]} atualizado para: {valor_adicionar} UNIDADES")
                else:
                    messagebox.showinfo("Cancelado", "Não é possível remover números menores que zero.")
            else:
                messagebox.showinfo("Cancelado", "Pedido cancelado!")
        else:
            messagebox.showinfo("Erro", "Este produto não existe. Verifique-o na lista!")



def apagar():
    prg_itemapagar = item_entry.get()
    if prg_itemapagar == "":
        messagebox.showinfo("Erro", "Adicione o ID do produto na tabela para continuarmos!")
    else:
        sql_a = f"SELECT * FROM wms.estoque where id = '{prg_itemapagar}'"
        c = conn.cursor()
        c.execute(sql_a)
        r = c.fetchall()
        if r:
            confirmation = messagebox.askquestion("Confirmação", f"Você quer remover o produto '{r[0][1]}' permanentemente?")

            if confirmation == "yes":

                remover = f"delete from wms.estoque where id = '{prg_itemapagar}'"
                c = conn.cursor()
                c.execute(remover)
                conn.commit()
                messagebox.showinfo("Sucesso", f"O produto: {r[0][1]} foi deletado!")
            else:
                messagebox.showinfo("Cancelado", "Pedido cancelado!")
        else:
            messagebox.showinfo("Erro", "Este produto não existe. Verifique-o na lista!")
            
janela = tk.Tk()
janela.title("Sistema de Gerenciamento de Estoque")
janela.geometry("300x300")
janela.configure(background="#FFFAFA")

item_label = tk.Label(janela, text="Nome do produto:\n(USE O ID DO PRODUTO PARA DADOS UNITARIOS)")
item_label.pack()

item_entry = tk.Entry(janela)
item_entry.pack()

quantity_label = tk.Label(janela, text="Quantidade:")
quantity_label.pack()

quantity_entry = tk.Entry(janela)
quantity_entry.pack()

rua_label = tk.Label(janela, text="Rua:")
rua_label.pack()

rua_entry = tk.Entry(janela)
rua_entry.pack()

menu_button = tk.Menubutton(janela, text="Opções", relief="raised")
menu_button.pack()

menu = tk.Menu(menu_button, tearoff=0)
menu_button.config(menu=menu)

menu.add_command(label="Listar Produtos", command=list_products)
menu.add_separator()
menu.add_command(label="Ver Dados de Produto", command=show_data)
menu.add_separator()
menu.add_command(label="Adicionar Produtos", command=Adicionar)
menu.add_separator()
menu.add_command(label="Remover produtos", command=remover)
menu.add_separator()
menu.add_command(label="Novo Produto", command=adicionar_produto)
menu.add_separator()
menu.add_command(label="Apagar produto", command=apagar)
menu.add_separator()
menu.add_command(label="Atualizar produto", command=atualizar)

janela.mainloop()

conn.close()
