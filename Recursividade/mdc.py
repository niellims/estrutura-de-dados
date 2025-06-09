def mdc(a: int, b: int) -> int:
    if b == 0:
        return a
    return mdc(b, a % b)