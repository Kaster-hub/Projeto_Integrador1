'''
Projeto Integrador I => Input de peso
'''

def pesoValor():
    pesoValido = False
    while not pesoValido:
        try:
            peso = float(
                input('\nFavor, digite seu peso, em quilogramas (ex: 70.6): ')
            )
            if peso <= 0:
                print('<<<ERRO: Valor inválido, use APENAS números positivos>>>')
            else:
                pesoValido = True

        except ValueError:
            print('<<<ERRO: Valor inválido, use APENAS números>>>')
            
    return peso