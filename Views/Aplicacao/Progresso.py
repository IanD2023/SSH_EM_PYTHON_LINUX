import os
from tkinter import *

def Progresso(comandos):

        container = LabelFrame(window, width=200, height=100,bg='white')
        container.place(x=430,y=170)
        s = Style()
        s.configure("TProgressbar", foreground="green", background="green", thickness=10)

        def Sair(event):

            os.system("rm -r config/saidas/out")
            container.destroy()
        def Cancelar(event):
            os.system(vars.conexao+" killall apt -9")
            os.system(vars.conexao+" killall wget -9")
            os.system(vars.conexao+" killall dpkg -9")
            os.system("rm -r config/saidas/out")
            container.destroy()

        def start_training_images():
            #x=1
            #comandos=['apt update','apt install cups-pdf','apt update']
            x=0
            for i in range(0,len(comandos)):
                apt_update=os.popen("if "+vars.conexao+" "+comandos[i]+vars.out)
                out=os.system("cat config/saidas/out")

                while out != 0:
                 x +=1
                 progress['value'] += x
                 out=os.system("cat config/saidas/out")
                 btn_start.bind("<Button-1>", Cancelar)
                 if os.popen(" cat config/saidas/out").read().rstrip() == "0":
                      mensagem="Não foi possível fazer o download\nVerifique a conexão"
                      cor="red"
                      x=420
                      y=170
                      Mensagem(mensagem,x,y,cor)
                      os.system("rm -r config/saidas/out")
                      container.destroy()
                      return 0
                 if out == 0:

                  label_train['text']="Instalando"
                  os.system("rm -r config/saidas/out")
                 #label_progress.config(text=str(x)+"%")

                 container.update()
                 time.sleep(0.5)

            btn_start['text']="ok"
            btn_start.bind("<Button-1>", Sair)
            label_train['text']="Pacote instalado"


        ttk.Style().configure('green/white.TButton', foreground='black', background="white",font=("arial", 10),bd=2,highlightthickness=0.5,
        activebackground="white", activeforeground="black",relief=GROOVE,highlightbackground = "#9c203c", highlightcolor= "#9c203c")

        label_train =Label(container, text="Download", font='arial 10',background="white")
        label_train.pack(padx=20, pady=10)

        progress = Progressbar(container, style="TProgressbar", length=100, mode="indeterminate")
        progress.pack(padx=10, pady=5)

        btn_start = ttk.Button(container, text="Cancelar",style='green/white.TButton')
        btn_start.pack(padx=20, pady=15)

        container.after(1, start_training_images)