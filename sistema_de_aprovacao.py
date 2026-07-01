from datetime import date
data_atual = date.today()

try:
    nome = str(input('Digite o seu nome: '))
    nota = float(input('Digite sua primeira nota:'))
    nota2 = float(input('Digite sua segunda nota:'))
    resultado = (nota + nota2) / 2
    print('Olá \033[1;32;40m{}\033[0m, sua primeira nota foi \033[1;32;40m{}\033[0m e sua segunda nota você tirou \033[1;32;40m{}\033[0m com isso seu resultado final é: \033[1;33;40m{}\033[0m a data de hoje é \033[1;32;40m{}\033[0m'.format(nome,nota,nota2,resultado,data_atual))
except ValueError:
    print('Digite algo válido!')