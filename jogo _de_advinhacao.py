import random
#titulo do jogo:
def titulo():
    nome_jogo = "******* JOGO DE ADVINHAÇÃO *******"
    estrela = "*" * len(nome_jogo) 
    print(estrela)
    print(nome_jogo)
    print(estrela)

#apresentação do jogo:
def instrucao():
    print("\nVocê deve advinhar um numero de a à 1 a 10")
   
#mensagem ganhador:
def ganhou():
    return print("Você ganhou o jogo!")
#mensagem perdedor:
def perdeu():
    return print("Game over")

titulo()
instrucao()

#função random.randonint = escolhe um numero aletorio entre um intervalo pré determinado
numero_secreto = random.randint(1,10)
chute = int(input("Digite um número: "))

if chute == numero_secreto:
   ganhou() 
else:
    perdeu()
