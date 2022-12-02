from tkinter import *
import Funcoes
import Senha

def Configurar_vnc(seleciona_usuario,Usuario,window,versao,Ip):

    if seleciona_usuario != Usuario:

        saida=1

        titulo=("Digite a senha para\n"+seleciona_usuario)

        Senha.Senha(titulo, saida, seleciona_usuario, window, Ip,versao)


def VncConfig(botao_vnc,Usuario,UsuariosLogados,Ip,event,window,versao):

    m = Menu(botao_vnc, tearoff=0)
    sub_menu = Menu(m, tearoff=0)

    def add(seleciona_usuario):

        sub_menu.add_command(
        label=seleciona_usuario,
        command=lambda: [Configurar_vnc(seleciona_usuario,Usuario,window,versao,Ip)]
        )

    for s in range(0, len(UsuariosLogados)):

        seleciona_usuario = UsuariosLogados[s]

        if seleciona_usuario != "root":

            add(seleciona_usuario)

    # add the File menu to the menubar
    if Usuario != "root":

        seleciona_usuario = Usuario
        m.add_command(
        label="Configurar",
        command=lambda: [Configurar_vnc(seleciona_usuario,Usuario,window,versao,Ip)]
        )


    else:

        m.add_cascade(label="Configurar", menu=sub_menu)

    m.add_command(label="Conectar", command=lambda: [Funcoes.Vnc.Vnc(Ip)])
    m.add_separator()
    m.add_command(label="Sair", command=lambda: print(""))

    try:

        m.tk_popup(event.x_root, event.y_root)

    finally:

        print("")