import os

out=(" > /dev/null; then echo 1 > Config/saidas/out; else echo 0 > Config/saidas/out; fi")
output=os.system("cat s/saidas/out")
apaga_out=os.system("rm -r Config/saidas/out")
vnc_user=os.popen(conexao+" users").read().rstrip()
vnc_users=[]
user=""
for x in range(0, len(vnc_user)):
  if vnc_user[x] != " ":
      user+=vnc_user[x]

  if vnc_user[x] == " " or x == len(vnc_user)-1:
      vnc_users.append(user)
      user=""