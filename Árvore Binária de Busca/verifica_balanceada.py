from binarytree import bst, Node

def altura(node):
    if node is None:
        return 0
    return 1 + max(altura(node.left), altura(node.right))

def esta_balanceada(node):
    if node is None:
        return True
    
    altura_esq = altura(node.left)
    altura_dir = altura(node.right)

    # Verifica se a diferença de alturas é maior que 1
    if abs(altura_esq - altura_dir) > 1:
        return False

    # Verifica recursivamente nas subárvores
    return esta_balanceada(node.left) and esta_balanceada(node.right)

# Gerar uma BST aleatória com altura até 4
arvore = bst(height=4, is_perfect=False)

# Mostrar a árvore
print("Árvore BST gerada:")
print(arvore)

# Verificar se está balanceada
balanceada = esta_balanceada(arvore)
print(f"A árvore está balanceada? {balanceada}")