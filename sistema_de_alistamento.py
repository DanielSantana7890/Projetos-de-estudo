from datetime import date
ano_atual = date.today().year

try:
    nasci = int(input('Digite o seu ano de nascimento:').strip())
    nasci = ano_atual - nasci

    if nasci >= 18:
     print('Você está aprovado para se alistar no quartel!')
    else:
     print('Você precisa esperar completar 18 anos para se alistar!')

except ValueError:
    print('Digite algo válido!')