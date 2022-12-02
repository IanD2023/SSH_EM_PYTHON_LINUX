import os
import time

def Vnc(Ip):

        os.popen("remmina -c vnc://root@"+Ip)

def Configurar_vnc(versao,conexao):


        if versao == "bionic":

            os.popen(conexao+" env XDG_CURRENT_DESKTOP=GNOME gnome-control-center sharing")

        if versao == "xenial":

            os.popen(conexao + " killall vino-server -9").read()
            print('processo encerrado')
            time.sleep(2)
            os.system(conexao+" 'vino-preferences'")
            time.sleep(2)
            print('Configuracoes feitas')
            os.system(conexao+" 'DISPLAY=:0 /usr/lib/vino/vino-server &>> arquivo.log &'")

def Vnc_user_config(seleciona_usuario,conexao):

    if str(vars.versao) == "bionic":

        ubuntu_18=(os.popen(conexao+" env XDG_CURRENT_DESKTOP=GNOME gnome-control-center sharing"))

    else:

        #os.system(conexao+" killall vino-server")
        os.system(conexao+" vino-preferences")
        os.system(conexao+" killall vino-server -9")
        os.system(conexao+" 'DISPLAY=:0 /usr/lib/vino/vino-server &>> arquivo.log &'")