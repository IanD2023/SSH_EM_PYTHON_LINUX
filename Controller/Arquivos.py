import os

def Nautilus(conexao):

        os.popen(conexao+" nautilus")


def Nautilus_Share(Ip):

        os.popen("nautilus ssh://"+Ip+"/home")