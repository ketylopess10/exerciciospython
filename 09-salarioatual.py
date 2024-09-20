salario_atual = float(input('informe o salario atual: '))
percentual_aumento = float(input('informe o percentual de aumento: '))

novo_salario = salario_atual + (salario_atual * (percentual_aumento / 100))                          

print(f'O novo salário é: R$ {novo_salario:.2f}')