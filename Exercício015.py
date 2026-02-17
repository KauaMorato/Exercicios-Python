# Aluguel de Carros

Dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))
Pago = (Dias * 60) + (Km * 0.15)

print(f'O total a pagar é de R${Pago:.2f}')
