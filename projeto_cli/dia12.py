while True:

    try: ## bloco de verificação de erros se o valor for valido ele ira parar o loop caso nao ira cair no except 
        idade = int(input('Informe sua idade:'))
        break
    except: # usado para capturar o erro.
        print('VALOR INVALIDO')