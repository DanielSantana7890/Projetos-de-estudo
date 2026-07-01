peso = float(input('Qual é o seu peso(kg):'))
altura = float(input('Qual é a sua altura(m):'))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc <= 25:
    print('Você está no peso Ideal!')
elif imc <= 30:
    print('Você está com Sobrepeso!')
elif imc <= 40:
    print('Você está com Obesidade!')
else:
    print('Você está com Obesidade Mórbida!')