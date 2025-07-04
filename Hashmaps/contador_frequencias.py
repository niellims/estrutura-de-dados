# Contador de frequências
from collections import Counter
texto = input('Digite um texto: ')
t_min = texto.lower()
c = Counter(t_min)

print(c.most_common())

