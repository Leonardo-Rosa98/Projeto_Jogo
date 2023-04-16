import textwrap
import random

class Jogo_da_forca:
    def __init__(self):
        self.palavras = ["banana", "abacate", "laranja", "tomate", "melancia", "uva"]
        self.palavra_secreta = random.choice(self.palavras)
        self.quantidade_de_letras = ["_" for i in self.palavra_secreta]
        self.chances = len(self.palavra_secreta)
        self.jogar()

    def titulo_do_jogo(self):
        """
        Essa função cria o nome do jogo em uma forma apresentavél
        """   
        nome_do_jogo = "*" * 10 + " Jogo da Forca " + "*" * 10
        titulo = print("*" * len(nome_do_jogo), nome_do_jogo, "*" * len(nome_do_jogo), sep="\n")
        return titulo

    def instrucao(self):
        """Esse método passa instruções do jogo para o usuário"""
        mensagem = textwrap.dedent(f"""
        Bem vindo, ao jogo da Forca!
        Você deve acertar a palavra secreta antes de ser inforcado.
        Para isso é necessário que você acerte todas as letras.""")
        print(mensagem)

    def mensagens(self, texto):
        mensagens = {
            "letra_certa": "Letra certa!",
            "letra_errada": "Letra errada!",
            "letra_repetida": "Você ja utilizou essa letra!",
            "opcao_invalida": "Você deve colocar uma opção válida!",
            "entrada": "Por favor, digite uma letra de A a Z:",
            "ganhador": "Parabéns você acertou a palavra secreta!",
            "fim_de_jogo": "Game over!"
        }
        print(mensagens[texto])

    def ganhou(self, letras_acertadas):
        """
        Essa função verifica se o jogador ganhou o jogo.
        """
        if "_" not in letras_acertadas:
            return True
        
    def chute(self):
        """
        Essa função pede um chute do usuário, sendo ela uma letra do alfabéto, caso contrário
        retornará um erro.
        """
        while True:
             chute = str(input(""))
             if len(chute) == 1 and chute.isalpha():
                break
             else:
                    self.mensagens("opcao_invalida")
                    self.mensagens("entrada")
        return chute    
    
    def validar_chute(self, chute):
        """
        Essa função valida se o chute do usuário está certo.
        """
        palavra = self.palavra_secreta
        if chute in palavra:
           return True
        else:
            return False
    
    def atualizar_qtd_de_letras(self, letras_acertadas, chute):
        """
        Essa função retorna a lista atualizada de letras acertadas
        """
        palavra_secreta  = self.palavra_secreta
        for indice, letra in enumerate(palavra_secreta):
            if chute == letra:
                letras_acertadas[indice] = chute
        return letras_acertadas
    
    def chutes_do_usuario(self,chute,chutes):
        """
        Essa função lista os chutes do usuário
        """
        chutes.append(chute)
        return chutes
    
    def jogar(self):
        """
        Essa função inicia o jogo.
        """
        self.titulo_do_jogo()
        self.instrucao()
        palavra_secreta = self.palavra_secreta
        letras_acertadas = self.quantidade_de_letras
        chutes = []
        chances = self.chances
        while "_" in letras_acertadas:
            self.mensagens("entrada")
            chute = self.chute()
            lista_chutes = self.chutes_do_usuario(chute,chutes)
            if chute in letras_acertadas:
                self.mensagens("letra_repetida")
                continue
            if self.validar_chute(chute):
                self.mensagens("letra_certa")
                letras_acertadas = self.atualizar_qtd_de_letras(letras_acertadas, chute)
            else:
                self.mensagens("letra_errada")
                chances -= 1
                print(f'Suas chances são de: {chances}')
            if chances == 0:
                self.mensagens("fim_de_jogo")
                break    
            print(letras_acertadas)
            print(f"Listas de chutes: {lista_chutes}" )
        if self.ganhou(letras_acertadas):
            self.mensagens("ganhador")

#-----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    jogo_da_forca = Jogo_da_forca()