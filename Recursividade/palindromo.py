def eh_palindromo(palavra: str) -> bool:
    if len(palavra) <= 1:
        return True
    if palavra[0] != palavra[-1]:
        return False
    return eh_palindromo(palavra[1:-1])