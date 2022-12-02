import os

def WPS():

            global link
            link="https://wdl1.pcfg.cache.wpscdn.com/wpsdl/wpsoffice/download/linux/11664/wps-office_11.1.0.11664.XA_amd64.deb"
            vars.apaga_out
            os.popen(vars.conexao+" rm -r wps*")

            link_on=os.system("wget -q -c -S --spider "+link)

            if int(link_on) == 0:
                arquivo="config/pacotes/wps.deb"
                pasta=":/root/"
                vars.scp(arquivo,pasta)
                comandos=['wget --tries=2 '+link,'dpkg -i wps*',' rm -r wps*']

                Progresso(comandos)
            else:
             os.system(vars.conexao+" rm -r wps*")
             mensagem="Erro de conexão\nVerifique o link"
             cor="red"
             x=420
             y=170
             Mensagem(mensagem,x,y,cor)