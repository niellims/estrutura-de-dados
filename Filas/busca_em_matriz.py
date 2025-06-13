# Função que realiza a busca em largura (BFS) no labirinto
def bfs_labirinto(matriz: list, inicio: tuple, fim: tuple) -> bool:
    # Fila para armazenar as posições a explorar
    fila = [inicio]

    # Marca a posição inicial como visitada
    matriz[inicio[0]][inicio[1]] = 'V'  # V de "visitado"

    # Possíveis movimentos: cima, baixo, esquerda, direita
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(fila) > 0:
        posicao = fila.pop(0)
        linha = posicao[0]
        coluna = posicao[1]

        # Se chegou ao destino
        if (linha, coluna) == fim:
            return True

        # Explora os vizinhos
        for i in range(4):  # 4 direções
            nova_linha = linha + movimentos[i][0]
            nova_coluna = coluna + movimentos[i][1]

            # Verifica se está dentro dos limites da matriz
            if nova_linha >= 0 and nova_linha < len(matriz) and nova_coluna >= 0 and nova_coluna < len(matriz[0]):
                vizinho = matriz[nova_linha][nova_coluna]
                # Se o vizinho é caminho livre ou o fim
                if vizinho == 0 or vizinho == 'E':
                    fila.append((nova_linha, nova_coluna))
                    # Marca como visitado se não for o fim
                    if vizinho != 'E':
                        matriz[nova_linha][nova_coluna] = 'V'

    return False  # Se a fila acabar e não encontrar o fim

# Função para encontrar as posições de início (S) e fim (E)
def encontrar_inicio_fim(matriz: list) -> tuple:
    inicio = (-1, -1)
    fim = (-1, -1)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 'S':
                inicio = (i, j)
            elif matriz[i][j] == 'E':
                fim = (i, j)
    return (inicio, fim)

# Função principal
def main() -> None:
    # Exemplo de labirinto
    labirinto = [
        [1, 1, 1, 1, 1, 1],
        [1, 'S', 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 'E', 1],
        [1, 1, 1, 1, 1, 1]
    ]

    inicio, fim = encontrar_inicio_fim(labirinto)

    if inicio == (-1, -1) or fim == (-1, -1):
        print("Início ou fim não encontrados no labirinto.")
        return

    if bfs_labirinto(labirinto, inicio, fim):
        print("Caminho encontrado até o destino!")
    else:
        print("Não existe caminho até o destino.")

# Executa o programa
main()
