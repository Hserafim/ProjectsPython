import requests

def main():
    print('######################')
    print('#### CONSULTA CEP ####')
    print('######################')
    print()

    cep_input = input('Digite um cep para a consulta (somente números): ')

    if len(cep_input) != 8:
        print('Quantidade ou caracteres inválidos!')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('==> CEP ENCONTRADO <==')

        print('CEP: {}'.format(address_data['cep']))
        print('Logradouro: {}'.format(address_data['logradouro']))
        print('Complemento: {}'.format(address_data['complemento']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))

    else:
        print('{}: Cep inválido!'.format(cep_input))
    print('-----------------------------------------------------------------')
    option = int(input('Deseja realizar uma nova consulta?\n1. Sim\n2. Sair\n'))
    if option == 1:
         main()
    else:
        print('Obrigado por utilizar nossos serviços, até mais.')

if __name__ == '__main__':
    main()
