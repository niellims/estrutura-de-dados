# 11. Implementar uma hashtable simples
# Sem usar o tipo dict , implemente uma estrutura básica de tabela hash com
# inserção e busca simples.

class HashTable:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        chave_str = str(chave)  # Garante que a chave seja string
        soma = 0
        for caractere in chave_str:
            # Transforma o caractere em número somando a posição do alfabeto (a=1, b=2...) manualmente
            alfabeto = "abcdefghijklmnopqrstuvwxyz"
            caractere = caractere.lower()
            posicao = alfabeto.find(caractere)
            if posicao != -1:
                soma += posicao + 1  # Ex: 'a' → 1, 'b' → 2, ...
            else:
                soma += 0  # Ignora outros caracteres
        return soma % self.tamanho


    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for i, (k, v) in enumerate(self.tabela[indice]):
            if k == chave:
                self.tabela[indice][i] = (chave, valor)  # Atualiza valor se chave já existe
                return
        self.tabela[indice].append((chave, valor))  # Inserção normal

    def buscar(self, chave):
        indice = self._hash(chave)
        for k, v in self.tabela[indice]:
            if k == chave:
                return v
        return None  # Não encontrado

    def __str__(self):
        return str(self.tabela)


ht = HashTable()

ht.inserir("Ana", 8.5)
ht.inserir("Carlos", 7.0)
ht.inserir("João", 9.0)
ht.inserir("Ana", 9.5)  # Atualiza

print(ht.buscar("Carlos"))  # Saída: 7.0
print(ht.buscar("Ana"))     # Saída: 9.5
print(ht.buscar("Maria"))   # Saída: None

print(ht)  # Visualiza a tabela
