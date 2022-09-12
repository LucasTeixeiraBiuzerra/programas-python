#---- Lista de exercícios Q3 ----#
notaum = float (input("Primeira nota: "))
notadois = float (input("Segunda nota: "))
notatres = float (input("Terceira nota: "))

pesoum = float (input("Primeiro peso: "))
pesodois = float (input("Segundo peso:"))
pesotres = float (input("Terceiro peso: "))

contaum = notaum*pesoum + notadois*pesodois + notatres*pesotres
contadois = pesoum+pesodois+pesotres
contatres = contaum/contadois

print('Resultado da operação: {:.2f}'.format(contatres))