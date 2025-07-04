from collections import defaultdict, Counter

indice = defaultdict(set)
frequencia = Counter()
print('Digite no formato: PÁG [numero da pag] TEXTO...')
while True:
    linha = input()
    if linha.strip().upper() == 'FIM':
        break

    partes = linha.split()
    if partes[0] == 'PAG':
        pagina = int(partes[1])
        palavras = partes[2:]

        for palavra in palavras:
            palavra = palavra.lower().strip('.,;:!?()[]{}"')  
            if palavra:
                indice[palavra].add(pagina)
                frequencia[palavra] += 1


print("\nÍNDICE REMISSIVO:")
for palavra in sorted(indice):
    print(f"{palavra}: {sorted(indice[palavra])}")


print("\nTOP 10 PALAVRAS MAIS FREQUENTES:")
for palavra, contagem in frequencia.most_common(10):
    print(f"{palavra}: {contagem}")
