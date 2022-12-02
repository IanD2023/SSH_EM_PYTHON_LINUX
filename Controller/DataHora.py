import os

def DataHora(conexao,versao):

        if versao == "bionic":

            ubuntu_18=(os.popen(conexao+" env XDG_CURRENT_DESKTOP=GNOME gnome-control-center datetime"))

        if versao == "xenial":

            ubuntu_16=(os.popen(conexao+" unity-control-center datetime"))