def pot(numero:int, p:int) -> int:
    if p == 0:
        return 1
    return numero * pot(numero,p-1)

num = 3