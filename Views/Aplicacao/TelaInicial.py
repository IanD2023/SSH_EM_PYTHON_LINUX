from tkinter import *
import os

def Aplicacoes(Usuario,Senha,Ip,conexao,hostname,versao):

    AplicacoesWindow = Toplevel()
    AplicacoesWindow.title("")
    AplicacoesWindow.geometry('1010x510')
    AplicacoesWindow.resizable(width=0, height=0)

    window_principal = LabelFrame(AplicacoesWindow,bg='white')
    window_principal.pack(fill="both", expand="yes")

    import Funcoes
    import imagens
    import Desligar
    import Usuarios
    import VncConfig

    UsuariosLogados=Funcoes.UsuariosLogados.Usuarios(conexao)
    window = Frame(window_principal,bg='white')
    window.pack(pady=10)


    cor="white"
    cor_barra = "lightgrey"
    linha1=22
    linha2=23
    padx=50
    pady=10

    if Usuario == "root":
        linha1=20
        linha2=21
        padx=22
        pady=8

    Nome_computador = Label(window_principal, text=Usuario+" em "+str(hostname),bg='green', foreground='black', width=125, height=1)
    Nome_computador.place(x=0,y=0)

    label_espaco = Label(window, text="",bg=cor, foreground='black')
    label_espaco.grid(row=8, column=1, padx=0, pady=23 )

    label_impressoras = Label(window, text="Instalar impressoras",bg=cor,foreground='black')
    label_impressoras.grid(row=9, column=1, padx=padx, pady=pady )

    botao_impressoras = Button(window, image=imagens.img_impressoras,command=lambda: [Funcoes.Impressoras.Impressoras(conexao)],bd=0,bg=cor,highlightthickness=0.5)
    botao_impressoras.config(highlightbackground = "white", highlightcolor= "white")
    botao_impressoras.grid(row=10, column=1, padx=padx, pady=pady )

    label_config = Label(window, text="Configurações",bg=cor,foreground='black')
    label_config.grid(row=9, column=2,padx=padx, pady=pady )
    botao_config = Button(window, image=imagens.img_config,command=lambda: [Funcoes.Configuracoes.Configuracoes(conexao,versao)],bd=0,bg=cor,highlightthickness=0.5)
    botao_config.config(highlightbackground = cor, highlightcolor= cor)
    botao_config.grid(row=10, column=2, padx=padx, pady=pady )

    label_redes = Label(window, text="Redes",bg=cor,foreground='black')
    label_redes.grid(row=9, column=3, padx=padx, pady=pady )
    botao_redes = Button(window, image=imagens.img_redes,command=lambda: [Funcoes.Redes.Redes(conexao,versao)],bd=0,bg=cor,highlightthickness=0.5)
    botao_redes.config(highlightbackground = cor, highlightcolor= cor)
    botao_redes.grid(row=10, column=3,padx=padx, pady=pady )

    label_dataehora = Label(window, text="Data e Hora",bg=cor,foreground='black')
    label_dataehora.grid(row=9, column=4, padx=padx, pady=pady )
    botao_dataehora = Button(window, image=imagens.img_dataehora,command=lambda: [Funcoes.DataHora.DataHora(conexao,versao)],bd=0, bg=cor,highlightthickness=0.5)
    botao_dataehora.config(highlightbackground = cor, highlightcolor= cor)
    botao_dataehora.grid(row=10, column=4, padx=padx, pady=pady )

    label_arquivos = Label(window, text="Arquivos", bg=cor,foreground='black')
    label_arquivos.grid(row=9, column=5, padx=padx, pady=pady )
    botao_arquivos = Button(window, image=imagens.img_arquivos,command=lambda: [Funcoes.Arquivos.Nautilus(conexao)],bd=0, bg=cor,highlightthickness=0.5)
    botao_arquivos.config(highlightbackground = cor, highlightcolor= cor)
    botao_arquivos.grid(row=10, column=5, padx=padx, pady=pady )

    if Usuario == "root":

        label_pdf = Label(window, text="Instalar impressora PDF", bg=cor,foreground='black')
        label_pdf.grid(row=linha1, column=1, padx=padx, pady=pady )
        botao_pdf = Button(window, image=imagens.img_PDF,command=lambda: [Funcoes.PDF.PDF(Usuario,Senha,Ip)],bd=0, bg=cor,highlightthickness=0.5)
        botao_pdf.config(highlightbackground = cor, highlightcolor= cor)
        botao_pdf.grid(row=linha2, column=1, padx=padx, pady=pady )

        label_APTconfig = Label(window, text="APT update & upgrade",bg=cor,foreground='black')
        label_APTconfig.grid(row=20, column=2, padx=padx, pady=pady )
        dados=1
        botao_APTconfig = Button(window, image=imagens.img_APTconfig,command=lambda: [Funcoes.APT_opcoes.APT_opcoes(conexao)],bd=0, bg=cor,highlightthickness=0.5)
        botao_APTconfig.config(highlightbackground = cor, highlightcolor= cor)
        botao_APTconfig.grid(row=21, column=2, padx=padx, pady=pady )

        label_wps = Label(window, text="Instalar ou atualizar WPS", bg=cor,foreground='black')
        label_wps.grid(row=20, column=3, padx=padx, pady=pady )
        botao_wps = Button(window, image=imagens.img_WPS,command=lambda: [Funcoes.WPS.WPS(conexao)],bd=0, bg=cor,highlightthickness=0.5)
        botao_wps.config(highlightbackground =cor, highlightcolor= cor)
        botao_wps.grid(row=21, column=3, padx=padx, pady=pady )

        label_chrome = Label(window, text="Instalar ou atualizar Chrome", bg=cor,foreground='black')
        label_chrome.grid(row=20, column=4, padx=padx, pady=pady )
        botao_chrome = Button(window, image=imagens.img_Chrome,command=lambda: [Funcoes.Chrome.Chrome(conexao)],bd=0, bg=cor,highlightthickness=0.5)
        botao_chrome.config(highlightbackground =cor, highlightcolor= cor)
        botao_chrome.grid(row=21, column=4, padx=padx, pady=pady )

    label_arquivos_share = Label(window, text="Compartilhamento\nde\nArquivos", bg=cor,foreground='black')
    label_arquivos_share.grid(row=linha1, column=5, padx=padx, pady=pady )
    botao_arquivos_share = Button(window, image=imagens.img_arquivos_share,command=lambda: [Funcoes.Arquivos.Nautilus_Share(Ip)],bd=0, bg=cor,highlightthickness=0.5)
    botao_arquivos_share.config(highlightbackground = cor, highlightcolor= cor)
    botao_arquivos_share.grid(row=linha2, column=5, padx=padx, pady=pady )

    label_marketplace = Label(window, text="Loja", bg=cor,foreground='black')
    label_marketplace.grid(row=22, column=1, padx=padx, pady=pady)
    botao_marketplace = Button(window, image=imagens.img_Marketplace,command=lambda: [Funcoes.Loja.Loja(conexao)],bd=0, bg=cor,highlightthickness=0.5)
    botao_marketplace.config(highlightbackground = cor, highlightcolor= cor)
    botao_marketplace.grid(row=23, column=1, padx=padx, pady=pady)

    label_gerenciador = Label(window, text="Gerenciador", bg=cor,foreground='black')
    label_gerenciador.grid(row=22, column=2, padx=padx, pady=pady )
    botao_gerenciador = Button(window, image=imagens.img_Gerenciador,command=lambda: [Funcoes.Gerenciador.Gerenciador(conexao)],bd=0, bg=cor,highlightthickness=0.5)
    botao_gerenciador.config(highlightbackground = cor, highlightcolor= cor)
    botao_gerenciador.grid(row=23, column=2, padx=padx, pady=pady)

    label_dconf = Label(window, text="Dconf", bg=cor,foreground='black')
    label_dconf.grid(row=22, column=3, padx=padx, pady=pady )
    botao_dconf = Button(window, image=imagens.img_Dconf,command=lambda: [Funcoes.Dconf.Dconf(conexao)],bd=0, bg=cor,highlightthickness=0.5)
    botao_dconf.config(highlightbackground = cor, highlightcolor=cor)
    botao_dconf.grid(row=23, column=3, padx=padx, pady=pady )

    label_terminal = Label(window, text="Terminal", bg=cor,foreground='black')
    label_terminal.grid(row=22, column=4, padx=padx, pady=pady )
    botao_terminal = Button(window, image=imagens.img_Terminal,command=lambda: [Funcoes.Terminal.Terminal(conexao,versao)],bd=0, bg=cor,highlightthickness=0.5)
    botao_terminal.config(highlightbackground = cor, highlightcolor= cor)
    botao_terminal.grid(row=23, column=4, padx=padx, pady=pady )

    Barrainferiror = Label(window_principal, foreground='black', width=125, height=2)
    Barrainferiror.place(x=0,y=478)

    botao_desligar = Button(window_principal, image=imagens.img_Desligar,command=lambda: [Desligar.Desligar(AplicacoesWindow,window_principal,conexao,Ip,Usuario,Nome_computador,hostname)],bd=0,bg=cor_barra,highlightthickness=0.5)
    botao_desligar.config(activebackground = cor_barra,highlightbackground = cor_barra, highlightcolor= cor_barra)
    botao_desligar.place(x=970,y=478)

    troca_usuario = Button(window_principal, image=imagens.usuario_img,command=lambda: [Usuarios.Usuarios(AplicacoesWindow,window,UsuariosLogados,Ip,hostname,versao,window_principal)],bd=0,bg=cor_barra,highlightthickness=0.5)
    troca_usuario.config(activebackground = cor_barra,highlightbackground = cor_barra, highlightcolor= cor_barra)
    troca_usuario.place(x=937,y=478)

    def vnc(event):

        VncConfig.VncConfig(botao_vnc, Usuario, UsuariosLogados, Ip,event,window,versao)

    botao_vnc = Button(window_principal, image=imagens.img_Vnc,command=lambda: [Funcoes.Vnc.Vnc(Ip)],bd=0,bg=cor_barra,highlightthickness=0.5)
    botao_vnc.config(activebackground = cor_barra,highlightbackground = cor_barra, highlightcolor= cor_barra)
    botao_vnc.place(x=910,y=482)
    botao_vnc.bind("<Button-3>", vnc)


    ##Botoes()
