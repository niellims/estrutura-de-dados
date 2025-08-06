from binarytree import bst, Node
from collections import deque  # Usamos deque para a fila

def percurso_em_nivel(root):
    if root is None:
        return []

    fila = deque()
    resultado = []

    fila.append(root)  # Começa pela raiz

    while fila:
        no_atual = fila.popleft()  # Remove o nó do início da fila
        resultado.append(no_atual.value)

        # Adiciona os filhos do nó atual na fila, se existirem
        if no_atual.left:
            fila.append(no_atual.left)
        if no_atual.right:
            fila.append(no_atual.right)

    return resultado

# Gerar uma BST aleatória
arvore = bst(height=3, is_perfect=False)

# Mostrar a árvore
print("Árvore BST gerada:")
print(arvore)

# Executar o percurso em nível
sequencia = percurso_em_nivel(arvore)
print("Percurso em nível (Level-Order):")
print(sequencia)
