def criar_pilha(capacidade: int) -> list[int]:
    return []  # Retorna uma lista vazia representando a pilha

def empilhar(pilha: list[int], elemento: int, capacidade: int) -> None:
    if len(pilha) >= capacidade:
        print("Erro: pilha cheia. Não é possível empilhar o elemento.")
    else:
        pilha.append(elemento)
        print(f"Elemento {elemento} empilhado.")

def desempilhar(pilha: list[int]) -> int:
    if len(pilha) == 0:
        print("Erro: pilha vazia. Não é possível desempilhar.")
        return -1  # Valor de erro; pode ser ajustado conforme o uso
    else:
        elemento = pilha.pop()
        print(f"Elemento {elemento} desempilhado.")
        return elemento

def topo(pilha: list[int]) -> int:
    if len(pilha) == 0:
        print("Pilha vazia. Nenhum elemento no topo.")
        return -1
    return pilha[-1]

def esta_vazia(pilha: list[int]) -> bool:
    return len(pilha) == 0

def esta_cheia(pilha: list[int], capacidade: int) -> bool:
    return len(pilha) >= capacidade


def exemplo_uso_pilha() -> None:
    capacidade = 3
    pilha = criar_pilha(capacidade)

    empilhar(pilha, 10, capacidade)
    empilhar(pilha, 20, capacidade)
    empilhar(pilha, 30, capacidade)
    empilhar(pilha, 40, capacidade)  # Deve dar erro (pilha cheia)

    print("Topo da pilha:", topo(pilha))

    desempilhar(pilha)
    desempilhar(pilha)
    desempilhar(pilha)
    desempilhar(pilha)  # Deve dar erro (pilha vazia)

# Executa o exemplo
exemplo_uso_pilha()



# 🧠 Lógica:
# A pilha é representada por uma lista.

# A função empilhar verifica se a pilha atingiu a capacidade máxima antes de inserir.

# A função desempilhar verifica se a pilha está vazia antes de remover.

# O topo, checagem de vazio e de cheio são funções auxiliares úteis para controle.

# Se quiser uma versão com menu interativo (inserir, remover, ver topo, sair), posso montar também. Deseja isso?