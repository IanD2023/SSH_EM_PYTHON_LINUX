import os

def scp(usuario,senha,ip,arquivo,pasta):

    os.popen("sshpass -p '"+ senha +"' scp -o StrictHostKeyChecking=no -C "+arquivo+" "+ usuario + "@" + ip + pasta)
