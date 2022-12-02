
from tkinter import *
from tkinter import ttk
import os
import imagens
import Funcoes


def Usuarios(root,window,UsuariosLogados,Ip,hostname,versao,window_principal):

    root['bg'] = 'lightgrey'
    container = Frame(window, bg='white', highlightthickness=0.5)
    container.config(highlightbackground="lightgrey", highlightcolor="lightgrey")
    container.place(x=415, y=120)

    containerTitulo = LabelFrame(container, width=200, height=37, bg='lightgrey', highlightthickness=0.5, bd=0)
    containerTitulo.config(highlightbackground="lightgrey", highlightcolor="lightgrey")
    containerTitulo.pack(fill="x", expand="yes")

    containerInput = Frame(container, width=200, height=170, bg='white', highlightthickness=0.1, bd=0)
    containerInput.config(highlightbackground="lightgrey", highlightcolor="lightgrey")
    containerInput.pack(fill="x", expand="yes", pady=15)

    Titulo = Label(containerTitulo, text="Trocar Usuário", font=("arial 12"), bg="lightgrey")
    Titulo.pack(padx=5, pady=5)

    ttk.Style().configure('white.TButton', foreground='black', background="white", font=("arial", 10), border=0,
                          highlightthickness=0.2,
                          activebackground="lightgrey", activeforeground="lightgrey", relief=RIDGE,
                          highlightbackground="lightgrey", highlightcolor="lightgrey")

    selecionar_usuario = StringVar()

    labelUsuario = Label(containerInput, image=imagens.login, font=("arial 10"), bg="white")
    labelUsuario.pack()

    usuarios = ttk.Combobox(containerInput, textvariable=str(selecionar_usuario), style='white.TButton', width=17,
                            height=5, justify='center')
    usuarios['values'] = [UsuariosLogados[x] for x in range(0, len(UsuariosLogados))]
    usuarios.focus_set()
    usuarios.pack(pady=15)

    labelSenha = Label(containerInput, image=imagens.senha, font=("arial 10"), bg="white")
    labelSenha.pack()

    SenhaUsuario = Entry(containerInput, highlightthickness=0.5, width=18, bd=0, show="*", justify='center')
    SenhaUsuario.config(highlightbackground="lightgrey", highlightcolor="lightgrey", )
    SenhaUsuario.pack(ipady=3, pady=15, side=BOTTOM)


    containerRodape = LabelFrame(container, bg='lightgrey', highlightthickness=0.5, bd=0)
    containerRodape.config(highlightbackground="lightgrey", highlightcolor="lightgrey")
    containerRodape.pack(fill="x", expand="yes")

    botaoCancelar = Button(
    containerRodape, text="Cancelar", font=("arial 10"), bg="red", fg="white", width=5,highlightthickness=0.1, bd=0
    )
    botaoCancelar.config(
        highlightbackground="red", highlightcolor="red",
        activebackground="darkred", activeforeground="white"
    )
    botaoCancelar.pack(padx=15, pady=10, side=LEFT)

    botaoConfirma = Button(
    containerRodape, text="Ok", font=("arial 10"), bg="blue", fg="white", width=5,highlightthickness=0.1, bd=0,
    command=lambda: [trocou_usuario()])
    botaoConfirma.config(
        highlightbackground="blue", highlightcolor="lightgrey",
        activebackground="darkblue", activeforeground="white"
    )
    botaoConfirma.pack(padx=15, pady=5, side=LEFT)

    def trocou_usuario():

        usuario = selecionar_usuario.get()
        senha = SenhaUsuario.get()
        conexao = ("sshpass -p '" + str(senha) + "' ssh -o StrictHostKeyChecking=no -X -C -q " + str(
            usuario) + "@" + Ip)

        host = os.system(conexao + " exit")

        if host == 0:

            Usuario = usuario
            Senha = senha

            root.destroy()

            Funcoes.TrocarUsuario.TrocarUsuario(Usuario, Senha, Ip, conexao, hostname, versao)


        else:

            while host != 0:
                container.destroy()

                host = os.system(conexao + " exit")

                return Usuarios(root,window,UsuariosLogados,Ip,hostname,versao)

    def sair(event):

        container.destroy()

    botaoCancelar.bind("<Button-1>", sair)
    window.bind("<Button-1>", sair)
