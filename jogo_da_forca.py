import textwrap
class Jogo_da_forca:
    def __init__(self):
        self.nome = self.titulo_do_jogo()
        self.instrucao_do_jogo =  self.instrucao()
        self.palavra = self.palavra_secreta()
        self.quantidade_de_letras = self.qtd_letras()
        self.jogar()
    
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
        print(qtd_letras)
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
    
    """Essa função valida se o chute do usuário está certo."""
    def validar_chute(self, chute):
        palavra = self.palavra
        if chute in palavra:
           print("Letra acertada!") 
           return True
        else:
            print("Letra incorreta!")
            return False
    
    """Essa função retorna a lista atualizada de letras acertadas """
    def atualizar_qtd_de_letras(self, letras_acertadas, chute):
        palavra_secreta  = self.palavra
        for indice, letra in enumerate(palavra_secreta):
            if chute == letra:
                letras_acertadas[indice] = chute
        return letras_acertadas
    
    """Essa função lista os chutes do usuário"""
    def chutes_do_usuario(self,chute,chutes):
        chutes.append(chute)
        return chutes
    
    """Essa função determina o numero de chances de acordo com o tamanho da palavra"""
    def chances(self, palavra):
        chances = len(palavra)
        return chances
    
    """Essa função verifica se o jogador ganhou o jogo."""
    def ganhou(self, letras_acertadas):
        if "_" not in letras_acertadas:
            return print("Parabéns você acertou a palavra secreta!")
        
    """Essa função inicia o jogo."""
    def jogar(self):
        palavra_secreta = self.palavra
        letras_acertadas = self.quantidade_de_letras
        chutes = []
        chances = self.chances(palavra_secreta)
        while "_" in letras_acertadas:
            chute = self.chute()
            lista_chutes = self.chutes_do_usuario(chute,chutes)
            if chute in letras_acertadas:
                print("Você já utilizou essa letra!")
                continue
            if self.validar_chute(chute):
                letras_acertadas = self.atualizar_qtd_de_letras(letras_acertadas, chute)
            else:
                chances -= 1
                print("\nSuas chances atuais são de: {chances}")
            if chances == 0:
                print("Game Over!")
                break    
            print(letras_acertadas)
            print(f'\nminha lista de chutes: {lista_chutes}')
        self.ganhou(letras_acertadas)

#-----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    jogo_da_forca = Jogo_da_forca()