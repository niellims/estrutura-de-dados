# Função que lê a sequência de números do usuário
def ler_sequencia(tamanho: int) -> list:
    sequencia = []
    for i in range(tamanho):
        valor = int(input(f"Digite o {i + 1}º número: "))
        sequencia.append(valor)
    return sequencia

# Função que usa uma pilha para verificar se a sequência é um palíndromo
def verificar_palindromo(sequencia: list) -> bool:
    pilha = []
    tamanho = len(sequencia)

    # Empilha a primeira metade da sequência
    for i in range(tamanho // 2):
        pilha.append(sequencia[i])

    # Define o ponto de início para comparar com a pilha
    # Se o tamanho for ímpar, ignoramos o elemento do meio
    inicio_segunda_metade = (tamanho // 2) + (tamanho % 2)

    # Compara a segunda metade com os elementos desempilhados
    for i in range(inicio_segunda_metade, tamanho):
        topo = pilha.pop()
        if sequencia[i] != topo:
            return False

    return True

# Função principal que executa o programa
def main() -> None:
    tamanho = int(input("Digite a quantidade de números da sequência: "))
    sequencia = ler_sequencia(tamanho)

    if verificar_palindromo(sequencia):
        print("A sequência É um palíndromo.")
    else:
        print("A sequência NÃO é um palíndromo.")

# Executa a função principal
main()
