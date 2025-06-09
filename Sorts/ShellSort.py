def shell_sort(lista: list[int]) -> list[int]:
    n = len(lista)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and lista[j - gap] > lista[j]:
                aux = lista[j]
                lista[j] = lista[j - gap]
                lista[j - gap] = aux
                j -= gap
        gap //= 2 

    return lista