# Filtragem de dados
# Dado um dicionário de produtos e seus preços, crie um novo dicionário contendo apenas os produtos com preço acima de R$ 50.

produtos = {
    "mouse": 25.00,
    "teclado": 70.00,
    "monitor": 450.00,
    "cabo HDMI": 35.00,
    "webcam": 150.00
}

produtos_filtrados = {}

for produto, preco in produtos.items():
    if preco > 50:
        produtos_filtrados[produto] = preco

print(produtos_filtrados)