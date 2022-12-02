from tkinter import *
import sys
sys.path.insert(1, "/home/pcweb/ssh_python/config")
#imagem de fundo
img_fundo = PhotoImage(file="imagens/ubuntu.png")
#imagem_fundo = Label (window, image=img_fundo)

#imagem_fundo.place(x=1,y=1)

#impressoras
img_impressoras = PhotoImage(file="imagens/printer.png")
#impressoras = Label (window, image=img_impressoras)

#Confuguracoes
img_config = PhotoImage(file="imagens/configuracao.png")
#configuracao = Label (window, image=img_config)

#Redes
img_redes = PhotoImage(file="imagens/redes.png")
#redes = Label (window, image=img_redes)

#Data e hora
img_dataehora = PhotoImage(file="imagens/dataehora.png")
#dataehora = Label (window, image=img_dataehora)

#Gerenciador de arquivos
img_arquivos = PhotoImage(file="imagens/nautilus.png")
#arquivos = Label (window, image=img_arquivos)

#Compartilhamento de arquivos
img_arquivos_share = PhotoImage(file="imagens/arquivos.png")
#arquivos_share = Label (window, image=img_arquivos_share)

#Impressora PDF
img_PDF = PhotoImage(file="imagens/cups-pdf.png")
#PDF_imagem = Label (window, image=img_PDF)

#APT utilitarios
img_APTconfig = PhotoImage(file="imagens/apt_opcoes.png")
#APTconfig = Label (window, image=img_APTconfig)

#Instalar ou atualizar WPS
img_WPS = PhotoImage(file="imagens/WPS.png")
#WPS_imagem = Label (window, image=img_WPS)

#Instalar ou atualizar CHROME
img_Chrome = PhotoImage(file="imagens/chrome.png")
#chrome = Label (window, image=img_Chrome)

img_Dconf = PhotoImage(file="imagens/dconf.png")
#dconf = Label (window, image=img_Dconf)

img_Terminal = PhotoImage(file="imagens/terminal.png")
#terminal = Label (window, image=img_Terminal)

img_Marketplace = PhotoImage(file="imagens/marketplace.png")
#marketplace = Label (window, image=img_Marketplace)

img_Gerenciador = PhotoImage(file="imagens/gerenciador.png")
#gerenciador = Label (window, image=img_Gerenciador)

img_Desligar = PhotoImage(file="imagens/desligar.png")
#desligar = Label (window, image=img_Desligar)

img_Vnc = PhotoImage(file="imagens/vnc.png")
#vnc = Label (window, image=img_Vnc)

##IMAGEM DOS BOTOES
img_desliga = PhotoImage(file="imagens/desligar_color.png")
#imagem_desliga = Label (container, image=img_desliga)

img_reinicia = PhotoImage(file="imagens/reiniciar.png")
#imagem_reinicia = Label (container, image=img_reinicia)

processo_finalizado = PhotoImage(file="imagens/ok.png")

erro_img = PhotoImage(file="imagens/erro.png")

frameCnt = 43
frames_label = [PhotoImage(file='imagens/carregando_old.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

download_img=PhotoImage(file="imagens/download.png")

usuario_img=PhotoImage(file="imagens/usuario.png")

login=PhotoImage(file="imagens/login.png")

senha=PhotoImage(file="imagens/senha.png")

host=PhotoImage(file="imagens/host.png")
