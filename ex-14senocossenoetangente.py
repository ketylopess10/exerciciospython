import math
angulo = float(input('Digite o angulo que voce deseja: '))

seno = math.sin(math.radians(angulo)) #math.sin calcula o seno
print(f"O angulo de {angulo} tem o SENO de{seno:.2f}")

cosseno = math.cos(math.radians(angulo))#math.cos calcula o cosseno
print(f"o angulo de {angulo} tem o COSSENO de {cosseno:.2f}")

tangente = math.tan(math.radians(angulo))#math.tan calcula o tangente
print(f"O angulo de {angulo} tem a TANGENTE de {tangente:.2f}")