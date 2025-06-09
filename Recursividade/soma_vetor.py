def soma_vetor(vetor: list[int]) -> int:
    if len(vetor) == 0:
        return 0
    return vetor[0] + soma_vetor(vetor[1:])