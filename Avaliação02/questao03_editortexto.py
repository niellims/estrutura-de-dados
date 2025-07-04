def escrever(texto: str, conteudo: str, historico: list[str]) -> str:
    historico.append(texto)  # salva o estado atual antes da mudança
    return texto + conteudo

def desfazer(historico: list[str]) -> str:
    if len(historico) > 0:
        return historico.pop()  # restaura o último estado salvo
    return ""  # se não há nada para desfazer, retorna texto vazio


def editor_de_texto() -> None:
    texto = ""
    historico = []
    # inicializando com o texto e o histórico vazios

    
    texto = escrever(texto, "Olá", historico)
    print("Texto:", texto)

    texto = escrever(texto, " mundo", historico)
    print("Texto:", texto)

    texto = escrever(texto, " cruel!", historico)  
    print("Texto:", texto)

    texto = desfazer(historico) 
    print("Texto após desfazer:", texto)

editor_de_texto()

