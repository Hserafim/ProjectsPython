import requests
import json

page = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
resp = json.loads(page.content)
data = resp.get('USDBRL')
dolar = data.get('bid')


def real_dolar(x,y):

    conversor = x / float(y)

    return print(f"R${input_real} reais valem hoje US${'%.2f' %conversor} dolars")


def dolar_real(x,y):

    conversor = float(x) * (y)

    return print(f"US${input_dolar} dolars valem hoje RS{'%.2f' %conversor} reais")


print("\n1 - Real para Dolar\n2 - Dolar para Real")
escolha = int(input("\nDigite o número para qual conversão deseja realizar: "))

if escolha == 1:
    input_real = float(input("\nDigite o valor em Reais que deseja converter em Dolars: "))
    real_dolar(input_real, dolar)

elif escolha == 2:
        input_dolar = float(input("\nDigite o valor em Dolars que deseja converter em Reais: "))
        dolar_real(dolar, input_dolar)

else:
    print("Opção inválida!")
