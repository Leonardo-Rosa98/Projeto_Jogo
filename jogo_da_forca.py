import textwrap
class Jogo_da_forca:
    def __init__(self):
        self.nome = self.titulo_do_jogo()
        self.instrucao_do_jogo =  self.instrucao()
        self.palavra = self.palavra_secreta()
        self.quantidade_letras = self.qtd_letras()
        self.chute_usuario = self.chute

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
        Para isso é necessário que você acerte todas as letras.""")
        print(mensagem)
    
    """Essa função escolhe aleatoriamente uma palavra, que será nossa (PALAVRA SECRETA)"""
    def palavra_secreta(self):
        palavra_secreta = "banana"
        return palavra_secreta
    
    """Essa função mostra a quantidade de letra que existe na palavra"""
    def qtd_letras(self):    
        palavra = self.palavra
        qtd_letras = ["_" for i in palavra]
        return qtd_letras
    
    """Essa função pede um chute do usuário, sendo ela uma letra do alfabéto, caso contrário
     retornará um erro. """
    def chute(self):
        while True:
             chute = str(input("Por favor, digite uma letra de A á Z: "))
             if len(chute) == 1 and chute.isalpha():
                break
             else:
                 print("Você deve colocar uma opção válida!") 
        return chute    
    
    



#-----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    jogo_da_forca = Jogo_da_forca()
    jogo_da_forca.nome
    jogo_da_forca.instrucao_do_jogo    
    