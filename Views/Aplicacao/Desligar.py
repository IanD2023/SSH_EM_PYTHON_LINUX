from tkinter import *
import imagens
import os
import time

def Desligar(root,window_principal,conexao,Ip,Usuario,Nome_computador,hostname):

        container = Frame(window_principal, width=310, height=210,bg='white',highlightthickness=0.5,bd=0)
        container.config(highlightbackground="lightgrey", highlightcolor="lightgrey")
        container.place(x=823,y=404)

        def sair(event):

            container.destroy()
    

        def desligar(event):

            #os.popen(conexao+" poweroff")
            os.system(conexao+" hostname")

            container.destroy()
            

        def reiniciar(event):

            host=os.popen(conexao+" reboot")
            
            container.destroy()
            Nome_computador['bg']="red"
            Nome_computador['text']="Reiniciando"  
            window_principal.update() 
            time.sleep(10)

            OnOff(Ip)  

        def OnOff(Ip):

            onoroff=os.system("ping -c 2 "+ Ip)

            while onoroff != 0:

                onoroff=os.system("ping -c 2 "+ Ip)

                if onoroff == 0:

                    Nome_computador['bg']="green"
                    Nome_computador['text']=(Usuario +" em "+ hostname)
        
        labelDesligar = Label(container, text="Desligar", bg='white',foreground='black')
        labelDesligar.grid(row=1, column=1, padx=15, pady=4)

        botaoDesligar = Button(container,image=imagens.img_desliga,
        relief=GROOVE, bd=0,bg='white',highlightthickness=0.5)
        botaoDesligar.config(highlightbackground = "white")
        botaoDesligar.grid(row=2, column=1, padx=15, pady=4)

        labelReiniciar = Label(container, text="Reiniciar", bg='white',foreground='black')
        labelReiniciar.grid(row=1, column=2, padx=15, pady=4)

        botaoReiniciar = Button(container, image=imagens.img_reinicia,
        relief=GROOVE, bd=0, bg='white',highlightthickness=0.5)
        botaoReiniciar.config(highlightbackground = "white")
        botaoReiniciar.grid(row=2, column=2, padx=15, pady=4 )

        botaoDesligar.bind("<Button-1>", desligar)
        botaoReiniciar.bind("<Button-1>", reiniciar)   
 
        root.bind("<Button-1>", sair)
