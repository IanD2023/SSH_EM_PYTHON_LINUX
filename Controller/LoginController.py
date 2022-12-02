import sys
import os
import TelaInicial 

def login(root,Ip,Usuario,Senha,mensagem):

    host=os.system("ping -c 2 "+ Ip)
    conexao=("sshpass -p '"+ Senha +"' ssh -o StrictHostKeyChecking=no -X -C -q " + Usuario + "@" + Ip)
    versao=(os.popen(conexao+" cat /etc/*-release | grep DISTRIB_CODENAME | cut -d'=' -f2")).read().rstrip()

    if host == 0:

       ConexaoIp=os.system(conexao+" hostname")

       if ConexaoIp == 0:

            #root.destroy()
            mensagem["text"] = ""
            hostname = os.popen(conexao+" hostname").read().rstrip()
            

            TelaInicial.Aplicacoes(Usuario,Senha,Ip,conexao,hostname,versao)

       else:

            mensagem["text"] = "usuário ou senha incorretos"

    else:

          mensagem["text"] = "Host não encontrado"


           