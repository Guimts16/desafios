import tkinter as tk
import pyautogui as py
from time import sleep

def msg():

    mnsg1 = mnsg1_entry.get()
    mnsg2 = mnsg2_entry.get()
    tmp = int(tmp_entry.get())
    qtd = int(qtd_entry.get())
    timer = float(time_entry.get())

    if tmp > 0:
        sleep(tmp)
    else:
        sleep(3)

    for i in range(qtd):
        if mnsg1:
            py.write(f"{mnsg1}")
            py.press("enter")
        if timer > 0:
            sleep(timer)
        if mnsg2:
            py.write(f"{mnsg2}")
            py.press("enter")


janela = tk.Tk()
janela.title("Auto mensagem")
janela.geometry("300x300")
janela.configure(background="#FFFAFA")

mnsg1_label = tk.Label(janela, text="Mensagem 1:")
mnsg1_label.pack()

mnsg1_entry = tk.Entry(janela)
mnsg1_entry.pack()
mnsg1_entry.insert(0, "<By MTS>")

mnsg2_label = tk.Label(janela, text="Mensagem 2:")
mnsg2_label.pack()

mnsg2_entry = tk.Entry(janela)
mnsg2_entry.pack()

tmp_label = tk.Label(janela, text="Tempo de espera de execução:\nPadrão: 3")
tmp_label.pack()

tmp_entry = tk.Entry(janela)
tmp_entry.pack()
tmp_entry.insert(0, "3")

qtd_label = tk.Label(janela, text="Quantidade:")
qtd_label.pack()

qtd_entry = tk.Entry(janela)
qtd_entry.pack()
qtd_entry.insert(0, "1")

time_label = tk.Label(janela, text="Tempo espera:\nPadrão: 0")
time_label.pack()

time_entry = tk.Entry(janela)
time_entry.pack()
time_entry.insert(0, "0")

menu_button = tk.Menubutton(janela, text="Opções", relief="raised")
menu_button.pack()

menu = tk.Menu(menu_button, tearoff=0)
menu_button.config(menu=menu)

menu.add_command(label="Auto mensagem", command=msg)
menu.add_separator()

janela.mainloop()
