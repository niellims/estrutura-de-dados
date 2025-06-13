# Questão 2: Estatísticas com Recursividade
# Implemente uma função recursiva para somar todos os elementos de um vetor de notas.
# Depois, ordene esse vetor com insertion sort e calcule a mediana.

def soma_vetor(vetor: list[int]) -> int: #função recursiva para somar as notas
    if len(vetor) == 0:
        return 0
    return vetor[0] + soma_vetor(vetor[1:]) #somo o elemento atual com a soma dos proximos elementos

mediana = 0



def mediana(lista: list[float]) -> float: 
    tamanho = len(lista)
    meio = tamanho//2

    if tamanho%2==0: #se a lista conter uma qntd par de elementos, ela vai pegar o elemento do meio e o próx e fazer uma média entre eles
        mediana = (lista[meio-1]+lista[meio])/2
        return mediana
    else: #porém se a qntd de elementos for impar, a mediana será o elemento central da lista
        mediana = lista[meio]
        return mediana
    


lista = [6.7, 8.5, 5.4, 9.0, 7.8]


def insertion_sort(lista: list[float]) -> list[float]:
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j] < lista[j - 1]:
            # Troca com variável auxiliar
            aux = lista[j]
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            j -= 1
    return lista




lista_ordenada = insertion_sort(lista)


print('Soma total: ', soma_vetor(lista))
print('Lista ordenada: ',lista_ordenada)
print('Mediana: ', mediana(lista_ordenada))