from binarytree import bst, Node

def contar_folhas(node):
    if node is None:
        return 0
    # Se o nó não tem filhos, é folha
    if node.left is None and node.right is None:
        return 1
    # Soma as folhas à esquerda e à direita
    return contar_folhas(node.left) + contar_folhas(node.right)

# Gerar uma BST aleatória com altura máxima 4
arvore = bst(height=4, is_perfect=False)

# Mostrar a árvore
print("Árvore BST gerada:")
print(arvore)

# Contar e exibir o número de folhas
quantidade_folhas = contar_folhas(arvore)
print(f"Quantidade de folhas: {quantidade_folhas}")
