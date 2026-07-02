from random import randint
print('=-'*12)
print('{}JOKENPÔ'.format(" "*7))
print('=-'*12)
print('[1]Pedra\n[2]Papel\n[3]Tesoura')
print('=-'*12)
opcao = int(input('Digite sua escolha:'))
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
escolha = 'null'

match opcao:
    case 1:
        escolha = 'Pedra'
        if itens[computador] == 'Papel':
            print('Sinto muito você perdeu!')
        elif itens[computador] == 'Pedra':
            print('Empatou!')
        else:
            print('Você ganhou!')
    case 2:
        escolha = 'Papel'
        if itens[computador] == 'Tesoura':
            print('Sinto muito você perdeu!')
        elif itens[computador] == 'Papel':
            print('Empatou!')
        else:
            print('Você ganhou!')
    case 3:
        escolha = 'Tesoura'
        if itens[computador] == 'Pedra':
            print('Sinto muito você perdeu!')
        elif itens[computador] == 'Tesoura':
            print('Empatou!')
        else:
            print('Você ganhou!')
print('O computador escolheu {}'.format(itens[computador]))