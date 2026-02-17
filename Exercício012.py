# Calculando Descontos

Produto = float(input('Digite o valor do produto: R$'))
Promo = Produto - (Produto * 5 /100)

print(f'O produto que custava R${Produto}, na promoção com desconto de 5% vai custar R${Promo:.2f}')
