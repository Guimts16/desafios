    prg = input('Olá, gostaria de participar de umas perguntas sobre o Gui? ').lower()
    pontos = 0
    rspt = ['sim']
    if prg in rspt:
        print("Certo! Então vamos às perguntas.")

        rsptprg1 = ["vermelho"]
        print("=========\nPrimeira pergunta.")
        prg1 = input("Qual a cor favorita dele? ").lower()
        if prg1 in rsptprg1:
            print("Certa resposta! +1P\n=========")
            pontos += 1
            perg2 = input('Quem é o maior amor dele? ').lower()
            respt2 = ['eloah', 'eloh', 'loh', 'loloh']
            if perg2 in respt2:
                print("Correto!!! Eloah é um amorzinho <3 +1P ")
                pontos += 1

                os.system('pause')

            else:
                input('Errado..')
        else:
            input('Errado!')
    if prg not in rspt:
        print("Tudo bem. Até a próxima!")
        input("Pressione <Enter> para continuar.")