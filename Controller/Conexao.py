import os

def Conexao(Ip,Usuario,Senha):

    conexao = ("sshpass -p '" + Senha + "' ssh -o StrictHostKeyChecking=no -X -C -q " + Usuario + "@" + Ip)
    host = os.system(conexao + " hostname")

    if host == 0:

        return conexao

    else:

        return 1
