import os

def Usuarios(conexao):

    usuario=os.popen(conexao+" users").read().rstrip()

    usuarios=[]

    user=""

    for x in range(0, len(usuario)):

        if usuario[x] != " ":

            user+=usuario[x]

        if usuario[x] == " " or x == len(usuario)-1:

            usuarios.append(user)

            user=""

    return usuarios  