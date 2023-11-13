from random import randint
acertou = False
dificuldade = int(input("Dificuldade: 1 Facil, 2 Medio, 3 Dificil: "))

if dificuldade == 1:
    numero = randint(1, 10)
    while acertou is False:
        jogo = int(input("Nivel facil. Chute um número de 1-10: "))
        if jogo > numero:
            print("Número chutado MAIOR que o número sorteado!")

        if jogo < numero:
            print("Número chutado MENOR que o número sorteado")

        if jogo == numero:
            print("=======\nVocê acertou!")
            print("Fim de jogo.\n=======")
            acertou = True

if dificuldade == 2:
    numero = randint(1, 50)
    while acertou is False:
        jogo = int(input("Nivel medio. Chute um número de 1-50: "))
        if jogo > numero:
            print("Número chutado MAIOR que o número sorteado!")

        if jogo < numero:
            print("Número chutado MENOR que o número sorteado")

        if jogo == numero:
            print("=======\nVocê acertou!")
            print("Fim de jogo.\n=======")
            acertou = True

if dificuldade == 3:
    numero = randint(1, 100)
    while acertou is False:
        jogo = int(input("Nivel dificil. Chute um numero de 1-100: "))
        if jogo > numero:
            print("Número chutado MAIOR que o número sorteado!")

        if jogo < numero:
            print("Número chutado MENOR que o número sorteado")

        if jogo == numero:
            print("=======\nVocê acertou!")
            print("Fim de jogo.\n=======")
            acertou = True