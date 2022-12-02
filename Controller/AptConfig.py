import os

def APT_opcoes():

        #time.sleep(5)
        arquivo="config/pacotes/apt.conf"
        pasta=":/etc/apt/"
        vars.scp(arquivo,pasta)
        apt="'apt update && apt upgrade -y && apt -f install -y && apt autoremove -y'"
        xterm=(' "xterm -bg white -fg black -e '+apt+'"')

        os.popen(vars.conexao+xterm)