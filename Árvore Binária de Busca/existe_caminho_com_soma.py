# Usaremos recursão para:

# Subtrair o valor do nó atual do valor alvo

# Verificar se chegamos a uma folha (nó sem filhos) e o valor restante é igual ao valor do nó

# Se não for folha, verificar recursivamente à esquerda e à direita

from binarytree import bst, Node

def existe_caminho_com_soma(node, valor_alvo):
    if node is None:
        return False

    # Se for folha, verifica se o valor do nó é igual ao valor restante
    if node.left is None and node.right is None:
        return node.value == valor_alvo

    # Subtrai o valor do nó atual e continua buscando nas subárvores
    restante = valor_alvo - node.value
    return (
        existe_caminho_com_soma(node.left, restante) or
        existe_caminho_com_soma(node.right, restante)
    )

# Gerar uma BST aleatória
arvore = bst(height=3, is_perfect=False)

# Mostrar a árvore
print("Árvore BST gerada:")
print(arvore)

# Definir o valor alvo
alvo = 60  # você pode testar com outros valores também

# Verificar se existe caminho com essa soma
existe = existe_caminho_com_soma(arvore, alvo)
print(f"Existe caminho com soma {alvo}? {existe}")
