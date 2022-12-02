def Mensagem(mensagem,x,y,cor):

        container = LabelFrame(window,bg='white')
        container.place(x=x,y=y)

        def Sair():

            container.destroy()

        text = Label(container, text=mensagem, font=("ariel 10 bold"),bg="white",fg=cor)
        text.pack(padx=30, pady=15,side=TOP)
        new = Button(container, text="ok", font=("ariel 10"), width=5,command=lambda: [Sair()],
        relief=GROOVE, bd=0, bg='white',fg="black",activebackground="white", activeforeground="black")
        new.pack(padx=30, pady=15)