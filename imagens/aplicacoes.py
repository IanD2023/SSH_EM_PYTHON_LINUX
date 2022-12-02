from tkinter import *
import sys
import os
from tkinter import messagebox
import time
import aviso
#import pergunta

global saida
Mensagem_instalacao = "Instalação Completa"

def Aplicacoes():
    usuario=(os.popen("cat config/saidas/dados | cut -d',' -f1")).read().rstrip('\n')
    senha=(os.popen("cat config/saidas/dados | cut -d',' -f2")).read().rstrip('\n')
    ip=(os.popen("cat config/saidas/dados | cut -d',' -f3")).read().rstrip('\n')
    conexao=("sshpass -p '"+ senha +"' ssh -o StrictHostKeyChecking=no -X -C -q " + usuario + "@" + ip)
    hostname=(os.popen(conexao+" hostname")).read().rstrip('\n')
    versao=(os.popen(conexao+" sed -n '/^DISTRIB_RELEASE/p' /etc/*-release | cut -d'=' -f2")).read().rstrip('\n')
    out=(" > /dev/null; then out=1; else out=0; fi; echo $out")
    output=(os.popen("cat config/saidas/out")).read().rstrip('\n')
    saida = "echo 1 > config/saidas/out"
    print(sys.path)

    window = Tk()

    window.title("SSH grafico")

    window.geometry('1000x500')
    window.resizable(width=0, height=0)

    ##funcoes##

    def Impressoras():

        os.popen(conexao+" system-config-printer && exit")

    def Configuracoes():

        if float(versao) > 18:

         ubuntu_18=(os.popen(conexao+" gnome-control-center && exit"))

        else:

         ubuntu_16=(os.popen(conexao+" unity-control-center && exit"))

    def DataHora():

        os.popen(conexao+" date -s "+data)
        os.popen(conexao+" date -s "+hora)

    def Nautilus():

        os.popen("nautilus ssh://"+ip+"/home")

    def PDF():

        pdf = os.system(conexao+" apt install cups-pdf -y")

        if int(pdf) == 0:

           aviso.Aviso()

        else:

           error=(os.popen(conexao+" apt install cups-pdf >> config/saidas/out")).read()

           aviso.Mensagem()


    def APT_opcoes():
        #apt update
        aviso.Ler_saidas()
        apt_update = os.system(conexao+" apt update -y")

        if int(apt_update) == 0:
            print("Processo Finalizado")
        else:
            print("Processo com erro")
        #apt upgrade
        apt_upgrade = os.system(conexao+" apt upgrade -y")

        if int(apt_upgrade) == 0:
            print("Processo Finalizado")
        else:
            print("Processo com erro")
        #apt -f install
        apt_install = os.system(conexao+" apt -f install -y")

        if int(apt_install) == 0:
            print("Processo Finalizado")
        else:
            print("Processo com erro")
        #apt autoremove
        apt_autoremove = os.system(conexao+" apt autoremove -y")

        if int(apt_autoremove) == 0:
            print("Processo Finalizado")
        else:
            print("Processo com erro")

    def WPS():

            link="https://wdl1.pcfg.cache.wpscdn.com/wpsdl/wpsoffice/download/linux/11664/wps-office_11.1.0.11664.XA_amd64.deb"

            os.popen(conexao+" rm -r wps*")

            link_on=os.system("wget -q -c -S --spider "+link)

            if int(link_on) == 0:

               wps = os.system("curl -I "+link+" >> out")

               output=os.popen("sed -n '/^content-length/p' out | cut -d' ' -f2").read().rstrip()

               progresso = os.system("python3 config/progress.py &")

               download_wps = os.popen(conexao+" wget --tries=2 "+link+"; echo 1 > config/saidas/out")


               #if download_wps != 0:

                # return 0

                  #installandremove_wps=os.system(conexao+" dpkg -i wps*;"+conexao+" rm -r wps*")

               #else:

                  #return 0
            else:

                os.popen("rm -r config/saidas/out")

                error=(os.popen("echo 'Não foi possivel realizar o download' >> config/saidas/out")).read()

                os.popen("python3 config/alerta.py")

                #print(end - start)

    def Chrome():
        os.popen("rm -r config/saidas/out")
        os.popen("python3 config/pergunta.py")

        pergunta=(os.popen("cat config/saidas/out")).read().rstrip('\n')

        while pergunta == "":

          pergunta=(os.popen("cat config/saidas/out")).read().rstrip('\n')

          if pergunta == "1":

             download_chrome=(os.popen(conexao+" rm -r google*; "+conexao+" wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &")).read()
             installandremove_chrome=(os.popen(conexao+" dpkg -i google*; "+conexao+" rm -r wps*")).read()

          if pergunta == "0":

             print("FIM")

    def Dconf():

        os.popen(conexao+" dconf-editor")

    def Terminal():

        os.popen(conexao+" gnome-terminal")

    def Loja():

        os.popen(conexao+" gnome-software")

    def Gerenciador():

        os.popen(conexao+" gnome-system-monitor")

    def Desligar():

        aviso.Desligar()




    #imagem de fundo
    img_fundo = PhotoImage(file="imagens/ubuntu.png")
    imagem_fundo = Label (window, image=img_fundo)
    #imagem_fundo.place(x=1,y=1)

    #impressoras
    img_impressoras = PhotoImage(file="imagens/printer.png")
    impressoras = Label (window, image=img_impressoras)

    #Confuguracoes
    img_config = PhotoImage(file="imagens/configuracao.png")
    configuracao = Label (window, image=img_config)

    #Data e hora
    img_dataehora = PhotoImage(file="imagens/dataehora.png")
    dataehora = Label (window, image=img_dataehora)

    #Gerenciador de arquivos
    img_arquivos = PhotoImage(file="imagens/arquivos.png")
    arquivos = Label (window, image=img_arquivos)

    #Impressora PDF
    img_PDF = PhotoImage(file="imagens/cups-pdf.png")
    PDF_imagem = Label (window, image=img_PDF)

    #APT utilitarios
    img_APTconfig = PhotoImage(file="imagens/apt_opcoes.png")
    APTconfig = Label (window, image=img_APTconfig)

    #Instalar ou atualizar WPS
    img_WPS = PhotoImage(file="imagens/WPS.png")
    WPS_imagem = Label (window, image=img_WPS)

    #Instalar ou atualizar CHROME
    img_Chrome = PhotoImage(file="imagens/chrome.png")
    chrome = Label (window, image=img_Chrome)

    img_Dconf = PhotoImage(file="imagens/dconf.png")
    dconf = Label (window, image=img_Dconf)

    img_Terminal = PhotoImage(file="imagens/terminal.png")
    terminal = Label (window, image=img_Terminal)

    img_Marketplace = PhotoImage(file="imagens/marketplace.png")
    marketplace = Label (window, image=img_Marketplace)

    img_Gerenciador = PhotoImage(file="imagens/gerenciador.png")
    gerenciador = Label (window, image=img_Gerenciador)

    img_Desligar = PhotoImage(file="imagens/desligar.png")
    desligar = Label (window, image=img_Desligar)
    #Botoes


    label_impressoras = Label(window, text=usuario+" em "+hostname,bg='green', foreground='black', width=125, height=1)
    label_impressoras.place(x=0,y=0)

    botao_desligar = Button(window, image=img_Desligar,command=lambda: [Desligar()],bd=0,bg='white',highlightthickness=0.5)
    botao_desligar.config(activebackground = "#9c203c",highlightbackground = "#9c203c", highlightcolor= "#9c203c")
    botao_desligar.place(x=490,y=444)

    label_espaco = Label(window, text="",bg='#8d1545', foreground='black')
    label_espaco.grid(row=8, column=1, padx=0, pady=23 )

    label_impressoras = Label(window, text="Instalar impressoras",bg='#8d1545',foreground='white')
    label_impressoras.grid(row=9, column=1, padx=60, pady=15 )
    botao_impressoras = Button(window, image=img_impressoras,command=lambda: [Impressoras()],bd=0,bg='#8d1545',highlightthickness=0.5)
    botao_impressoras.config(highlightbackground = "#8d1545", highlightcolor= "#8d1545")
    botao_impressoras.grid(row=10, column=1, padx=60, pady=15 )

    label_config = Label(window, text="Configurações",bg='#9c203c',foreground='white')
    label_config.grid(row=9, column=2, padx=(30,0) )
    botao_config = Button(window, image=img_config,command=lambda: [Configuracoes()],bd=0,bg='#9c203c',highlightthickness=0.5)
    botao_config.config(highlightbackground = "#9c203c", highlightcolor= "#9c203c")
    botao_config.grid(row=10, column=2, padx=(30,0) )

    label_dataehora = Label(window, text="Data e Hora",bg='#a92731',foreground='white')
    label_dataehora.grid(row=9, column=3, padx=(30,0) )
    botao_dataehora = Button(window, image=img_dataehora,command=lambda: [DataHora()],bd=0, bg='#a92731',highlightthickness=0.5)
    botao_dataehora.config(highlightbackground = "#a92731", highlightcolor= "#a92731")
    botao_dataehora.grid(row=10, column=3, padx=(30,0) )

    label_arquivos = Label(window, text="Arquivos", bg='#d54519',foreground='white')
    label_arquivos.grid(row=9, column=4, padx=(30,0) )
    botao_arquivos = Button(window, image=img_arquivos,command=lambda: [Nautilus()],bd=0, bg='#d54519',highlightthickness=0.5)
    botao_arquivos.config(highlightbackground = "#d54519", highlightcolor= "#d54519")
    botao_arquivos.grid(row=10, column=4, padx=(30,0) )

    label_dconf = Label(window, text="Dconf", bg='#d54519',foreground='white')
    label_dconf.grid(row=9, column=5, padx=(30,0) )
    botao_dconf = Button(window, image=img_Dconf,command=lambda: [Dconf()],bd=0, bg='#d54519',highlightthickness=0.5)
    botao_dconf.config(highlightbackground = "#d54519", highlightcolor= "#d54519")
    botao_dconf.grid(row=10, column=5, padx=(30,0) )

    label_pdf = Label(window, text="Instalar impressora PDF", bg='#8d1545',foreground='white')
    label_pdf.grid(row=20, column=1, padx=5, pady=10 )
    botao_pdf = Button(window, image=img_PDF,command=lambda: [PDF()],bd=0, bg='#8d1545',highlightthickness=0.5)
    botao_pdf.config(highlightbackground = "#8d1545", highlightcolor= "#8d1545")
    botao_pdf.grid(row=21, column=1, padx=5, pady=10 )

    label_APTconfig = Label(window, text="APT update & upgrade",bg='#9c203c',foreground='white')
    label_APTconfig.grid(row=20, column=2, padx=(30,0) )
    botao_APTconfig = Button(window, image=img_APTconfig,command=lambda: [APT_opcoes()],bd=0, bg='#9c203c',highlightthickness=0.5)
    botao_APTconfig.config(highlightbackground = "#9c203c", highlightcolor= "#9c203c")
    botao_APTconfig.grid(row=21, column=2, padx=(30,0) )

    label_wps = Label(window, text="Instalar ou atualizar WPS", bg='#a92731',foreground='white')
    label_wps.grid(row=20, column=3, padx=(30,0) )
    botao_wps = Button(window, image=img_WPS,command=lambda: [WPS()],bd=0, bg='#a92731',highlightthickness=0.5)
    botao_wps.config(highlightbackground = "#a92731", highlightcolor= "#b93327")
    botao_wps.grid(row=21, column=3, padx=(30,0) )

    label_chrome = Label(window, text="Instalar ou atualizar Chrome", bg='#b93327',foreground='white')
    label_chrome.grid(row=20, column=4, padx=(30,0) )
    botao_chrome = Button(window, activebackground="#b93327", activeforeground="white",image=img_Chrome,command=lambda: [Chrome()],bd=0, bg='#b93327',highlightthickness=0.5)
    botao_chrome.config(highlightbackground = "#b93327", highlightcolor= "#b93327")
    botao_chrome.grid(row=21, column=4, padx=(30,0) )

    label_terminal = Label(window, text="Terminal", bg='#b93327',foreground='white')
    label_terminal.grid(row=20, column=5, padx=(30,0) )
    botao_terminal = Button(window, activebackground="#b93327", activeforeground="white",image=img_Terminal,command=lambda: [Terminal()],bd=0, bg='#b93327',highlightthickness=0.5)
    botao_terminal.config(highlightbackground = "#b93327", highlightcolor= "#b93327")
    botao_terminal.grid(row=21, column=5, padx=(30,0) )

    label_marketplace = Label(window, text="Loja", bg='#8d1545',foreground='white')
    label_marketplace.grid(row=22, column=1, padx=5, pady=10)
    botao_marketplace = Button(window, activebackground="#8d1545", activeforeground="white",image=img_Marketplace,command=lambda: [Loja()],bd=0, bg='#8d1545',highlightthickness=0.5)
    botao_marketplace.config(highlightbackground = "#8d1545", highlightcolor= "#8d1545")
    botao_marketplace.grid(row=23, column=1, padx=5, pady=10)

    label_gerenciador = Label(window, text="Gerenciador", bg='#9c203c',foreground='white')
    label_gerenciador.grid(row=22, column=2, padx=(30,0) )
    botao_gerenciador = Button(window, activebackground="#9c203c", activeforeground="white",image=img_Gerenciador,command=lambda: [Gerenciador()],bd=0, bg='#9c203c',highlightthickness=0.5)
    botao_gerenciador.config(highlightbackground = "#9c203c", highlightcolor= "#9c203c")
    botao_gerenciador.grid(row=23, column=2, padx=(30,0) )

    #Window.destroy()

    #window.transient(Window)
    #window.focus_force()
    #window.grab_set()

    #Window.destroy()



    window.mainloop()
