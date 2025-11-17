import numpy as np
import os


areajogo = np.zeros((3,3), dtype=int)
PLAYER1 = None
PLAYER2 = None
numeros_aceitaveis = np.arange(1,10)
i1 = 0
i2 = 1  
local_player = (1,1)  

cor_vermelha = "\033[31m"
reset = "\033[0m"

movimentacao = {
    'cima': [-1, 0],     'c': [-1, 0],
    'baixo': [1, 0],     'b': [1, 0],
    'esquerda': [0, -1], 'e': [0, -1],
    'direita': [0, 1],   'd': [0, 1]
}

# -------------------------------------------------------------
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def imprimir_jogo(localplayer):
    if isinstance(localplayer, list):
        localplayer = tuple(localplayer)

    for l in range(areajogo.shape[0]):
        for c in range(areajogo.shape[1]):
            pos = (l, c)

            if pos == localplayer:
                celula = f"{cor_vermelha}{areajogo[l][c]}{reset}"
            else:
                celula = f"{areajogo[l][c]}"

            if c < 2:
                print(f" {celula} |", end="")
            else:
                print(f" {celula}")
                if l < 2:
                    print("-----------")


# -------------------------------------------------------------Verifica vitória 

def verificar_vitoria(matriz, p):
    if np.any(np.all(matriz == p, axis=1)): return True
    if np.any(np.all(matriz == p, axis=0)): return True
    if np.all(np.diag(matriz) == p): return True
    if np.all(np.diag(np.fliplr(matriz)) == p): return True
    return False

def verificar_empate(matriz):
    return np.all(matriz != 0)


# -------------------------------------------------------------Escolha numeros players

while PLAYER1 not in numeros_aceitaveis or PLAYER2 not in numeros_aceitaveis or PLAYER1 == PLAYER2:
    print('Bem vindo ao jogo da velha!')
    if i1 > 0:
        print('Escolha números válidos (1 a 9) e diferentes!')
    
    try:
        PLAYER1 = int(input('Player 1 escolha seu número (1-9): '))
        PLAYER2 = int(input('Player 2 escolha seu número (1-9): '))
    except:
        PLAYER1 = None
        PLAYER2 = None

    limpar_tela()
    i1 += 1


# ------------------------------------------------------------- Pratica jogo

while True:
    imprimir_jogo(local_player)

    #-----------------------------------------------------------------Turno
    if i2 % 2 != 0:
        print('Jogada do Player 1')
        jogador_atual = PLAYER1
        jogador_oponente = PLAYER2
    else:
        print('Jogada do Player 2')
        jogador_atual = PLAYER2
        jogador_oponente = PLAYER1

    print('Movimente: (C)ima, (B)aixo, (D)ireita, (E)esquerda')
    print(f"Ou pressione '{jogador_atual}' para marcar a posição.")
    entrada = input('Digite: ').lower()

    #------------------------------------------------------------------------Entrada movimentacao
    if entrada in movimentacao:
        mov = movimentacao[entrada]
        novo_local = tuple(np.add(local_player, mov))

        #---------------------------------------------------Verifica limites do mapa
        if not (0 <= novo_local[0] < 3 and 0 <= novo_local[1] < 3):
            print("Movimento fora do mapa!")
            input("Pressione Enter")
            limpar_tela()
            continue

        local_player = novo_local
        limpar_tela()
        continue


    if entrada.isdigit():
        entrada = int(entrada)

        #---------------------------------------------Só pode marcar usando seu próprio número
        if entrada != jogador_atual:
            print("Você está tentando marcar com o número do outro player!")
            input("Pressione Enter")
            limpar_tela()
            continue

        #---------------------------------------------------Verificar se posição está vazia
        if areajogo[local_player] != 0:
            print("Local já selecionado!")
            input("Pressione Enter")
            limpar_tela()
            continue

        #------------------------------------------------------Marca no tabuleiro
        areajogo[local_player] = jogador_atual
        i2 += 1
    else:
        print("Entrada inválida!")
        input("Pressione Enter")
        limpar_tela()
        continue

    limpar_tela()

    # ---------------------------------------------------------Verificar vitória

    if verificar_vitoria(areajogo, PLAYER1):
        imprimir_jogo(local_player)
        print("Vitória do Player 1!")
        break

    if verificar_vitoria(areajogo, PLAYER2):
        imprimir_jogo(local_player)
        print("Vitória do Player 2!")
        break


    
    if verificar_empate(areajogo):
        imprimir_jogo(local_player)
        print("Jogo empatado!")
        break
