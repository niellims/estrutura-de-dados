# Função principal que avalia uma expressão em notação pós-fixa
def avaliar_expressao_posfixa(expressao: str) -> float:
    pilha = []  # Criamos uma pilha (lista) para armazenar os números temporariamente
    tokens = expressao.split()  # Quebramos a expressão em partes (tokens) separadas por espaço

    for token in tokens:  # Vamos processar cada token da expressão
        if eh_numero(token):  # Se o token for um número (positivo, negativo ou decimal)
            pilha.append(float(token))  # Convertimos para float e empilhamos
        else:
            # Se não for número, é operador. Então retiramos os dois últimos números da pilha
            b = pilha.pop()
            a = pilha.pop()
            # Aplicamos o operador sobre os dois valores
            resultado = aplicar_operador(a, b, token)
            pilha.append(resultado)  # Empilhamos o resultado da operação

    return pilha[0]  # Ao final, o único valor na pilha é o resultado da expressão

# Função auxiliar para verificar se um token é um número válido
def eh_numero(token: str) -> bool:
    # Se houver mais de um ponto, não é um número decimal válido
    if token.count('.') > 1:
        return False
    # Se começar com "-", retiramos para verificar se o resto é número
    if token.startswith('-'):
        token = token[1:]
    # Verifica se o token restante contém apenas dígitos ou um ponto
    return token.replace('.', '').isdigit()

# Função para aplicar um operador (+, -, *, /) entre dois valores
def aplicar_operador(a: float, b: float, operador: str) -> float:
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b
    else:
        raise ValueError(f"Operador inválido: {operador}")  # Caso o operador não seja conhecido

# Exemplo de uso:
expressao = "5 1 2 + 4 * + 3 -"
resultado = avaliar_expressao_posfixa(expressao)
print(f"Resultado: {resultado}")
