casa = float(input('Quanto é o valor da casa: R$'))
salario = float(input('Quanto você recebe: R$'))
anos = int(input('Quantos Anos de financiamento: R$'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestacao será de R${:.2f}'.format(casa,anos,prestacao))
if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")