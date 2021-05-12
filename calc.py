print('---------------------------------------')
print('|----------CALCULADORA BASIC----------|')
print('---------------------------------------')

def main():

    print('Selecione o número da operação desejada: \n\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n')
    escolha = int(input('Digite sua opção (1/2/3/4): '))

    if escolha == 1:
        print('\n[Adição]\n')
        num1 = int(input('Digite o primeiro nº da soma: '))
        num2 = int(input('Digite o segundo nº da soma: '))
        print('%s + %r = '%(num1, num2),num1 + num2)

    elif escolha == 2:
        print('\n[Subtração]\n')
        num1 = int(input('Digite o primeiro nº: '))
        num2 = int(input('Digite o segundo nº: '))
        print('%s - %r = ' % (num1, num2), num1 - num2)

    elif escolha == 3:
        print('\n[Multiplicação]\n')
        num1 = int(input('Digite o primeiro nº: '))
        num2 = int(input('Digite o segundo nº: '))
        print('%s x %r = ' % (num1, num2), num1 * num2)

    elif escolha == 4:
        print('\n[Divisão]\n')
        num1 = int(input('Digite o primeiro nº: '))
        num2 = int(input('Digite o segundo nº: '))
        print('%s / %r = ' % (num1, num2), num1 / num2)

    else:
        print('O número digitado não corresponde as operações!\nTente novamente...\n')
        return main()

if __name__ == '__main__':
    main()