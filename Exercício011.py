# Pintando Parede

Largura = float(input('Largura da parede: '))
Altura = float(input('Altura da parede: '))
Area = Largura * Altura

print(f'Sua parede tem a dimensão de {Largura}x{Altura} e sua área é de {Area}m² \n'
      f'Para pintar essa parede, você precisará de {Area / 2}l de tinta')
