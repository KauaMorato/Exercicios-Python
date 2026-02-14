# Dissecando uma Variável

Algo = input('Digite algo: ')

print(type(Algo))
print('Só tem espaços?', Algo.isspace())
print('É um numérico?', Algo.isnumeric())
print('É alfabético', Algo.isalpha())
print('É alfanumérico', Algo.isalnum())
print('Está em maiúsculas?', Algo.isupper())
print('Está em minúsculas?', Algo.islower())
print('Está capitalizada', Algo.istitle())