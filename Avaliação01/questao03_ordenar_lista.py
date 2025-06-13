# Questão 3: Vetor Ordenado? Use Recursão!
# Você recebeu uma lista de números inteiros. Escreva uma função recursiva para verificar se
# a lista está ordenada em ordem crescente. Em seguida, ordene a lista usando shell sort
# caso não esteja ordenada.

lista = [10, 15, 12, 20, 25]
#lista = [10, 12, 15, 20, 25]

def esta_ordenada(lista: list[int], index=0) -> bool: #para verificar com os prox elementos, já setei o index por padrão como 0
    if index >= len(lista) - 1: #verificação pra ver se o elemento atual é maior que o anterior
        return True
    if lista[index] > lista[index + 1]:
        return False
    return esta_ordenada(lista, index + 1)

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



print('Está ordenada? ', esta_ordenada(lista))
if not esta_ordenada(lista):
    lista_ordenada = shell_sort(lista)
    print('Lista ordenada: ', lista_ordenada)

