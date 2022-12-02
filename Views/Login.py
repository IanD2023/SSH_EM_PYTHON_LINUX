from tkinter import *
import LoginController

def Login():

    root = Tk()
    root.geometry('220x330')
    root.title("")
    root.configure(bg='white')
    root.resizable(width=0, height=0)

    global ip, usuario, senha, mensagem
    import imagens

    fontePadrao = ("Arial", "10")



    primeiroContainer = Frame(root, bg="white",highlightthickness=0.5)
    primeiroContainer.config(highlightbackground = "lightgrey", highlightcolor= "lightgrey")
    primeiroContainer.pack(fill="x",expand="yes")

    containerLogin = Frame(root, bg="white")
    containerLogin.pack(fill="x", expand="yes",pady=5)

    segundoContainer = Frame(containerLogin, bg="white")
    segundoContainer.pack(pady=5,padx=10)

    terceiroContainer = Frame(containerLogin, bg="white")
    terceiroContainer.pack(pady=5,padx=10)

    quartoContainer = Frame(containerLogin, bg="white")
    quartoContainer.pack(pady=5,padx=10)

    quintoContainer = Frame(containerLogin, bg="white")
    quintoContainer.pack(pady=5, padx=10)

    sextoContainer = Frame(containerLogin, bg="white")
    sextoContainer.pack(pady=5, padx=10)

    setimoContainer = Frame(containerLogin, bg="white")
    setimoContainer.pack(pady=5, padx=10)

    oitavoContainer = Frame(root, bg="white")
    oitavoContainer.pack(fill="both", expand="yes")

    nonoContainer = Frame(root, bg="white",highlightthickness=0.5)
    nonoContainer.config(highlightbackground = "lightgrey", highlightcolor= "lightgrey")
    nonoContainer.pack(fill="both",expand="yes")

    Titulo = Label(primeiroContainer, text="Login", font="arial,12", bg='white')
    Titulo.pack(side=TOP,pady=5)

    ipImagem = Label(segundoContainer , image=imagens.host, font=fontePadrao, bg='white')
    ipImagem.pack(side=LEFT)
    ipLabel = Label(segundoContainer, text="Host   ", font=fontePadrao, bg='white')
    ipLabel.pack(side=LEFT)

    ip = Entry(terceiroContainer, text="login", bd="0", bg='white',highlightthickness=0.5,width=20)
    ip.config(highlightbackground = "lightgrey", highlightcolor= "lightgrey",justify="center")
    ip.focus_set()
    ip.pack(fill="both",expand="yes",padx=10,ipady=5)

    #terceiro Container
    usuarioImagem = Label(quartoContainer, image=imagens.login, font=fontePadrao, bg='white')
    usuarioImagem.pack(side=LEFT)
    usuarioLabel = Label(quartoContainer,text="Usuario", font=fontePadrao,bg='white')
    usuarioLabel.pack(side=LEFT)

    usuario = Entry(quintoContainer, text="", bd="0", bg='white',highlightthickness=0.5,width=20)
    usuario.config(highlightbackground = "lightgrey", highlightcolor= "lightgrey",justify="center")
    usuario.pack(fill="both",expand="yes",padx=10,ipady=5)

    #quarto Container
    senhaImagem = Label(sextoContainer, image=imagens.senha, font=fontePadrao, bg='white')
    senhaImagem.pack(side=LEFT)
    senhaLabel = Label(sextoContainer, text="Senha  ", font=fontePadrao,bg='white')
    senhaLabel.pack(side=LEFT)

    senha = Entry(setimoContainer, bd="0", bg='white',highlightthickness=0.5,width=20,show="*")
    senha.config(highlightbackground = "lightgrey", highlightcolor= "lightgrey",justify="center")
    senha.pack(fill="both",expand="yes",padx=10,ipady=5)

    #quinto Container

    autenticar = Button(nonoContainer,bg='green',fg='white', highlightthickness=0.5,width=23, font=("Arial", "8"),bd=0,text="Conectar")
    autenticar.config(
        highlightbackground="green", highlightcolor="blue",
        activebackground="darkgreen", activeforeground="white"
    )
    autenticar.pack(ipady=5,pady=10)

    mensagem = Label(oitavoContainer, width=23,font=fontePadrao,bg='white',fg='red')
    mensagem.pack()

    def login(event):

        Ip = ip.get()
        Usuario = usuario.get()
        Senha = senha.get()

        if Ip != "" and Usuario != "" and Senha != "":

           LoginController.login(root,Ip,Usuario,Senha,mensagem)

    ip.bind('<Return>', login)
    usuario.bind('<Return>', login)
    senha.bind('<Return>', login)
    autenticar.bind('<Return>', login)
    autenticar.bind('<Button-1>', login)

    root.mainloop()

