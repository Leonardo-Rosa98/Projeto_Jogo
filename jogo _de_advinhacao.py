import random
#titulo do jogo:
def titulo():
    nome_jogo = "*" * 15 + " JOGO DE ADVINHAÇÃO " + 15 * "*"
    print("*" * len(nome_jogo) , nome_jogo, "*" * len(nome_jogo) , sep="\n" )
    
#apresentação do jogo:
def instrucao():
    print("\nVocê deve advinhar um numero de a à 1 a 10!")
   
#mensagem ganhador:
def ganhou():
    return print("Você ganhou o jogo!")

#mensagem Fim de jogo:
def fim_de_jogo():
    return print("Game over ;(")

#mensagem_de_erro:

def voce_errou(chances):
    if chances == 0:
        print("Número errado!\nVocê esgotou suas chances!")
        return None
    print("Número errado, tente novamente!\n")
    if chances > 1:
        print(f"Você tem mais {chances} chances!")
    else:
        print(f"Você tem mais {chances} chance!")
        
#selecionando dificuldade.
def dificuldade_do_jogo():
   print("Por favor, digite o nível da dificuldade: \n")
   chances = {"Fácil": 6,"Médio": 4 , "Difícil": 3}
   mapa_chances = {1:"Fácil", 2: "Médio", 3: "Difícil"}
   dificuldade = int(input("(1) Fácil - (2) Médio - (3) Difícil: "))
   
   while dificuldade not in mapa_chances:
        print("\nPor favor digite uma opção válida!")
        dificuldade = int(input("(1) Fácil - (2) Médio - (3) Difícil: "))
       
   chances = chances[mapa_chances[dificuldade]]
   
   return chances

#inicia o jogo:
def start():
    chances = dificuldade_do_jogo()
    print(f'Você terá {chances} chances para acertar o número secreto!\nBoa sorte! \o/\n')
    #função random.randonint = escolhe um numero aletorio entre um intervalo pré determinado
    numero_secreto = random.randint(1,10)
    chute = int(input("Digite um número: "))
    ganhador = False
    while chances > 0:
        if chute == numero_secreto:
            ganhou()
            ganhador = True
            break 

        else:
             chances -= 1
             voce_errou(chances)
             if chances != 0:
                chute = int(input("Digite um número: "))   
    if not ganhador:
      fim_de_jogo()

#------------------------------------------------------------------------------------------------------------

titulo()
instrucao()
start()