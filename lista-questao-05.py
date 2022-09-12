#---- Lista de exercícios Q5 ----#
salarioum = int (input('Salário: '))
aumento = int (input('Porcentagem de aumento: '))

salariodois = (aumento/100 *salarioum) + salarioum

print('O aumento: {:.2f}'.format(aumento /100 * salarioum))
print('O novo salário: {:.2f}'.format(salariodois))