def escrever(texto: str, conteudo: str, historico: list[str]) -> str:
    historico.append(texto)  # Salva o estado atual antes da mudança
    return texto + conteudo

def apagar(texto: str, quantidade: int, historico: list[str]) -> str:
    historico.append(texto)  # Salva o estado atual antes da mudança
    return texto[:-quantidade] if quantidade <= len(texto) else ""

def desfazer(historico: list[str]) -> str:
    if len(historico) > 0:
        return historico.pop()  # Restaura o último estado salvo
    return ""  # Se não há nada para desfazer, retorna texto vazio


def editor_de_texto() -> None:
    texto = ""
    historico = []

    # Simula ações
    texto = escrever(texto, "Olá", historico)
    print("Texto:", texto)

    texto = escrever(texto, " mundo", historico)
    print("Texto:", texto)

    texto = apagar(texto, 3, historico)  # Apaga "ndo"
    print("Texto após apagar:", texto)

    texto = desfazer(historico)  # Desfaz o apagar
    print("Texto após desfazer:", texto)

    texto = desfazer(historico)  # Desfaz a escrita " mundo"
    print("Texto após desfazer:", texto)

    texto = desfazer(historico)  # Desfaz a escrita "Olá"
    print("Texto após desfazer:", texto)

# Executa o editor
editor_de_texto()



# 🧠 Lógica:
# Cada vez que você escreve ou apaga, o estado anterior do texto é salvo na pilha de histórico.

# A função desfazer() simula o Ctrl+Z, restaurando o último estado da pilha (última ação feita).

# Se quiser posso fazer uma versão com múltiplos tipos de ações e refatorar como uma interface mais completa. Deseja isso?