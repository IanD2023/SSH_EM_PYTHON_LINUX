from tkinter import *


def Modal(root,window_principal,funcao):

        container = LabelFrame(window_principal, width=310, height=210,bg='white')
        container.place(x=350,y=150)

        def sair(event):

            container.destroy()
            

        root.bind("<Button-1>", sair)