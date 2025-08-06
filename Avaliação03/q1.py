from binarytree import bst, Node

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

# Função que define a altura da arveroe
def altura(root):
    if root is None:
        return 0
    return 1 + max(altura(root.left), altura(root.right))


# Função que verifica se está balanceada
def is_height_balanced(root):
    if root is None:
        return True
    
    altura_esq = altura(root.left)
    altura_dir = altura(root.right)

    # Verifica se a diferença de alturas é maior que 1
    if abs(altura_esq - altura_dir) > 1:
        return False

    # Verifica recursivamente nas subárvores
    resultado = is_height_balanced(root.left) and is_height_balanced(root.right)
    return resultado



# Gerar uma BST aleatória com altura até 4
arvore = bst(height=4)

print("Árvore BST gerada:")
print(arvore)

# Inserir os valores 5 e 2
inserir_bst(arvore, 5)
inserir_bst(arvore, 2)

print("Árvore BST após inserção de dados:")
print(arvore)

# Remover o valor 5
arvore = remover_bst(arvore, 5)

print("Árvore BST após remoção de dados:")
print(arvore)

# Verificar se está balanceada
balanceada = is_height_balanced(arvore)
print(f"A árvore está balanceada? {balanceada}")