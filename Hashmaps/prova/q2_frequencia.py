from collections import Counter

frequencia = Counter()

while True:
    linha = input()
    if linha.strip() == '':
        break
    palavras = linha.split()
    for palavra in palavras:
        limpa = ''.join(c for c in palavra if c.isalnum()).lower()
        if limpa:
            frequencia[limpa] += 1


print("\nTop 10 palavras mais frequentes:")
for palavra, contagem in frequencia.most_common(10):
    print(f"{palavra}: {contagem}")