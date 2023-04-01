from tkinter import *
class minhaGUI :
    def __init__ (self):
        self.janela_principal=Tk()
       
        self.frame_cima = Frame(self.janela_principal)
        self.frame_baixo = Frame(self.janela_principal)
       
        self.labe1 =Label(self.frame_cima,text='To no de cima')
        self.label2 =Label(self.frame_baixo,text = 'Tono de baixo')
       
        self.labe1.pack(side = 'top')
        self.label2.pack(side='top')

        self.frame_cima.pack() 
        self.frame_baixo.pack()
        mainloop()

minha_gui = minhaGUI()