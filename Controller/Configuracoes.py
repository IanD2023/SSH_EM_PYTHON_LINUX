import os

def Configuracoes(conexao,versao):

        
        if versao == "bionic":

            ubuntu_18=(os.popen(conexao+" env XDG_CURRENT_DESKTOP=GNOME gnome-control-center"))

        if versao == "xenial":

            ubuntu_16=(os.popen(conexao+" unity-control-center"))