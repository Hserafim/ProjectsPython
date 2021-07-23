import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

headers = {'User-Agent': 'GoogleChrome/91.0.4472.114'}

page = requests.get('https://br.investing.com/equities/', headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

data = soup.find("section", {"id": "leftColumn"}).find('tbody').find_all('tr')

cabecalho = ["Empresa".upper(), "Atual".upper(), "Máxima".upper(),
             "Mínima".upper(), "Variação".upper(), "Var %".upper(),
             "Volume".upper(), "Hora".upper()]

tabela = []

for paper in data:
    data_asset = paper.find_all("td")

    coleta = [data_asset[1].text, data_asset[2].text, data_asset[3].text,
              data_asset[4].text, data_asset[5].text,
              data_asset[6].text, data_asset[7].text, data_asset[8].text]

    tabela.append(coleta)

print(tabulate(tabela, headers=cabecalho, tablefmt="fancy_grid"))