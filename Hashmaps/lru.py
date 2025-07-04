# 15. LruCache (desafio)
# Implemente uma estrutura de cache do tipo LRU (Least Recently Used) usando
# dicionários e listas.

class LRUCache:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.cache = {}  # Armazena os dados (chave: valor)
        self.ordem_uso = []  # Lista para rastrear a ordem de uso (chave mais antiga no início)

    def get(self, chave):
        if chave in self.cache:
            # Move a chave para o final (usada recentemente)
            self.ordem_uso.remove(chave)
            self.ordem_uso.append(chave)
            return self.cache[chave]
        return -1  # Cache miss

    def put(self, chave, valor):
        if chave in self.cache:
            # Atualiza o valor e move para o final da ordem de uso
            self.cache[chave] = valor
            self.ordem_uso.remove(chave)
            self.ordem_uso.append(chave)
        else:
            # Se o cache está cheio, remove o menos recentemente usado
            if len(self.cache) >= self.capacidade:
                chave_removida = self.ordem_uso.pop(0)
                del self.cache[chave_removida]
            # Insere a nova chave
            self.cache[chave] = valor
            self.ordem_uso.append(chave)

    def __str__(self):
        return f"Cache: {self.cache}\nOrdem de uso: {self.ordem_uso}"


lru = LRUCache(3)
lru.put("a", 1)
lru.put("b", 2)
lru.put("c", 3)
print(lru)

# Acessando a chave 'a' (agora 'a' é a mais recente)
print("get a:", lru.get("a"))
print(lru)

# Adicionando uma nova chave deve remover a menos usada ('b')
lru.put("d", 4)
print(lru)
