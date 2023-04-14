import random
#titulo do jogo:
def titulo():
    nome_jogo = "*" * 15 + " JOGO DE ADVINHAÇÃO " + 15 * "*"
    print("*" * len(nome_jogo) , nome_jogo, "*" * len(nome_jogo) , sep="\n" )
#apresentação do jogo:
def instrucao():
    print("\nVocê deve advinhar um numero de a à 1 a 10!")
#mensagem ganhador  ou de perdedor:
def ganhou(ganhador):
    if ganhador:
        return print("Você ganhou o jogo!")
    if not ganhador:
        return print("Game over ;(")
#mensagem_de_erro
def voce_errou(chances):
    if chances == 0:
        print("Número errado!\nVocê esgotou suas chances!")
    else:
        plural = "s" if chances > 1 else ""
        print(f"Número errado, tente novamente!\nVocê tem mais {chances} chance{plural}!")
#selecionando dificuldade.
def dificuldade_do_jogo():
   print("Por favor, digite o nível da dificuldade: \n")
   niveis = {1:("Fácil", 7), 2:("Médio", 5), 3:("Difícil", 3)}
   while True:
       try:
           dificuldade = int(input("1 Fácil - 2 Médio - 3 Difícil: "))
           if dificuldade in niveis:
                break  
           else:
               print("\nPor favor, digite uma opção válida!")
       except ValueError:
                print("\nPor favor, digite um número válido!") 
   return niveis[dificuldade]                   
#inicia o jogo:
def start():
    modo, chances = dificuldade_do_jogo()
    print(f'Você escolheu o nível {modo} e terá {chances} chances para acertar o número secreto!\nBoa sorte! \o/\n')
    numero_secreto = random.randint(1,10)
    ganhador = False
    while chances > 0:
        try:
            chute = int(input("Digite um número: "))
        except ValueError:
            print("Por favor, digite um número válido!")    
            continue
        if chute == numero_secreto:
            ganhador = True
            break 
        else:
             chances -= 1
             voce_errou(chances)
    ganhou(ganhador)

#------------------------------------------------------------------------------------------------------------
titulo()
instrucao()
start()