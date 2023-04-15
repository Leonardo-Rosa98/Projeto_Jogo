import textwrap
class Jogo_da_forca:
    def __init__(self):
        self.nome = self.titulo_do_jogo()
        self.instrucao_do_jogo =  self.instrucao()

    """Essa função cria o nome do jogo em uma forma apresentavél"""    
    def titulo_do_jogo(self):
        nome_do_jogo = "*" * 10 + " Jogo da Forca " + "*" * 10
        titulo = print("*" * len(nome_do_jogo), nome_do_jogo, "*" * len(nome_do_jogo), sep="\n")
        return titulo

    """Esse método passa instruções do jogo para o usuário"""
    def instrucao(self):
        mensagem = textwrap.dedent(f"""
        Bem vindo, ao jogo da Forca!
        Você deve acertar a palavra secreta antes de ser inforcado.
        Para isso é necessário que você acerte todas as letras""")
        print(mensagem)

jogo_da_forca = Jogo_da_forca()
jogo_da_forca.nome
jogo_da_forca.instrucao_do_jogo    
        