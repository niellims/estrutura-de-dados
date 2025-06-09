def bubble_sort(lista: list[int]) -> list[int]:
    n = len(lista)
    for j in range(0,n):
        for i in range(0,n-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    
    return lista