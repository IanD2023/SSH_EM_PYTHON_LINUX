import os

def Loja(conexao):

    os.popen(conexao+" gnome-software")

def Gerenciador(conexao):

    os.popen(conexao+" gnome-system-monitor")