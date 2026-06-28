print('=-' * 20)
print('{}1-LOGAR\n{}2-CADASTRAR\n{}0-ENCERRAR PROGRAMA'.format(' '*12, ' '*12, ' '*12))
print('=-' * 20)

user = []
password = []

while True:
    try:

        esco = int(input('Digite sua escolha: '))

        match esco:
            case 1:
                user_login = input('Digite seu usuário: ')
                password_login = int(input('Digite sua senha: '))

                if user_login in user:
                    indice = user.index(user_login)

                    if password[indice] == password_login:
                        print('Pode entrar!')
                    else:
                        print('Senha incorreta!')
                else:
                    print('Usuário não existe!')
            case 2:
                new_user = input('Digite seu login: ')
                if new_user in user:
                    print('Esse usuário já existe!')
                    continue
                new_password = int(input('Digite sua senha: '))
                user.append(new_user)
                password.append(new_password)
                print('Usuário cadastrado com sucesso!')
            case 0:
                print('Encerrando Sistema...')
                break
            case _:
                print('Escolha inválida!')
    except ValueError:
        print('Digite um valor válido!')