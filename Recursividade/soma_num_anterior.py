def soma(numero: int) -> int:
    if numero == 0:
        return 0
    return numero + soma(numero - 1)