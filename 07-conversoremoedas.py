real= float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 5.43
euro = real / 6.06
print('Com R${:.2F}voce pode comprar US {:.2f}' .format(real, dolar))
print('Com R${:.2F}voce pode comprar € {:.2f}' .format(real, euro))
