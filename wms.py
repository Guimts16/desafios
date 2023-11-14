from tkinter import *

class MinhaGUI:
    def __init__(self):
    # Criando a janela principal
        self.janela_principal = Tk()
        
        # Criando os frames
        self.frame_cima = Frame(self.janela_principal, bg="white", height=70, width=400)
        self.frame_baixo = Frame(self.janela_principal, bg='red', height=70, width=400)
        
        # Posicionando o frame
        self.frame_cima.pack()
        self.frame_baixo.pack()

  # Fazer o Tkinter exibir o looping da janela
    mainloop()

minha_gui = MinhaGUI()