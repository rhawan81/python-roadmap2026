def cadastro_user():
    cadastrados = []
    while True:
        nome = input()
        idade = int(input('Informe sua idade'))
        if nome == 'nenhum' and idade == 0:
            break
        else:
            cadastrados.append(nome)
            print(f'Usuario com nome {nome} cadastrado com sucesso !')
    print (cadastrados)

cadastro_user()


## O principal objetivo aqui era cadastrar usuarios e armazena- los em uma lista depois listar o cadastrados