#1: ** Potencia, 2: * Mult, 3:/ Divisão, 4: // Divisão inteira, 5: % resto da divisão

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2 
mult = n1 * n2 
div = n1 / n2 
divint= n1 // n2 
poten = n1 ** n2 
print('A soma é {}, o produto e a divisão e´{:.3f}' .format(soma, mult, div, divint, poten), end= '')
print('Divisão inteira {} e potencia {}' .format(div, poten))
