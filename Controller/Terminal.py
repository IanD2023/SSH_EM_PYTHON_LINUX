import os

def Terminal(conexao,versao):

        if versao == "bionic":

            ubuntu_18=(os.popen(conexao+" xterm"))

        if versao == "xenial":

            ubuntu_16=(os.popen(conexao+" xterm"))
            #gnome-terminal"))