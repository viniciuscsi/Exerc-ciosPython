import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo {} tem o SEN de {:.2f} '.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))