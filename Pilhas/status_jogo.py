class EstadoDoJogo:
    def __init__(self, nivel, pontuacao, vidas):
        self.nivel = nivel
        self.pontuacao = pontuacao
        self.vidas = vidas

    def __str__(self):
        return f"Nível: {self.nivel}, Pontuação: {self.pontuacao}, Vidas: {self.vidas}"

class Jogo:
    def __init__(self):
        self.estado_atual = None       # Estado atual do jogo
        self.historico_estados = []    # Pilha de estados anteriores

    def salvar_estado(self):
        if self.estado_atual:
            self.historico_estados.append(self.estado_atual)
            print("Estado salvo.")

    def atualizar_estado(self, nivel, pontuacao, vidas):
        self.salvar_estado()  # Salva o estado antes de atualizar
        self.estado_atual = EstadoDoJogo(nivel, pontuacao, vidas)
        print("Novo estado atualizado:")
        print(self.estado_atual)

    def voltar_estado(self):
        if not self.historico_estados:
            print("Não há estados anteriores para voltar.")
            return
        self.estado_atual = self.historico_estados.pop()
        print("Estado restaurado:")
        print(self.estado_atual)

    def mostrar_estado_atual(self):
        print("\n=== Estado Atual do Jogo ===")
        if self.estado_atual:
            print(self.estado_atual)
        else:
            print("Nenhum estado definido.")
        print("=============================\n")

# Simulação
jogo = Jogo()

# Primeira situação do jogo
jogo.atualizar_estado(nivel=1, pontuacao=100, vidas=3)
jogo.atualizar_estado(nivel=2, pontuacao=200, vidas=3)
jogo.atualizar_estado(nivel=3, pontuacao=250, vidas=2)

# Voltar no tempo duas vezes
jogo.voltar_estado()
jogo.voltar_estado()

# Mostrar o estado atual
jogo.mostrar_estado_atual()
