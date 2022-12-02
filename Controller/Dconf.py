import os

def Dconf(conexao):

        os.popen(conexao+" dconf-editor")