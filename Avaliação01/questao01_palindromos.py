#Questão 1: Detectando Palíndromos com Ordenação Duas palavras são palíndromos se podem ser lidas da mesma forma de trás para frente. Escreva uma função recursiva que verifique se uma palavra é palíndromo. Em seguida, organize uma lista de palavras, incluindo palíndromos e não-palíndromos, em ordem crescente (ordem alfabética) utilizando insertion sort.


def eh_palindromo(palavra: str) -> bool:
    if len(palavra) <= 1: # se a palavra tiver menos ou igual um caractere, ela é palindromo
        return True
    if palavra[0] != palavra[-1]: #aqui eu verifico se um caractere é diferente da anterior caso seja eu descarto de fazer a verificação completa
        return False
    return eh_palindromo(palavra[1:-1])


lista = ["ana", "casa", "arara", "luz", "radar"]
palindromos = []

for i in range(len(lista)):
    if eh_palindromo(lista[i]):
        palindromos.append(lista[i]) #to acrescentando apenas as palavras que sao palindromos na lista de palindromos

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        # Comparando strings em ordem alfabética
        while j >= 0 and lista[j].lower() > chave.lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

print('Lista ordernada: ', insertion_sort(lista))
print('Palíndromos identificados: ', palindromos)