from binarytree import bst, Node
import random

# criando uma BST com altura 4
arvore = bst(height=4)

# Imprimir a árvore
print("Árvore Binária de Busca com altura 4:")
print(arvore)

# Garantir que a árvore seja sempre a mesma para fins de testes
random.seed(42)

# Criar a BST com altura 4
arvore = bst(height=4)

print("Árvore original:")
print(arvore)

# Função de inserção manual em uma BST
def inserir_bst(raiz, valor):
    if valor < raiz.value:
        if raiz.left is None:
            raiz.left = Node(valor)
        else:
            inserir_bst(raiz.left, valor)
    elif valor > raiz.value:
        if raiz.right is None:
            raiz.right = Node(valor)
        else:
            inserir_bst(raiz.right, valor)
    # Se for igual, não insere (para evitar duplicatas)

# Inserir os valores 5 e 2
inserir_bst(arvore, 5)
inserir_bst(arvore, 2)

print("\nÁrvore após inserção de 5 e 2:")
print(arvore)


# Função de percurso pré-ordem
def pre_ordem(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz is not None:
        resultado.append(raiz.value)
        pre_ordem(raiz.left, resultado)
        pre_ordem(raiz.right, resultado)
    return resultado

# Executar percurso em pré-ordem
sequencia = pre_ordem(arvore)
print("\nPercurso em pré-ordem:")
print(sequencia)

# Função de percurso em ordem
def em_ordem(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz is not None:
        em_ordem(raiz.left, resultado)
        resultado.append(raiz.value)
        em_ordem(raiz.right, resultado)
    return resultado

print("Árvore após inserção de 5 e 2:")
print(arvore)

# Executar percurso em pré-ordem
sequencia_in_order = em_ordem(arvore)
print("\nPercurso em ordem (in-order):")
print(sequencia_in_order)

# Função de percurso em pós-ordem
def pos_ordem(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz is not None:
        pos_ordem(raiz.left, resultado)
        pos_ordem(raiz.right, resultado)
        resultado.append(raiz.value)
    return resultado

print("Árvore após inserção de 5 e 2:")
print(arvore)

# Executar percurso em pós-ordem
sequencia_post_order = pos_ordem(arvore)
print("\nPercurso em pós-ordem (post-order):")
print(sequencia_post_order)


# Função de busca
def buscar_bst(raiz, valor):
    if raiz is None:
        return False
    if raiz.value == valor:
        return True
    elif valor < raiz.value:
        return buscar_bst(raiz.left, valor)
    else:
        return buscar_bst(raiz.right, valor)

# Buscar o valor 6
valor_procurado = 6
encontrado = buscar_bst(arvore, valor_procurado)

print("Árvore atual:")
print(arvore)

if encontrado:
    print(f"\nValor {valor_procurado} encontrado na BST.")
else:
    print(f"\nValor {valor_procurado} NÃO encontrado na BST.")



# Função para remover um valor da BST
def remover_bst(raiz, valor):
    if raiz is None:
        return None

    if valor < raiz.value:
        raiz.left = remover_bst(raiz.left, valor)
    elif valor > raiz.value:
        raiz.right = remover_bst(raiz.right, valor)
    else:
        # Nó folha
        if raiz.left is None and raiz.right is None:
            return None
        # Um filho
        elif raiz.left is None:
            return raiz.right
        elif raiz.right is None:
            return raiz.left
        # Dois filhos
        else:
            sucessor = raiz.right
            while sucessor.left:
                sucessor = sucessor.left
            raiz.value = sucessor.value
            raiz.right = remover_bst(raiz.right, sucessor.value)
    return raiz

# Remover o valor 5
arvore = remover_bst(arvore, 5)

print("\nÁrvore após a remoção do valor 5:")
print(arvore)




# Função para encontrar o valor mínimo
def encontrar_minimo(raiz):
    if raiz is None:
        return None
    atual = raiz
    while atual.left is not None:
        atual = atual.left
    return atual.value

print("Árvore atual:")
print(arvore)

minimo = encontrar_minimo(arvore)
print(f"\nValor mínimo na BST: {minimo}")


# Função para encontrar o valor maximo
def encontrar_maximo(raiz):
    if raiz is None:
        return None
    atual = raiz
    while atual.right is not None:
        atual = atual.right
    return atual.value

print("Árvore atual:")
print(arvore)

max = encontrar_maximo(arvore)
print(f"\nValor maximo na BST: {max}")



# Função para calcular altura
def calcular_altura(raiz):
    if raiz is None:
        return -1  # altura como número de arestas
    return 1 + max(calcular_altura(raiz.left), calcular_altura(raiz.right))

print("Árvore atual:")
print(arvore)

altura = calcular_altura(arvore)
print(f"\nAltura da BST: {altura}")