import random

def gerar_cartela(modo):
    if modo == 0:
        cartela = [
            random.sample(range(1, 11), 2),
            random.sample(range(11, 21), 2),
            random.sample(range(21, 31), 2)
        ]
    else:
        cartela = [
            random.sample(range(1, 11), 3),
            random.sample(range(11, 21), 3),
            random.sample(range(21, 31), 3),
            random.sample(range(31, 41), 3)
        ]
    return cartela

def sortear_numero(sorteados, intervalo):
    numero = random.choice([n for n in intervalo if n not in sorteados])
    sorteados.append(numero)
    return numero

def marcar_cartela(cartela, sorteados):
    for linha in cartela:
        for i in range(len(linha)):
            if linha[i] in sorteados:
                linha[i] = 'X'


def imprimir_cartela(cartela):
    for linha in cartela:
        print(f"{linha}")

def simular_bingo(modo):
    intervalo = list(range(1, 31)) if modo == 0 else list(range(1, 41))
    
    cartela_jogador1 = gerar_cartela(modo)
    cartela_jogador2 = gerar_cartela(modo)

    sorteados = []
    
    print("\nIniciando o jogo...")

    while True:
        numero = sortear_numero(sorteados, intervalo)
        print(f"\nNúmero sorteado: {numero}")
        print(f"Dezenas sorteadas até o momento: {sorted(sorteados)}")

        marcar_cartela(cartela_jogador1, sorteados)
        marcar_cartela(cartela_jogador2, sorteados)

        print("\nCartela do Jogador 1:")
        imprimir_cartela(cartela_jogador1)
        
        print("\nCartela do Jogador 2:")
        imprimir_cartela(cartela_jogador2)

        ganhou_jogador1 = all(num == 'X' for linha in cartela_jogador1 for num in linha)
        ganhou_jogador2 = all(num == 'X' for linha in cartela_jogador2 for num in linha)

        if ganhou_jogador1 and ganhou_jogador2:
            print("\nAmbos os jogadores ganharam ao mesmo tempo!")
            break
        elif ganhou_jogador1:
            print("\nO jogador 1 venceu!")
            break
        elif ganhou_jogador2:
            print("\nO jogador 2 venceu!")
            break

        input("\nPressione ENTER para sortear o próximo número...")

def jogar():
    print("Bem-vindo ao simulador de Bingo! \n")

    print("Você pode escolher um destes:")
    print("MODO RÁPIDO: 0")
    print("MODO DEMORADO: 1 \n")
    
    while True:
        modo = input("Indique o modo de jogo desejado: ")
        
        if modo not in ['0', '1']:
            print("Modo inválido! Escolha 0 para rápido ou 1 para demorado.")
        else:
            modo = int(modo)
            break

    simular_bingo(modo)

jogar()
