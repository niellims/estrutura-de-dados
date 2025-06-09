def insertion_sort(lista: list[float]) -> list[float]:
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j] > lista[j - 1]:
            # Troca com variável auxiliar
            aux = lista[j]
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            j -= 1
    return lista