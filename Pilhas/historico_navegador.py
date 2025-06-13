class Navegador:
    def __init__(self):
        self.pilha_voltar = []   # Pilha com as páginas anteriores
        self.pilha_avancar = []  # Pilha com as páginas futuras
        self.pagina_atual = None # Página atual exibida no navegador

    def visitar_pagina(self, url):
        if self.pagina_atual:
            self.pilha_voltar.append(self.pagina_atual)  # Salva a página atual na pilha de voltar
        self.pagina_atual = url   # Atualiza a página atual
        self.pilha_avancar.clear()  # Limpa a pilha de avançar, pois visitamos uma nova página
        print(f"Visitando: {self.pagina_atual}")

    def voltar(self):
        if not self.pilha_voltar:
            print("Não há páginas para voltar.")
            return
        self.pilha_avancar.append(self.pagina_atual)  # Salva a atual na pilha de avançar
        self.pagina_atual = self.pilha_voltar.pop()   # Volta para a última página visitada
        print(f"Voltando para: {self.pagina_atual}")

    def avancar(self):
        if not self.pilha_avancar:
            print("Não há páginas para avançar.")
            return
        self.pilha_voltar.append(self.pagina_atual)   # Salva a atual na pilha de voltar
        self.pagina_atual = self.pilha_avancar.pop()  # Avança para a próxima página
        print(f"Avançando para: {self.pagina_atual}")

    def mostrar_estado(self):
        print("\n--- Estado Atual ---")
        print(f"Página atual: {self.pagina_atual}")
        print(f"Pilha voltar: {self.pilha_voltar}")
        print(f"Pilha avançar: {self.pilha_avancar}")
        print("---------------------\n")

# Exemplo de uso
navegador = Navegador()
navegador.mostrar_estado()
navegador.visitar_pagina("google.com")
navegador.mostrar_estado()
navegador.visitar_pagina("wikipedia.org")
navegador.mostrar_estado()
navegador.visitar_pagina("openai.com")
navegador.mostrar_estado()
navegador.voltar()
navegador.mostrar_estado()
navegador.voltar()
navegador.mostrar_estado()
navegador.avancar()
navegador.mostrar_estado()
navegador.visitar_pagina("github.com")
navegador.mostrar_estado()
