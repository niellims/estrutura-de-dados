from binarytree import bst, Node

def soma_nos(node):
    if node is None:
        return 0
    return node.value + soma_nos(node.left) + soma_nos(node.right)

# Gerar uma BST aleatória
arvore = bst(height=3, is_perfect=False)

# Mostrar a árvore
print("Árvore BST gerada:")
print(arvore)

# Calcular e mostrar a soma
soma_total = soma_nos(arvore)
print(f"Soma de todos os nós: {soma_total}")