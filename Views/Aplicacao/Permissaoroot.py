def Permissao_root():

        if vars.usuario != "root":
            titulo="Informe a senha para\nroot"
            saida=5
            seleciona_usuario="root"
            Senha(titulo,saida,seleciona_usuario)
        else:
            conexao=vars.conexao
            Desligar(conexao)