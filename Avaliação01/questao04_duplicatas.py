# Questão 4: Verificação de Duplicatas e Ordenação
# Implemente uma função (não recursiva) que conte quantas vezes um número aparece em
# uma lista. Depois, ordene a lista com shell sort e imprima os números que aparecem mais
# de uma vez.

def contar_ocorrencias(lista):
    unicos = [] # lista para armazenar os números únicos encontrados
    quantidades = [] # lista paralela que armazena a quantidade de vezes que cada número apareceu

    for i in range(len(lista)):
        encontrado = False
         # verifica se o número já está na lista de únicos
        for j in range(len(unicos)):
            if lista[i] == unicos[j]:
                quantidades[j] += 1  # se encontrou, incrementa a quantidade
                encontrado = True
                break # já encontrou, não precisa continuar o laço
        if not encontrado: # se não encontrou o número ainda, adiciona como novo
            unicos.append(lista[i]) 
            quantidades.append(1) # começa a contagem com 1
    
    return unicos, quantidades


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

numeros = [3, 5, 2, 3, 8, 5, 1, 5]


unicos, quantidades = contar_ocorrencias(numeros)


shell_sort(numeros)


print("Lista ordenada:", numeros)
print("Números que aparecem mais de uma vez:")
for i in range(len(unicos)):
    if quantidades[i] > 1:
        print(f"{unicos[i]} aparece {quantidades[i]} vezes")


