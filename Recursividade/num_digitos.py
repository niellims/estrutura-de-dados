def numero_digitos(num:int) -> int:
    if num<10:
        return 1
    return 1 + numero_digitos(num//10)