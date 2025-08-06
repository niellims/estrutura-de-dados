from binarytree import bst

def list_leaf_values(root, result=None):
    if result is None:
        result = []
    if root is not None:
        # Se não tem filhos, é nó folha
        if root.left is None and root.right is None:
            result.append(root.value)
        else:
            # Recursão nos filhos
            list_leaf_values(root.left, result)
            list_leaf_values(root.right, result)
    return result

# Gerar uma árvore BST aleatória com altura 4
arvore = bst(height=4)

# Imprimir a árvore
print("Árvore Binária de Busca com altura 4:")
print(arvore)

# Obter valores dos nós folha
folhas = list_leaf_values(arvore)

# Exibir os valores dos nós folha
print("\nValores dos nós folha:")
print(folhas)
