chute = "a"
palavra = "banana"
palavras_acertadas = ["_" for i in palavra]

if chute in palavra:
    for indice, letra in enumerate(palavra):
        if chute == letra:
            palavras_acertadas[indice] = chute




