import datetime
import os

agora = datetime.datetime.now()

agora_hora = agora.strftime("%I:%M")
agora_minuto = int(agora.strftime("%M"))
nome = input(f"Bom dia. Agora são {agora_hora}... Qual é seu apelido? ")

print(f"Belo nome, {nome}!")
idade = int(input("Quantos anos você tem? "))

letras_nome = len(nome)-nome.count(" ")


if idade >= 18:
    print(f"Interessante, você já um adulto. Que legal, {nome}!")
if idade < 18:
    print(f"Está jovem ainda. Ótima idade, {nome}!")

jogar = input(f"{nome}, você gostaria de jogar um jogo? ").lower()

resposta1 = ['sim']
repostas2 = ['não', 'nao']
respostaU = ['guimts']

os.system('cls') or None

if jogar in resposta1:
    print("Otimo, vamos jogar então!!\n=======")
    game = True

    while game is True:

        primeira_perg = int(input("Em que ano houve a primeira revolução industrial? "))
        if primeira_perg == 1760:
            print('Isso mesmo! A primeira evolução ocorreu em 1760 e terminou em 1840\n=====')
            segunda_pergunta = int(input("Qual idade você registrou no jogo? "))
            if segunda_pergunta == idade:
                print("Correto! Aparentemente você não mentiu.\n=====")
                ter_perg = int(input("Quantas letras tem seu apelido? "))
                if ter_perg == letras_nome:
                    print(f"Correto! Seu apelido há {letras_nome} letras\n=====")
                    quart_perg = int(input("Em que minuto começamos a conversar? "))
                    if quart_perg == agora_minuto:
                        print("Correto! Boa memoria!!\n=====")
                        quint_perg = input("Última pergunta. Quem foi que me programou? \nGuimts ou Starss? ").lower()
                        if quint_perg in respostaU:
                            print("Correto!!! Você venceu o jogo, meus parabéns!")
                            game = False
                            os.system('pause')
                        else:
                            print("Não acredito que disse isso....\n=====")
                    else:
                        print("Acho que não deve lembrar...\n=====")
                else:
                    print("Errado! Conte novamente\n=====")
            else:
                print("Você mentiu no inicio? Ou só não lembra...?\n=====")
        else:
            print('Aaah, você errou... Tenta de novo!\n=====')

if jogar in repostas2:
    print("Tudo bem! Até depois.")
    os.system('pause')