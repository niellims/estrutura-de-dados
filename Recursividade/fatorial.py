def fat(n:int) -> int:
    if n == 1:
        return 1
    
    return n * fat(n-1)