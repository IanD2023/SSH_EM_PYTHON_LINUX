import scp
import Views.Aplicacao.Progresso as Progresso

def PDF(usuario,senha,ip):

        arquivo="config/pacotes/apt.conf"
        pasta=":/etc/apt/"
        scp.scp(usuario,senha,ip,arquivo,pasta)

        comandos=['apt update','apt install cups-pdf -y']

        Progresso.Progresso(comandos)

        # pdf = os.system(vars.conexao+" apt install cups-pdf -y")
        #
        # if int(pdf) == 0:
        #
        #     mensagem = "Instalação Completa"
        #     cor="black"
        #     x=402
        #     y=170
        #     Mensagem(mensagem,x,y,cor)
        #
        # else:
        #
        #     x=170
        #     y=170
        #     cor="black"
        #     mensagem=(os.popen(vars.conexao+" apt install cups-pdf")).read().rstrip()
        #     Mensagem(mensagem,x,y,cor)