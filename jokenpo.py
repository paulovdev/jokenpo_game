
import random
import time

soma_pont = 0
soma_pont1 = 0

global jogador, lista_computador, computador


def jokenpo():
    print("")
    print("\033[34mJO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PÔ")
    time.sleep(0.5)
    print("")


def menu():
    print("\033[4;35m------------------JOKENPÔ------------------")
    print("")
    print("\033[0;35mEscolha uma opção:")


def player():
    global jogador
    jogador = int(input("\033[33m[1]\033[7;30;m Pedra"
                        "    \033[33m[2]\033[7;30;m Papel"
                        "    \033[33m[3]\033[7;30;m Tesoura\n"))

    if jogador == 1:
        print('\033[32mJogador\033[m jogou com Pedra')
        jokenpo()

    elif jogador == 2:
        print('\033[32mJogador\033[m jogou com Papel')
        jokenpo()

    elif jogador == 3:
        print('\033[32mJogador\033[m jogou com Tesoura')
        jokenpo()

    else:
        print("\033[31mValor inválido")
        quit()


def cpu():
    global computador
    computador = random.randint(0, 2)

    if computador == 0:
        print('\033[31mComputador\033[m jogou com Pedra')

    elif computador == 1:
        print('\033[31mComputador\033[m jogou com Papel')

    elif computador == 2:
        print('\033[31mComputador\033[m jogou com Tesoura')


def game():
    global computador, jogador, soma_pont, soma_pont1

    # empates:
    if jogador == 1 and computador == 0 or jogador == 2 and computador == 1 or jogador == 3 and computador == 2:
        print("")
        print("\033[36mEmpate\033[m")

    elif jogador == 1 and computador == 2 or jogador == 3 and computador == 1:
        print("")
        print("\033[32mJogador\033[m venceu!")
        soma_pont1 = soma_pont1 + 1

    elif computador == 0 and jogador == 3 or computador == 2 and jogador == 2 or jogador == 1 and computador == 1 \
            or jogador == 2 and computador == 0:
        print("")
        print("\033[31mComputador\033[m venceu!")
        soma_pont = soma_pont + 1


def pontuacao():
    print("")
    print("\033[35m------------------RESULTADO------------------")

    time.sleep(0.4)
    print("\033[32mJOGADOR:\033[m", soma_pont1, "\033[31m  COMPUTADOR:\033[m", soma_pont)


def pontuacaofinal():
    print("")
    print("\033[35m------------------RESULTADO FINAL------------------")

    time.sleep(0.4)
    print("\033[32mJOGADOR:\033[m", soma_pont1, "\033[31m  COMPUTADOR:\033[m", soma_pont)
    if soma_pont > soma_pont1:
        print("\033[31mCOMPUTADOR\033[m FEZ MAIS PONTOS!")
    elif soma_pont1 > soma_pont:
        print("JOGADOR\033[m FEZ MAIS PONTOS!")
    else:
        print("\033[36mEMPATE!\033[m")


def play():
    i = 0
    while i < 3:
        i += 1
        menu()
        player()
        cpu()
        game()


def reiniciar():
    print("")
    start_stop = int(input("\033[33m[1]\033[m Jogar novamente\n"
                           "\033[33m[2]\033[m Sair"))
    if start_stop == 1:
        play()
        pontuacao()
        reiniciar()
    elif start_stop == 2:
        pontuacaofinal()
        quit()


play()
pontuacao()
reiniciar()


