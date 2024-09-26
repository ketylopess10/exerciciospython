from math import hypot
comCatOposto = float(input('Comprimento do cateto oposto: '))
comCatAdj = float(input('Comprimento do cateto adjacente:'))
hip = hypot(comCatOposto, comCatAdj)
print(f"A hipotenusa vai medir {hip:.2f}")
