print('{}\n{}BEM-VINDO(A) AO JOGO DA VERDADE OU DESAFIO!\n{}'.format('-='*22,' ','-='*22))
cont = 0

while True:

        escolha = str(input('Escolha \033[1;36;40mVERDADE \033[0mou \033[1;31;40mDESAFIO\033[0m:')).lower().strip()
        if escolha == 'verdade':
            print('\n\033[4;37;40mFale um segredo seu!\033[0m\n')
            cont = cont + 1
        elif escolha == 'desafio':
            print('\n\033[4;37;40mFaça um desafio pedido!\033[0m\n')
            cont = 0
        else:
            print('\033[1;33;40mDigite algo Válido!\033[0m\n')
            continue
        
        if cont == 3:
            while 0 == 0:
                print('\033[1;33;40mAVISO:\033[1;34;40mNúmero MAXIMO de \033[1;36;40mVERDADE\033[1;34;40m atingido!\033[0m\n\033[1;33;40mFaça um \033[1;31;40mDESAFIO\033[1;33;40m para continuar no jogo!\033[0m')
                cont = 0
                try:
                    x = int(input('[1] COMPLETEI O DESAFIO\n[2] ENCERRAR JOGO\nEscolha:'))
                    match x:
                        case 1:
                            print('\033[1;33;40mVoltando ao jogo...\033[0m\n')
                            break
                        case 2:
                            print('\033[1;33;40mEncerrando o jogo...\033[0m')
                            exit()
                except ValueError:
                    print('\033[1;33;40mDigite algo Válido!\033[0m\n')