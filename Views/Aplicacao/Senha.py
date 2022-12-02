from tkinter import *
import Funcoes

def Senha(titulo,saida,seleciona_usuario,window,Ip,versao):

    Conexao=""

    container = Frame(window, bg='white', highlightthickness=0.5)
    container.config(highlightbackground="lightgrey", highlightcolor="lightgrey")
    container.place(x=415, y=120)

    containerTitulo = LabelFrame(container, width=200, height=37, bg='lightgrey', highlightthickness=0.5, bd=0)
    containerTitulo.config(highlightbackground="lightgrey", highlightcolor="lightgrey")
    containerTitulo.pack(fill="x", expand="yes")

    containerInput = Frame(container, width=200, height=170, bg='white', highlightthickness=0.1, bd=0)
    containerInput.config(highlightbackground="lightgrey", highlightcolor="lightgrey")
    containerInput.pack(fill="x", expand="yes", pady=15)

    Titulo = Label(containerTitulo, text="Senha", font=("arial 12"), bg="lightgrey")
    Titulo.pack(padx=5, pady=5)

    labelSenha = Label(containerInput, text=("Digite a senha para\n" + seleciona_usuario), font=("arial 10"), bg="white")
    labelSenha.pack()

    SenhaUsuario = Entry(containerInput, highlightthickness=0.5, width=18, bd=0, show="*", justify='center')
    SenhaUsuario.config(highlightbackground="lightgrey", highlightcolor="lightgrey", )
    SenhaUsuario.pack(ipady=3, pady=15, side=BOTTOM)

    containerRodape = LabelFrame(container, bg='lightgrey', highlightthickness=0.5, bd=0)
    containerRodape.config(highlightbackground="lightgrey", highlightcolor="lightgrey")
    containerRodape.pack(fill="x", expand="yes")

    botaoCancelar = Button(
        containerRodape, text="Cancelar", font=("arial 10"), bg="red", fg="white", width=5, highlightthickness=0.1, bd=0,
    command=lambda: [Sair()])
    botaoCancelar.config(
        highlightbackground="red", highlightcolor="red",
        activebackground="darkred", activeforeground="white"
    )
    botaoCancelar.pack(padx=15, pady=10, side=LEFT)

    botaoConfirma = Button(
        containerRodape, text="Ok", font=("arial 10"), bg="blue", fg="white", width=5, highlightthickness=0.1, bd=0,
        command=lambda: [Conexao()])
    botaoConfirma.config(
        highlightbackground="blue", highlightcolor="lightgrey",
        activebackground="darkblue", activeforeground="white"
    )
    botaoConfirma.pack(padx=15, pady=5, side=LEFT)

    def Conexao():

        senha=SenhaUsuario.get()

        NovaConexao=Funcoes.Conexao.Conexao(Ip,seleciona_usuario,senha)

        if NovaConexao != 1:

           print("Nova Senha")
           if saida == 1:

               Funcoes.Vnc.Configurar_vnc(versao, NovaConexao)

        else:

           container.destroy()
           return Senha(titulo,saida,seleciona_usuario,window,Ip)

    def Sair():

        container.destroy()

    return Conexao
