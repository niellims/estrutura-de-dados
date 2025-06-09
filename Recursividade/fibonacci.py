def fib(numero: int) -> int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fib(numero - 1) + fib(numero - 2)