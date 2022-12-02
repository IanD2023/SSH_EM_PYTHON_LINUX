import os

def Impressoras(conexao):

        os.popen(conexao+" system-config-printer && exit")