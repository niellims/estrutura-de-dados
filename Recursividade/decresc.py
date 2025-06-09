def imprimir_decrescente(n: int):
    if n == 0:
        return
    print(n)
    imprimir_decrescente(n - 1)