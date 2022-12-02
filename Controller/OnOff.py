import os
import time

def on_off():

        onoroff=os.system("ping -c 2 "+ vars.ip)

        while onoroff != 0:

            onoroff=os.system("ping -c 2 "+ vars.ip)

            if onoroff == 0:

               return 0

            #Nome_computador['bg']="green"
            #Nome_computador['text']=vars.hostname



def desligar(conexao):

    #os.popen(conexao+" poweroff")
    os.system(conexao+" hostname")
    #container.destroy()
    

def reiniciar(conexao,container):

    host=os.popen(conexao+" reboot")
    
    container.destroy()
    #Nome_computador['bg']="red"
    #Nome_computador['text']="Reiniciando"  
    #window_principal.update() 
    time.sleep(10)
    on_off()    