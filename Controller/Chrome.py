import os

def Chrome():

        global link
        link= "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
        vars.apaga_out
        os.popen(vars.conexao+" rm -r google*")

        link_on=os.system("wget -q -c -S --spider "+link)

        if int(link_on) == 0:

            comandos=['wget --tries=2 '+link,'dpkg -i google*',' rm -r google*']

            Progresso(comandos)

        else:

         mensagem="Erro de conexão\nVerifique o link"
         cor="red"
         x=420
         y=170
         Mensagem(mensagem,x,y,cor)