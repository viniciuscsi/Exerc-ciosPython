print('----------------------Aluguel de Carros--------------------')

dias =int(input('Quantos dias alugados ?'))
Km =float(input('Quantos Km rodados ?'))
pago = (dias*60) + (Km * 0.15)
print('O total a pagar e de {:.2f} R$'.format(pago))
